# vincentkoc/tokenjuice -- full detail

[Back to orientation](tokenjuice.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vincentkoc/tokenjuice/43a621ab06ef0198d728b93c93660ce5c381cb11/b841247bdb2e28e8.json](../../../wiki/dossiers/vincentkoc/tokenjuice/43a621ab06ef0198d728b93c93660ce5c381cb11/b841247bdb2e28e8.json)

## specifications (1 claim(s))

- [observation/documented] tokenjuice is described as a deterministic output compactor for terminal-heavy agent workflows: it observes command output after execution and returns a smaller payload built from rule-driven reducers instead of the full terminal text. -- evidence: [README.md#L9-L9](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L9-L9) (`clm_9236783652fb6073241ccd2c6160a2b6df79cef51773d2d8df8258f43f40b27f`)

## components (1 claim(s))

- [observation/documented] The reduction engine is rule-driven: built-in JSON rules live in src/rules, user overrides in ~/.config/tokenjuice/rules, and project overrides in .tokenjuice/rules, with later layers overriding earlier ones by rule id. -- evidence: [README.md#L192-L192](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L192-L192) (`clm_c4076aa8303a4fe2a278b2ee6ba86f0fdb8a1d32183dc38d1d7b2ce591ba1fff`)

## design-choices (2 claim(s))

- [observation/documented] The design keeps command semantics untouched, exposes raw output only via explicit --raw/--full or opt-in artifact storage, keeps rules as inspectable JSON, and keeps host integrations as thin wrappers around one shared core reducer. -- evidence: [README.md#L11-L11](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L11-L11), [README.md#L9-L9](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L9-L9) (`clm_a61f3305173e2669b96b8618c2fcb64b7a5f9cb5f05c4cafdfdbf3a027eaa995`)
- [observation/documented] Host adapters apply a narrow safe-inventory policy: exact file-content reads stay raw, standalone repository inventory commands can be compacted, and unsafe mixed command sequences stay raw. -- evidence: [README.md#L192-L192](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L192-L192) (`clm_1baf119d122b6de0611f2750b4801eb0a8641396e85f7ac74c4570636c8325f6`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: Homebrew publication is owned by the Tokenjuice workflow in the canonical vincentkoc/homebrew-tap repository, and release maintainers dispatch it manually with the published tag until GitHub App automation lands. -- evidence: [README.md#L139-L141](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L139-L141) (`clm_6b1c93925aca75d3c71781f7ffffa0a712075c9edddc351d57440f94fc21e496`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The CLI has three surfaces: `reduce` compacts existing text, `wrap` runs a command and compacts its observed output, and `reduce-json` provides a stable machine protocol for host adapters. -- evidence: [README.md#L190-L190](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L190-L190) (`clm_2aed415c8051e4b113c13b67c42346d05963b8fe58f50e20418c8295f6c44335`)
- [observation/documented] `reduce-json` reads JSON from stdin or a file and always writes JSON to stdout; the documented payload includes fields such as toolName, command, argv, combinedText, and exitCode. -- evidence: [README.md#L218-L226](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L218-L226), [README.md#L214-L214](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L214-L214) (`clm_8563deaaa301352baa4c73d3913786e76f8ec4a7f11e3a00d0f27e1c028ed95e`)
- [observation/documented] Statistics use bounded metadata segments, support paging via --limit and a returned --cursor, report partial coverage, and can be disabled with TOKENJUICE_STATS=off or --no-stats; artifact retention is opt-in via --store. -- evidence: [README.md#L201-L201](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L201-L201) (`clm_798e8d56af8265e89e755d8d3222777cddce51f50f3fbfb205a6d277e166807e`)
- [observation/documented] The CLI ships install/uninstall commands covering many agent hosts (including claude-code, codex, cursor, droid, copilot-cli), plus `doctor hooks` to check installed wiring and `doctor <host>` for a single integration. -- evidence: [README.md#L163-L186](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L163-L186), [README.md#L145-L150](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L145-L150), [README.md#L190-L190](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L190-L190) (`clm_12ea4a9761d815c0765fd9fb08e4dadbc95984e948a10978c95757180111e2e4`)
- [observation/documented] Documented integrations include Claude Code, CodeBuddy, Codex CLI, Cursor, Droid, GitHub Copilot CLI, and OpenClaw, each with an install command and hook/settings file location; OpenClaw support is bundled on the OpenClaw side and requires version 2026.4.22 or newer. -- evidence: [README.md#L159-L159](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L159-L159), [README.md#L152-L153](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L152-L153), [README.md#L17-L28](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L17-L28) (`clm_1b39b28e54f0344981ba85b66ddae5196177e6fed2c9fd316f57c39ace214af2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] tokenjuice is distributed via npm (`npm install -g tokenjuice`), pnpm, yarn global, and a Homebrew tap (`brew tap vincentkoc/tap; brew install tokenjuice`). -- evidence: [README.md#L133-L133](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L133-L133), [README.md#L131-L131](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L131-L131), [README.md#L135-L137](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L135-L137), [README.md#L128-L129](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L128-L129) (`clm_6262ae9de4ca0a4a1de7af14adff2f8b3676b54349a88b1ffff12f6003abc0f4`)

## limitations (2 claim(s))

- [observation/documented] Several integrations (AdaL, Aether, Agent Layer, Agentlink) are documented as beta and guidance-only: they write instruction files telling agents to use `tokenjuice wrap`, but do not intercept or replace terminal command output. -- evidence: [docs/agent-layer-integration.md#L3-L3](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/agent-layer-integration.md#L3-L3), [docs/agentlink-integration.md#L33-L34](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/agentlink-integration.md#L33-L34), [docs/agentinit-integration.md#L3-L3](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/agentinit-integration.md#L3-L3), [docs/agentlink-integration.md#L3-L3](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/agentlink-integration.md#L3-L3), [docs/aether-integration.md#L32-L35](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/aether-integration.md#L32-L35), [docs/agent-layer-integration.md#L38-L40](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/agent-layer-integration.md#L38-L40), [docs/adal-integration.md#L31-L32](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/adal-integration.md#L31-L32), [docs/adal-integration.md#L3-L3](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/docs/adal-integration.md#L3-L3) (`clm_7d8678b137277b1f3874b1c7d5de25001dad27d72211fcff0b4c49c899459906`)
- [observation/documented] The project's stated status is a usable foundation for token reduction with diagnostics and a growing reducer set, now focused on deeper coverage and tuning. -- evidence: [README.md#L318-L318](https://github.com/vincentkoc/tokenjuice/blob/43a621ab06ef0198d728b93c93660ce5c381cb11/README.md#L318-L318) (`clm_6820141872b1c8bab63a6b6b95af564a3f20a45d0b1067f322c30de42590e81f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

