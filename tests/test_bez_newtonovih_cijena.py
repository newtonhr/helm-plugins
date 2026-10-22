"""Client plugins never carry Newton's pricing or internal process.

Newton's price list, day rates and Projektni zadatak tooling live in
newtonhr/helm-plugins-newton. Everything under plugins/ here is installed on
client accounts, so none of it may name them.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

PLUGINS = Path(__file__).resolve().parents[1] / "plugins"
FORBIDDEN = [
    r"02_CJENIK", r"Axon-Knowledge", r"axon-sow-architect", r"pz-compiler",
    r"helm-newton", r"dnevnic", r"day rate", r"€\s*/\s*h", r"/h\b.*€", r"\buplift\b",
]
FILES = sorted(p for p in PLUGINS.rglob("*") if p.is_file() and p.suffix in {".md", ".json"})


def test_there_are_client_files_to_check() -> None:
    assert FILES


@pytest.mark.parametrize("path", FILES, ids=lambda p: str(p.relative_to(PLUGINS)))
def test_no_newton_pricing_in_client_plugins(path: Path) -> None:
    text = path.read_text("utf-8")
    for pattern in FORBIDDEN:
        assert not re.search(pattern, text, re.I), f"{path.name}: {pattern}"
