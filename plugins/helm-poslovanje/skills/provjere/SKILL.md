---
name: provjere
description: "Marina Stores, Helm. Redovne provjere trgovine koje javljaju samo kad treba nešto napraviti: zaliha koja nestaje, velike promjene i greške u cijenama, katalog koji pada, nove greške na webu, roba koja stoji, pretrage bez rezultata i traženi artikli kojih nema. Pokreni za \"provjere\", \"ponedjeljak provjera\", \"javi mi kad\", \"prati zalihu\", \"što trebam pogledati ovaj tjedan\". NE pokreći za jednokratni izvještaj (tjedni-pregled)."
---

# Provjere

A check looks often but speaks rarely. Most runs end with "Nema ništa za napraviti" in
one line. Talk in Croatian, formal "Vi". Read-only: a check never proposes a change; it
hands the work to the skill that makes it.

Call `my_access` first and skip a check whose tool the person cannot open; list it at the
end. Never use `read_sql` or a grant as a workaround.

## Each check has seven parts

**Kada** (how often it looks; match it to how fast the thing changes) · **Djeluje kad**
(what must be true to report anything) · **Poziv** · **Provjera prije** (rule out noise
before reporting) · **Pamćenje** · **Stani** (when to skip or hand over) · **Ishod**.

**Pamćenje without files:** each check reads only its own window (the last 7 days for a
weekly check), so the same item is never reported twice and nothing must be saved.

## The checks

| # | Check | Kada | Poziv | Djeluje kad | Provjera prije | Ishod |
|---|---|---|---|---|---|---|
| 1 | Zaliha nestaje | weekly | `pos_stockout_risk(days=30, max_days_of_cover=7)` | under 7 days of stock and nothing on its way | `pos_article_history` on the top 3: one big order is not demand | List to order |
| 2 | Cijene | weekly | `pos_price_changes(days=7, min_change_pct=10)`, `pos_price_check()` | a change of 10 % or more, or a broken price | `get_product_details`: an ended discount is not a price change | List for whoever keeps prices in the till |
| 3 | Katalog | weekly | `catalog_completeness(days=7)` | the percentage fell, or a category lost criteria | the snapshot is daily; today's work shows tomorrow | → `sto-fali` |
| 4 | Greške na webu | daily, only if asked | `telemetry_errors(hours=24)` | a group first seen in the window with 20+ events, or any error on checkout or payment pages | `telemetry_error_detail` on it: one browser or one bot is noise | → `novi-zahtjev` |
| 5 | Roba stoji | monthly | `pos_dead_stock(days=90)` | locked value grew since last month (ask the person for last month's figure, or skip the comparison) | not a seasonal item out of season | → `akcija` |
| 6 | Pretrage bez rezultata | weekly | `telemetry_overview(hours=168)` → `sales.zero_result_terms` | a term searched 5+ times | `search_products` with that word: do we have it under another name? | → `glas-kupca` |
| 7 | Traže, a nema | weekly | `telemetry_overview(hours=168)` → `sales.out_of_stock_views` | a product with 50+ views while out of stock | `get_product_details`: that variant may be back in stock | Order it or link a substitute (`dovrsi-proizvod`) |

## Which checks run when

- **Ponedjeljak** (default when the person just says "provjere"): 1, 2, 3, 6, 7.
- **Prvi u mjesecu**: add 5.
- **Svaki dan**: only 4, and only when the person asks for it.

Do not run every check every day. A check that speaks too often gets ignored.

## Running on a schedule

If the Claude the person uses offers scheduled tasks, suggest one: "Pokreni provjere"
every Monday at 8:00. Otherwise the person starts it by hand on Monday. The value is the
same checks every week, not the automation.

## The answer

Only the checks that found something, each as: what, how many, the top 3, the next step
(which skill or who). Then one line: "Ostale provjere: nema ništa." Then the skipped
checks, if any.

## Never

- Never act on a single data point: run the "Provjera prije" step first.
- Never propose, apply or send anything from a check.
- No customer names or e-mails.
