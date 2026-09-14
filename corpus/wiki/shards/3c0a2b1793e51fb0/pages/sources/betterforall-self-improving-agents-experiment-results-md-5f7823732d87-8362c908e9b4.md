---
access: public
aliases: []
claim_ids:
- clm_3463f9d610c8dc6a766bad608c5e5a04d9fb7385a2b98eb27059e7a33a4d5930
- clm_70559fc3ab565d228764941c42db1cffbaba2f0a46ec4681726845199516f74a
- clm_9330320c5a646097cdfdf3a2af2509ded50ce4fea9819d67d6d57cf4b7fb9cdf
- clm_ef49a4f6948d2520039c9289c30bd8c1cf483950fa1fce48b69798b9031e3fd3
maturity: draft
page_id: pg_999747499fc352a4b2998362c908e9b4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f87ec2c135f0505ab547d3c3b21bc3e1
title: BetterForAll/self-improving-agents/experiment-results.md @ 5f7823732d87
updated_at: '2026-09-14T01:38:01Z'
---

# BetterForAll/self-improving-agents/experiment-results.md @ 5f7823732d87

<!-- rcw:begin owner=source:src_f87ec2c135f0505ab547d3c3b21bc3e1 block=evidence -->
- Cross-validation shows Levels 1-3 scored 90-100% on email_validation's original 20 tests but dropped to 62-66% on the expanded 50-case adversarial suite, while Arena levels held at 70% on the combined suite. [@claim:clm_3463f9d610c8dc6a766bad608c5e5a04d9fb7385a2b98eb27059e7a33a4d5930]
- Experiments used Gemini 2.5 Flash across five levels and three tasks (email_validation, snake, support) in 15 total experiments, with per-level metrics, costs, and token counts reported. [@claim:clm_70559fc3ab565d228764941c42db1cffbaba2f0a46ec4681726845199516f74a]
- For support, rubric-based boolean scoring (keyword match plus LLM YES/NO fallback) reduced judge noise from over 30 points to under 7; Feedback Loop scored highest (82.091) on the expanded 19 questions. [@claim:clm_9330320c5a646097cdfdf3a2af2509ded50ce4fea9819d67d6d57cf4b7fb9cdf]
- The results document acknowledges single runs per experiment (N=1, no error bars), a small task set of three tasks, and a single model (Gemini 2.5 Flash), so findings may not generalize. [@claim:clm_ef49a4f6948d2520039c9289c30bd8c1cf483950fa1fce48b69798b9031e3fd3]
<!-- rcw:end owner=source:src_f87ec2c135f0505ab547d3c3b21bc3e1 block=evidence -->

## Researcher notes

