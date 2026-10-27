# helm-poslovanje

Samo za Marina Stores: pregled poslovanja iz Helma. Samo čita; izmjene radi skill koji je
za to napravljen (`akcija`, `dovrsi-proizvod`, `novi-artikli`, `novi-zahtjev`).

Instalacija (Claude Code): `/plugin install helm-poslovanje --marketplace newtonhr/helm-plugins`

| Skill | Za što |
|---|---|
| `tjedni-pregled` | Jedna stranica za ponedjeljak: narudžbe, web, prodaja, što naručiti, što stoji, katalog, nove greške; usporedba s prošlim tjednom i tri stvari za napraviti. |
| `provjere` | Sedam redovnih provjera koje javljaju samo kad treba nešto napraviti. Svaka ima ritam, uvjet, provjeru prije javljanja i sljedeći korak. |
| `glas-kupca` | Što kupci traže i kako to zovu: pretrage, pretrage bez rezultata, traženi artikli bez zalihe, poruke i recenzije; popis sinonima i rečenice kupaca. |
| `jutarnji-pregled` | Jutarnji pregled za zakazani zadatak u claude.ai: što čeka Vas, jučerašnja prodaja na webu, akcije, rad tima, zahtjevi i katalog na jednoj kratkoj stranici. Ponedjeljkom i tjedni pregled. |
| `uvidi` | Četiri pitanja za upravu: što se prodaje u dućanu a slabo na webu, kako radi tim, je li promjena pomogla i sidrene cijene dok akcija traje. |

Svaki skill prvo pozove `my_access` i preskoči ono što osoba ne smije vidjeti. Web brojke
traže ulogu vlasnika ili analitičara; poruke kupaca puni pristup.

Ideje su prilagođene iz projekata s licencom MIT (vidi `THIRD_PARTY_NOTICES.md` u korijenu
repoa): obrazac provjere i pravilo ritma iz coreyhaines31/marketingskills, e-commerce
pokazatelji iz wondelai/skills (Lean Analytics).
