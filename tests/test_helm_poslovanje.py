"""Checks on the helm-poslovanje plugin.

Its skills only read: they report and hand work to the skill that makes a change. Every
Helm tool a skill names must exist in the server (tests/katalog.json, scripts/katalog.py),
and every skill it hands over to must exist in this marketplace.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "helm-poslovanje"
SKILLS = PLUGIN / "skills"
KATALOG = json.loads((ROOT / "tests" / "katalog.json").read_text("utf-8"))
TOOLS = set(KATALOG["helm_alati"]) | set(KATALOG["alati"])
ALL_SKILLS = {p.parent.name for p in (ROOT / "plugins").glob("*/skills/*/SKILL.md")}
EXPECTED = {"tjedni-pregled", "provjere", "glas-kupca", "jutarnji-pregled", "uvidi"}
# Fields of a tool's answer that look like tool names.
FIELDS = {"search_terms"}
TOOL_WORD = re.compile(
    r"\b((?:pos|get|list|propose|apply|telemetry|catalog|search|find|my|read)_[a-z_]+)\b")


def _skill(name: str) -> tuple[dict[str, str], str]:
    text = (SKILLS / name / "SKILL.md").read_text("utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    assert m, name
    meta = {k: json.loads(v) if v.startswith('"') else v
            for k, v in (line.split(": ", 1) for line in m.group(1).splitlines())}
    return meta, m.group(2)


def test_the_plugin_has_one_skill_per_job() -> None:
    assert {p.name for p in SKILLS.iterdir()} == EXPECTED


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_each_skill_is_named_and_described_for_marina_stores(name: str) -> None:
    meta, body = _skill(name)
    assert meta["name"] == name
    assert meta["description"].startswith("Marina Stores, Helm.")
    assert len(meta["description"]) <= 1024
    assert len(body.split()) < 700


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_every_tool_and_skill_a_skill_names_exists(name: str) -> None:
    _, body = _skill(name)
    for tool in set(TOOL_WORD.findall(body)) - FIELDS:
        assert tool in TOOLS, f"{name}: unknown Helm tool {tool}"
    for word in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", body):
        assert word in ALL_SKILLS, f"{name}: unknown skill `{word}`"


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_each_skill_checks_access_and_only_reads(name: str) -> None:
    _, body = _skill(name)
    assert TOOL_WORD.findall(body)[0] == "my_access", "my_access is the first call"
    assert not re.search(r"\b(propose|apply)_", body), "a reading skill hands changes over"
    assert "read_sql" not in body or re.search(r"Never use\s+`read_sql`", body)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_no_skill_carries_secrets_or_people(name: str) -> None:
    _, body = _skill(name)
    assert not re.search(r"https?://|cnu_|tok_", body)
    assert not re.search(r"Stjepan|Darko|Ivan|Boban", body)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_each_skill_has_evals(name: str) -> None:
    data = json.loads((SKILLS / name / "evals" / "evals.json").read_text("utf-8"))
    assert data["skill_name"] == name
    assert len(data["evals"]) >= 3
    assert all(e["assertions"] for e in data["evals"])


def test_the_marketplace_lists_the_plugin_at_its_folder() -> None:
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text("utf-8"))
    entry = next(p for p in market["plugins"] if p["name"] == "helm-poslovanje")
    assert entry["source"] == "./plugins/helm-poslovanje"


def test_the_bundle_step_in_akcija_names_real_tools() -> None:
    body = (ROOT / "plugins" / "helm-katalog" / "skills" / "akcija" / "SKILL.md").read_text()
    for tool in TOOL_WORD.findall(body):
        assert tool in TOOLS, f"akcija: unknown Helm tool {tool}"
