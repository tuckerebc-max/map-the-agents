---
access: public
aliases: []
claim_ids:
- clm_59db4708848d5fae7af17a22cb1146fba3f487cdb1ca2146967a7ee43ff2afa8
- clm_a749448530b64115cb7a22d572bf71f69a51f234046be065a86a8f7b8532d7a9
- clm_dd4f84a04013e3473b26f875b20b99b9520b69335ed1142f69b8ca6c882299e1
- clm_e6a7c744c8bae06c0de0284053194c022af1f65f2bed1cfc23ac739f5200a839
maturity: draft
page_id: pg_9396ed71db815c20bb1e2a775e4952f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_db7ff6322863554684b358606cb2b467
title: lemony-ai/cascadeflow/docs/ARCHITECTURE.md @ d8251001a51c
updated_at: '2026-09-14T04:06:05Z'
---

# lemony-ai/cascadeflow/docs/ARCHITECTURE.md @ d8251001a51c

<!-- rcw:begin owner=source:src_db7ff6322863554684b358606cb2b467 block=evidence -->
- The repository is a pnpm/Turborepo monorepo with a Python package and a TypeScript packages/core library; the TypeScript library is described as an MVP supporting only the OpenAI provider. [@claim:clm_59db4708848d5fae7af17a22cb1146fba3f487cdb1ca2146967a7ee43ff2afa8]
- CascadeAgent (agent.py) is the main orchestrator and entry point for all queries, exposing run, run_streaming, and stream_events and coordinating routing, cost calculation, metrics, and callbacks. [@claim:clm_a749448530b64115cb7a22d572bf71f69a51f234046be065a86a8f7b8532d7a9]
- WholeResponseCascade is described as the core cascade execution engine, with an execute(query, drafter, verifier) method that runs the speculative cascade. [@claim:clm_dd4f84a04013e3473b26f875b20b99b9520b69335ed1142f69b8ca6c882299e1]
- The core mechanism is speculative execution with quality validation: run a cheap drafter first, validate responses against configurable thresholds, and escalate to a larger model only when validation fails. [@claim:clm_e6a7c744c8bae06c0de0284053194c022af1f65f2bed1cfc23ac739f5200a839]
<!-- rcw:end owner=source:src_db7ff6322863554684b358606cb2b467 block=evidence -->

## Researcher notes

