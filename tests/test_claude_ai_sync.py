"""What claude.ai's marketplace sync warns about, caught before a push.

On 2026-10-22 the sync stripped `icon` from plugin.json ("unrecognized key") and cut
novi-zahtjev's description at 1024 characters.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

PLUGINS = Path(__file__).resolve().parents[1] / "plugins"
SKILLS = sorted(PLUGINS.glob("*/skills/*/SKILL.md"))
MANIFESTS = sorted(PLUGINS.glob("*/.claude-plugin/plugin.json"))
SYNC_KEYS = {"name", "displayName", "version", "description", "author", "homepage",
             "repository", "license", "keywords"}


@pytest.mark.parametrize("path", SKILLS, ids=lambda p: p.parent.name)
def test_skill_description_fits_claude_ai(path: Path) -> None:
    front = re.match(r"---\n(.*?)\n---\n", path.read_text("utf-8"), re.S).group(1)
    raw = re.search(r'^description: (".*"|.*)$', front, re.M).group(1)
    text = json.loads(raw) if raw.startswith('"') else raw
    assert len(text) <= 1024, f"{len(text)} characters"


@pytest.mark.parametrize("path", MANIFESTS, ids=lambda p: p.parent.parent.name)
def test_manifest_has_only_keys_claude_ai_keeps(path: Path) -> None:
    assert set(json.loads(path.read_text("utf-8"))) <= SYNC_KEYS
