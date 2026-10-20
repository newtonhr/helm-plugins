"""Checks on the helm-studio plugin, moved from marina-ops-mcp with the plugin.

The plugin stays thin: one skill that points at Helm's own knowledge (studio_znanje) and
sends Claude through the free copy check before any image is made.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1] / "plugins" / "helm-studio"
SKILL = PLUGIN / "skills" / "helm-studio" / "SKILL.md"


def test_the_plugin_is_thin_and_points_at_helm() -> None:
    skills = sorted(p.name for p in (PLUGIN / "skills").iterdir())
    assert skills == ["helm-studio"]
    text = SKILL.read_text(encoding="utf-8")
    assert "studio_znanje" in text
    assert "prednost" in text
    assert not re.search(r"\b\d{3,4}\s*[x×]\s*\d{3,4}\b", text)
    assert len(text.split()) < 300


def test_the_skill_sends_claude_through_the_copy_check() -> None:
    assert "studio_provjeri_tekst" in SKILL.read_text(encoding="utf-8")


def test_the_marketplace_lists_the_plugin_at_its_folder() -> None:
    root = Path(__file__).resolve().parents[1]
    market = json.loads((root / ".claude-plugin" / "marketplace.json").read_text("utf-8"))
    [entry] = [p for p in market["plugins"] if p["name"] == "helm-studio"]
    assert (root / entry["source"]).resolve() == PLUGIN
    manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text("utf-8"))
    assert manifest["name"] == "helm-studio"
