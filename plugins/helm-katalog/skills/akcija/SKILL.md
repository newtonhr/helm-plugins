---
name: akcija
description: "Marina Stores, Helm. Popust ili akcijska cijena na više proizvoda za razdoblje: proizvodi, popust (postotak, iznos ili nova cijena) i datumi skupe se jednom, prikaže se tablica stara/nova cijena i sve se odobri jednom. Pokreni za \"akcija\", \"popust\", \"sniženje\", \"posebna cijena za ove artikle do …\"."
---

# Akcija

Talk to the person in Croatian, formal "Vi".

1. **Collect the campaign once**: which products (codes, a category, or a file — for a
   file run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/cjenik_redovi.py <file>`), the discount
   (% or € off, or a new price), from–to dates. Missing dates → ask; never leave an end
   date out without the person saying "bez kraja".
2. **Resolve products** with `search_products` / `get_category_products`. For products
   with variants, ask: whole product or only some variants.
3. **Show the table before proposing**: product, current price, new price, dates. Flag
   anything above 50 % off and any product that already has a discount in that period.
4. On yes, `propose_create_specific_price` per product/variant (`date_to` as
   `YYYY-MM-DD`, it counts to 23:59). Then **one `apply_plans`** for the batch (≤ 50 per
   call; more → several calls, say so).
5. Report applied / refused. The shop caps discounts (default 70 %) and refuses price
   rises and exact duplicates — explain a refusal in one sentence.

Changing or ending an existing discount: `propose_update_specific_price` /
`propose_delete_specific_price`, same one-approval batch.
