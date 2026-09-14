---
access: public
aliases: []
claim_ids:
- clm_31614ee8d45f114e1f5cfd704bfde4cf8aff960ddd190bad2d3339953db9b9e9
- clm_56362f1b1d86421c033df958698df75f390bad0c74f09e68a7484887539641ba
- clm_8d60816fe7a3c7c586d50d095029cd8d434adea918445aa4b9662b93ee352a5d
- clm_9dc05de35934eee74b658c016c9fba0b0203167a8f5ae3bc948454c1814ce0c9
- clm_f2ee48ade199175ce7a65363c17f2a84e0440065382924263e8e339f0e193de8
maturity: draft
page_id: pg_d01c02b10d895f4690afe0b6b1de7bc6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2b5525f8934e5d8b945a1f1bfec523ef
title: echoVic/blade-code/README.md @ 8917e4e0ef61
updated_at: '2026-09-14T02:00:47Z'
---

# echoVic/blade-code/README.md @ 8917e4e0ef61

<!-- rcw:begin owner=source:src_2b5525f8934e5d8b945a1f1bfec523ef block=evidence -->
- The product ships as an interactive CLI ('blade'), a Web UI ('blade web'), a headless HTTP server ('blade serve'), non-interactive modes '--headless' with JSONL output, and a single-turn '--print' mode. [@claim:clm_31614ee8d45f114e1f5cfd704bfde4cf8aff960ddd190bad2d3339953db9b9e9]
- In-session slash commands include /model add and /model switch, /cost, /compact, /btw for side questions, /memory list, /tasks, and /goal to start Goal mode. [@claim:clm_56362f1b1d86421c033df958698df75f390bad0c74f09e68a7484887539641ba]
- The repository layout places the agent core and execution loop in packages/cli/src/agent, the pi-ai adapter in services/pi, a TypeBox-based tool system, a Hono web server, and a React+Vite web UI. [@claim:clm_8d60816fe7a3c7c586d50d095029cd8d434adea918445aa4b9662b93ee352a5d]
- The runtime uses the pi-ai library to unify 38+ model providers (OpenAI, Anthropic, DeepSeek, Google, Bedrock) with model metadata fetched dynamically from the pi-ai catalog. [@claim:clm_9dc05de35934eee74b658c016c9fba0b0203167a8f5ae3bc948454c1814ce0c9]
- Repository development practice: contributors clone the repo and run 'bun install && bun run dev' to develop locally, and a CONTRIBUTING.md guide is referenced. [@claim:clm_f2ee48ade199175ce7a65363c17f2a84e0440065382924263e8e339f0e193de8]
<!-- rcw:end owner=source:src_2b5525f8934e5d8b945a1f1bfec523ef block=evidence -->

## Researcher notes

