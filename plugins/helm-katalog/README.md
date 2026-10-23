# helm-katalog

Samo za Marina Stores: uređivanje kataloga kroz Helm.

Instalacija (Claude Code): `/plugin install helm-katalog --marketplace newtonhr/helm-plugins`

| Skill | Za što |
|---|---|
| `dovrsi-proizvod` | Jedan proizvod do kraja: tekst, polja, svojstva, kategorije, opisi slika — pa **jedno** odobrenje (`apply_plans`). |
| `novi-artikli` | Novi artikli iz cjenika: prvo provjera (već na webu / varijanta postojećeg / nema u blagajni), zatim izrada u seriji. |
| `spajanje-sifri` | Spajanje proizvoda u varijante i premještanje POS šifri, uz provjeru sukoba prije prijedloga. |
| `akcija` | Popust na više proizvoda: tablica stara/nova cijena, jedno odobrenje. |
| `sto-fali` | Što nedostaje u katalogu (`catalog_completeness`), bez ručnog SQL-a. |

**Hook** (`hooks/plan_batch.py`) samo savjetuje, nikad ne blokira i šuti kad nešto ne
radi: pamti otvorene prijedloge i, kad Claude krene odobravati jedan po jedan, podsjeti
ga da ih odobri zajedno; prije `read_sql` uputi na alate za čitanje. Treba `python3`
na računalu korisnika (Cowork ga ima).

**Skripta** `scripts/cjenik_redovi.py <datoteka>`: cjenik (CSV/XLSX) u JSON redove
(`sifra`, `naziv`, `cijena`, `ean`, `lalizas`, `popust`). XLSX treba `openpyxl`.

Nastao iz korištenja Helma 16.–23. 10. 2026.: ~1.000 pojedinačnih odobrenja tjedno,
40 neuspjelih SQL upita i 50 odbijenih prijedloga, većinom kod spajanja šifri. Nakon
tjedan dana provjeriti `usage_report` po osobi: `apply_plans` treba zamijeniti većinu
`apply_plan` poziva.
