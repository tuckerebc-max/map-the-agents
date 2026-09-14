---
access: public
aliases: []
claim_ids:
- clm_1c21cb6e16de6c98bffd03a5bacee83ebb995cd1367701fc65ecb8807dbbf5c3
- clm_4ac7621e362e7ff4a6a5eaa471539192141fd7f2d8c224814b79729ccfbf7448
- clm_52f744dcb896bdb82625534c942f6a7320cc5677be56c04fbb8d0b68b5776252
- clm_7579999285389999537281730cc0a3fe6ef67362161033c0032b571d2eb7cb78
- clm_c51554f832154dc9ec002117528db5497c86f528de2a0c23195766dc20bd08b1
- clm_caa1e9c43fbcf3d467be6d59e5648a07cfc0d73779707ab8f83efa73f16a1425
maturity: draft
page_id: pg_4f8d975d1c405cec87a900102fc3d5ec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb80f4fa79135291822c7d1cf90b863a
title: vivekhaldar/seed/README.md @ cd79a60acafe
updated_at: '2026-09-14T05:05:12Z'
---

# vivekhaldar/seed/README.md @ cd79a60acafe

<!-- rcw:begin owner=source:src_eb80f4fa79135291822c7d1cf90b863a block=evidence -->
- The README describes seed.py as calling a language model with a single exec tool that runs shell commands, loading its system prompt from self/SELF.md, with the agent able to edit self/ to retain tools, notes, and behavior between sessions. [@claim:clm_1c21cb6e16de6c98bffd03a5bacee83ebb995cd1367701fc65ecb8807dbbf5c3]
- Documentation states models and keys are handled by Simon Willison's llm library, chosen over LiteLLM, PydanticAI, and a raw OpenAI SDK/OpenRouter combination for its multi-provider plugin model, per-conversation session state, and plain-function tool calling. [@claim:clm_4ac7621e362e7ff4a6a5eaa471539192141fd7f2d8c224814b79729ccfbf7448]
- The license text labels itself Sovereign Source License v0.3 and describes an Apache 2.0 extension with optional development-data services. It says basic use under Apache 2.0 terms involves no data collection. [@claim:clm_52f744dcb896bdb82625534c942f6a7320cc5677be56c04fbb8d0b68b5776252]
- Documentation states planting creates a fresh, private git repo at the target directory (or nests git under self/ inside an existing repo) and never overwrites an existing seed.py or run_seed.sh, so a grown loop cannot be clobbered by a later plant. [@claim:clm_7579999285389999537281730cc0a3fe6ef67362161033c0032b571d2eb7cb78]
- Setup is documented as detecting an existing provider credential or asking interactively, verifying it with one minimal model request unless --no-verify is passed, and storing a pasted key only in llm's user-level key store, never writing it into run_seed.sh, seed.py, or git. [@claim:clm_c51554f832154dc9ec002117528db5497c86f528de2a0c23195766dc20bd08b1]
- Documentation states each session is fresh and its conversation is discarded on exit, so nothing survives except what the agent wrote into self/; a separate verbatim transcript is recorded per session as a flight recorder that is never loaded at boot. [@claim:clm_caa1e9c43fbcf3d467be6d59e5648a07cfc0d73779707ab8f83efa73f16a1425]
<!-- rcw:end owner=source:src_eb80f4fa79135291822c7d1cf90b863a block=evidence -->

## Researcher notes

