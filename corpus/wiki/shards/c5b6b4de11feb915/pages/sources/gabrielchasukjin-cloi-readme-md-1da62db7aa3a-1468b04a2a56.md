---
access: public
aliases: []
claim_ids:
- clm_04405ea117b0360bc196b082552e13688623560cb5c9242ab6aeed91a1801b91
- clm_1273b03afdd4bc7ec1b57ac956a9d539f1825be0b3fd199af9148e7b9bcb3cc8
- clm_16c16421cb2fc7e7814a764289f41260d13dcd1f91b27b95b7fe93eecf222178
- clm_32e14c06adb7276e6915091da5e9bf544336b1f595d1171d68e818aca174645d
- clm_388c2c0247634f8219ee7dcacd582dedac6ea9d8f336ef1c5a1ec8394fb47127
- clm_5bc9a9e5d6c98c8ae885a9e7c188502d62d4fd9e794f0e26f450f25f1a8b641a
- clm_6a22bb37ede2132577d01c54ec088bd43af0c4a84f7911a2d21c169a979531ea
- clm_6bfc78956d372a0a800ac32527e41f7d3c2d0c4959eefd9d44668c8a858bad8d
- clm_7367ecce71a775df3bb55397a2e52ba8b460f05b43b584f4255c482c4e436df1
- clm_773c74c32026905dd6ff4250ec877444d5cfe980f7b85bb51d3ff48cda75e2a1
- clm_bfcba7695cf5b7d090fa5c557ab0b5529f458a5d035c4d07dd8cdcab54956be5
- clm_c0d6581da761cf70cb22e969b11c3128ea7ede387b7a1f85c964a3f5560f8478
- clm_e49387aa311048d2d0f7b76d4a60e8fcdab907387d16a7468931483193f5433f
- clm_ecf9a3f84f8f03a973cd30e513c6fe220f0580aa477d9c4fdb0870004f311931
- clm_fa80952c07bd32bb66e0f0564131bbb99a2480d4c6c0af4c7842d03a177e4c97
maturity: draft
page_id: pg_9228e6d93f7c5ab89c381468b04a2a56
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_056886ad297f5cf4be4b95a47ccc59c6
title: gabrielchasukjin/cloi/README.md @ 1da62db7aa3a
updated_at: '2026-09-14T01:50:01Z'
---

# gabrielchasukjin/cloi/README.md @ 1da62db7aa3a

<!-- rcw:begin owner=source:src_056886ad297f5cf4be4b95a47ccc59c6 block=evidence -->
- A session-long Python interpreter exposes stored results as variables and tools as callable functions; variables, imports and helpers persist across sessions, and the namespace is saved per variable between runs. [@claim:clm_04405ea117b0360bc196b082552e13688623560cb5c9242ab6aeed91a1801b91]
- Substantial tool results are stored in full under argument-derived handles (e.g. stats_js, npm_test) and can be recalled whole, sliced, or searched; results over 256 KB are not stored. [@claim:clm_1273b03afdd4bc7ec1b57ac956a9d539f1825be0b3fd199af9148e7b9bcb3cc8]
- Setup reads VRAM, RAM and core count and proposes two models: a primary that must fit in VRAM and a fallback that only needs to fit in RAM, stepping down the primary if the prediction was wrong. [@claim:clm_16c16421cb2fc7e7814a764289f41260d13dcd1f91b27b95b7fe93eecf222178]
- Licensed under MIT; relevant as a reference for local-model agent loop design, escalation, verification, and small-model failure guardrails. [@claim:clm_32e14c06adb7276e6915091da5e9bf544336b1f595d1171d68e818aca174645d]
- Running Cloi requires Ollama, Node 22.5+, and a tool-capable model; it is installed via npm as @cloi-ai/cloi. [@claim:clm_388c2c0247634f8219ee7dcacd582dedac6ea9d8f336ef1c5a1ec8394fb47127]
- Tools called from the Python scratchpad still ask permission, so approving a cell does not approve everything it can reach; the python tool also runs with the sanitised environment. [@claim:clm_5bc9a9e5d6c98c8ae885a9e7c188502d62d4fd9e794f0e26f450f25f1a8b641a]
- Documented gaps: only Ollama is wired up, no sub-agents, no MCP, no web access, and hard cross-file debugging scored 0/12 in the benchmark for models fitting 8 GB. [@claim:clm_6a22bb37ede2132577d01c54ec088bd43af0c4a84f7911a2d21c169a979531ea]
- Escalation to a stronger model is triggered by six observed-failure signals (e.g. repeated identical calls, consecutive tool failures, disproved claims), and the escalated model inherits the full conversation plus a handoff note. [@claim:clm_6bfc78956d372a0a800ac32527e41f7d3c2d0c4959eefd9d44668c8a858bad8d]
- Subprocesses run with a sanitised environment stripping credential-shaped variables, and live secret values are redacted from tool output; the docs note this is defence in depth, not a guarantee. [@claim:clm_7367ecce71a775df3bb55397a2e52ba8b460f05b43b584f4255c482c4e436df1]
- Writes, edits and shell commands ask permission first with three answers (once, always-for-this-tool, no); 'always' is scoped to the running process, and autoApprove config grants durable approval. [@claim:clm_773c74c32026905dd6ff4250ec877444d5cfe980f7b85bb51d3ff48cda75e2a1]
- When the prompt nears the context window, the older half of history is replaced by a summary; nothing is deleted and the on-disk transcript stays whole. [@claim:clm_bfcba7695cf5b7d090fa5c557ab0b5529f458a5d035c4d07dd8cdcab54956be5]
- The CLI supports interactive sessions, one-shot requests, --continue to resume a session, and cloi setup to re-pick models; in-session slash commands include /model, /tools, /plan, /usage, /sessions, /help. [@claim:clm_c0d6581da761cf70cb22e969b11c3128ea7ede387b7a1f85c964a3f5560f8478]
- Cloi is described as a local-first terminal coding agent that reads, searches, writes and edits files and runs commands in the workspace, with everything running locally and no API key. [@claim:clm_e49387aa311048d2d0f7b76d4a60e8fcdab907387d16a7468931483193f5433f]
- Answers are verified before display: filesystem-settled claims are checked without a model call (line citations, quotes, absence claims), and a model-based judge review runs only after an escalation. [@claim:clm_ecf9a3f84f8f03a973cd30e513c6fe220f0580aa477d9c4fdb0870004f311931]
- The repo includes benchmark scripts (bench/compare.js, bench/python-tool.js) that drive the real agent against real tools; a python-tool benchmark showed accuracy moving from 0/8 to 3/8 with worked examples in the tool description. [@claim:clm_fa80952c07bd32bb66e0f0564131bbb99a2480d4c6c0af4c7842d03a177e4c97]
<!-- rcw:end owner=source:src_056886ad297f5cf4be4b95a47ccc59c6 block=evidence -->

## Researcher notes

