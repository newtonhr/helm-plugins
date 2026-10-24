---
name: studio-reklama
description: Helm Studio — reklamne slike i oglasi za proizvode iz webshopa klijenta, iz pravih fotografija (studio_izradi). Pokreni kad korisnik u Helm Studiju traži reklamu, oglas, banner, sliku proizvoda za Instagram ili Facebook, ili nove verzije oglasa za shop klijenta. Only when working through Helm Studio.
---

# Reklama za proizvod

Svaka ideja ima izvor: činjenica iz trgovine, ili recenzija i komentar koje je osoba
dala. Bez izvora nema ideje.

## Prije početka

Pitaj samo što ne znaš:
- koji proizvodi (id ili naziv);
- povod: sezona, akcija, novi proizvod;
- recenzije, pitanja kupaca ili komentari ispod starih oglasa, ako ih imaju. Zalijepe ih
  u razgovor.

## Koraci

1. `studio_brand`, zatim `studio_znanje("dizajn-reklame")`, `studio_znanje("kuka-i-poruka")`
   i `studio_znanje("strukture-oglasa")`.
2. `studio_provjeri_tekst(proizvodi)`: dobiješ činjenice trgovine (opis, cijena, pravi
   popust). Samo njih smiješ tvrditi. Popust postoji samo ako ga trgovina daje.
3. Napiši 2–5 **različitih** pristupa po vodičima iz koraka 1. Svaki: naslov, poruka,
   izvor.
4. `studio_provjeri_tekst(proizvodi, pristupi=…)`. Popravi sve što kaže `popravak`, dok
   nije `ok: true`. Upozorenja reci osobi.
5. **Pitaj osobu** u jednoj poruci, s prijedlogom za svako: poruka, formati, a za
   proizvod s pravim popustom prikaz u € ili %. Reci cijenu: jedan set po proizvodu, a
   kad setova nema, tokeni (`studio_tokeni`). Izrada počinje tek kad potvrde.
6. `studio_izradi(…, pristupi=…)`, pa `studio_cekaj(posao)` dok ne kaže gotovo. Pokaži
   sliku.
7. Ako `studio_brand` ima `ponude`: Studio prvo da do 4 male ponude. Pitaj koju žele
   (A–D) i imaju li komentar. Ako komentar traži novu scenu ili kažu „nijedna”, ponovi
   što će se napraviti i čekaj „da”. Zatim `studio_odaberi` i `studio_cekaj`.
   Ako nema `ponude`, nema odabira.
8. `studio_status` za rezultat provjera svake slike. Na kraju poveznicu iz
   `studio_galerija` daj osobi koja je tražila. Podsjeti je na AI oznaku pri objavi.

Ispravak jedne slike: `studio_ispravi`. Prvih 5 ispravaka je besplatno, svaki sljedeći
košta kao nova slika (najviše 10). Prije plaćenog ispravka reci cijenu i čekaj „da”.
Stare verzije ostaju: `studio_cekaj` ih daje u `starije_verzije`, galerija ih pokazuje.
Prvo predloži fotku iz banke (`studio_pozadine`), jer ne treba AI. Za novu AI scenu
pitaj osobu.
Komentar mijenja samo scenu, nikad proizvod. Kad osoba traži proizvod u upotrebi
(„stavi gumenjak na more”, „neka ga netko drži”), pošalji i `nacin="u_upotrebi"`: tada
AI crta i proizvod. Reci osobi da ga usporedi s pravom fotografijom po popisu iz
`popravak` provjere `proizvod_ai`.

## Iz rezultata

Kad osoba zalijepi brojeve po oglasu (prikazi, klikovi, kupnje):
1. Usporedi pristupe. Reci zašto misliš da je jedan bolji, i da je to procjena.
2. Prag za presudu uzmi iz `studio_znanje("kampanja")`. Ako ga vodič nema, reci da je
   presuda rana; ne izmišljaj broj.
3. Novi krug: zadrži najbolji pristup, promijeni jednu stvar, dodaj jedan nov pristup.
4. Ako se obrazac ponavlja, predloži redak za „naučeno” (`studio-brand`).

## Nikad

- AI ne crta tekst, logo ni cijenu. Proizvod crta samo `u_upotrebi`.
- Nema izmišljenih brojeva, normi, recenzija ni popusta.
- Ne spominji AI kredite ni naš trošak u eurima.
- Studio ne objavljuje.

## Dalje

`studio-objave` za tekst objave i raspored, `studio-oglasi` za kampanju.
