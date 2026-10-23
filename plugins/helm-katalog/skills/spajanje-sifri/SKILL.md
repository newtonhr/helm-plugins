---
name: spajanje-sifri
description: "Marina Stores, Helm. Spajanje više proizvoda u jedan s varijantama, premještanje POS šifre na drugi proizvod ili varijantu, dodavanje artikla iz blagajne kao nove varijante i čišćenje duplikata (WEB-OLD). Prije svakog prijedloga provjerava gdje je šifra sada i što bi se sukobilo. Pokreni za \"spoji proizvode\", \"prebaci šifru\", \"dodaj kao varijantu\", \"duplikat\"."
---

# Spajanje šifri

This is where most refused proposals come from. Check first, propose second.
Talk to the person in Croatian, formal "Vi"; say "šifra", "varijanta", "spajanje".

## Before proposing anything — the pre-check

For every POS code involved:
1. `pos_get_article_by_code` — the code exists in POS and is active.
2. `search_products` / `find_catalog_items` with the code — **which rows carry it now**
   (product reference or combination reference). Write them down.
3. For the target product, `get_product_variants` — its attribute group and the
   existing combinations (so you never create one that already exists).

Then show a small table: code → where it is now → where it will go. Stop and explain
in plain words if:
- the code is on **two** rows already (a duplicate — say which, ask which to keep);
- the target already has a **different** POS code;
- the target already has a combination with the same attribute values;
- the code is not in POS.

## Which move

`propose_move_pos_reference(source, target)`:
- **Merge simple products** into one with variants: first the product that becomes
  the parent, onto itself (`source {"product": P}`, `target {"product": P,
  "new_combination": [value ids]}`), then each other product onto the parent
  (`source {"product": X}`, `target {"product": P, "new_combination": [...]}`). The old
  product is switched off, renamed `WEB-OLD-<code>` and redirected — do not delete it
  and do not rename it yourself.
- **POS article not on the web yet, as a new variant**: `source {"pos_article": "<code>"}`.
  Not `propose_create_combination` (it refuses POS products).
- **Move a combination's code**: `source {"product": id, "combination": id}`.

Missing attribute value (e.g. a new size): `propose_create_attribute_value` first,
approve it alone, then the moves.

## Approval

The parent-onto-itself move must be applied before the others: ask once, then
`apply_plans` with the parent's plan **first** in the list. The others follow in the
same call. The sync brings price and stock within ~5 minutes; tell the person, and
that a moved combination cannot be undone by a button.

If a plan is refused anyway, read the reason, tell the person in one sentence, and
cancel the leftover proposals for that merge with `cancel_plan` rather than leaving
them open.
