---
name: studio-oglasi
description: Helm Studio — plan plaćenih oglasa na Meti (Facebook, Instagram) i Googleu za webshop klijenta i tjedna provjera rezultata, s kreativama iz Helm Studija. Pokreni kad korisnik u Helm Studiju traži kampanju, budžet za oglase ili zalijepi rezultate oglasa shopa klijenta. Only when working through Helm Studio.
---

# Oglasi: plan i tjedna provjera

Plugin ne vidi oglasni račun. Radi plan i provjeru iz brojeva koje osoba zalijepi.
Oglase u Meti ili Googleu postavlja čovjek.

## Prije početka

- Što žele postići, s brojem i rokom („40 narudžbi do 15. 6.”)?
- Budžet po mjesecu i razdoblje.
- Što već rade: oglasi, rezultati.

## Koraci (plan)

1. `studio_brand` i `studio_znanje("kampanja")`. Prije tvrdnji o cijeni, akciji ili
   sigurnosti `studio_znanje("pravila-oglasavanja")`. Za oblik oglasa po fazi kupnje
   `studio_znanje("strukture-oglasa")`.
2. Cilj i mjeru odaberi prema odjeljku „Cilj i mjera” iz `kampanja`. Cilj ima broj i rok.
3. Publiku, kutove i budžet složi prema odjeljcima „Publika”, „Kutovi” i „Testiranje i
   budžet” iz `kampanja`.
4. Za svaki oglas napiši što očekuješ, tako da se može provjeriti: mjera, usporedba,
   smjer.
5. Stranica na koju oglas vodi ponavlja obećanje iz oglasa.
6. Kreative predaj skillu `studio-reklama`.

## Tjedna provjera

Kad osoba zalijepi brojeve po oglasu:
1. Ima li oglas dovoljno vremena i prikaza za presudu? Prag iz `kampanja`. Ako ga vodič
   nema, ne izmišljaj broj; reci da je rano.
2. Za svaki oglas: **zadrži**, **ugasi** ili **pojačaj**, s razlogom u jednoj rečenici.
3. Sljedeći test: mijenja se jedna stvar, redom iz „Testiranje i budžet”.
4. Stručne riječi objasni pri prvom spomenu, npr. „udio klikova (CTR)”.

## Nikad

- Ne obećavaj rezultat (broj kupnji, povrat ulaganja).
- Ne izmišljaj prosjeke tržišta. Brojke samo iz `studio_znanje` ili od osobe.
- Ne traži pristup oglasnom računu i ne traži lozinke.

## Dalje

`studio-reklama` za kreative, `studio-brand` za zapis „naučeno”.
