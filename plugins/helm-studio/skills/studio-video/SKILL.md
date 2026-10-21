---
name: studio-video
description: Helm Studio — kratki video s pričom (Reels, TikTok, Shorts, video oglas) za webshop ili uslugu klijenta. AI kadrovi s ljudima i proizvodom u upotrebi nastaju iz ključnih slika koje osoba odobri; Studio ih montira. Pokreni kad korisnik u Helm Studiju traži reel, TikTok, video reklamu, video za uslugu ili scenarij. Only when working through Helm Studio.
---

# Kratki video s pričom

Ti si redatelj. Ljudi kupuju osjećaj, tuđe iskustvo. Video pokazuje to iskustvo, a proizvod
ga omogućuje. AI ne crta tekst, logo ni cijenu; to dodaje montaža.

## Prije početka

1. `studio_brand`, zatim `studio_znanje("video-redatelj")` i `studio_znanje("video-price")`.
   Za uslugu (salon, servis) i `studio_znanje("video-usluge")`.
2. Pitaj osobu, s prijedlogom za svako:
   - organsko ili plaćeno, i koja mreža;
   - koji osjećaj prodajemo (sigurnost, mir, sreća);
   - što nudimo i do kada vrijedi;
   - kako se kupac javlja (poveznica, poruka, telefon, rezervacija);
   - za pravog čovjeka u kadru: ima li pisani pristanak.
3. Provjeri u trgovini što proizvod stvarno može. Priča smije pokazati samo to.

## Koraci

1. Napiši osjećaj u jednoj rečenici, jednu poruku i jedan poziv.
2. Predloži 2–3 priče u dvije rečenice. Osoba bira.
3. Napiši knjigu snimanja: `likovi`, kadrovi (`slika_opis`, `ai_opis`, `proizvod`),
   natpisi, kraj, tekst objave, 3–5 hashtagova, naslovnica. Jedna varijanta.
   Nezgoda ima vidljiv uzrok (val, mokra ruka), a lice nosi emociju u krupnom planu.
   Kadar proizvoda ima `scena` (prazan set), a ne golu fotografiju iz kataloga.
4. `studio_video_kadrovi(knjiga)`: ključne slike i setovi. Ponavljaj dok ne kaže `gotovo`.
   Pokaži slike osobi redom, kao strip. Popravi `slika_opis` ili `likovi` gdje ne valja.
5. Kad osoba kaže da: `studio_video_kadrovi(knjiga, odobri=[kf_…])`.
6. `studio_video_provjeri(knjiga)` (besplatno). Popravi što kaže. Ponovi dok nije `ok`.
7. **Pitaj osobu**: pokaži vremensku crtu, natpise i koliko AI sekundi video troši.
   Čekaj „da”.
8. `studio_video_izradi(knjiga)`, pa odmah `studio_cekaj(posao)` dok ne kaže gotovo.
   Pokaži ključne kadrove. Video se gleda i preuzima u galeriji.
9. Reci osobi: glazbu dodaje u aplikaciji iz knjižnice za tvrtke.

Ispravak: promijeni knjigu snimanja. Odobrene slike i gotovi AI kadrovi se ne plaćaju
ponovo. `studio_ispravi` ne radi za video.

## Nikad

- AI ne crta tekst, logo ni cijenu.
- Proizvod ne radi ništa što stvarno ne može.
- Nitko ništa ne baca. U opisu nema „baci”, „ispusti” ni „ispadne”, nego uzrok pa klizanje.
- Nema izmišljenih brojeva, recenzija ni obećanja (trajno, bezbolno, zajamčeno).
- Za usluge nema AI kože, rezultata tretmana ni prije/poslije.
- Nema AI kadra bez odobrene ključne slike, osim scene bez ljudi i proizvoda.
- Cijena samo iz trgovine; ponuda s datumom.
- Pravi čovjek u kadru samo uz pisani pristanak.
- Ne objavljuj. Objavu radi čovjek.

## Dalje

`studio-objave` za tekst objave uz video, `studio-oglasi` za video oglas, `studio-reklama`
za slike iste kampanje.
