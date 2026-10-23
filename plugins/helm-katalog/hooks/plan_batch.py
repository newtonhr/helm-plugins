#!/usr/bin/env python3
"""helm-katalog hook: nudge Claude to approve a product's proposals in one batch.

post: remember plan ids returned by propose_* calls; forget them once applied or cancelled.
pre:  before a single review_plan/apply_plan, if two or more proposals are still open,
      tell Claude to show one summary and use apply_plans; before read_sql, point to the
      read tools.

Advisory only: it never blocks a call (the server's plan pipeline is the real gate),
and any error exits 0 silently so Helm keeps working without it.
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

PLAN_ID = re.compile(r"pln_[0-9a-f]{12}")


def _state_path(session_id: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_-]", "", session_id) or "default"
    d = Path(tempfile.gettempdir()) / "helm-katalog"
    d.mkdir(exist_ok=True)
    return d / f"{safe}.json"


def _load(p: Path) -> list[str]:
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return []


def _save(p: Path, ids: list[str]) -> None:
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(ids))
    os.replace(tmp, p)


def _tool(name: str) -> str:
    return name.rsplit("__", 1)[-1]


def _context(event: str, text: str) -> None:
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event,
                                             "additionalContext": text}}))


def post(data: dict) -> None:
    p = _state_path(data.get("session_id", ""))
    ids = _load(p)
    tool = _tool(data.get("tool_name", ""))
    inp = data.get("tool_input") or {}
    if tool.startswith("propose_"):
        for pid in PLAN_ID.findall(json.dumps(data.get("tool_response"))):
            if pid not in ids:
                ids.append(pid)
    else:
        done = set(inp.get("plan_ids") or []) | {inp.get("plan_id")}
        ids = [i for i in ids if i not in done]
    _save(p, ids[-200:])


def pre(data: dict) -> None:
    tool = _tool(data.get("tool_name", ""))
    if tool == "read_sql":
        _context("PreToolUse",
                 "helm-katalog: prefer find_catalog_items, search_products, "
                 "get_category_products or catalog_completeness over read_sql. Use SQL "
                 "only if none of them can answer, and tell the person what was missing.")
        return
    ids = _load(_state_path(data.get("session_id", "")))
    if len(ids) >= 2:
        _context("PreToolUse",
                 f"helm-katalog: {len(ids)} proposals are still open in this session "
                 f"({', '.join(ids[-10:])}). If they belong to the same product or batch, "
                 "do not approve them one by one: show the person one summary, ask once, "
                 "then call apply_plans with all their ids.")


def main() -> None:
    try:
        data = json.load(sys.stdin)
        {"post": post, "pre": pre}[sys.argv[1]](data)
    except Exception:  # noqa: BLE001 - advisory hook must never break the session
        pass


if __name__ == "__main__":
    main()
