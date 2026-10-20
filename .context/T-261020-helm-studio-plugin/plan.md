**Trebam od Vas: odluke P1–P7 (§1) i GO za dio A. Ništa se ne gradi prije GO.**

# Helm Studio plugin za Claude — plan (20. 10. 2026.)

Radni zadatak: `T-261020-helm-studio-plugin`. Repo: `grgur/helm-plugins`, grana
`claude/project-thread-db29u7`. Server Helm je u `grgur/marina-ops-mcp`.
Ovo je samo plan. Nema koda, nema AI poziva, nema produkcije.

Ocjene dokaza: **[O]** provjerio sam danas, **[I]** slijedi iz provjerenog, **[A]**
pretpostavka (dokument, sjećanje). Dokazi za [O] su u `task.md`.

## 0. Ukratko

- Danas plugin ima jedan skill od 21 retka [O]. On samo kaže „pozovi `studio_znanje`”.
- Novi plugin ima **7 skillova**, po jedan za svaki posao: ulaz, brand i kontekst,
  reklama, oglasi, objave, video, prvi koraci.
- Skill vodi posao korak po korak. **Znanje struke ostaje u Helmu** (`studio_znanje`,
  pravila, primjeri). Skill ga ne kopira, nego ga poziva po imenu teme.
- Zato bez plugina sve i dalje radi. Plugin samo daje bolji tok i bolja pitanja.
- Iz marketingskills (v2.13.0, MIT [O]) uzimamo **oblik** skillova i nekoliko novih
  ideja. Nove ideje idu u Helmove vodiče (dio B), ne u plugin.
- Nit „Marketinško znanje u Studiju” dodaje Vaš priručnik za oglase u Helm: PR #15 [O]
  (vodič `strukture-oglasa`, kampanje, pristup „problem”). Dio B gradi na njemu.

## 1. Odluke za Vas

| # | Pitanje | Prijedlog | Razlog |
|---|---|---|---|
| P1 | Gdje plugin živi? | **U repou `grgur/helm-plugins`** (napravili ste ga 20. 10.). **Odlučeno 20. 10.:** „Nema smisla da to radimo u ovom repo kad imamo repo samo za plugin”. Korijen: `.claude-plugin/marketplace.json`, plugin u `plugins/helm-studio/`. Plugin i ovaj plan preseljeni su iz `marina-ops-mcp`. | Zaposlenici ne trebaju pristup kodu servera (dio G faze 2). Marketplace radi za Claude Code i katalog organizacije [A]. Cijena: test mora čitati teme i alate iz drugog repoa (dio D). |
| P2 | Za koga je plugin? | **Jedan plugin za sve:** Vi, Newton i zaposlenici klijenta. Bez AI troška i bez internih alata u tekstu. | Klijent nikad ne vidi AI trošak [O] (`memory-bank/client-communication.md`). Dva plugina bi se brzo razišla. |
| P3 | Što znači „onboarding”? | **Uvođenje novog klijenta i zaposlenika u Studio**: najkraći put do prvog dobrog seta. | Upstream `onboarding` govori o aktivaciji korisnika u aplikaciji [O]. Za Studio je to isti problem: prvi set mora uspjeti u prvoj sesiji. Savjeti za onboarding na klijentovom shopu nisu posao Studija. |
| P4 | Video | **Scenarij i kadrovi.** Kadrove Studio radi kao slike 9:16 iz pravih fotki. Pravi video ide u fazu 3. | Studio danas ne radi video [O] (vodič `video-scenarij`). Video model je novi dobavljač, novi trošak i nova pravna provjera. |
| P5 | Oglasi na Meti i Googleu | **Plugin radi plan i tjednu provjeru iz brojeva koje korisnik zalijepi.** Nema spajanja na oglasni račun. | Spajanje treba Meta pristup; to je „sloj 5”, izvan dosega [O] (`T-261020-helm-studio-oglasi/task.md`). |
| P6 | Gdje se pamti kontekst klijenta i „naučeno”? | **U brand paketu u Helmu** (dio D faze 2, uz J6 `studio_stil`). | Upstream ga drži u lokalnoj datoteci [O]. claude.ai i Cowork nemaju trajnu datoteku po klijentu [A]. Jedan izvor istine za sve klijente i sve uređaje. |
| P7 | Recenzije i komentari kao temelj oglasa | **Sada: korisnik ih zalijepi u razgovor.** Poslije: provjeriti može li ih Helm čitati iz shopa. | Upstream kaže: bez stvarnih recenzija ne izmišljaj [O]. [A] Ne znam ima li shop modul recenzija s podacima. |

