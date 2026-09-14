---
access: public
aliases: []
claim_ids:
- clm_0e8bfce9495b6677b00fc54c44b5cfc111fa9b06ad8d718c703e015ba4e77650
- clm_13c4763e188a75beb6a7d1ff4993baab7ef12093a1691476e620f9e1fc4200f9
- clm_289f7e217cb42d4b90ced9a03d4cc02e101e176f17a834eac8729ed875ebec79
- clm_2bcec3fd6c2c4d7cc3627e07188fd6d5d8b5e04f6262e02efbe134ac544436fd
- clm_32812d565baeb9f4522742a5f580623b19eb86f465ad1e78367d6d7cd8a398f0
- clm_3c620221a7fe310d14dcc0ec56ecad6ea03e245e0ec20d47f30c70ff745b2ab9
- clm_5035704f2989db7dbda9e93d5e91ca3f9a958918e1be301f46b0002cae5b557d
- clm_516b880a87f290c6a6159f98f743ffa4f4059fa8182bd1c3e99c7b41519e31a2
- clm_5a723f86f5f1e5f2972d932cb59d1edeb4a1be1a955d0f184ff2780961896446
- clm_6e9ac9b3c2cf95db8d9311f007cbbd06316e46223a8000db1749ccaa0eef7308
- clm_b8b632b0e976d05802f39be926e0caf791fae40cc95d5686207835980b5e271d
- clm_c8541eab83c8b010786fcaaa446ac33204fa161c982648ba1c90baa6a7b0d58f
- clm_ddc9ada0fdc8b6b0d57cfb5af467f512fac61f0ef4faa706de65a97ce526b45c
- clm_fca552743ffad0fa79d056472d10066a7a576605b5635e86f990c59802ee42d8
maturity: draft
page_id: pg_8f2d2cd0a86457abbeeb876dd247f069
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb3f68c4732e52deacd2194c84bee553
title: sanbuphy/learn-coding-agent/README.md @ ce8ca4a8e722
updated_at: '2026-09-14T04:19:35Z'
---

# sanbuphy/learn-coding-agent/README.md @ ce8ca4a8e722

<!-- rcw:begin owner=source:src_eb3f68c4732e52deacd2194c84bee553 block=evidence -->
- Documented design patterns include AsyncGenerator streaming through the query chain, a buildTool factory with safe defaults, compile-time feature-flag dead-code elimination via Bun, and AsyncLocalStorage for per-agent context isolation. [@claim:clm_0e8bfce9495b6677b00fc54c44b5cfc111fa9b06ad8d718c703e015ba4e77650]
- Each tool implements a documented lifecycle (validateInput, checkPermissions, call) plus capability predicates like isConcurrencySafe, isReadOnly, and isDestructive, and React/Ink renderers for tool use and results. [@claim:clm_13c4763e188a75beb6a7d1ff4993baab7ef12093a1691476e620f9e1fc4200f9]
- The repository is a learning/research project on CLI Agent architecture, compiled entirely from publicly available online references and discussions, focused on claude-code. [@claim:clm_289f7e217cb42d4b90ced9a03d4cc02e101e176f17a834eac8729ed875ebec79]
- The repository's own disclaimer prohibits commercial use of its content and limits it to research and educational purposes. [@claim:clm_2bcec3fd6c2c4d7cc3627e07188fd6d5d8b5e04f6262e02efbe134ac544436fd]
- Context management uses three compression strategies: autoCompact (summarize old messages via an API call when tokens exceed a threshold), snipCompact, and contextCollapse, the latter two behind feature flags. [@claim:clm_32812d565baeb9f4522742a5f580623b19eb86f465ad1e78367d6d7cd8a398f0]
- The documentation frames Claude Code as a minimal agent loop (call API, check stop_reason for tool_use, execute tools, append results) wrapped by a production harness adding permissions, streaming, concurrency, compaction, sub-agents, persistence, and MCP. [@claim:clm_3c620221a7fe310d14dcc0ec56ecad6ea03e245e0ec20d47f30c70ff745b2ab9]
- The entry layer routes interactive use through a REPL and headless/SDK use through QueryEngine, whose submitMessage returns an AsyncGenerator of SDKMessages streamed to the consumer. [@claim:clm_5035704f2989db7dbda9e93d5e91ca3f9a958918e1be301f46b0002cae5b557d]
- The documented permission flow orders validateInput, user-defined PreToolUse hooks, always-allow/deny/ask rules from settings or CLI args, an interactive Allow Once/Always/Deny prompt, then tool-specific checkPermissions logic such as path sandboxing. [@claim:clm_516b880a87f290c6a6159f98f743ffa4f4059fa8182bd1c3e99c7b41519e31a2]
- Documentation reports roughly 1,884 TS/TSX files, ~512,664 lines, ~40+ built-in tools, ~80+ slash commands, and a Bun runtime compiled to a Node.js >= 18 bundle. [@claim:clm_5a723f86f5f1e5f2972d932cb59d1edeb4a1be1a955d0f184ff2780961896446]
- The documented dependency footprint is about 192 node_modules packages, with the runtime built on Bun and compiled to a Node.js >= 18 bundle. [@claim:clm_6e9ac9b3c2cf95db8d9311f007cbbd06316e46223a8000db1749ccaa0eef7308]
- Sub-agents can spawn in four modes: default in-process with shared conversation, fork as a child process with fresh messages, worktree isolation, or remote via a bridge; agents communicate via SendMessageTool and a shared task board. [@claim:clm_b8b632b0e976d05802f39be926e0caf791fae40cc95d5686207835980b5e271d]
- The documented source layout includes main.tsx (REPL bootstrap), QueryEngine.ts (headless/SDK lifecycle), query.ts (main agent loop, largest file), Tool.ts, tools.ts, commands.ts, and a bridge/ directory for Claude Desktop/remote sessions. [@claim:clm_c8541eab83c8b010786fcaaa446ac33204fa161c982648ba1c90baa6a7b0d58f]
- Sessions persist as append-only JSONL under ~/.claude/projects/<hash>/sessions/, with resume options --continue, --resume <id>, and --fork-session; user messages are written blocking for crash recovery while assistant messages use a fire-and-forget queue. [@claim:clm_ddc9ada0fdc8b6b0d57cfb5af467f512fac61f0ef4faa706de65a97ce526b45c]
- The analyzed target is Claude Code v2.1.88; reports cover telemetry, codenames, undercover mode, remote control, and a future roadmap. [@claim:clm_fca552743ffad0fa79d056472d10066a7a576605b5635e86f990c59802ee42d8]
<!-- rcw:end owner=source:src_eb3f68c4732e52deacd2194c84bee553 block=evidence -->

## Researcher notes

