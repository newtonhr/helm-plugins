---
name: helm-studio
description: Helm Studio — ulaz za posao u Helm Studiju (studio_* alati) za webshop klijenta, kad nije jasno koji je posao. Pokreni kad korisnik spominje Helm Studio ili Studio, ili traži reklamu, objavu ili kampanju za shop klijenta preko Helma. Only when working through Helm Studio.
---

# Helm Studio

Znanje struke (marketing, dizajn, društvene mreže, pravila oglašavanja) je u Helmu, ne u
ovom pluginu. Plugin kaže redoslijed posla i kad pitati osobu.

## Koji skill

| Posao | Skill |
|---|---|
| Prvi put u Studiju, novi klijent ili zaposlenik | `studio-prvi-koraci` |
| Publika, glas branda, „zapamti ovo” | `studio-brand` |
| Reklamne slike za proizvod, oglas, banner | `studio-reklama` |
| Kampanja na Meti ili Googleu, budžet, rezultati oglasa | `studio-oglasi` |
| Objave, kalendar, newsletter | `studio-objave` |
| Reel, TikTok, video reklama, video za uslugu | `studio-video` |
| Slike proizvoda u upotrebi za galeriju na stranici proizvoda | `studio-galerija` |
| Kratka animacija proizvoda (odskok, njihanje, svjetlo) | `studio-animacija` |

Ako ništa ne odgovara: pozovi `studio_znanje` bez teme. Dobiješ popis tema i kada koju
koristiti. Za posao pozovi `studio_znanje(tema)`.

## Vrijedi uvijek

1. `studio_brand` prvi. Brand paket klijenta ima prednost pred vodičem.
2. Tekst prije slike provjeri sa `studio_provjeri_tekst` (besplatno). Popravi što kaže.
3. Prije svakog koraka koji radi novu AI scenu pitaj osobu: `studio_izradi`, ispravak s
   novom scenom, komentar ili „nijedna” u odabiru.
4. Nakon `studio_izradi`, `studio_video_izradi`, `studio_animacija`, `studio_odaberi` i `studio_ispravi`
   pozovi `studio_cekaj` dok ne kaže gotovo. Pokaži sliku iz odgovora.
5. AI nikad ne crta proizvod, tekst, logo ni cijenu.
6. Studio ništa ne objavljuje. Objavu radi čovjek.
7. Brojevi, norme i popusti samo iz trgovine (`studio_provjeri_tekst`). Od osobe smiješ
   uzeti samo recenzije, pitanja i komentare kupaca.
8. Prije izrade reci cijenu u paketu: reklama uzima set, a kad setova nema, plaća se
   tokenima; galerija, animacija i video plaćaju se tokenima (`studio_tokeni`). Reci i
   koliko ostaje. Posao bez ispravnog rezultata se vraća.
9. Ne spominji AI kredite, naš trošak u eurima ni interne alate.
