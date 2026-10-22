# What Helm already does — lane A triage list

If the colleague's wish is on this list, no request to Newton is needed. Say so
in one sentence and offer to do it as a normal Helm task (outside this skill,
with the usual approval step). Sentences to use are in the right column.

## Answers from data (no approval needed)

| Wish sounds like | Helm does it now | Say |
|---|---|---|
| "koliko imamo na zalihi", "što treba naručiti", "što se ne miče", "prodajemo li ispod nabavne", "što se najbolje prodaje", "što se promijenilo u cijeni" | warehouse and POS analytics (`pos_*` tools) | "To Vam mogu odgovoriti odmah — želite li za cijeli asortiman ili za određene artikle?" |
| "koje narudžbe su stigle", "što je s narudžbom X" | `list_orders`, `get_order` | "Evo — …" |
| "postoji li artikl X na shopu", "koja mu je cijena" | `search_products`, `get_product`, `pos_search_articles` | "Provjerio sam: …" |
| "radi li shop", "je li nešto palo" | `health_check`, `list_recent_errors` | "Sustav radi / vidim ove greške: …" |
| "kada se zadnji put sinkronizirala blagajna" | `pos_sync_status` | "Zadnja sinkronizacija …" |
| tjedni / mjesečni pregled zaliha i prodaje | `pos_inventory_summary`, `pos_top_movers`, `pos_dead_stock`, `pos_price_changes` | "Mogu sastaviti pregled — za koje razdoblje?" |

## Changes Helm performs with approval (propose → review → apply)

| Wish sounds like | Helm does it now | Say |
|---|---|---|
| "promijeni cijenu artikla X" | `propose_update_product_price` (within the configured limit) | "Mogu predložiti promjenu; potvrđuje je osoba s pravom odobrenja." |
| "postavi zalihu na …" | `propose_update_product_stock` (within limit) | same |
| "označi narudžbu kao …" (not cancelled/refunded) | `propose_update_order_status` | same |
| "dodaj bilješku na narudžbu" | `propose_add_order_note` | same |
| "stranica prikazuje staro / osvježi prikaz" | `propose_clear_page_cache`, `propose_clear_smarty_cache`, `propose_flush_memcached` | "Vjerojatno je predmemorija — mogu je osvježiti." |
| "isključi / uključi dio shopa X" | `propose_disable_module` / `propose_enable_module` (technical level) | "To je tehnička razina — mogu predložiti, potvrđuje uprava." |
| "pokreni sinkronizaciju s blagajnom" | `propose_pos_sync` | same |
| "promijeni postavku X" | `propose_set_configuration` | same |

## Operations Helm performs directly (technical level)

| Wish sounds like | Helm does it now |
|---|---|
| "napravi sigurnosnu kopiju", "je li kopija u redu" | `create_db_backup`, `verify_backup_integrity`, `list_db_backups` |
| "shop je spor", "što se događa sa serverom" | `diagnose_performance`, `get_service_status` |

## Lane B — something that worked has stopped

Helm tries first. Hand off to a normal Helm task: check `health_check`,
`list_recent_errors`, `search_logs`, the module's state, the cache — and repair where
Helm is allowed to (cache, module state, a setting, a restore from backup at the
technical level). Only when Helm cannot put it right does the colleague get a
**Prijava kvara** for Newton, with the evidence Helm already collected.

## Lane C — a request to Newton

- a capability the shop does not have today: a new page, field, rule, or a report
  Helm cannot assemble from existing data
- a new connection between the shop and another system (POS, SAP, a supplier, a
  payment provider) or a change in how an existing connection works

## Neither A nor C — Helm refuses by design; the decision belongs to the management

- changes above the configured limits (large price or stock moves) — the limit itself
  is a management decision, not a request to Newton
- cancelling or refunding orders — stays manual by design
- deleting products permanently — technical level, with a backup first
Say so in one sentence and stop; do not write a request.

A change of look, text, visibility or behaviour that Helm can perform today is lane
A, even in areas where Newton has delivered projects (search, images, translations,
customer accounts). Lane C is for what the shop cannot do yet.

## How to hand off from lane A

Say what you would do, in one sentence, and ask for a yes. Then leave this skill —
the actual change runs as a normal Helm task with its own approval. Never combine
"I will do X now" with "and I will also write a request".
