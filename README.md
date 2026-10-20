# helm-plugins

Pluginovi za Claude (Claude Code, Cowork, claude.ai) koji rade s Helmom.
Server Helm je u zasebnom repou; ovdje su samo pluginovi.

| Plugin | Što radi |
|---|---|
| [`helm-studio`](plugins/helm-studio/) | Reklame, objave, newsletter i kampanje za webshop klijenta preko Helm Studija (`studio_*` alati). |

Instalacija u Claude Code: `/plugin marketplace add grgur/helm-plugins`, zatim
`/plugin install helm-studio@helm-plugins`. Plugin ne nosi URL konektora; konektor
Helma dodaje se zasebno.

Testovi (bez AI-ja): `uvx pytest -q tests`. Provjeravaju i da svaka tema i alat koji
skill spomene postoji u Helmu, prema `tests/katalog.json`. Nakon promjene Studija u
`marina-ops-mcp` osvježi katalog: `python3 scripts/katalog.py <putanja do marina-ops-mcp>`.

Plan novog plugina: [`.context/T-261020-helm-studio-plugin/plan.md`](.context/T-261020-helm-studio-plugin/plan.md).
