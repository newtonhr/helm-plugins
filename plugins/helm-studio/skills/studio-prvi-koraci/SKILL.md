---
name: studio-prvi-koraci
description: Helm Studio — prva sesija u Helm Studiju za novog klijenta ili zaposlenika webshopa: najkraći put do prvog dobrog seta reklama. Pokreni kad netko prvi put koristi Helm Studio ili pita „kako počinjem u Studiju”. First Helm Studio session only.
---

# Prvi koraci u Studiju

Cilj: prvi dobar set u prvoj sesiji. Sve ostalo čeka. Svaki korak koji nije nužan za
prvi set preskoči.

## Koraci

1. **Pristup.** Pozovi `studio_brand`. Ako alat javi grešku, reci da Studio trenutno nije
   dostupan i prenesi poruku greške.
2. **Spremnost.** Ako `generation` nije `spremno`, reci da izrada slika trenutno ne radi.
   Ne pitaj za proizvod.
3. **Brand paket.** Ako je `provisional: true` ili je `voice` prazan: pokreni
   `studio-brand`. Vrati se ovdje kad nacrt postoji.
4. **Jedan proizvod.** Pitaj za jedan proizvod koji se dobro prodaje ili koji sada žele
   gurati. Više proizvoda ide u drugi krug.
5. **Prvi set.** Vodi ga `studio-reklama`: tekst se provjeri, osoba potvrdi, Studio radi.
6. **Gotovo.** Daj poveznicu iz `studio_galerija` osobi koja je tražila. Reci jednu
   rečenicu što može dalje: više proizvoda, objave za tjedan ili kampanja.

## Nikad

- Ne nabrajaj sve alate i teme. Pokaži samo sljedeći korak.
- Ne traži fotke, fontove ni reference prije prvog seta. Studio radi s fotkama iz
  trgovine.
- Ne spominji trošak ni kredite AI-ja.

## Za Newton (novi klijent)

Prije prvog seta klijent treba: shop s fotkama proizvoda, logo, boje i jednu rečenicu o
glasu branda. Brand paket postavlja Newton. Do tada je paket privremen.

## Dalje

`studio-reklama` za sljedeći set, `studio-objave` za tjedan objava.
