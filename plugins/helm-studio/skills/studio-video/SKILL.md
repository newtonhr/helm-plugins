---
name: studio-video
description: Helm Studio — scenarij i popis kadrova za kratki video (Reels, TikTok, Shorts, video oglas) za webshop klijenta. Studio ne radi video. Pokreni kad korisnik u Helm Studiju traži reel, TikTok, video reklamu ili scenarij za proizvod iz shopa klijenta. Only when working through Helm Studio.
---

# Kratki video

**Studio ne radi video.** Daje scenarij i popis kadrova; statične kadrove 9:16 iz pravih
fotki proizvoda može napraviti `studio-reklama`. Video snima ili slaže čovjek (mobitel,
aplikacija za montažu). Reci to osobi na početku.

## Prije početka

- Mreža i koliko kratko video može biti.
- Cilj: upoznati proizvod, pokazati upotrebu ili prodati?
- Mogu li snimiti proizvod mobitelom? Ima li osoba koja govori u kameru?

## Koraci

1. `studio_brand`, `studio_znanje("video-scenarij")` i za mrežu
   `studio_znanje("tekst-tiktok")` ili `studio_znanje("tekst-instagram")`.
2. Početak i strukturu odaberi iz vodiča `video-scenarij` (odjeljci „Početak” i
   „Strukture”).
3. Za svaki kadar: trajanje, slika, izgovoreno, natpis. Pravila za zvuk i natpise su u
   odjeljku „Zvuk i tekst”.
4. Kadrove s proizvodom može dati `studio-reklama` kao slike za story. Samo nakon
   potvrde osobe.
5. Popis kadrova koje treba snimiti mobitelom (proizvod u ruci, na brodu, u pokretu).

## Nikad

- Ne obećavaj gotov video ni AI video.
- AI ne crta proizvod. Proizvod u pokretu se snima.
- Nema izmišljenih brojeva ni recenzija u scenariju.

## Dalje

`studio-objave` za tekst objave uz video, `studio-oglasi` za video oglas.
