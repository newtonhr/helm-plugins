# helm-plugins

Pluginovi za Claude (Claude Code, Cowork, claude.ai) koji rade s Helmom.
Server Helm je u zasebnom repou; ovdje su samo pluginovi.

| Plugin | Što radi |
|---|---|
| [`helm-studio`](plugins/helm-studio/) | Reklame, objave, newsletter i kampanje za webshop klijenta preko Helm Studija (`studio_*` alati). |
| [`marina-zahtjev`](plugins/marina-zahtjev/) | Samo za Marina Stores: vođeni razgovor koji želju ili kvar pretvara u zahtjev za Newton, uz dokaze iz Helma. |
| [`e-commerce-audit`](plugins/e-commerce-audit/) | E-commerce audit: provjera web shopa prema dokazanim praksama velikih trgovaca, izvještaj na hrvatskom i .xlsx popis poslova po učinku i trudu. Samo čita. |

Instalacija, tako da nove verzije stižu same:

- **claude.ai, desktop, Cowork:** Customize › Plugins › Add › Add marketplace ›
  `grgur/helm-plugins`. Uključite **Sync automatically**, pa dodajte `helm-studio`. Repo je
  privatan, pa dijalog traži GitHub račun i Claude GitHub App s pristupom repou.
- **Claude Team (organizacija klijenta):** Owner doda marketplace u postavkama
  organizacije (Plugins & skills) i označi plugin kao *installed by default* ili *required*.
- **Claude Code:** `/plugin marketplace add grgur/helm-plugins`, zatim
  `/plugin install helm-studio@helm-plugins`. U `/plugin` › Marketplaces uključite
  *Enable auto-update*.

Nova verzija stiže samo kad se promijeni `version` u `plugin.json`. Zipovi ostaju za
ručno slanje.

Plugin nosi Helm konektor (`plugins/helm-studio/.mcp.json`, `https://helm.newton.hr/mcp`).
Adresa nije tajna; osoba se prijavi osobnim kodom.

Testovi (bez AI-ja): `uvx pytest -q tests`, a za E-commerce audit `python3 -m unittest discover -s plugins/e-commerce-audit/skills/e-commerce-audit/scripts/tests`. Provjeravaju i da svaka tema i alat koji
skill spomene postoji u Helmu, prema `tests/katalog.json`. Nakon promjene Studija u
`marina-ops-mcp` osvježi katalog: `python3 scripts/katalog.py <putanja do marina-ops-mcp>`.

Plan novog plugina: [`.context/T-261020-helm-studio-plugin/plan.md`](.context/T-261020-helm-studio-plugin/plan.md).
