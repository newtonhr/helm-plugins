"""helm-katalog: the batching hook advises (never blocks) and the price-list reader parses."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1] / "plugins" / "helm-katalog"
HOOK = PLUGIN / "hooks" / "plan_batch.py"
SCRIPT = PLUGIN / "scripts" / "cjenik_redovi.py"


def _hook(mode: str, event: dict, tmp_path: Path) -> str:
    env = {"TMPDIR": str(tmp_path), "PATH": "/usr/bin:/bin"}
    r = subprocess.run([sys.executable, str(HOOK), mode], input=json.dumps(event),
                       capture_output=True, text=True, env=env, check=True)
    return r.stdout


def test_hook_suggests_batching_then_goes_quiet(tmp_path: Path) -> None:
    s = {"session_id": "t"}
    for pid in ("pln_aaaaaaaaaaaa", "pln_bbbbbbbbbbbb"):
        _hook("post", {**s, "tool_name": "mcp__helm__propose_update_product_text",
                       "tool_response": {"content": [{"text": json.dumps({"plan_id": pid})}]}},
              tmp_path)
    out = _hook("pre", {**s, "tool_name": "mcp__helm__apply_plan"}, tmp_path)
    ctx = json.loads(out)["hookSpecificOutput"]
    assert ctx["hookEventName"] == "PreToolUse" and "apply_plans" in ctx["additionalContext"]
    assert "permissionDecision" not in ctx
    _hook("post", {**s, "tool_name": "mcp__helm__apply_plans",
                   "tool_input": {"plan_ids": ["pln_aaaaaaaaaaaa", "pln_bbbbbbbbbbbb"]}}, tmp_path)
    assert _hook("pre", {**s, "tool_name": "mcp__helm__apply_plan"}, tmp_path) == ""


def test_hook_points_sql_to_read_tools(tmp_path: Path) -> None:
    out = _hook("pre", {"session_id": "t", "tool_name": "mcp__helm__read_sql"}, tmp_path)
    assert "catalog_completeness" in out


def test_hook_is_silent_on_garbage(tmp_path: Path) -> None:
    r = subprocess.run([sys.executable, str(HOOK), "pre"], input="nonsense",
                       capture_output=True, text=True, env={"TMPDIR": str(tmp_path)})
    assert (r.returncode, r.stdout) == (0, "")


def test_price_list_reader(tmp_path: Path) -> None:
    f = tmp_path / "c.csv"
    f.write_text("Opis;Šifra artikla;MPC;EAN\nVitlo X1;409557;1.234,50;8001234567890\n"
                 ";;;\nBez sifre;;12,00;\nSidro;92286.0;99;\n", "utf-8")
    out = json.loads(subprocess.run([sys.executable, str(SCRIPT), str(f)],
                                    capture_output=True, text=True, check=True).stdout)
    assert [(r["sifra"], r["cijena"]) for r in out["rows"]] == [("409557", "1234.50"),
                                                               ("92286", "99.00")]
    assert out["preskoceno"] == [{"red": 4, "razlog": "nema šifre"}]
