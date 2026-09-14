---
access: public
aliases: []
claim_ids:
- clm_138096f7ff345494150fc199d68913fe2f5b3035c23c5be92471c5b4854c1609
- clm_e9f03b5b2fbd135e331d6f0c3345c39ab4ec6124de05e87ad26caab4eed37c09
maturity: draft
page_id: pg_422a2c67c42b588caef20820fad89b19
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c8ceca53380f583fad5fb8741540c0d8
title: open-multi-agent/open-multi-agent/docs/budgets-and-limits.md @ eaeb420c4364
updated_at: '2026-09-14T02:26:17Z'
---

# open-multi-agent/open-multi-agent/docs/budgets-and-limits.md @ eaeb420c4364

<!-- rcw:begin owner=source:src_c8ceca53380f583fad5fb8741540c0d8 block=evidence -->
- When maxTurns is reached the run stops before the next model call and is still reported successful with no distinguishing flag; the docs suggest comparing toolCalls or message counts, or setting a lower maxTurns and treating a long run as an alert. [@claim:clm_138096f7ff345494150fc199d68913fe2f5b3035c23c5be92471c5b4854c1609]
- Budgets are checked only at turn and task boundaries, so a run can overshoot its ceiling by up to one model turn; exhausting a budget is reported via a budget_exceeded event and result fields rather than thrown. [@claim:clm_e9f03b5b2fbd135e331d6f0c3345c39ab4ec6124de05e87ad26caab4eed37c09]
<!-- rcw:end owner=source:src_c8ceca53380f583fad5fb8741540c0d8 block=evidence -->

## Researcher notes

