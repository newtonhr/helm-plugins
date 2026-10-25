"""Licence: the repo and every plugin are MIT, and borrowed work keeps its notice.

Also: a plugin whose files changed against main carries a new version, because clients
only receive an update when `version` in plugin.json changes.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = sorted((ROOT / "plugins").glob("*/.claude-plugin/plugin.json"))
SOURCES = ("coreyhaines31/marketingskills", "wondelai/skills")


def test_the_repo_is_mit_licensed_by_newton() -> None:
    text = (ROOT / "LICENSE").read_text("utf-8")
    assert text.startswith("MIT License") and "Newton d.o.o." in text


@pytest.mark.parametrize("path", MANIFESTS, ids=lambda p: p.parent.parent.name)
def test_each_plugin_declares_mit(path: Path) -> None:
    assert json.loads(path.read_text("utf-8")).get("license") == "MIT"


def test_borrowed_work_keeps_its_licence_text() -> None:
    text = (ROOT / "THIRD_PARTY_NOTICES.md").read_text("utf-8")
    for source in SOURCES:
        assert source in text
    assert text.count("Permission is hereby granted") == len(SOURCES)
    assert "Copyright (c) 2025 Corey Haines" in text
    assert "Copyright (c) 2025 Wondel.ai sp. z o.o." in text


def _git(*args: str) -> str | None:
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


@pytest.mark.parametrize("path", MANIFESTS, ids=lambda p: p.parent.parent.name)
def test_a_changed_plugin_has_a_new_version(path: Path) -> None:
    base = (_git("merge-base", "HEAD", "origin/main") or "").strip()
    if not base:
        pytest.skip("no origin/main to compare with")
    plugin = path.parent.parent.relative_to(ROOT).as_posix()
    changed = [f for f in (_git("diff", "--name-only", base, "--", plugin) or "").split()
               if "/evals/" not in f and not f.endswith("README.md")]
    old = _git("show", f"{base}:{plugin}/.claude-plugin/plugin.json")
    if not changed or old is None:
        return
    assert json.loads(old)["version"] != json.loads(path.read_text("utf-8"))["version"], (
        f"{plugin} changed but its version did not")
