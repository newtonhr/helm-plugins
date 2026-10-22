# marina-zahtjev — Marina Stores: od ideje do jasnog zahtjeva, uz Helm

Plugin za **Marina Stores (Lalizas Marina)**, instalira se na Claude račune
zaposlenika. Newton d.o.o. ga održava.

Instalacija u Claude Code: `/plugin install marina-zahtjev --marketplace newtonhr/helm-plugins`.



Jedan skill, `novi-zahtjev`. Kad zaposlenik Marina Storesa kaže Helmu da želi
promjenu na web shopu, skladištu ili blagajni, skill:

1. **Razvrsta** želju: (A) Helm to može odmah — nema zahtjeva; (B) nešto što je
   radilo više ne radi — Helm prvo sam pokuša otkloniti, a prijavu Newtonu piše tek
   ako ne može; (C) novi zahtjev — vođeni razgovor.
2. **Vodi razgovor** — najviše osam pitanja, jedno po poruci, samo o činjenicama i
   odlukama koje zna samo Marina Stores. Nikad ne pita ono što Helm može sam
   provjeriti.
3. **Sam prikuplja dokaze** kroz Helm: stanje sustava, postojeći dijelovi shopa,
   artikli iz primjera (web shop i skladište), narudžbe, zapisi grešaka.
4. **Piše zahtjev** po predlošku, na poslovnom hrvatskom, bez tehničkih riječi, bez
   cijena i sati, bez imena zaposlenika, bez osobnih podataka kupaca.
5. **Isporučuje** kroz Helm ako postoji alat `zahtjev_submit`; inače sprema datoteku
   koju zaposlenik pošalje Newtonu.

## Što skill nikad ne radi

- ne navodi cijenu, sate ni trajanje — to Newton predlaže nakon što pročita zahtjev
- ne čita radne datoteke servera; pretražuje samo dijelove shopa (`modules`, `themes`)
- ne mijenja shop (nijedan `propose_*`) — lane A i B predaju običnom Helm zadatku
- ne kopira osobne podatke kupaca u zahtjev
- ne ocjenjuje kako Marina Stores radi danas

## Ovisnosti

- Konektor **Marina_Ops - Helm** uključen na računu zaposlenika. Bez njega skill staje.
- Razina pristupa zaposlenika u Helmu (`analyst`, `web_ops`, `dev_ops`) određuje
  koje provjere Helm može napraviti. Skill bilježi odbijanja i nastavlja.

## Provjereno 18.09.2026 (razina `analyst`)

Rade: `ping`, `health_check`, `get_shop_config`, `list_configuration`, `search_products`,
`pos_search_articles`, `pos_inventory_summary`, `pos_sync_status`, `list_orders`,
`get_order`, `list_modules`, `search_code`.
Odbijeno: `list_plans` (dev_ops/web_ops), `get_customer_threads` (dev_ops).

## Struktura

```
marina-zahtjev/
  .claude-plugin/plugin.json
  README.md
  skills/novi-zahtjev/
    SKILL.md                          — tijek: triage → intervju → dokazi → zahtjev → isporuka
    references/helm_alati.md          — koji alat za što, razine pristupa, pravila degradacije
    references/pitanja.md             — banka pitanja i popis zabranjenih pitanja
    references/zahtjev_predlozak.md   — predložak zahtjeva i predložak prijave kvara
    references/sto_helm_vec_moze.md   — lista za razvrstavanje (lane A)
```

5. **Odgovara na pitanja analize** (od 0.2.0): kad Newtonova analiza zatraži odgovore
   (e-mail "[Helm zahtjev] ZHT-… · Helm ima pitanja" s poveznicom), skill postavi pitanja
   jedno po jedno, zabilježi odgovore zaposlenika i pošalje ih alatom `zahtjev_answer`;
   analiza se nastavlja sama.

## Verzije
- 0.2.0 (2026-10-13) — odgovaranje na pitanja analize (`zahtjev_answer`, `zahtjev_thread`);
  okidač na poveznicu iz e-maila; provjera otvorenih pitanja na početku razgovora.

- 0.1.0 (2026-09-18) — prva verzija. Isporuka kroz `zahtjev_submit` čeka alat na
  Helmu; do tada datoteka + e-mail. Neovisna recenzija: dva kruga.
