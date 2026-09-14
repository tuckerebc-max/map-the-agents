---
access: public
aliases: []
claim_ids:
- clm_08a4698c9777671be9af674afd88ad7bf562e08fb16927831b1c2aa65f8d37dc
- clm_11e64d916805d30c3201bd8bb7f526120ca0edd22553aa3f51477bbedc88ecf3
- clm_28cb513f6d52157a603006b66b91e06b62146aa13cdf1bcbec39b30d29363502
- clm_35cf78ed31309ee492e2cd5dcc181c6e135756570a97199ec494a264d21350a6
- clm_3a592963e2cb61660455d4eb346b1ad8c10d3ca9818595bac5bf61172e6c4633
- clm_4fa1cd83424ef363126652a1a8a3442d99677a29993f358988b3d95d8c8bb0b9
- clm_630c05f2e5bb06b805cec0874d81445f7dde6597b376b95493115579a3a21adb
- clm_6314dbfccd3808b30e8364578bb547a53dacfbdbfc33aa18676700529bfc314b
- clm_92e2335f67aa067d8c69d1b4bddf0cbec100549622391cc8b34df4ed467aca09
- clm_a1053f8fd5691740716296e86212648ba500b433e6a59381242ce6f3293afeef
- clm_f40bae198e20f25b8d59f031a691403ec4dd07a3ded0cf5a51f51b5bf35660e3
maturity: draft
page_id: pg_2e3833c6e8ba5e09a32e0de889f5c71d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_84c0c3e796265a29bd591ca9b8bbc0e1
title: cortexkit/aft/README.md @ c0c8e80220ac
updated_at: '2026-09-14T03:42:55Z'
---

# cortexkit/aft/README.md @ c0c8e80220ac

<!-- rcw:begin owner=source:src_84c0c3e796265a29bd591ca9b8bbc0e1 block=evidence -->
- Motor tools include edit with fuzzy matching and multi-file transactions, write, apply_patch with atomic rollback, aft_import, and ast_grep_search/ast_grep_replace. [@claim:clm_08a4698c9777671be9af674afd88ad7bf562e08fb16927831b1c2aa65f8d37dc]
- The Rust core includes tree-sitter parsing for ~30 languages, symbol/call-graph computation, diff/format/backup, an LSP client, trigram index, and semantic index. [@claim:clm_11e64d916805d30c3201bd8bb7f526120ca0edd22553aa3f51477bbedc88ecf3]
- Sensory tools include aft_outline, aft_zoom, aft_search (hybrid semantic+lexical), aft_callgraph, aft_inspect, and trigram-indexed grep/glob backed by a file watcher. [@claim:clm_28cb513f6d52157a603006b66b91e06b62146aa13cdf1bcbec39b30d29363502]
- The brainstem layer provides background bash tasks (bash_status, bash_kill, bash_watch) that survive restarts, PTY sessions driven via bash_write, and multi-tier output compression. [@claim:clm_35cf78ed31309ee492e2cd5dcc181c6e135756570a97199ec494a264d21350a6]
- AFT has no uninstall CLI verb; doctor --clear only clears selected caches, not registration, config, or shared storage, and removal requires manual harness de-registration steps. [@claim:clm_3a592963e2cb61660455d4eb346b1ad8c10d3ca9818595bac5bf61172e6c4633]
- AFT data (backups, search indexes, LSP servers) persists under ~/.local/share/cortexkit/aft/, and aft_safety provides a per-file undo stack with named checkpoints that survives restarts. [@claim:clm_4fa1cd83424ef363126652a1a8a3442d99677a29993f358988b3d95d8c8bb0b9]
- A benchmark suite covering search latency, retrieval quality, bash-output token reduction, and end-to-end agent task success is described as in progress, with numbers not yet published. [@claim:clm_630c05f2e5bb06b805cec0874d81445f7dde6597b376b95493115579a3a21adb]
- The Rust core communicates with adapters over a JSON-over-stdio request/response protocol, with one persistent process per project root shared across sessions. [@claim:clm_6314dbfccd3808b30e8364578bb547a53dacfbdbfc33aa18676700529bfc314b]
- AFT ships as a Rust binary with thin TypeScript adapter packages for OpenCode, Pi, and OMP, distributed via crates.io and npm. [@claim:clm_92e2335f67aa067d8c69d1b4bddf0cbec100549622391cc8b34df4ed467aca09]
- Adapters hoist the host's built-in read/write/edit/grep tool slots so existing tool names are backed by AFT, while also registering an aft_-prefixed tool family; hoist_builtin_tools toggles this behavior. [@claim:clm_a1053f8fd5691740716296e86212648ba500b433e6a59381242ce6f3293afeef]
- Repository development practice: contributions require an issue with the design-approved label before a PR is reviewable (typo fixes exempt), and bun run format plus cargo fmt must be run before submitting since CI rejects unformatted code. [@claim:clm_f40bae198e20f25b8d59f031a691403ec4dd07a3ded0cf5a51f51b5bf35660e3]
<!-- rcw:end owner=source:src_84c0c3e796265a29bd591ca9b8bbc0e1 block=evidence -->

## Researcher notes

