# Predložak — Zahtjev za Newton

Fill every section, in this order and with these numbers. Where a section is
genuinely empty, write one line saying so ("Nema vanjskih strana."). Business
Croatian. Technical identifiers (ids, codes, module names, settings) appear only in
sections 9 and 11.

```markdown
# Zahtjev: <poslovni naziv promjene, bez imena dobavljača i proizvoda>

Podnosi: <uloga — npr. administrator web shopa>   Datum: <YYYY-MM-DD>
Vrsta: Novi zahtjev

## 1. Što nas je potaknulo
<2–4 rečenice: zadnja konkretna situacija, koliko često se ponavlja>

## 2. Kako to radimo danas
<tko (uloga), kojim koracima, koliko traje, gdje stoje podaci — činjenice, bez ocjene>

## 3. Što želimo da bude drugačije, i kako ćemo znati da radi
Odnosi se na: <samo naziv web shopa, npr. „MARINA Stores WEBSHOP"; ili „sve shopove">
Drugačije: <1–3 rečenice u riječima podnositelja>
Znat ćemo da radi kad:
- <provjerljiva rečenica — što netko vidi ili dobije>
- <…>

## 4. Stvarni primjeri
| Primjer | Što je Helm našao |
|---|---|
| Šifra 92250 | Web shop: nije objavljen. Skladište: Sidro Bruce inox 10 kg, zaliha 6, u dolasku 10 (30.10.). |
| Narudžba 4400 | 17.9., status poslano, 25,00 EUR, 1 stavka. |
| <datoteka / poveznica> | priložena / opisana |

## 5. Naše odluke
| Odluka | Odgovor Marina Storesa |
|---|---|
| <npr. Što kad artikl nema šifru u blagajni?> | <preskočiti i javiti administratoru> |
| <…> | <…> |

## 6. Što nam ne treba
- <dio koji je podnositelj svjesno ispustio, s jednom rečenicom zašto>
- <…>

## 7. Vanjske strane i rokovi
- Vanjski sustav / dobavljač: <naziv, što imamo od njih — dokument, primjer, kontakt (uloga)>
- Rok: <zakonski / grupni / nema roka> — <što se događa ako se propusti>
- Razdoblja kad promjena ne dolazi u obzir: <…>

## 8. Što Marina Stores priprema
- <radni nalog u prvom licu množine, npr. „Pripremit ćemo popis 20 stvarnih pretraga koje kupci upisuju."">

## 9. Što je Helm provjerio
| Provjera | Alat | Nalaz |
|---|---|---|
| Stanje sustava | health_check | shop i baza rade, bez grešaka |
| Postojeći dijelovi shopa | list_modules | <relevantni moduli i na kojim shopovima> |
| Koji web shopovi postoje | get_shop_config PS_SHOP_NAME | <popis> |
| Postoji li već ova funkcija | search_code „<pojam>" (modules, themes) | <0 pogodaka / nađeno u …> |
| Koliko je toga | pos_search_articles (filter …) total / pos_inventory_summary | <npr. 412 od 14.500 artikala bez cijene> |
| Artikli iz primjera | search_products, pos_search_articles | <sažetak> |
| Narudžbe iz primjera | get_order | <sažetak> |
| <…> | <…> | <nije dostupno mojoj razini pristupa (analyst)> |

## 10. Otvoreno
Za Newton:
- <što podnositelj nije znao odgovoriti — najviše pet stavki>
Za dobavljača / vanjski sustav:
- <pitanja koja može odgovoriti samo dobavljač — Newton ih prosljeđuje>
Za pravnu službu ili grupu:
- <pitanja koja može odgovoriti samo pravna služba ili Lalizas grupa>

## 11. Podaci o zahtjevu
- Web shop: <naziv i id iz PS_SHOP_NAME>
- Razina pristupa podnositelja u Helmu: <analyst / web_ops / dev_ops>
- Alati koje je Helm pozvao: <broj>; odbijeni: <popis ili „nijedan"">
- Verzija: marina-zahtjev 0.1.0 / novi-zahtjev
```

---

# Predložak — Prijava kvara (lane B)

Shorter. Same language rules. Newton treats this as a defect report, not a request.

```markdown
# Prijava kvara: <što ne radi, poslovnim riječima>

Podnosi: <uloga>   Datum: <YYYY-MM-DD>
Vrsta: Kvar na postojećoj funkciji

## Što ne radi
<1–3 rečenice: što se očekuje, što se umjesto toga događa>

## Kad je zadnji put radilo
<datum ili „ne znamo"; što se od tada promijenilo, ako podnositelj zna>

## Kako ponoviti
1. <korak>
2. <korak>
3. <što se vidi>

## Primjeri
| Primjer | Što je Helm našao |
|---|---|
| Narudžba <broj> | <status, iznos, stavke> |
| Šifra <kod> | <web shop / skladište> |

## Što je Helm pokušao
| Korak | Ishod |
|---|---|
| <npr. osvježavanje predmemorije> | <nije pomoglo / popravak nije dostupan mojoj razini pristupa (analyst)> |
| <…> | <…> |

## Što je Helm provjerio
| Provjera | Alat | Nalaz |
|---|---|---|
| Stanje sustava | health_check | <…> |
| Zapisi grešaka | search_logs „<tekst greške>" (prestashop, php-fpm) | <broj pogodaka, prvi redak / nije dostupno> |
| Uključeni dijelovi | list_modules / get_module „<naziv>" | <…> |

## Koliko smeta
<koga pogađa, koliko često, postoji li zaobilazni način>

## Podaci o prijavi
- Razina pristupa u Helmu: <…>
- Verzija: marina-zahtjev 0.1.0 / novi-zahtjev
```
