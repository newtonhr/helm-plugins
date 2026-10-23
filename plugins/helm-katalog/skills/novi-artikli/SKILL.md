---
name: novi-artikli
description: "Marina Stores, Helm. Dodavanje novih proizvoda na web iz cjenika dobavljača, Lalizas kataloga, tablice (CSV/XLSX) ili popisa POS šifri: prvo provjera je li artikl već na webu, je li varijanta postojećeg i postoji li u blagajni, zatim izrada u seriji uz jedno odobrenje. Pokreni za \"dodaj nove artikle\", \"novi proizvodi iz cjenika\", \"stavi ovo na web\"."
---

# Novi artikli

Talk to the person in Croatian, formal "Vi", plain words.

## Steps

1. **Get the list.** A file (CSV/XLSX) or pasted rows. For a file, run
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/cjenik_redovi.py <file>`: it prints one JSON
   row per article (`sifra`, `naziv`, `cijena`, `ean`, ...) and lists the rows it could
   not read. Show the person how many rows were read and which were skipped.
2. **Duplicate check, every row, before anything is created:**
   - `pos_get_article_by_code` — is the code in POS at all? Not in POS → the shop
     cannot sell it; tell the person and leave the row out.
   - `search_products` with the code — is it already on the web (as a product or a
     combination)? Already there → it is not new: offer `dovrsi-proizvod` instead.
   - Same product in another size/colour already on the web (same name stem)? → it
     should be a new combination of that product, not a new product: use
     `spajanje-sifri` (adding an ERP article: `{"pos_article": "<code>"}`).
3. **Show the triage**: new / already on the web / variant of an existing one / not
   in POS. Ask which to continue with.
4. **Create** with `propose_create_product` (POS code as reference, so the sync matches
   it). A grouped product with no single POS code gets a `WEB-<BREND>-<OPIS>` reference.
   Then, for each new product, the same finishing steps as `dovrsi-proizvod`
   (text, fields, features, categories) — proposed, not approved yet.
5. **One approval per product** (or per ≤ 5 products): summary table, one question,
   one `apply_plans`.
6. New products start **inactive** unless the person says otherwise; tell them which
   ones still need photos (`create_image_upload_link` gives them a link to upload).
