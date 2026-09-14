---
access: public
aliases: []
claim_ids:
- clm_2d4cd98a783a23e48c175d22742ab00c20dec9a496038197f369091daec82af3
- clm_83588e36928427d7e20021b8153c665ff1b59d50beac42fb2faf24404ea9beea
- clm_915110b53b566041c048c8578b226d2d84a2347d511aa977e073d9667ab4b760
- clm_9813c92cc8a5d7265e9f2d1e9767c0b515cc229ad39154aebb9da2144e7e5dcf
maturity: draft
page_id: pg_95b6097c2ec750a8884012724760cc0d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_529c6745829e5cb1b9dc7574eca57036
title: hotovo/aider-desk/docs/adr/README.md @ cb7ee89bf213
updated_at: '2026-09-14T02:04:46Z'
---

# hotovo/aider-desk/docs/adr/README.md @ cb7ee89bf213

<!-- rcw:begin owner=source:src_529c6745829e5cb1b9dc7574eca57036 block=evidence -->
- Repository development practice: the ADR review checklist requires tracing call paths against source, separating current behavior from desired future state, and avoiding absolute security or durability claims unless the code enforces them. [@claim:clm_2d4cd98a783a23e48c175d22742ab00c20dec9a496038197f369091daec82af3]
- The ADR set was written retroactively by analyzing the existing codebase, documenting de-facto decisions that are descriptive of current architecture and prescriptive for future changes. [@claim:clm_83588e36928427d7e20021b8153c665ff1b59d50beac42fb2faf24404ea9beea]
- Repository development practice: new ADRs follow a template with global sequential numbering, retroactive ADRs may be Accepted only after verification against current source, and Accepted decisions are never edited in place. [@claim:clm_915110b53b566041c048c8578b226d2d84a2347d511aa977e073d9667ab4b760]
- Repository development practice: every ADR must include a mandatory 'Guardrails for Agents' section with do/don't rules, and changes conflicting with an ADR require updating the ADR first or changing the approach. [@claim:clm_9813c92cc8a5d7265e9f2d1e9767c0b515cc229ad39154aebb9da2144e7e5dcf]
<!-- rcw:end owner=source:src_529c6745829e5cb1b9dc7574eca57036 block=evidence -->

## Researcher notes

