---
name: sto-fali
description: "Marina Stores, Helm. Što nedostaje u katalogu i na čemu raditi sljedeće: koliko je kategorija dovršena, koji proizvodi nisu sređeni i što im fali, odvojeno od podataka koje daje samo dobavljač. Pokreni za \"što fali\", \"koji proizvodi nisu sređeni\", \"koliko je kategorija gotova\", \"na čemu da radim\"."
---

# Što fali

Answer from Helm's read tools, not SQL. Talk in Croatian, formal "Vi".

1. **Category or person given** → `catalog_completeness(category=..., days=1)` (or
   `person=`). It lists, per product, what is still missing ("što nedostaje", up to 60)
   and the category's percentage.
2. **Nothing given** → `catalog_completeness()` and show the 5 weakest categories with
   their percentage; ask which one to take.
3. **A specific gap across products** (no brand, no EAN, no default category, no image
   caption) → `find_catalog_items` / `get_category_products`, then `get_product_details`
   for the candidates.
4. Group the answer by what **the person can fix** vs **"podaci dobavljača"** (EAN,
   weight, supplier features — only the supplier can give those). Do not list the
   supplier ones as work for the person.
5. Offer the next step: "Želite li da sredimo ove proizvode jedan po jedan?" → hand over
   to `dovrsi-proizvod` with the list.

If `catalog_completeness` is refused (no permission), say so plainly and continue with
step 3; do not try `read_sql` as a workaround.

The snapshot is taken once a day (afternoon), so today's work shows tomorrow — say so
when the person expects to see their progress immediately.
