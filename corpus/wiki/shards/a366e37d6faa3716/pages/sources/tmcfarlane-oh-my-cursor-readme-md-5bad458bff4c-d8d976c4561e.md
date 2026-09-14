---
access: public
aliases: []
claim_ids:
- clm_175a675379fb5ebfae4db9c351020961944ce3f75e6259db51a1a75ae6e0d90d
- clm_218c206cdf72a2a5a326ac004db0c58386493041add66c49c1bd7dd5cf4f0c2e
- clm_22d5c6340e728f553e5e992f22048e97181d9668881f11cfb8792ebfac3c00a5
- clm_28235d4db184be1f31a9edae28411c37017f841f75d732636de60e280a4979d8
- clm_2c206cd08c2fabaeead0b2d3451a0e6333cf7a9d79f545d6a15205347648ff82
- clm_50699e2f38d65fcdd6fd4838f1ea70160d72f821a047ca6018945507c6ceacdd
- clm_57651503d8478abd2c8bef4b5f0f2dc31262c0eeb8dbc9da2b1fd86d722e3671
- clm_57bb1ec049a4b97399cd70947302af05245d4e61bccf10c0e369a52d2df1918f
- clm_6da49be344dcd27065b82a9c85f22c10cca84912cc0b39e3a9b56eb6ed7fc0b4
- clm_7cb6ed239ff8b943c9be60f56704dec43f47c49a25732229f61c4032a72f9b78
- clm_843034a99a7e9a0c48e2ea18d0d59ff954b90d2711a91d5dc7cc2f097d36756d
- clm_911d9c9bd8f5e4a4a42658eb309c648c1814ba4608ba475e03839058f46bcbf8
- clm_c1693add8051da1924624812cf80bf10efe56b6a4e275d472bd5c203f4e35094
- clm_df796cde9d43da13b49cce5f3477cfbdaae861f3e215bf17c2befbdc90e5e277
- clm_ff47ac7fd69edc911c5fe8b48e1923fc1a6d1356c594426f8fbdfa8eba518abe
maturity: draft
page_id: pg_d068923c33e059248b0dd8d976c4561e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_448adfbd88f35385863558a3cbcfbc92
title: tmcfarlane/oh-my-cursor/README.md @ 5bad458bff4c
updated_at: '2026-09-14T04:26:36Z'
---

# tmcfarlane/oh-my-cursor/README.md @ 5bad458bff4c

<!-- rcw:begin owner=source:src_448adfbd88f35385863558a3cbcfbc92 block=evidence -->
- 19 community-sourced skills are vendored in-repo as SKILL.md directories that Cursor auto-discovers, installed by default with a --no-skills option to skip them. [@claim:clm_175a675379fb5ebfae4db9c351020961944ce3f75e6259db51a1a75ae6e0d90d]
- Slash commands map to agents: /plan (Sokka), /build (Aang), /search (Toph), /fix (Katara), /tasks (Appa), /scout (Momo), /doc (Iroh), /image (Zuko), and /cactus-juice (swarm). [@claim:clm_218c206cdf72a2a5a326ac004db0c58386493041add66c49c1bd7dd5cf4f0c2e]
- Per-agent model routing uses Cursor's model: frontmatter field; the default is composer-2.5-fast, with Sokka and Iroh on claude-opus-4-8-thinking-high and Zuko on gemini-3.1-pro. [@claim:clm_22d5c6340e728f553e5e992f22048e97181d9668881f11cfb8792ebfac3c00a5]
- The installer supports user (default ~/.cursor) and project (./.cursor) scopes, plus --claude/--codex cross-tool installs, --dry-run, --force, --uninstall, and --disable/--enable orchestration flags. [@claim:clm_28235d4db184be1f31a9edae28411c37017f841f75d732636de60e280a4979d8]
- Repository development practice: contributors clone the repo and run bash install.sh (or install.ps1 on Windows) to install from source; changes to agents, rules, commands, or hooks take effect after reinstalling. [@claim:clm_2c206cd08c2fabaeead0b2d3451a0e6333cf7a9d79f545d6a15205347648ff82]
- On Cursor 3.4+ a two-tier swarm pattern applies: coordinators (Aang, Sokka, Katara, Appa) spawn worker agents (Toph, Momo) as leaf nodes with max depth 2; Zuko is root-only. [@claim:clm_50699e2f38d65fcdd6fd4838f1ea70160d72f821a047ca6018945507c6ceacdd]
- A '/cactus-juice' swarm mode decomposes requests into 5-10 independent single-file micro-tasks and spawns up to 10 parallel fast-model subagents, with the root collecting and verifying results. [@claim:clm_57651503d8478abd2c8bef4b5f0f2dc31262c0eeb8dbc9da2b1fd86d722e3671]
- A permissions.json auto-review policy auto-runs safe calls (lints, tests, builds, read-only git) and holds risky ones (destructive filesystem, history rewrites, credential access, outbound network) for review. [@claim:clm_57bb1ec049a4b97399cd70947302af05245d4e61bccf10c0e369a52d2df1918f]
- The README states hooks and auto-review are best-effort and not a security boundary, reducing footguns and approval spam without replacing real sandboxing. [@claim:clm_6da49be344dcd27065b82a9c85f22c10cca84912cc0b39e3a9b56eb6ed7fc0b4]
- The orchestrator rule makes the root thread a pure dispatcher whose only permitted tools are Task, TodoWrite, AskQuestion, and SwitchMode, delegating all work to specialist agents. [@claim:clm_7cb6ed239ff8b943c9be60f56704dec43f47c49a25732229f61c4032a72f9b78]
- Hooks wired via .cursor/hooks.json include guard-shell.sh, which blocks destructive shell commands and commits containing anti-patterns like 'as any' or '@ts-ignore', returning allow/deny/ask decisions on beforeShellExecution. [@claim:clm_843034a99a7e9a0c48e2ea18d0d59ff954b90d2711a91d5dc7cc2f097d36756d]
- The project ships 8 agent manifests, 8 slash commands, hooks, and one orchestration rule as pure Markdown/config files for Cursor, with no external runtime or wrapper CLI. [@claim:clm_911d9c9bd8f5e4a4a42658eb309c648c1814ba4608ba475e03839058f46bcbf8]
- docs/E2E-TEST.md is described as a 15-check runbook (model routing, hook enforcement, auto-review) run attended against a live Cursor app, producing a pass/fail table; v0.4.1 validation moved from 13/15 to 15/15 on Cursor 3.9.8. [@claim:clm_c1693add8051da1924624812cf80bf10efe56b6a4e275d472bd5c203f4e35094]
- An invalid model slug does not error but silently falls back to composer-2.5-fast, so a typo can make an agent run the wrong model unnoticed; slugs also change between Cursor versions. [@claim:clm_df796cde9d43da13b49cce5f3477cfbdaae861f3e215bf17c2befbdc90e5e277]
- Requires Cursor 3.4+ with agent mode (subagents); the project is MIT licensed and validated against Cursor 3.8.23 and 3.9.8 per its badges and changelog. [@claim:clm_ff47ac7fd69edc911c5fe8b48e1923fc1a6d1356c594426f8fbdfa8eba518abe]
<!-- rcw:end owner=source:src_448adfbd88f35385863558a3cbcfbc92 block=evidence -->

## Researcher notes

