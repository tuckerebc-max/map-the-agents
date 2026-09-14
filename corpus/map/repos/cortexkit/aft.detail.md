# cortexkit/aft -- full detail

[Back to orientation](aft.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cortexkit/aft/c0c8e80220ac45e45be98a87c86b28db02c96f49/6ee76353dadd17a8.json](../../../wiki/dossiers/cortexkit/aft/c0c8e80220ac45e45be98a87c86b28db02c96f49/6ee76353dadd17a8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] AFT ships as a Rust binary with thin TypeScript adapter packages for OpenCode, Pi, and OMP, distributed via crates.io and npm. -- evidence: [README.md#L52-L52](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L52-L52), [README.md#L13-L20](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L13-L20) (`clm_92e2335f67aa067d8c69d1b4bddf0cbec100549622391cc8b34df4ed467aca09`)
- [observation/documented] The Rust core includes tree-sitter parsing for ~30 languages, symbol/call-graph computation, diff/format/backup, an LSP client, trigram index, and semantic index. -- evidence: [README.md#L200-L227](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L200-L227) (`clm_11e64d916805d30c3201bd8bb7f526120ca0edd22553aa3f51477bbedc88ecf3`)

## design-choices (1 claim(s))

- [observation/documented] Adapters hoist the host's built-in read/write/edit/grep tool slots so existing tool names are backed by AFT, while also registering an aft_-prefixed tool family; hoist_builtin_tools toggles this behavior. -- evidence: [README.md#L74-L76](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L74-L76), [README.md#L52-L52](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L52-L52) (`clm_a1053f8fd5691740716296e86212648ba500b433e6a59381242ce6f3293afeef`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions require an issue with the design-approved label before a PR is reviewable (typo fixes exempt), and bun run format plus cargo fmt must be run before submitting since CI rejects unformatted code. -- evidence: [README.md#L301-L301](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L301-L301), [README.md#L303-L303](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L303-L303) (`clm_f40bae198e20f25b8d59f031a691403ec4dd07a3ded0cf5a51f51b5bf35660e3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The Rust core communicates with adapters over a JSON-over-stdio request/response protocol, with one persistent process per project root shared across sessions. -- evidence: [README.md#L229-L229](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L229-L229), [README.md#L198-L198](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L198-L198) (`clm_6314dbfccd3808b30e8364578bb547a53dacfbdbfc33aa18676700529bfc314b`)
- [observation/documented] Sensory tools include aft_outline, aft_zoom, aft_search (hybrid semantic+lexical), aft_callgraph, aft_inspect, and trigram-indexed grep/glob backed by a file watcher. -- evidence: [README.md#L112-L117](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L112-L117) (`clm_28cb513f6d52157a603006b66b91e06b62146aa13cdf1bcbec39b30d29363502`)
- [observation/documented] Motor tools include edit with fuzzy matching and multi-file transactions, write, apply_patch with atomic rollback, aft_import, and ast_grep_search/ast_grep_replace. -- evidence: [README.md#L127-L131](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L127-L131) (`clm_08a4698c9777671be9af674afd88ad7bf562e08fb16927831b1c2aa65f8d37dc`)

## memory-state (1 claim(s))

- [observation/documented] AFT data (backups, search indexes, LSP servers) persists under ~/.local/share/cortexkit/aft/, and aft_safety provides a per-file undo stack with named checkpoints that survives restarts. -- evidence: [README.md#L231-L231](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L231-L231), [README.md#L139-L143](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L139-L143) (`clm_4fa1cd83424ef363126652a1a8a3442d99677a29993f358988b3d95d8c8bb0b9`)

## orchestration (1 claim(s))

- [observation/documented] The brainstem layer provides background bash tasks (bash_status, bash_kill, bash_watch) that survive restarts, PTY sessions driven via bash_write, and multi-tier output compression. -- evidence: [README.md#L139-L143](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L139-L143) (`clm_35cf78ed31309ee492e2cd5dcc181c6e135756570a97199ec494a264d21350a6`)

## tools-permissions (1 claim(s))

- [observation/documented] Under sandbox.enabled, first-party bash commands run through Landlock (Linux) or Seatbelt (macOS); unsupported non-Unix platforms fail closed with sandbox_unavailable, and a one-command host escape prompts via an escalation permission ask. -- evidence: [ARCHITECTURE.md#L123-L128](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/ARCHITECTURE.md#L123-L128) (`clm_0ac38f5ead68ab71d3f9f64df8cf27b16796aebca0ab83673ae06b0722dec6b0`)

## evaluation (1 claim(s))

- [observation/documented] A benchmark suite covering search latency, retrieval quality, bash-output token reduction, and end-to-end agent task success is described as in progress, with numbers not yet published. -- evidence: [README.md#L149-L149](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L149-L149), [README.md#L151-L151](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L151-L151) (`clm_630c05f2e5bb06b805cec0874d81445f7dde6597b376b95493115579a3a21adb`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] AFT has no uninstall CLI verb; doctor --clear only clears selected caches, not registration, config, or shared storage, and removal requires manual harness de-registration steps. -- evidence: [README.md#L82-L85](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L82-L85), [README.md#L87-L88](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L87-L88) (`clm_3a592963e2cb61660455d4eb346b1ad8c10d3ca9818595bac5bf61172e6c4633`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

