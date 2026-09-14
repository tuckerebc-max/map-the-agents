# 1jehuang/jcode -- full detail

[Back to orientation](jcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/1jehuang/jcode/37159430c3d02545fd7c10b0bd13e754b49f871b/b7be00436905e014.json](../../../wiki/dossiers/1jehuang/jcode/37159430c3d02545fd7c10b0bd13e754b49f871b/b7be00436905e014.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] User input is interleaved with the working agent as soon as it can be sent without breaking the KV cache; shift-enter instead queues the message until the agent finishes its turn. -- evidence: [README.md#L672-L672](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L672-L672) (`clm_17707422749be4f1f2051cd4ff5d261b46a5237d84496d4ca284af084a492e14`)
- [observation/documented] An 'agent grep' tool augments grep output with file structure information (function lists, offsets) and adaptively truncates results based on what the agent has already seen to save context. -- evidence: [README.md#L670-L670](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L670-L670) (`clm_a37ac9b968663d997b15d6d4b41befb623754fd2f6ad7a1d146a64c157e241d8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are not all loaded at startup; embedding hits on the conversation inject relevant skills automatically, and skills can also be activated manually via a skill tool or slash commands. -- evidence: [README.md#L680-L680](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L680-L680) (`clm_946e9862b151210f9e8e21927e398d7321c285fe58037da8ce21403c3ad7eb2e`)

## interfaces (5 claim(s))

- [observation/documented] jcode offers built-in login flows via `jcode login --provider <id>` for providers including claude, openai, gemini, copilot, azure, fireworks, novita, minimax, lmstudio, ollama, and custom OpenAI-compatible endpoints. -- evidence: [README.md#L352-L364](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L352-L364) (`clm_8a5ded1a1c5b93ca80c76384e555bc464ac45aeebf72322a9a6605fb24a0f77e`)
- [observation/documented] MCP servers are configured in ~/.jcode/mcp.json (global) and .jcode/mcp.json (project-local); Claude Code config files (~/.claude.json, .mcp.json, .claude/mcp.json) are read live, and a one-time import from ~/.codex/config.toml is performed. -- evidence: [README.md#L573-L575](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L573-L575), [README.md#L568-L569](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L568-L569), [README.md#L577-L584](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L577-L584) (`clm_1f452482d459dd2daa950150229f9c172a02906230f3beb49f31ddcad4b06ae1`)
- [observation/documented] Headless OAuth is supported via --no-browser (printing auth URL/QR for manual paste), and a two-step --print-auth-url / --callback-url or --auth-code pattern exists for openai, gemini, claude, and antigravity. -- evidence: [README.md#L626-L627](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L626-L627), [README.md#L618-L620](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L618-L620), [README.md#L611-L611](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L611-L611), [README.md#L609-L609](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L609-L609) (`clm_e3923c2064cf33c4bb6802dd198b485082c3ef9c22f63b33bb819cb503afe6d1`)
- [observation/documented] The side panel can display files updated in real time, receive agent-written content, act as a diff viewer, and render mermaid diagrams inline in both panel and chat. -- evidence: [README.md#L311-L312](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L311-L312) (`clm_f5c2440557548e283a75276e3dceb87733471b3fa63efe430c3e7da4856609a7`)
- [observation/documented] Updates run via /update in the TUI or `jcode update`; dev builds compare the running binary's Git commit against the release tag and stop rather than risk a downgrade when ancestry cannot be verified. -- evidence: [README.md#L50-L52](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L50-L52), [README.md#L54-L59](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L54-L59) (`clm_0385d37866a63894f262dca3a002077ddb37e023ae5803fe01bd8c9bc847f5ab`)

## memory-state (4 claim(s))

- [observation/documented] Each conversation turn is embedded as a semantic vector and queried against a memory graph via cosine similarity; hits are injected into the conversation, optionally after verification by a memory sideagent. -- evidence: [README.md#L287-L289](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L287-L289) (`clm_8ade5080eaf55fd5d31ad6fa69138bf5b3a981a0fab3661047f7d99e6b6efcd6`)
- [observation/documented] Memories are extracted by a memory sideagent at triggers such as semantic drift, a K-turn interval, or session end, and added to the memory graph. -- evidence: [README.md#L287-L289](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L287-L289) (`clm_8c7d255f2686db133ffc6430b5e57137d9ff644101c1a5efb4e457729e319c5c`)
- [observation/documented] Besides passive background recall, jcode provides explicit memory tools for active search/store, plus session search performing traditional RAG over previous sessions. -- evidence: [README.md#L291-L291](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L291-L291) (`clm_882610b9676cf4753adab4f2c626c4225531e12cc5205089b5e0efb0d26b6048`)
- [observation/documented] An ambient mode periodically consolidates memories, reorganizing them and checking for staleness and conflicts. -- evidence: [README.md#L293-L293](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L293-L293) (`clm_f675a67985250349fafd70ccc92c0370485350ded68446fc7c749e17a1dcc20b`)

## orchestration (2 claim(s))

- [observation/documented] Multiple agents spawned in the same repo are managed by a server: when one agent edits a file another has read, the server notifies the reader, which can ignore it or check the diff; agents can DM, broadcast, or message repo-scoped peers. -- evidence: [README.md#L330-L330](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L330-L330) (`clm_3e0adbd6ce51b05c6f2d4d1f6234706c1011a17c36a8530edefbd67001bdb400`)
- [observation/documented] Agents have a swarm tool to autonomously spawn teammates for parallel work, turning the main agent into a coordinator; groups, messaging channels, and completion statuses are managed automatically, headed or headless. -- evidence: [README.md#L342-L342](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L342-L342) (`clm_a133509c1534db3799addcdf629d5139f7dd41f5ada37c9dd1cb8038e7e4c7f6`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The README reports self-measured benchmarks: jcode at 14.0 ms time-to-first-frame and 48.7 ms time-to-first-input versus slower figures for Codex CLI, Claude Code, OpenCode, Cursor Agent, and others, across 10 interactive PTY launches on one Linux machine. -- evidence: [README.md#L229-L238](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L229-L238), [README.md#L223-L223](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L223-L223), [README.md#L210-L219](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L210-L219) (`clm_19f58047b4b99221f073f6d7dc26569123c7ba80507fb7dfb645ed33cf625183`)
- [observation/documented] A memory-scaling comparison reports ~9.9-10.4 MB extra PSS per added jcode session versus larger figures for competing tools, with tested versions listed (e.g. jcode v0.9.1888-dev, codex-cli 0.120.0, Claude Code 2.1.86). -- evidence: [README.md#L248-L258](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L248-L258), [README.md#L263-L270](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L263-L270) (`clm_97ee62fef9916269e668e2a36f42572e7a030d34e3e231b5138b45c402cc8c28`)

## dependencies (1 claim(s))

- [observation/documented] The author wrote a separate Rust mermaid rendering library (mermaid-rs-renderer) with no browser or TypeScript dependency, claimed to render diagrams 1800x faster. -- evidence: [README.md#L314-L314](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L314-L314) (`clm_01af36b892d1797872911d773e5ba85d9fa61e41494b21d224e51f3322be7088`)

## limitations (2 claim(s))

- [observation/documented] jcode currently supports only stdio (command-based) MCP servers; HTTP/SSE entries are recognized and skipped with a log line. -- evidence: [README.md#L586-L586](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L586-L586) (`clm_0dc258fa4732a92229eba3bc9faa2d4ba08da316ae3d719c4f3030657196a529`)
- [observation/documented] Smooth partial-line scrolling is not possible with jcode's custom scrollback in normal terminals due to a terminal-level limitation; the author's separate Handterm terminal with a native scroll API is a work in progress addressing this. -- evidence: [README.md#L320-L320](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L320-L320) (`clm_4b31bb09421f7fd4a18d467167ae822772ff4a3546a6a76301388ffa285661b1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

