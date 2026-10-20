---
name: studio-video
description: Helm Studio — kratki video (Reels, TikTok, Shorts, video oglas) za webshop ili uslugu klijenta, iz njegovih pravih fotografija i klipova; Studio ga montira. Pokreni kad korisnik u Helm Studiju traži reel, TikTok, video reklamu, video za uslugu ili scenarij. Only when working through Helm Studio.
---

# Kratki video

Ti si redatelj. Studio montira video iz pravih fotografija i klipova klijenta. AI nikad
ne radi proizvod, ljude, tekst, logo ni cijenu.

## Prije početka

1. `studio_brand`, zatim `studio_znanje("video-redatelj")`. Za uslugu (salon, servis) i
   `studio_znanje("video-usluge")`.
2. Pitaj osobu, s prijedlogom za svako:
   - organsko ili plaćeno, i koja mreža;
   - što nudimo i do kada vrijedi;
   - kako se kupac javlja (poveznica, poruka, telefon, rezervacija);
   - tko je u kadru i ima li pisani pristanak;
   - govori li netko u kameru.
3. `studio_materijali`: koje fotografije i klipove imamo. Novi materijal osoba šalje
   preko `studio_pozadine_link` (obrazac „Klip”).

## Koraci

1. Napiši jednu poruku i jedan poziv. Odaberi strukturu i recept iz vodiča.
2. Predloži 2–3 različita koncepta u dvije rečenice. Osoba bira.
3. Napiši knjigu snimanja: kadrovi, natpisi, kraj, dvije dodatne kuke, tekst objave,
   3–5 hashtagova, naslovnica.
4. `studio_video_provjeri(knjiga)` (besplatno). Popravi što kaže. Ponovi dok nije `ok`.
5. Ako vrati `popis_snimanja`, pošalji ga osobi jednostavnim riječima i pričekaj klipove.
6. **Pitaj osobu**: pokaži vremensku crtu (kadar po kadar, natpisi) i upozorenja.
   Čekaj „da”.
7. `studio_video_izradi(knjiga)`, pa odmah `studio_cekaj(posao)` dok ne kaže gotovo.
   Pokaži ključne kadrove. Video se gleda i preuzima u galeriji.
8. Reci osobi: glazbu dodaje u aplikaciji iz knjižnice za tvrtke; varijante A, B i C
   imaju različite kuke za test.

Ispravak: promijeni knjigu snimanja i ponovo provjeri. `studio_ispravi` ne radi za video.

## Nikad

- AI ne radi proizvod, ljude, kožu, lice ni rezultat tretmana.
- Nema izmišljenih brojeva, recenzija ni obećanja (trajno, bezbolno, zajamčeno).
- Cijena samo iz trgovine; ponuda s datumom.
- Nitko u kadru bez pisanog pristanka.
- Ne objavljuj. Objavu radi čovjek.

## Dalje

`studio-objave` za tekst objave uz video, `studio-oglasi` za video oglas, `studio-reklama`
za slike iste kampanje.
