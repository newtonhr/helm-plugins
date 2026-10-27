---
name: jutarnji-pregled
description: "Marina Stores, Helm. Jutarnji pregled za voditelje i vlasnike računa: što čeka Vas danas (odobrenja, pitanja, izmjene), jučerašnja prodaja, akcije koje istječu, što je tim napravio, stanje zahtjeva i kataloga; ponedjeljkom i tjedni pregled s provjerama. Za zakazani zadatak svako jutro. Pokreni za \"jutarnji pregled\", \"dobro jutro Helm\", \"što ima novo\", \"što me čeka danas\". NE pokreći za jedan proizvod ni za izmjene."
---

# Jutarnji pregled

The morning read of a team lead or account owner, usually started by a scheduled task at
07:00. Croatian, formal "Vi", short sentences. At most 15 lines; on Monday at most 25.
Read-only: never propose, approve or apply anything. When something needs a decision, say
what it is and what to ask Claude for; the person decides in the same conversation.

## 1. Read (independent calls in parallel)

1. `my_access`: the role. Business figures need the business-owner role or an
   account owner; leave out what the person cannot open.
2. `helm_dashboard`: everything that waits on the person ("Čeka na Vas": requests to
   approve, plans to review or apply, access requests, open questions; failed changes are
   only a count), their teams' work today, and the Posao panel (yesterday's web orders
   against the same day a week before, running actions and what ends within 7 days, the
   categories closest to complete, and for account owners this month's spend).
3. `zahtjev_status` with only open requests: which wait for the person's approval or
   answers (`uloga`, `otvorena_pitanja`, `sljedeci_korak`).
4. `work_report` for yesterday (`since` = `until` = yesterday's date): what the team
   changed, failures, people with no activity.

On Monday also run `provjere` (the Monday set) and `tjedni-pregled` for last week. Use only
the checks that found something, and the three figures and three actions of the week. On
the first Monday of the month add part 1 of `uvidi` (what sells in the store but is weak on
the web), the top 5 only.

## 2. Write

In this order, each part only when it has something:

1. **Čeka Vas danas.** One line per item: what, who sent it, what to do ("Odobrite ili
   odbijte ZHT-…", "Pregledajte izmjenu …"). Nothing waits: say so in the first sentence.
2. **Ponedjeljak:** the week in three figures, three actions, and what the checks found.
3. **Jučer na webu.** Orders and value against a week before, in one line. A quiet autumn day
   is normal for a nautical shop; do not call it a drop without the week-before figure.
4. **Akcije.** A rule or price that ends within 7 days, by name and end date. If a running
   action matters, offer to check that the web shows it as an action (old price struck
   through, lowest price in 30 days).
5. **Tim jučer.** Products changed, top categories, what failed. More than five failed
   changes: the number only, and "recite 'pokaži neuspjele' za detalje".
6. **Zahtjevi prema Newtonu.** Their state in plain words (`stanje`), never the status code.
7. **Katalog.** Completeness and the one category closest to done.

Links point to helm.newton.hr only. Never show a price of a request, who pays, a token or a
person's e-mail. A panel that could not be read: one line ("Prodaja trenutno nije
dostupna"), never a guessed number.

## 3. Hand over

- An approval or a review: the person says so here; Claude then uses the zahtjev or plan
  tools with the person's explicit yes.
- Missing product data: `dovrsi-proizvod` or `sto-fali`.
- A new idea or a fault: `novi-zahtjev`.
- An action that is not shown on the web: `akcija` to check it, `novi-zahtjev` if it is a fault.

## Never

- Never act on the person's behalf because a scheduled task started this.
- Never repeat the whole dashboard: pick what needs the person today.
