# sanbuphy/learn-coding-agent -- full detail

[Back to orientation](learn-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sanbuphy/learn-coding-agent/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/e96abc602fa9c456.json](../../../wiki/dossiers/sanbuphy/learn-coding-agent/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/e96abc602fa9c456.json)

## specifications (2 claim(s))

- [observation/documented] The analyzed target is Claude Code v2.1.88; reports cover telemetry, codenames, undercover mode, remote control, and a future roadmap. -- evidence: [README.md#L59-L65](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L59-L65), [README.md#L24-L24](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L24-L24) (`clm_fca552743ffad0fa79d056472d10066a7a576605b5635e86f990c59802ee42d8`)
- [observation/documented] Documentation reports roughly 1,884 TS/TSX files, ~512,664 lines, ~40+ built-in tools, ~80+ slash commands, and a Bun runtime compiled to a Node.js >= 18 bundle. -- evidence: [README.md#L83-L91](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L83-L91) (`clm_5a723f86f5f1e5f2972d932cb59d1edeb4a1be1a955d0f184ff2780961896446`)

## components (1 claim(s))

- [observation/documented] The documented source layout includes main.tsx (REPL bootstrap), QueryEngine.ts (headless/SDK lifecycle), query.ts (main agent loop, largest file), Tool.ts, tools.ts, commands.ts, and a bridge/ directory for Claude Desktop/remote sessions. -- evidence: [README.md#L121-L248](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L121-L248) (`clm_c8541eab83c8b010786fcaaa446ac33204fa161c982648ba1c90baa6a7b0d58f`)

## design-choices (2 claim(s))

- [observation/documented] Documented design patterns include AsyncGenerator streaming through the query chain, a buildTool factory with safe defaults, compile-time feature-flag dead-code elimination via Bun, and AsyncLocalStorage for per-agent context isolation. -- evidence: [README.md#L779-L791](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L779-L791) (`clm_0e8bfce9495b6677b00fc54c44b5cfc111fa9b06ad8d718c703e015ba4e77650`)
- [observation/documented] The documentation frames Claude Code as a minimal agent loop (call API, check stop_reason for tool_use, execute tools, append results) wrapped by a production harness adding permissions, streaming, concurrency, compaction, sub-agents, persistence, and MCP. -- evidence: [README.md#L112-L115](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L112-L115), [README.md#L101-L109](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L101-L109) (`clm_3c620221a7fe310d14dcc0ec56ecad6ea03e245e0ec20d47f30c70ff745b2ab9`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The entry layer routes interactive use through a REPL and headless/SDK use through QueryEngine, whose submitMessage returns an AsyncGenerator of SDKMessages streamed to the consumer. -- evidence: [README.md#L254-L314](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L254-L314) (`clm_5035704f2989db7dbda9e93d5e91ca3f9a958918e1be301f46b0002cae5b557d`)
- [observation/documented] Each tool implements a documented lifecycle (validateInput, checkPermissions, call) plus capability predicates like isConcurrencySafe, isReadOnly, and isDestructive, and React/Ink renderers for tool use and results. -- evidence: [README.md#L375-L375](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L375-L375), [README.md#L377-L402](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L377-L402) (`clm_13c4763e188a75beb6a7d1ff4993baab7ef12093a1691476e620f9e1fc4200f9`)

## memory-state (2 claim(s))

- [observation/documented] Sessions persist as append-only JSONL under ~/.claude/projects/<hash>/sessions/, with resume options --continue, --resume <id>, and --fork-session; user messages are written blocking for crash recovery while assistant messages use a fire-and-forget queue. -- evidence: [README.md#L640-L645](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L640-L645), [README.md#L626-L631](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L626-L631), [README.md#L633-L638](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L633-L638) (`clm_ddc9ada0fdc8b6b0d57cfb5af467f512fac61f0ef4faa706de65a97ce526b45c`)
- [observation/documented] Context management uses three compression strategies: autoCompact (summarize old messages via an API call when tokens exceed a threshold), snipCompact, and contextCollapse, the latter two behind feature flags. -- evidence: [README.md#L542-L548](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L542-L548) (`clm_32812d565baeb9f4522742a5f580623b19eb86f465ad1e78367d6d7cd8a398f0`)

## orchestration (1 claim(s))

- [observation/documented] Sub-agents can spawn in four modes: default in-process with shared conversation, fork as a child process with fresh messages, worktree isolation, or remote via a bridge; agents communicate via SendMessageTool and a shared task board. -- evidence: [README.md#L494-L498](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L494-L498), [README.md#L500-L503](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L500-L503) (`clm_b8b632b0e976d05802f39be926e0caf791fae40cc95d5686207835980b5e271d`)

## tools-permissions (1 claim(s))

- [observation/documented] The documented permission flow orders validateInput, user-defined PreToolUse hooks, always-allow/deny/ask rules from settings or CLI args, an interactive Allow Once/Always/Deny prompt, then tool-specific checkPermissions logic such as path sandboxing. -- evidence: [README.md#L438-L474](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L438-L474) (`clm_516b880a87f290c6a6159f98f743ffa4f4059fa8182bd1c3e99c7b41519e31a2`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The documented dependency footprint is about 192 node_modules packages, with the runtime built on Bun and compiled to a Node.js >= 18 bundle. -- evidence: [README.md#L83-L91](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L83-L91) (`clm_6e9ac9b3c2cf95db8d9311f007cbbd06316e46223a8000db1749ccaa0eef7308`)

## limitations (2 claim(s))

- [observation/documented] The telemetry report states first-party event logging cannot be disabled by direct Anthropic API users, with no user-facing setting to turn it off, and that OTEL_LOG_TOOL_DETAILS=1 enables full tool input logging. -- evidence: [docs/en/01-telemetry-and-privacy.md#L78-L78](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/docs/en/01-telemetry-and-privacy.md#L78-L78), [docs/en/01-telemetry-and-privacy.md#L104-L104](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/docs/en/01-telemetry-and-privacy.md#L104-L104), [docs/en/01-telemetry-and-privacy.md#L90-L90](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/docs/en/01-telemetry-and-privacy.md#L90-L90) (`clm_afa90ea1e619ea00dfc7f85d72dedeeca0d260a1ea753a50bea910bab7f17397`)
- [observation/documented] The repository's own disclaimer prohibits commercial use of its content and limits it to research and educational purposes. -- evidence: [README.md#L71-L73](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L71-L73), [README.md#L5-L5](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L5-L5) (`clm_2bcec3fd6c2c4d7cc3627e07188fd6d5d8b5e04f6262e02efbe134ac544436fd`)

## relevance (1 claim(s))

- [observation/documented] The repository is a learning/research project on CLI Agent architecture, compiled entirely from publicly available online references and discussions, focused on claude-code. -- evidence: [README.md#L3-L3](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L3-L3) (`clm_289f7e217cb42d4b90ced9a03d4cc02e101e176f17a834eac8729ed875ebec79`)

