"""Every client plugin carries the Helm connector, and only the shared URL.

The URL is the same for everyone; the person logs in with a personal code. A
personal connector link (/c/cnx_…) or token must never ship in a plugin.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text("utf-8"))
PLUGINS = [ROOT / e["source"] for e in MARKETPLACE["plugins"]]


@pytest.mark.parametrize("plugin", PLUGINS, ids=lambda p: p.name)
def test_each_plugin_carries_only_the_shared_helm_url(plugin: Path) -> None:
    text = (plugin / ".mcp.json").read_text("utf-8")
    assert json.loads(text)["mcpServers"] == {
        "helm": {"type": "http", "url": "https://helm.newton.hr/mcp"}}
    assert not re.search(r"cnx_|cnu_|tok_|/c/", text)
