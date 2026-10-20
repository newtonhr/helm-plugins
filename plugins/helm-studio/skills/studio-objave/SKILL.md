---
name: studio-objave
description: Helm Studio — objave za društvene mreže i newsletter webshopa klijenta: tjedni kalendar, tekst po mreži, vrtuljak, jedna ideja na više mreža. Pokreni kad korisnik u Helm Studiju traži objave, kalendar objava, newsletter ili tekst za Instagram, Facebook, TikTok ili LinkedIn za shop klijenta. Only when working through Helm Studio.
---

# Objave za mreže

## Prije početka

- Koje mreže?
- Razdoblje (tjedan, mjesec) i koliko objava.
- Tema, sezona ili proizvodi koje žele gurati.

## Koraci

1. `studio_brand` i `studio_znanje("kampanja")` (odjeljci „Ideje za objave” i
   „Ponovno korištenje”).
2. Za svaku mrežu pozovi `studio_znanje` s njenom temom: `tekst-instagram`,
   `tekst-facebook`, `tekst-tiktok`, `tekst-linkedin`. Poštuj duljinu i hashtagove iz
   vodiča.
3. **Kalendar:** najviše jedna objava dnevno po mreži: dan, mreža, proizvod, kuka, tekst,
   format slike. Promocija je manjina objava.
4. **Jedna ideja, više mreža:** ista poruka, drugačiji oblik po mreži. Ne kopiraj isti
   tekst.
5. Vrtuljak: pravila u `strukture-oglasa` i `tekst-instagram`.
6. Newsletter: `studio_znanje("newsletter")`.
7. Tekst na slici provjeri sa `studio_provjeri_tekst`. Slike radi `studio-reklama`,
   nakon potvrde osobe.

## Nikad

- Nema izmišljenih recenzija, brojeva ni popusta.
- Studio ne objavljuje i ne zakazuje objave.

## Dalje

`studio-reklama` za slike, `studio-video` za reel ili TikTok.