Već odlučeno, samo ugrađujem:
- Kršenje pravila **upozorava autora, ne blokira** (projektna memorija). Nova pravila iz
  dijela B (npr. „AI izgled” teksta) zato su upozorenja.
- Prije `studio_izradi` Claude pita osobu (troši AI) [O] (`STUDIO_INSTRUCTIONS`).
- Lalizas uvijek prvo dobije 4 ponude, pa bira (J6) [O].
- Testovi ne troše AI.

## 2. Kako plugin radi

**Načelo: skill je recept, Helm je kuharica.** Skill kaže redoslijed, pitanja i kada
pitati osobu. Sve brojke, pravila i primjeri dolaze iz Helma.

Zašto tako:
- Promjena vodiča u Helmu odmah stigne do svih, bez nove verzije plugina [I].
- Klijent bez plugina (claude.ai web, drugi MCP klijent) dobije isto znanje [O]
  (upute servera + `studio_znanje`).
- Test može provjeriti da svaka tema iz skilla postoji u Helmu (dio D).

**Što uzimamo od marketingskills (oblik, ne tekst):**

| Upstream obrazac | U pluginu |
|---|---|
| „Before Starting”: 3–5 pitanja prije posla | Svaki skill počinje s „Prije početka”. Pita samo ono što `studio_brand` i shop ne znaju. |
| `product-marketing-context`: jedan dokument koji svi skillovi čitaju | `studio_brand` je taj dokument. Skillovi ga uvijek pozivaju prvi. |
| „Grounded inputs”: svaka ideja navodi izvor | Svaki pristup navodi izvor: činjenica iz kataloga (`studio_provjeri_tekst`), recenzija ili komentar koji je osoba zalijepila. |
| „Learnings” s dokazom i statusom | Odjeljak „naučeno” u brand paketu (dio C). Skill predloži redak, Vi odobrite. |
| Modovi (od nule / iz rezultata / serija) | `studio-reklama` i `studio-oglasi` imaju „nova” i „iz rezultata”. |
| „Related skills” na dnu | Svaki skill kaže koji skill dalje. |
| `evals/evals.json` po skillu | Isto, dio D. |
| Creative review page (HTML za klijenta) | Ne radimo. Galerija i 4 ponude (J6) već služe tome [O]. |

**Što ne uzimamo:** upute za tuđe alate (Remotion, HeyGen, Google Ads CLI), SaaS
primjere, B2B/ABM, poveznice na plaćene usluge autora.

## 3. Skillovi (dio A)

Imena skillova su s prefiksom `studio-`, da se ne sudaraju s marketing-skills.
[O] U mojoj sesiji je marketing-skills 1.9.0 instaliran kao plugin, s temama koje se preklapaju.
Opis svakog skilla kaže „za webshop klijenta preko Helma” i nosi hrvatske i engleske
okidače.

