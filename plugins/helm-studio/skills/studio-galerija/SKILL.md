---
name: studio-galerija
description: Helm Studio — slike proizvoda u sceni za galeriju na stranici proizvoda (PDP) u webshopu klijenta, bez teksta i cijene (studio_izradi vrsta galerija). Pokreni kad korisnik u Helm Studiju traži slike proizvoda u upotrebi, lifestyle slike, slike za galeriju ili stranicu proizvoda. Only when working through Helm Studio.
---

# Slike za galeriju proizvoda

Kupac na stranici proizvoda ne može proizvod dotaknuti. Slika u upotrebi pokaže
veličinu, način korištenja i osjećaj. Ljudi kupuju tuđe iskustvo, ne predmet.

## Prije početka

Pitaj samo što ne znaš:
- koji proizvodi (id ili naziv);
- gdje proizvod stvarno živi (brod, kokpit, plaža): to je `motiv`, isti za sve slike
  jednog proizvoda.

## Koraci

1. `studio_brand`, zatim `studio_znanje("galerija")`.
2. `studio_provjera_fotki(proizvodi)`: koliko pravih fotki proizvod ima. Kadar detalj
   ide samo iz prave fotke iz trgovine.
3. Predloži kadrove, 1–4 po proizvodu: u_upotrebi (osoba koristi proizvod), na_mjestu
   (proizvod gdje živi, bez ljudi), mjerilo (u ruci, prava veličina), detalj (prava
   fotka). Odrasla veličina ide s odraslim modelom.
4. `studio_tokeni`: reci osobi cijenu u tokenima (svaka AI slika, detalj je besplatan)
   i koliko ostaje.
5. **Pitaj osobu**: proizvodi, kadrovi, mjesto. Izrada počinje tek kad potvrde.
6. `studio_izradi(proizvodi, vrsta="galerija", kadrovi=…, motiv=…)`, pa
   `studio_cekaj(posao)` dok ne kaže gotovo. Pokaži slike.
7. Recite osobi da svaku AI sliku usporedi s pravom fotkom: boja, natpis, dijelovi.
   Slika ne smije pokazati ono što proizvod nema.
8. Poveznicu iz `studio_galerija` daj osobi. Svaka AI slika u shopu dobije opis
   „Ilustracija u upotrebi”. Naslovna slika proizvoda ostaje prava fotka.

Slika za galeriju se ne ispravlja. Za drugačiju sliku napravi novi posao.

## Nikad

- Nema teksta, cijene ni loga na slici za galeriju.
- AI ne crta detalj; detalj je prava fotka.
- Ne spominji AI kredite ni naš trošak u eurima.
- Studio ne objavljuje i ne mijenja shop.

## Dalje

`studio-animacija` za animaciju istog proizvoda, `studio-reklama` za oglas.
