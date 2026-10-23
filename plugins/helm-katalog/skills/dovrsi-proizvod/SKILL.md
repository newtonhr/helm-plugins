---
name: dovrsi-proizvod
description: "Marina Stores, zaposlenici koji uređuju katalog kroz Helm. Sređivanje jednog ili više postojećih proizvoda na webu u jednom prolazu: tekst, polja (EAN, težina, dimenzije, marka), svojstva, kategorije, opisi slika i varijante, pa jedno odobrenje po proizvodu. Pokreni za \"sredi proizvod\", \"dovrši\", \"uredi opis i svojstva\" ili kad korisnik zalijepi POS ili Lalizas šifru i želi potpun proizvod. NE pokreći za cijene i zalihu (dolaze s blagajne) ni za popuste (akcija)."
---

# Dovrši proizvod

Goal: take ONE product from "partly filled" to "complete" in one pass, and ask the
person for approval **once per product**, not once per change.

Talk to the person in Croatian, formal "Vi", short sentences, no technical terms
(say "prijedlog", "odobrenje", never "plan", "apply", "API").

## Steps

1. **Find the article.** By POS code `pos_get_article_by_code`; by Lalizas code
   `pos_get_article_by_lalizas_code`; by words `pos_search_articles`. If none of those
   finds it, say so and ask for another code — do not guess.
2. **Find the web product** with `search_products` (reference = POS code) and read it
   with `get_product_details`. If there are two candidates (an old one and a new one),
   stop: that is a merge — switch to the `spajanje-sifri` skill.
3. **Gap list.** Compare against the checklist below and show the person a short list:
   what is missing, what you will propose. Use the supplier's data (POS, the Lalizas
   catalogue the person gives you); never invent technical values (dimensions,
   weight, power, EAN). Missing supplier data → write "nedostaje od dobavljača" and
   leave it.
4. **Propose everything for that product**, without approving anything in between:
   - text: `propose_update_product_text` (name, description_short, description,
     meta_title, meta_description)
   - fields: `propose_update_product_fields` (ean13, weight, width/height/depth,
     id_manufacturer)
   - features: `propose_update_product_features`
   - categories: `propose_update_product_categories` (one correct default category)
   - image captions: `propose_update_image_legends`
   - variants only if needed: `propose_update_combination` / `propose_update_product_variants`
   Collect every returned plan id.
5. **One summary, one question.** Show a table: change → what it does. Ask:
   "Odobravate li ove izmjene za <naziv>?"
6. **On yes: one `apply_plans`** with all the plan ids for that product. Never call
   `review_plan` + `apply_plan` one by one for them.
7. Report per plan: applied / refused. A refused one: read its reason, fix, propose
   only that one again, and ask again for that one only.
8. Next product. For a list of products, finish one fully before starting the next;
   at most ~5 products per `apply_plans` call (it takes at most 50 plans).

## Checklist — a product is complete when

- Name: brand + product type + key spec (e.g. "Lofrans vitlo X1 Alu 12V 500W 6mm").
- Short description: 1–2 sentences, what it is and for whom.
- Description: use, features list, technical data, what is in the package.
- Meta title ≤ 60 characters, meta description ≤ 160.
- Brand set (`id_manufacturer`), EAN, weight and dimensions when the supplier gives them.
- Features filled for this category's feature set (look at 2–3 complete products in
  the same category with `get_category_products` + `get_product_details` and match them).
- Exactly one sensible default category, plus the parent categories the shop uses.
- Every image has a caption (product name + variant).

## Do not

- Do not approve plans one at a time.
- Do not write SQL to find products; `find_catalog_items`, `search_products` and
  `get_category_products` cover it. If you truly need something else, tell the person
  what you were looking for — that is a missing tool, worth reporting.
- Do not change prices or stock here (prices come from POS; discounts → `akcija`).
