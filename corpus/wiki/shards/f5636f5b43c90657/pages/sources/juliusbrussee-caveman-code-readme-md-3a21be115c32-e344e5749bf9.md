---
access: public
aliases: []
claim_ids:
- clm_0935caeba3d8a8cb512cf4c40336fd91d14c0ffed4edc920e7cf6466b391ed17
- clm_145664b82c194b450e86b577f10792e6196286390cbdcc48db2c50a286b0d85b
- clm_2d64d6167fcb505d94cf81f2867c964e2d9437ac0d6fb58c4664a2af2ab5c135
- clm_2e0edb83bd8559cee4110fe68ee45798169d5fbb2e3cf4b4e6e8ddce4945f68d
- clm_343c0d65b2c8bcc244f58e17ffb1369dbb9470a8d0e9b69c46ec807d1bd20289
- clm_4670ce2e3e9d8f01cc191cb86ce5e23ef49beb990a31d39b84bfabd369ac6349
- clm_596a53f0328b783dab9efb6ac9507da4eda66d2dfdda08d9af45ec7fd024c7c9
- clm_6e27a93845832ca0ab19b901e788c1277165e91ac5b1f4f762a2deb17520eac9
- clm_8389974b6b2e3846e78fa969dcc3110a517e092dc0879149a451467355a8ef3c
- clm_9925771e5142e28560805a64d09e7231b3b50395adaf1641bac9a9bbc3fc23f7
- clm_9d3d8dd76127445195cadf2a2c4bd6a9040aa4f3c6e8bea6a61c86937ee48337
- clm_b1005c391272f4010296e5c50b86dab123f6880cc8507a2a3974c831c0503e3a
- clm_b35f0fbc5e4b02bb5463955a71b601abe606348617352571d4db845d0270eb52
- clm_bea2baea5a088d570b286a5853cc0e0cbac3b62a6231622e7c187824fe442272
- clm_e45d6fc99ae27f816d6b6bc4816b49ffb345e2c98b59007ae33c9fde016aa548
- clm_ff8557c07fa4761aef7ead63b95f2bbe609ae09b86db57b0049e641481bd1f9a
maturity: draft
page_id: pg_4e626c6368d55595ad4ee344e5749bf9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_40b843c1c27a55bfa661dab740534527
title: JuliusBrussee/caveman-code/README.md @ 3a21be115c32
updated_at: '2026-09-14T02:08:09Z'
---

# JuliusBrussee/caveman-code/README.md @ 3a21be115c32

