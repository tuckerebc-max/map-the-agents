---
access: public
aliases: []
claim_ids:
- clm_324cc7c5b1f0dbb27e19261818620eff197ec378cbebffd88d48089893509bdc
- clm_7e1c3ab25b0ee7dec7eff79888b3c423dddeb4e290579e02f9f9fc87c6a2b748
- clm_95fba6fe4638d0c11be02732049650374d8487396ca5d876c807f912a5aaf4b7
maturity: draft
page_id: pg_b7fa6ae1338956c68f125de48c0f077a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9e7b56e7670d50f19d2dddb570627aab
title: roberto-mello/lavra/site/src/content/docs/configuration.md @ 2e7e512eb90b
updated_at: '2026-09-14T04:18:53Z'
---

# roberto-mello/lavra/site/src/content/docs/configuration.md @ 2e7e512eb90b

<!-- rcw:begin owner=source:src_9e7b56e7670d50f19d2dddb570627aab block=evidence -->
- /lavra-work auto-routes between single-bead and multi-bead parallel execution, with a configurable max_parallel_agents (default 3) and per-task atomic commits whose bead IDs make git log grep useful. [@claim:clm_324cc7c5b1f0dbb27e19261818620eff197ec378cbebffd88d48089893509bdc]
- Behavior is configured via .lavra/config/lavra.json, which toggles workflow phases (research, plan_review, goal_verification, review_scope, testing_scope), execution parallelism, commit granularity, and model_profile; all fields are optional with documented defaults. [@claim:clm_7e1c3ab25b0ee7dec7eff79888b3c423dddeb4e290579e02f9f9fc87c6a2b748]
- Agents run at assigned model tiers (Haiku/Sonnet/Opus) by reasoning complexity; the 'quality' model_profile routes critical agents like security-sentinel and goal-verifier to Opus, with a documented claim of 60-70% cost reduction versus running everything on the top model. [@claim:clm_95fba6fe4638d0c11be02732049650374d8487396ca5d876c807f912a5aaf4b7]
<!-- rcw:end owner=source:src_9e7b56e7670d50f19d2dddb570627aab block=evidence -->

## Researcher notes

