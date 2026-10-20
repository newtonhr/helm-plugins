---
name: studio-brand
description: Helm Studio — kontekst webshop klijenta za reklame u Helm Studiju: publika, problemi i prigovori kupaca, jezik kupaca, dokazi, glas branda i naučeno iz prošlih oglasa. Pokreni kad korisnik u Helm Studiju pita tko su kupci, kakav je glas branda, kaže „zapamti ovo za reklame” ili postavlja novog klijenta. Only when working through Helm Studio.
---

# Brand i kontekst klijenta

Brand paket u Helmu je jedan izvor istine za sve skillove. Ovaj skill ga čita i piše
nacrt dopune. Ništa ne sprema sam: nacrt ostaje u razgovoru, a Newton ga upisuje kad
brand paket dobije te odjeljke.

## Prije početka

Pozovi `studio_brand`. Pitaj samo ono što paket nema. Najviše 3 pitanja odjednom.

## Što tražimo

| Odjeljak | Pitanje |
|---|---|
| Publika | Tko kupuje? Kad i zašto (sezona, prigoda)? |
| Problemi | Što kupca muči prije kupnje? Njegovim riječima. |
| Prigovori | Zašto kupac odustane? Cijena, povjerenje, dostava? |
| Jezik kupaca | Kako kupci sami opisuju proizvod? Doslovne rečenice iz recenzija, poruka, komentara. |
| Dokazi | Norme, certifikati, brojevi, nagrade, godine na tržištu. Samo provjerljivo. |
| Glas | Ti ili Vi? Kratko ili toplo? Što nikad ne kažemo? |
| Naučeno | Što je radilo, a što nije. Uz dokaz. |

Za načela pozovi `studio_znanje("psihologija-kupca")`. Za tržište klijenta pozovi temu
tržišta iz popisa `studio_znanje`.

## Naučeno

Jedan redak: **učenje** (jedna rečenica koja mijenja nacrt), **dokaz** (test ili
kampanja, broj, veličina uzorka), **vrijedi za** (mreža, proizvodi), **status** (aktivno,
pratiti, ukinuto).

- Jedan oglas bez broja nije učenje. Zapiši ga kao „pratiti” ili ga izostavi.
- Odluka osobe s razlogom jest učenje („nikad ne pišemo ‚jeftino’”).
- Ako je dostupan `studio_stil`, on pokazuje što klijent bira među ponudama. Ako se
  obrazac ponavlja, predloži redak.

## Koraci

1. `studio_brand`, pa pitanja za ono što fali.
2. Doslovne rečenice kupaca prepiši točno. Ne prepričavaj ih.
3. Napiši nacrt dopune po odjeljcima gore. Za svaku tvrdnju reci odakle je.
4. Pokaži nacrt osobi.

## Nikad

- Ne izmišljaj publiku, recenzije ni dokaze.
- Ne mijenjaj boje, fontove ni logo. To radi Newton.
- Zakonska pravila iz `studio_znanje("pravila-oglasavanja")` brand ne može ukinuti.

## Dalje

`studio-prvi-koraci` ako je klijent nov, inače `studio-reklama`.