| Skill | Upstream uzor | Kad se pokreće | Što radi, redom | Teme iz Helma |
|---|---|---|---|---|
| `helm-studio` (postoji) | — | Bilo koji Studio posao bez jasnog tipa | Prepozna posao i preda ga pravom skillu. Kaže pravila koja vrijede uvijek. | popis tema |
| `studio-brand` | product-marketing | „tko su nam kupci”, „glas branda”, novi klijent, „zapamti ovo” | Čita `studio_brand`. Pita što nedostaje (publika, problemi, prigovori, jezik kupaca, dokazi). Napiše nacrt promjene brand paketa. Ništa ne sprema sam (P6, dio C). | `psihologija-kupca`, tržište klijenta |
| `studio-reklama` | ad-creative | reklama, oglas, banner, „slike za proizvod” | 1) brand i znanje; 2) činjenice iz `studio_provjeri_tekst`; 3) matrica: kupac × motiv × oblik; 4) 2–5 različitih pristupa s izvorom; 5) provjera teksta dok nije ok; 6) pita osobu; 7) `studio_izradi` → 4 ponude → `studio_odaberi`; 8) „iz rezultata”: zalijepljeni CTR/klikovi → što zadržati, što novo. | `dizajn-reklame`, `kuka-i-poruka`, `pravila-oglasavanja`, `strukture-oglasa` (PR #15) |
| `studio-oglasi` | ads | kampanja na Meti/Googleu, budžet, „isplati li se”, ciljanje | Plan: cilj i mjera, struktura (test i skaliranje), publika, broj koncepata, budžet, retargeting s drugom ponudom, naslov oglasa = naslov stranice. Tjedna provjera iz zalijepljenih brojeva: zadrži, ugasi, povećaj. Kreative predaje skillu `studio-reklama`. | `kampanja`, `pravila-oglasavanja` |
| `studio-objave` | social | objave, kalendar, „što da objavimo”, karusel | Stupovi sadržaja iz brand paketa, tjedni kalendar, tekst po mreži, karusel, ponovna upotreba jedne ideje na više mreža. Slike preko `studio-reklama`. | `tekst-instagram`, `tekst-facebook`, `tekst-tiktok`, `tekst-linkedin`, `kampanja`, `newsletter` |
| `studio-video` | video | reel, TikTok, video reklama, scenarij | Scenarij 15–30 s, kuka u prve 3 s, popis kadrova. Kadrovi iz pravih fotki kao slike 9:16 (P4). Kaže da Studio ne radi video i što snimiti mobitelom. | `video-scenarij`, `tekst-tiktok`, `fotografija-proizvoda` |
| `studio-prvi-koraci` | onboarding | novi klijent ili zaposlenik, „kako počinjem”, prvi put u Studiju | Najkraći put do prvog dobrog seta: provjera pristupa → `studio_brand` → jedan proizvod → 4 ponude → odabir. Sve ostalo kasnije. Za Vas: popis što novi klijent treba (brand paket, fotke, logo). | `dizajn-reklame` |

Svaki skill ima isti kostur, najviše ~80 redaka:
1. **Prije početka** — pitanja (samo ono što Helm ne zna).
2. **Koraci** — pozivi Helmovih alata, redom.
3. **Pitaj osobu** — gdje se staje (trošak AI-ja, odabir ponude, objava).
4. **Nikad** — AI ne crta proizvod, tekst, logo ni cijenu; Studio ne objavljuje; nema
   izmišljenih brojeva, recenzija ni popusta; nema AI troška u tekstu za klijenta.
5. **Dalje** — koji skill slijedi.

**Bez komandi, agenata, hookova i `.mcp.json`.**
- Komande: MCP promptovi (`kampanja`, `objave-za-tjedan`, `reklama-za-proizvod`) već su u
  izborniku [O]; skillovi se i sami pozivaju preko „/”.
- `.mcp.json`: URL konektora je osobna vjerodajnica. Ne smije u plugin (CLAUDE.md).
- Agent „kritičar oglasa”: provjeru već radi server (`studio_provjeri_tekst`) [O].
  Agent bi bio druga, neusklađena provjera.

## 4. Što ide u Helm, ne u plugin (dio B)

Nove ideje iz upstream v2. U vodičima ih danas nema [O] (`grep` u `task.md`).
Usporedio sam s PR-om #15 [O]. On već pokriva strukture oglasa, faze kupnje, vrtuljak i
„AI izgled” slike. Te stavke ovdje izbacujem. Ostaje samo ovo:

| Ideja | Kamo | Kako |
|---|---|---|
| Kuka ima 3 dijela (slika, izgovoreno, natpis). Ne ponavljaju se. Na statičnoj slici naslov ne opisuje sliku. | `video-scenarij`, `dizajn-reklame` | načelo + primjer dobro/loše |
| Matrica kupac × motiv × oblik. Deset kuka za deset ćelija, ne trideset za jednu. | `kuka-i-poruka` | načelo |
| „AI izgled” teksta: „nije X, nego Y”, nizovi negacija, „Rezultat? …”, otrcane fraze, duga crtica u naslovu. | `pravila/tekst.yaml` | upozorenje (`strogo: ne`), uz rečenicu popravka |
| Hipoteza koja može pasti: mjera, usporedba, smjer. | `kampanja` | načelo, polje uz koncept |
| Meta danas: široka publika, kreativa cilja; puno svježih statičnih koncepata; slični oglasi su jedan koncept (već ima [O]). | `kampanja` | načelo |
| Presuda tek nakon ~5 dana ili ~1000 prikaza; zamor kreative; tjedna provjera. | `kampanja` | načelo, s izvorom |
| Retargeting s drugom ponudom; naslov oglasa ponovi naslov stranice. | `kampanja` | načelo |
| Sigurna zona vertikalnog videa. | `pravila/formati.yaml` | broj, nakon usporedbe s postojećim [A] |

Rangovi formata S–F iz upstreama su mišljenje jedne praktičarke [O] (izvor u
`static-ad-templates.md`). Ulaze najviše kao savjet s izvorom, nikad kao pravilo.

## 5. Kontekst klijenta i „naučeno” (dio C)

Ovisi o P6 i o dijelu D faze 2 (brand paket izvan koda).

- Brand paket dobije odjeljke: `publika`, `problemi`, `prigovori`, `jezik_kupaca`,
  `dokazi`, `nauceno`.
- Redak u `nauceno`: učenje (jedna rečenica), dokaz (broj i uzorak), vrijedi za, status
  (`aktivno`, `pratiti`, `ukinuto`). Upstream format [O].
- J6 već sprema odabire i komentare za učenje stila [O] (`studio_stil`). „Naučeno” je
  drugo: pisana pravila koja ste Vi potvrdili.
- Skill `studio-brand` piše nacrt. Spremanje ide kroz alat iz dijela D, uz Vašu potvrdu.
  Bez tog alata nacrt ostaje u razgovoru.

## 6. Testovi i evals (dio D)

**Test u `helm-plugins`, bez AI-ja:** `tests/test_plugin.py`, pokreće ga GitHub Actions.
Popis tema i alata dolazi iz `marina-ops-mcp`: taj repo izvozi `studio-katalog.json`
(teme iz `src/marina_ops/studio/znanje/`, alati iz `src/marina_ops/tools/studio.py`), a test u `helm-plugins` ga čita s `main`.
Ako se katalog promijeni, test u `helm-plugins` pada dok se skill ne uskladi.
- Svaka tema `studio_znanje("…")` u skillu postoji kao vodič.
- Svaki alat `studio_*` u skillu postoji u `tools/studio.py`.
- Nijedna datoteka nema URL konektora, `cnu_`, `tok_` ni ime klijenta.
- Opis skilla je kraći od 1024 znaka i ima prefiks `studio-` u imenu.

**Evals po skillu** (`evals/evals.json`, upstream oblik [O]): upit, očekivanje, provjere.
Primjer: „Napravi reklamu za prsluk 71060” → poziva `studio_brand` prvi; provjeri tekst
prije izrade; pita prije `studio_izradi`; ne spominje AI trošak.
[A] Evals pokreću Claudea i troše Claude tokene. Ne smiju pozvati `studio_izradi`.
Pokrećem ih ručno, ne u CI-ju.

## 7. Dijelovi, redom

| Dio | Što | Veličina | Deploy | Ovisi o |
|---|---|---|---|---|
| A | 7 skillova, plugin 0.4.0, README na hrvatskom | M | 0 | GO |
| D | pytest + evals | S | 0 | uz A |
| B | nove ideje u vodiče i `tekst.yaml` | M | 1, dijeli se sa sljedećim | PR #15 u `main` |
| C | kontekst i „naučeno” u brand paketu | M | 1 | P6, dio D faze 2 |
| E | objava plugina (marketplace, katalog organizacije, zip) | S | 0 | dio G faze 2 |

**Kriteriji.**
- A1: S pluginom, „napravi reklamu za [proizvod]” prođe: brand → znanje → provjera teksta
  → pitanje osobi → 4 ponude → odabir. Bez ijednog izmišljenog broja.
- A2: Uz instaliran marketing-skills, upit o reklami za shop klijenta pokrene
  `studio-reklama`, ne `ad-creative`.
- A3: Bez plugina isti upit i dalje radi preko uputa servera (regresija).
- A4: `studio-video` nikad ne obeća gotov video.
- D1: pytest je zelen i pada kad skill spomene nepostojeću temu ili alat.
- B1: svaka nova tvrdnja u vodiču ima izvor i datum provjere.
- C1: redak „naučeno” bez dokaza se odbija.

## 8. Rizici

- **Sudar okidača s marketing-skills.** Oba plugina reagiraju na „reklama”. Ublažava:
  prefiks, opis „za shop klijenta preko Helma”, kriterij A2.
- **Skill i Helm se raziđu.** Ublažava: skill ne nosi znanje; test D1.
- **Dupli posao s niti priručnika.** Ublažava: dio B kreće tek kad je PR #15 u `main`.
- **Klijent vidi interne stvari.** Ublažava: P2, provjera u evalsima.
- **Instalacija kod klijenta.** [A] Ne znam koji claude.ai plan i organizaciju imaju
  Stjepan i Darko. Rješava dio G faze 2.
- **Upstream se brzo mijenja** (u sesiji 1.9.0, upstream 2.13.0 [O]). Vodiči navode verziju i
  datum; ne pratimo svaku promjenu.

## 9. Grana

- `grgur/helm-plugins`, `claude/project-thread-db29u7`: marketplace, plugin 0.3.0 (preseljen
  bez promjene), dva testa preseljena iz servera, `task.md` i ovaj plan.
- `grgur/marina-ops-mcp`, `claude/project-thread-db29u7` (PR #14): brisanje
  `plugins/helm-studio/` i dviju provjera plugina iz testova servera.
