---
access: public
aliases: []
claim_ids:
- clm_017faa0cbaaf43ee23a1d3ec997a9dfb42a1d566b7437d275029ac48a5b64949
- clm_02011da69bbf74c81888bbae3faca43846633aa9a8c78a4f06a1e71fb4cdc6c2
- clm_127af993f42400a88dd4141a77e2e2c5e02f31dad4eed105f7fe14e6e3dcd847
- clm_161bcf4eddb511af5b2f7ff00ae51ed2c69e4692e7f4292ab68abd5b64b771ab
- clm_1eca237c3520f8342d800282c4ad374bc38ecc2dcb9c110ec69fa8c2f95fcd42
- clm_3ffc63cbc0879acdda1390af2392c9e6e1b71bf70bc50be7b539ca1d18fd655e
- clm_4d9c60a321fbb971b5ef835cfab111699ffb331093beebdc2ad24b6dccb01067
- clm_58973e8fe85ab373e8755372f95391b1ac06356fb2abea79894a7de474fb6a4a
- clm_c8120fae9c74cc2c013fd43d002e3f8705a2e2fa1653f571606615604cd03424
- clm_f781504c28d792a98b1db39c555896954a53e7c1415b1f8ae0f0e1642040448f
- clm_fc9074d29ede2832838747342a54e50e667e6b6505a9de115bab1a05c57661bd
maturity: draft
page_id: pg_5f1105f37d8f548da4c536fdce28fa75
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7a0a58936ecc5662b59e0741d37b912f
title: construct-worlds/construct/README.md @ cf75b7398c78
updated_at: '2026-09-14T01:44:06Z'
---

# construct-worlds/construct/README.md @ cf75b7398c78

<!-- rcw:begin owner=source:src_7a0a58936ecc5662b59e0741d37b912f block=evidence -->
- Every session gets construct's MCP tools, letting any harness spawn subagents, send them input, and read their output for agent-to-agent orchestration. [@claim:clm_017faa0cbaaf43ee23a1d3ec997a9dfb42a1d566b7437d275029ac48a5b64949]
- Construct wraps CLIs already on the machine; users must install and authenticate harnesses such as codex, claude, opencode, agy, grok, muse, and prime-agent, while smith is built in. [@claim:clm_02011da69bbf74c81888bbae3faca43846633aa9a8c78a4f06a1e71fb4cdc6c2]
- Lineage lets sessions branch like ideas: a session can be forked for a parallel attempt, including cross-harness forks, and results merged back. [@claim:clm_127af993f42400a88dd4141a77e2e2c5e02f31dad4eed105f7fe14e6e3dcd847]
- Sessions live in the daemon rather than the terminal, so SSH drops or laptop sleep do not stop agents, and users can reattach with scrollback intact. [@claim:clm_161bcf4eddb511af5b2f7ff00ae51ed2c69e4692e7f4292ab68abd5b64b771ab]
- `/remote-control` opens a browser-accessible web client with a QR code so users can connect from a phone without service signup or setup. [@claim:clm_1eca237c3520f8342d800282c4ad374bc38ecc2dcb9c110ec69fa8c2f95fcd42]
- The daemon owns sessions, persists state, and exposes the local IPC socket used by clients; lifecycle helpers include daemon start/stop/restart with session-safe stop variants. [@claim:clm_3ffc63cbc0879acdda1390af2392c9e6e1b71bf70bc50be7b539ca1d18fd655e]
- The harness adapter protocol uses separate adapter processes speaking JSON-RPC over stdio, so new tools can plug in without changing the daemon. [@claim:clm_4d9c60a321fbb971b5ef835cfab111699ffb331093beebdc2ad24b6dccb01067]
- Construct is a single Rust binary that includes a TUI, control CLI, daemon, ACP stdio server, an internal MCP bridge, and harness adapters. [@claim:clm_58973e8fe85ab373e8755372f95391b1ac06356fb2abea79894a7de474fb6a4a]
- `construct acp` runs an Agent Client Protocol stdio server that auto-starts the daemon if needed and maps ACP session lifecycle calls onto daemon sessions, with --harness/--model/--cwd defaults. [@claim:clm_c8120fae9c74cc2c013fd43d002e3f8705a2e2fa1653f571606615604cd03424]
- The TUI supports `?` for help and `M-x` for a command palette, and users can create sessions, switch agents, send input, inspect diffs, and interrupt work from it. [@claim:clm_f781504c28d792a98b1db39c555896954a53e7c1415b1f8ae0f0e1642040448f]
- Running `construct` auto-starts a background daemon and attaches if none is running; this can be disabled with CONSTRUCT_NO_AUTOSTART=1. [@claim:clm_fc9074d29ede2832838747342a54e50e667e6b6505a9de115bab1a05c57661bd]
<!-- rcw:end owner=source:src_7a0a58936ecc5662b59e0741d37b912f block=evidence -->

## Researcher notes

