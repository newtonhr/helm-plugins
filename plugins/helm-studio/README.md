# Helm Studio — plugin za Claude

Sedam skillova vodi posao u Helm Studiju korak po korak. **Znanje struke ostaje u Helmu**
(`studio_znanje`, pravila, primjeri); skillovi ga pozivaju po imenu teme. Bez plugina sve
radi isto, jer Helm sam daje upute i znanje svakom MCP klijentu. Plugin daje bolji tok i
bolja pitanja.

| Skill | Posao | Uzor (marketingskills v2.13.0, MIT) |
|---|---|---|
| `helm-studio` | ulaz: prepozna posao i preda ga | — |
| `studio-prvi-koraci` | novi klijent ili zaposlenik: najkraći put do prvog seta | onboarding |
| `studio-brand` | publika, prigovori, jezik kupaca, dokazi, glas, naučeno | product-marketing |
| `studio-reklama` | reklamne slike: pristupi, provjera teksta, 4 ponude, odabir | ad-creative |
| `studio-oglasi` | plan kampanje na Meti/Googleu i tjedna provjera brojeva | ads |
| `studio-objave` | stupovi sadržaja, kalendar, tekst po mreži, vrtuljak | social |
| `studio-video` | kratki video s pričom: likovi, ključne slike koje osoba odobri, AI kadrovi, montaža | video |

Svaki skill ima `evals/evals.json`: upit, očekivani tok i provjere. Evals pokreću
Claudea i troše Claude tokene; pokreću se ručno. U evalsima `studio_izradi` se ne smije
stvarno pozvati.

Pravila koja vrijede uvijek:

- AI nikad ne crta proizvod, tekst, logo ni cijenu. U videu AI smije samo scenu bez ljudi i
  proizvoda, kad ga vlasnik uključi.
- Brand paket klijenta ima prednost pred vodičem; zakonska pravila vrijede uvijek.
- Prije `studio_izradi` i `studio_video_izradi` Claude pita osobu.
- Studio ništa ne objavljuje. Objavu radi čovjek.

Plugin ne nosi URL konektora. Helm konektor je osobna vjerodajnica i dodaje se zasebno.
