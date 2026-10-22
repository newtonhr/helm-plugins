"""Checks on the helm-studio plugin.

The plugin stays thin: its skills say the order of the work and when to ask the person;
the trade knowledge lives in Helm (studio_znanje). Every topic and tool a skill names must
exist in the server (tests/katalog.json, written by scripts/katalog.py).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "helm-studio"
SKILLS = PLUGIN / "skills"
KATALOG = json.loads((ROOT / "tests" / "katalog.json").read_text("utf-8"))
TOPICS = set(KATALOG["teme"]) | set(KATALOG["na_cekanju"])
TOOLS = set(KATALOG["alati"])
MCP_PROMPTS = {"kampanja", "objave-za-tjedan", "reklama-za-proizvod"}
EXPECTED = {"helm-studio", "studio-brand", "studio-reklama", "studio-oglasi",
            "studio-objave", "studio-video", "studio-prvi-koraci", "studio-galerija",
            "studio-animacija"}


def _skill(name: str) -> tuple[dict[str, str], str]:
    text = (SKILLS / name / "SKILL.md").read_text("utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    assert m, name
    meta = dict(line.split(": ", 1) for line in m.group(1).splitlines())
    return meta, m.group(2)


def test_the_plugin_has_one_skill_per_job() -> None:
    assert {p.name for p in SKILLS.iterdir()} == EXPECTED


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_each_skill_is_named_and_described_for_helm(name: str) -> None:
    meta, body = _skill(name)
    assert meta["name"] == name
    assert meta["description"].startswith("Helm Studio")
    assert len(meta["description"]) < 1024
    assert "Helm" in meta["description"] and "webshop" in meta["description"]
    assert len(body.split()) < 450, "the skill carries knowledge that belongs in Helm"
    assert "studio_brand" in body


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_every_topic_and_tool_a_skill_names_exists_in_helm(name: str) -> None:
    _, body = _skill(name)
    for topic in re.findall(r'studio_znanje\("([^"]+)"\)', body):
        assert topic in TOPICS, f"{name}: unknown topic {topic}"
    for word in re.findall(r"`([a-z]+(?:-[a-z]+)+)`", body):
        assert word in TOPICS | MCP_PROMPTS | EXPECTED, f"{name}: unknown `{word}`"
    for tool in re.findall(r"\bstudio_[a-z_]+", body):
        assert tool in TOOLS, f"{name}: unknown tool {tool}"


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_no_skill_carries_secrets_client_names_cost_or_sizes(name: str) -> None:
    _, body = _skill(name)
    assert not re.search(r"https?://|cnu_|tok_|/c/", body)
    assert not re.search(r"Lalizas|Marina Stores|Stjepan|Darko", body)
    assert "studio_potrosnja" not in body
    assert not re.search(r"troši kredit|kredite paketa|cijena AI", body)
    assert not re.search(r"\b\d{3,4}\s*[x×]\s*\d{3,4}\b", body)


def test_the_entry_skill_points_at_helm_and_the_copy_check() -> None:
    _, body = _skill("helm-studio")
    assert "studio_znanje" in body
    assert "prednost" in body
    assert "studio_provjeri_tekst" in body


def test_the_ad_skill_checks_the_copy_and_asks_before_spending() -> None:
    _, body = _skill("studio-reklama")
    check = body.index("studio_provjeri_tekst(proizvodi, pristupi")
    ask = body.index("**Pitaj osobu**")
    make = body.index("studio_izradi(")
    wait = body.index("studio_cekaj(posao)")
    assert check < ask < make < wait
    assert body.index("studio_odaberi") > make
    assert "nijedna" in body and "čekaj „da”" in body


def test_the_video_skill_draws_frames_checks_asks_then_cuts() -> None:
    _, body = _skill("studio-video")
    frames = body.index("studio_video_kadrovi(knjiga)")
    approve = body.index("odobri=[kf_")
    check = body.index("studio_video_provjeri(knjiga)")
    ask = body.index("**Pitaj osobu**")
    make = body.index("studio_video_izradi(knjiga)")
    wait = body.index("studio_cekaj(posao)")
    assert frames < approve < check < ask < make < wait
    assert "Čekaj „da”" in body
    assert "studio_izradi(" not in body
    assert "pristan" in body and "AI ne crta tekst, logo ni cijenu" in body


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_each_skill_has_evals(name: str) -> None:
    data = json.loads((SKILLS / name / "evals" / "evals.json").read_text("utf-8"))
    assert data["skill_name"] == name
    assert len(data["evals"]) >= 2
    for e in data["evals"]:
        assert e["prompt"] and e["expected_output"] and e["assertions"]


def test_the_marketplace_lists_the_plugin_at_its_folder() -> None:
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text("utf-8"))
    [entry] = [p for p in market["plugins"] if p["name"] == "helm-studio"]
    assert (ROOT / entry["source"]).resolve() == PLUGIN
    manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text("utf-8"))
    assert manifest["name"] == "helm-studio"


def test_the_plugin_carries_only_the_shared_helm_url() -> None:
    """The Helm URL is the same for everyone; the person logs in with a personal code.
    A personal connector link (/c/cnx_…) or token must never ship in the plugin."""
    text = (PLUGIN / ".mcp.json").read_text("utf-8")
    servers = json.loads(text)["mcpServers"]
    assert servers == {"helm": {"type": "http", "url": "https://helm.newton.hr/mcp"}}
    assert not re.search(r"cnx_|cnu_|tok_|/c/", text)


def test_the_gallery_skill_prices_asks_then_makes_without_text() -> None:
    _, body = _skill("studio-galerija")
    price = body.index("studio_tokeni")
    ask = body.index("**Pitaj osobu**")
    make = body.index('studio_izradi(proizvodi, vrsta="galerija"')
    wait = body.index("studio_cekaj(posao)")
    assert price < ask < make < wait
    assert "Nema teksta, cijene ni loga" in body
    assert "Ilustracija u upotrebi" in body


def test_the_animation_skill_shows_the_key_frame_before_it_spends() -> None:
    _, body = _skill("studio-animacija")
    price = body.index("studio_tokeni")
    ask = body.index("**Pitaj osobu**")
    draw = body.index("studio_animacija(proizvod")
    approve = body.index("odobri=[kf_")
    wait = body.index("studio_cekaj(posao)")
    assert price < ask < draw < approve < wait
    assert "Čekaj „da”" in body
    assert "prave fotke" in body or "pravu fotku" in body
