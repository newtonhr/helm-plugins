---
name: uvidi
description: "Marina Stores, Helm. Uvidi za voditelje koji spajaju blagajnu, web i rad tima u odluku s brojem: što se dobro prodaje u dućanu a na webu je slabo ili ga nema, je li rad tima na proizvodima donio više pregleda, je li neka promjena na webu (checkout, akcija) pomogla, i mijenjaju li se sidrene cijene dok akcija traje. Pokreni za \"uvidi\", \"na čemu tim da radi\", \"je li se isplatilo\", \"je li pomoglo\", \"što se prodaje a nije na webu\". NE pokreći za tjedne brojke (tjedni-pregled) ni za redovne provjere (provjere)."
---

# Uvidi

Four analyses a manager asks for once a month or after a change. Croatian, formal "Vi".
Read-only: each ends with a short list and the skill that does the work.

Call `my_access` first. Website figures (`telemetry_query`, `telemetry_funnel`) need the
business-owner or analyst role; leave out what the person cannot open and say so in one
line. Never use `read_sql` or a grant as a workaround.

## 1. Prodaje se u dućanu, a slabo na webu

`pos_top_movers(days=30, limit=40)`. Rank by value, `units_out × mpc`, never by units: rope
and cable sell by the metre and would fill the list. Take the top 15. For each, find the web
product: `search_products` with two or three words of `naziv_artikla`, then
`get_product_variants` on the hit to match the code (a POS code is often a variant). Report
the ones that are not on the web, are inactive, or miss data (`catalog_completeness` with
the product's category lists what is missing). One line each: name, 30-day value, what is
wrong. Not found by name: say "nije pronađen po nazivu", never "nije na webu". Hand over:
`dovrsi-proizvod`, `novi-artikli`, `spajanje-sifri`.

## 2. Je li se rad tima isplatio

`work_report(days=31)` for the team: the products changed this month. For up to 30 of
them, product page views in the 14 days before the first change and the 14 days after:
`telemetry_query` on `ux.request` (page_type 'product', `is_doc AND status < 400`,
`NOT qa AND NOT is_bot`, grouped by `entity_id` and before/after). Report the total
before and after, and the five biggest gains. Fewer than 14 days after a change: say it is
too early. Views are not sales; say so once.

## 3. Je li promjena pomogla

The person names the change and its date (a new checkout step, an action). Compare the 14
days before with the 14 days after: `telemetry_query` on `ux.event` with kind 'funnel', per
step and day (real rows only: the request of the same day and rid is real, device not
'bot'), and `telemetry_funnel(hours=336)` for the current shape. Report each step's share
before and after. Under 100 sessions on a side: too little to judge, say so. Never claim a
cause; a season or an action can explain it too.

## 4. Sidrene cijene dok akcija traje

`cjenik_anchor_changes(days=30)`. An anchor price or anchor date that changed while an
action ran (see the dashboard's Posao panel or `akcija`) can break the shown "najniža cijena
u 30 dana". For each change, `cjenik_article` on that code shows the days. Report the code,
the change and the action. Hand over: `novi-zahtjev` when the web shows it wrong.

## What Helm cannot answer

The POS has no purchase price: no margin and no "below cost" from Helm. Say so if asked.

## Never

- Never act on one number: show the before and after, or the rank, with the period.
- Never propose, apply or send anything.
- No customer names or e-mails.
