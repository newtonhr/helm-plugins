---
name: helm-studio
description: Helm Studio — reklamne slike, objave za društvene mreže, newsletter i plan kampanje za webshop klijenta preko Helma (studio_* alati). Pokreni kad korisnik traži reklamu, objavu, slike za Instagram/Facebook/TikTok/LinkedIn, banner, newsletter, ideje za objave ili kampanju.
---

# Helm Studio

Znanje struke (marketing, dizajn, društvene mreže, pravila oglašavanja) je u Helmu, ne u
ovom pluginu. Plugin samo kaže kad koristiti Studio.

1. Prvo pozovi `studio_znanje` bez teme: dobiješ popis tema i kada koju koristiti.
2. Za posao pozovi `studio_znanje(tema)`: vodič, pravila (formati, dizajn) i primjeri.
3. `studio_brand` daje brand paket klijenta. Brand paket ima prednost pred vodičem.
4. Prije izrade provjeri tekst sa `studio_provjeri_tekst` (besplatno) i popravi što kaže.
   Slike radi `studio_izradi`, najbolje s 2-5 različitih pristupa. AI nikad ne crta
   proizvod, tekst, logo ni cijenu.
5. Česti tokovi su i MCP promptovi u izborniku: `kampanja`, `objave-za-tjedan`,
   `reklama-za-proizvod`.
6. Studio ništa ne objavljuje. Objavu radi čovjek.

Bez ovog plugina sve radi isto: Helm sam kaže Claudeu da pozove `studio_znanje`.