<!-- rcw:begin owner=source:src_40b843c1c27a55bfa661dab740534527 block=evidence -->
- The CLI installs two binaries, 'caveman' (primary) and 'caveman-code' (alias), and supports TUI, one-shot prompt, print mode (-p), stdin piping, session continue/resume (-c/-r), and 'goal start' for an autonomous loop. [@claim:clm_0935caeba3d8a8cb512cf4c40336fd91d14c0ffed4edc920e7cf6466b391ed17]
- Optional external dependencies include the RTK Rust binary (pipes bash output through compression before it enters context) and cavemem for memory; both are integrations the agent can use rather than hard requirements. [@claim:clm_145664b82c194b450e86b577f10792e6196286390cbdcc48db2c50a286b0d85b]
- An autonomous 'Ralph-style' goal loop is triggered by 'caveman goal start', with rolling state, per-iteration cost/token ledger, shadow-git checkpoints, and ranked termination conditions (sentinel, iteration cap, dollar cap, no-progress, SIGINT). [@claim:clm_2d64d6167fcb505d94cf81f2867c964e2d9437ac0d6fb58c4664a2af2ab5c135]
- A published 25-task MicroBench (gpt-5.5, xhigh reasoning, 2026-05-18) reports caveman at 524k fresh tokens and 14/25 pass rate versus Codex's 1,010k and 15/25, with each task verified by a task-specific verify.sh and raw CSV/logs published. [@claim:clm_2e0edb83bd8559cee4110fe68ee45798169d5fbb2e3cf4b4e6e8ddce4945f68d]
- Persistent memory is delegated to cavemem (hybrid BM25 + local vectors on SQLite/FTS5); the agent exposes memory_search and memory_save tools, auto-injects relevant recall each turn capped at 2k tokens by default, and can fall back to plain markdown files via memory.provider: files. [@claim:clm_343c0d65b2c8bcc244f58e17ffb1369dbb9470a8d0e9b69c46ec807d1bd20289]
- The benchmark is reproducible via 'npx tsx research/evals/run-honest-bench.ts --tools caveman,codex', and separate offline/replay/live bench scripts measure compression savings on tool-output fixtures (aggregate −86% across 10 fixtures). [@claim:clm_4670ce2e3e9d8f01cc191cb86ce5e23ef49beb990a31d39b84bfabd369ac6349]
- The core design is four always-on compression layers targeting two token sinks: model replies (Caveman Mode with lite/full/ultra levels) and tool output (tool budgets, read dedup, optional RTK). [@claim:clm_596a53f0328b783dab9efb6ac9507da4eda66d2dfdda08d9af45ec7fd024c7c9]
- Up to 7 parallel subagents run worktree-isolated via the Task tool, configured as frontmatter agent files at .cave/agents/*.md, with five shipped by default. [@claim:clm_6e27a93845832ca0ab19b901e788c1277165e91ac5b1f4f762a2deb17520eac9]
- Tool-output compression applies per-tool line caps (bash 80, read 300, grep 120), strips ANSI, collapses blank lines, and does semantic JSON/XML extraction, with claimed cuts of 67–94%. [@claim:clm_8389974b6b2e3846e78fa969dcc3110a517e092dc0879149a451467355a8ef3c]
- Provider support spans 20+ providers with 6 OAuth flows (Claude Pro/Max, ChatGPT Plus/Pro, Copilot, Gemini, Antigravity, Vertex) plus API-key providers and custom OpenAI-/Anthropic-/Google-compatible endpoints via ~/.cave/agent/models.json. [@claim:clm_9925771e5142e28560805a64d09e7231b3b50395adaf1641bac9a9bbc3fc23f7]
- Plan mode (/plan) restricts the model to read-only tools (read/grep/find/ls), produces a written plan without edits, and subagents inherit the gate; /act executes the saved plan. [@claim:clm_9d3d8dd76127445195cadf2a2c4bd6a9040aa4f3c6e8bea6a61c86937ee48337]
- The repository is described as a TypeScript monorepo of 9 packages, with the coding-agent package exporting full TypeScript types and hosting the daemon's OpenAPI 3.1 spec. [@claim:clm_b1005c391272f4010296e5c50b86dab123f6880cc8507a2a3974c831c0503e3a]
- A daemon mode ('caveman serve --port 39245') stores sessions in SQLite that survive SSH drops, supports TUI attach, and can dispatch prompts to remote 'caveman worker' processes by prefixing a prompt with '&'. [@claim:clm_b35f0fbc5e4b02bb5463955a71b601abe606348617352571d4db845d0270eb52]
- The package installs a 'caveman' binary that shadows the CLI from the newer caveman repo, so one must be uninstalled before installing the other. [@claim:clm_bea2baea5a088d570b286a5853cc0e0cbac3b62a6231622e7c187824fe442272]
- The project is marked frozen as of August 2026: it still installs and works but receives no new features or fixes, and its lesson moved into the separate 'caveman' project. [@claim:clm_e45d6fc99ae27f816d6b6bc4816b49ffb345e2c98b59007ae33c9fde016aa548]
- Caveman Code is MIT-licensed and described as a heavy fork of Mario Zechner's pi-code, with upstream tracked and fixes contributed back where generally useful. [@claim:clm_ff8557c07fa4761aef7ead63b95f2bbe609ae09b86db57b0049e641481bd1f9a]
<!-- rcw:end owner=source:src_40b843c1c27a55bfa661dab740534527 block=evidence -->

## Researcher notes

