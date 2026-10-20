# Helm Studio — plugin (neobavezan)

Plugin je tanak: jedan skill, `helm-studio`, koji kaže kad koristiti Studio i da znanje
dolazi iz Helma. **Bez plugina sve radi isto** — u svakom MCP klijentu (Claude, Cowork,
Claude Code) Helm sam daje upute serveru i alat `studio_znanje`.

Gdje je znanje (u Helmu, `src/marina_ops/studio/`):

| Vrsta | Mjesto | Kako ga Claude dobiva |
|---|---|---|
| Brojevi i pravila (dimenzije, sigurne zone, duljine, kontrast) | `pravila/formati.yaml`, `pravila/dizajn.yaml` | kod ih provjerava; `studio_znanje` ih vraća uz vodič |
| Načela i postupci | `znanje/*.md` (13 vodiča) | `studio_znanje(tema)` |
| Primjeri (dobro / loše, zašto) | `primjeri/<tema>/` | `studio_znanje(tema)` |
| Recept za scenu (Nano Banana) | vodič `fotografija-proizvoda`, `pravila/dizajn.yaml` | `studio_izradi` ga čita sam |

Alati: `studio_znanje`, `studio_brand`, `studio_izradi`, `studio_status`, `studio_ispravi`,
`studio_galerija`, `studio_potrosnja`, `studio_pozadine_link`, `studio_pozadine`,
`studio_pozadina_ukloni`. MCP promptovi: `kampanja`, `objave-za-tjedan`,
`reklama-za-proizvod`.

Pravila koja vrijede uvijek:

- AI nikad ne crta proizvod, tekst, logo ni cijenu.
- Brand paket klijenta ima prednost pred vodičem; zakonska pravila vrijede uvijek.
- Studio ništa ne objavljuje. Objavu radi čovjek.

Instalacija: samo datoteke u repou; plugin se ne instalira automatski.
