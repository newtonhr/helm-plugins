---
key: T-261020-helm-studio-plugin
type: feature
size: L
status: active
repo: grgur/helm-plugins (moved from grgur/marina-ops-mcp on 2026-10-20)
branch: claude/project-thread-db29u7
created: 2026-10-20
specs: .context/T-261020-helm-studio-f2-plan/plan-faza2.md (Dio G)
consent: 2026-10-20 owner "I also want a Helm Studio plugin for claude … Plan first" (plan only; NOT build, NOT production)
---

# T-261020-helm-studio-plugin — Helm Studio plugin za Claude: plan

## Directive

Owner (2026-10-20, verbatim): "Based on everything we talked about in threads and Helm
Studio sessions, I also want a Helm Studio plugin for claude. You can take further hints
from https://github.com/coreyhaines31/marketingskills, scoped to social, video,
product-marketing, onboarding, ads, ad-creative. Plan first".

Deliverable: `plan.md` in this folder, in Croatian, short sentences.

## Scope

- in: read the current plugin, the Studio knowledge and the phase 2 plan; read the six
  upstream skills (marketingskills v2.13.0, commit e85f3cb); write the plan.
- out: any file under `plugins/`, `src/`, `migrations/`; any AI call; any production write;
  merge into `main`; edits to `.claude/`, `.github/`, `CLAUDE.md`.

## Owner, later the same day

"ovo je samo .context sa planom. Prebaci to i sve relevantno u helm-plugins, ukljucujuci
plugins/helm-studio. Nema smisla da to radimo u ovom repo kad imamo repo samo za plugin".

## Coordination

- Thread "Marketinško znanje u Studiju" is folding the owner's ad playbook into Studio
  knowledge (a new guide on ad structures and creative patterns). This plan does not write
  that knowledge. It only names what the plugin needs from it.
- Phase 2 Dio G (plugin distribution) is the base for §6 of the plan.

## Acceptance criteria (for this planning item)

- AC1: `plan.md` opens with the owner's decisions, then the design, then the parts in
  order with size and acceptance criteria, then risks.
- AC2: every claim about the system carries a grade (Observed / Inferred / Assumed).
- AC3: nothing in the plan duplicates knowledge that lives in Helm; the plugin points at it.

## Evidence (Observed this session)

- `plugins/helm-studio/` (then in marina-ops-mcp) has one skill (21 lines), `plugin.json` version 0.3.0, neutral
  description (no client name).
- marina-ops-mcp `src/marina_ops/studio/znanje/` has 13 guides; several cite marketingskills v1 names
  (`social-content`, `paid-ads`) under MIT.
- Upstream now 2.13.0; the six skills are `social`, `video`, `product-marketing`,
  `onboarding`, `ads`, `ad-creative`.
- `grep` over the guides finds no "AI tells", no testable hypothesis, no Andromeda, no
  creative fatigue rules.
- marina-ops-mcp `src/marina_ops/tools/studio.py` registers `studio_odaberi` and `studio_stil` (J6).
- marina-ops-mcp `src/marina_ops/studio/mcp_prompts.py` has three prompts: `kampanja`,
  `objave-za-tjedan`, `reklama-za-proizvod`.
- This environment has marketing-skills 1.9.0 installed as a plugin; its skill names
  overlap the plugin's topics.
