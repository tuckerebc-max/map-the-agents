---
access: public
aliases: []
claim_ids:
- clm_20cf0afd1bfc4fbfa799056a44053e60c1ad0c62da330a877eb445ace790d2ed
- clm_4ac7621e362e7ff4a6a5eaa471539192141fd7f2d8c224814b79729ccfbf7448
- clm_7470a553d2958b5c1989a003d9ebff2ee12c2ab84ae770dc2593dbcacde1fcf5
- clm_7579999285389999537281730cc0a3fe6ef67362161033c0032b571d2eb7cb78
- clm_7ccdf33d506a3508ca4925ede4604280a7f8cae461bb8f01c7a5879cbcb880ab
- clm_b0cd2e8c122e601bf592a9351e866f9f379e5e2c585889bc9ed34600889af803
- clm_caa1e9c43fbcf3d467be6d59e5648a07cfc0d73779707ab8f83efa73f16a1425
maturity: draft
page_id: pg_fcc8763dbdd25d2b826550edb38cfb07
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_de619aa1d3955a94b6495120e2652153
title: vivekhaldar/seed/docs/DESIGN.md @ cd79a60acafe
updated_at: '2026-09-14T05:05:12Z'
---

# vivekhaldar/seed/docs/DESIGN.md @ cd79a60acafe

<!-- rcw:begin owner=source:src_de619aa1d3955a94b6495120e2652153 block=evidence -->
- The design doc states the seed prompt and the agent's self-description were collapsed into the same mutable file: the loop's only hardcoded context decision is reading self/SELF.md, re-read every turn so self-edits take effect immediately. [@claim:clm_20cf0afd1bfc4fbfa799056a44053e60c1ad0c62da330a877eb445ace790d2ed]
- Documentation states models and keys are handled by Simon Willison's llm library, chosen over LiteLLM, PydanticAI, and a raw OpenAI SDK/OpenRouter combination for its multi-provider plugin model, per-conversation session state, and plain-function tool calling. [@claim:clm_4ac7621e362e7ff4a6a5eaa471539192141fd7f2d8c224814b79729ccfbf7448]
- The design document frames its distinct claim as germinating a personal agent from an auditable seed in dialogue, with conversation as selection pressure rather than a benchmark-driven optimization loop. [@claim:clm_7470a553d2958b5c1989a003d9ebff2ee12c2ab84ae770dc2593dbcacde1fcf5]
- Documentation states planting creates a fresh, private git repo at the target directory (or nests git under self/ inside an existing repo) and never overwrites an existing seed.py or run_seed.sh, so a grown loop cannot be clobbered by a later plant. [@claim:clm_7579999285389999537281730cc0a3fe6ef67362161033c0032b571d2eb7cb78]
- The risk register documents ungated exec as a consciously accepted risk: the agent runs arbitrary bash as the invoking user with no sandbox or approval gate, though every command and its output is printed to the terminal. [@claim:clm_7ccdf33d506a3508ca4925ede4604280a7f8cae461bb8f01c7a5879cbcb880ab]
- The design doc states the one irreducible primitive is exec: the seed ships exactly one tool that runs a bash command and returns its output, with every other capability expressed through it rather than compressed further. [@claim:clm_b0cd2e8c122e601bf592a9351e866f9f379e5e2c585889bc9ed34600889af803]
- Documentation states each session is fresh and its conversation is discarded on exit, so nothing survives except what the agent wrote into self/; a separate verbatim transcript is recorded per session as a flight recorder that is never loaded at boot. [@claim:clm_caa1e9c43fbcf3d467be6d59e5648a07cfc0d73779707ab8f83efa73f16a1425]
<!-- rcw:end owner=source:src_de619aa1d3955a94b6495120e2652153 block=evidence -->

## Researcher notes

