---
access: public
aliases: []
claim_ids:
- clm_04405ea117b0360bc196b082552e13688623560cb5c9242ab6aeed91a1801b91
- clm_1273b03afdd4bc7ec1b57ac956a9d539f1825be0b3fd199af9148e7b9bcb3cc8
- clm_32e14c06adb7276e6915091da5e9bf544336b1f595d1171d68e818aca174645d
- clm_4b338359fc82b5fea5b1e263ffa51e18e4d947d9dcc61ce7deb90710b63250fe
- clm_5bc9a9e5d6c98c8ae885a9e7c188502d62d4fd9e794f0e26f450f25f1a8b641a
- clm_6bfc78956d372a0a800ac32527e41f7d3c2d0c4959eefd9d44668c8a858bad8d
- clm_7367ecce71a775df3bb55397a2e52ba8b460f05b43b584f4255c482c4e436df1
- clm_773c74c32026905dd6ff4250ec877444d5cfe980f7b85bb51d3ff48cda75e2a1
- clm_a0cf10ba086c1db606807cc798a634e10beb11ddb0627ffcf84a46caf75fb363
- clm_bfcba7695cf5b7d090fa5c557ab0b5529f458a5d035c4d07dd8cdcab54956be5
- clm_ecf9a3f84f8f03a973cd30e513c6fe220f0580aa477d9c4fdb0870004f311931
- clm_f3cd146bf441665f38fcf692c6376905d90341475533aa1ea1d58a53c49c7676
- clm_f428c48d7d504178ec3c6a10fac58529d2d3bcf24b672821af5a3dda9722cc00
- clm_fa80952c07bd32bb66e0f0564131bbb99a2480d4c6c0af4c7842d03a177e4c97
maturity: draft
page_id: pg_8447c99c328958868323133522efb8a8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e813ab72cfd51d8a47f70c867fc354e
title: gabrielchasukjin/cloi/docs/internals.md @ 1da62db7aa3a
updated_at: '2026-09-14T01:50:01Z'
---

# gabrielchasukjin/cloi/docs/internals.md @ 1da62db7aa3a

<!-- rcw:begin owner=source:src_7e813ab72cfd51d8a47f70c867fc354e block=evidence -->
- A session-long Python interpreter exposes stored results as variables and tools as callable functions; variables, imports and helpers persist across sessions, and the namespace is saved per variable between runs. [@claim:clm_04405ea117b0360bc196b082552e13688623560cb5c9242ab6aeed91a1801b91]
- Substantial tool results are stored in full under argument-derived handles (e.g. stats_js, npm_test) and can be recalled whole, sliced, or searched; results over 256 KB are not stored. [@claim:clm_1273b03afdd4bc7ec1b57ac956a9d539f1825be0b3fd199af9148e7b9bcb3cc8]
- Licensed under MIT; relevant as a reference for local-model agent loop design, escalation, verification, and small-model failure guardrails. [@claim:clm_32e14c06adb7276e6915091da5e9bf544336b1f595d1171d68e818aca174645d]
- Safety rails include Levenshtein tool-name repair, doom-loop detection, strike budgets, a hard iteration ceiling, and tool-output truncation at 2000 lines / 50 KB with overflow spilled to a readable temp file. [@claim:clm_4b338359fc82b5fea5b1e263ffa51e18e4d947d9dcc61ce7deb90710b63250fe]
- Tools called from the Python scratchpad still ask permission, so approving a cell does not approve everything it can reach; the python tool also runs with the sanitised environment. [@claim:clm_5bc9a9e5d6c98c8ae885a9e7c188502d62d4fd9e794f0e26f450f25f1a8b641a]
- Escalation to a stronger model is triggered by six observed-failure signals (e.g. repeated identical calls, consecutive tool failures, disproved claims), and the escalated model inherits the full conversation plus a handoff note. [@claim:clm_6bfc78956d372a0a800ac32527e41f7d3c2d0c4959eefd9d44668c8a858bad8d]
- Subprocesses run with a sanitised environment stripping credential-shaped variables, and live secret values are redacted from tool output; the docs note this is defence in depth, not a guarantee. [@claim:clm_7367ecce71a775df3bb55397a2e52ba8b460f05b43b584f4255c482c4e436df1]
- Writes, edits and shell commands ask permission first with three answers (once, always-for-this-tool, no); 'always' is scoped to the running process, and autoApprove config grants durable approval. [@claim:clm_773c74c32026905dd6ff4250ec877444d5cfe980f7b85bb51d3ff48cda75e2a1]
- Conversation state is persisted in SQLite and rebuilt from the database on every loop iteration, so interrupted turns leave a coherent, resumable session. [@claim:clm_a0cf10ba086c1db606807cc798a634e10beb11ddb0627ffcf84a46caf75fb363]
- When the prompt nears the context window, the older half of history is replaced by a summary; nothing is deleted and the on-disk transcript stays whole. [@claim:clm_bfcba7695cf5b7d090fa5c557ab0b5529f458a5d035c4d07dd8cdcab54956be5]
- Answers are verified before display: filesystem-settled claims are checked without a model call (line citations, quotes, absence claims), and a model-based judge review runs only after an escalation. [@claim:clm_ecf9a3f84f8f03a973cd30e513c6fe220f0580aa477d9c4fdb0870004f311931]
- The architecture includes src/agent modules (loop, prompt, permission, verify, judge), tools (fs-tools, shell, todo, workspace, registry), a SQLite session store, an Ollama provider, and setup/hardware/recommendation utilities. [@claim:clm_f3cd146bf441665f38fcf692c6376905d90341475533aa1ea1d58a53c49c7676]
- Repository development practice: tests are run with npm test; the suite covers 126 tests including tool-name repair, permission gating, credential containment, and regression tests for false positives found in live runs. [@claim:clm_f428c48d7d504178ec3c6a10fac58529d2d3bcf24b672821af5a3dda9722cc00]
- The repo includes benchmark scripts (bench/compare.js, bench/python-tool.js) that drive the real agent against real tools; a python-tool benchmark showed accuracy moving from 0/8 to 3/8 with worked examples in the tool description. [@claim:clm_fa80952c07bd32bb66e0f0564131bbb99a2480d4c6c0af4c7842d03a177e4c97]
<!-- rcw:end owner=source:src_7e813ab72cfd51d8a47f70c867fc354e block=evidence -->

## Researcher notes

