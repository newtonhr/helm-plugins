---
name: studio-animacija
description: Helm Studio — kratka animacija proizvoda iz webshopa klijenta (petlja od 4 s: odskok, ulazak u kadar, njihanje, svjetlo, u ruci) za stranicu proizvoda ili objavu (studio_animacija). Pokreni kad korisnik u Helm Studiju traži animaciju proizvoda, proizvod koji se okreće, skače ili privlači pažnju na webu. Only when working through Helm Studio.
---

# Animacija proizvoda

Animacija je petlja od 4 s bez rezova, bez teksta i bez zvuka. Proizvod se pomiče da
privuče pogled na webu ili u objavi.

## Prije početka

Pitaj samo što ne znaš:
- koji proizvod;
- gdje ide: stranica proizvoda (pozadina brand) ili objava (pozadina scena, `mjesto`);
- pluta li proizvod stvarno (samo tada plutanje).

## Koraci

1. `studio_brand`, zatim `studio_znanje("animacije")`.
2. Predloži pokret iz jedne fotke: odskok, ulazak, njihanje, svjetlo, u_ruci, plutanje.
   Prednja strana uvijek gleda kameru. Najviše 2 pokreta.
3. Okretanje, napuhavanje, kopčanje, sastavljanje i otvaranje traže pravu fotku tog
   stanja iz trgovine (`fotka`). `studio_provjera_fotki` pokaže koje fotke postoje.
   Bez nje predloži pokret iz jedne fotke. Za sada ti pokreti ne idu u video.
4. `studio_tokeni`: reci osobi cijenu animacije u tokenima i koliko ostaje.
5. **Pitaj osobu**: proizvod, pokret, format (kvadrat, feed, reel), pozadina.
6. `studio_animacija(proizvod, pokret, …)`: Studio nacrta ključnu sliku. Pokaži je.
   Proizvod mora izgledati kao na pravoj fotki.
7. Čekaj „da”. Zatim isti poziv s `odobri=[kf_…]`, pa `studio_cekaj(posao)` dok ne
   kaže gotovo.
8. Poveznicu iz `studio_galerija` daj osobi: MP4 i slika naslovnice.

## Nikad

- Nema teksta, cijene ni loga u animaciji; AI ne izmišlja dijelove ni stanja.
- Nema mutne pozadine; izgleda snimljeno kamerom.
- Ruka smije, lice ne.
- Ne spominji AI kredite ni naš trošak u eurima.
- Studio ne objavljuje.

## Dalje

`studio-galerija` za slike proizvoda u sceni, `studio-video` za reel s pričom.
