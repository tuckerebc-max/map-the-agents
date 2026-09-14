---
access: public
aliases: []
claim_ids:
- clm_01af36b892d1797872911d773e5ba85d9fa61e41494b21d224e51f3322be7088
- clm_0385d37866a63894f262dca3a002077ddb37e023ae5803fe01bd8c9bc847f5ab
- clm_0dc258fa4732a92229eba3bc9faa2d4ba08da316ae3d719c4f3030657196a529
- clm_17707422749be4f1f2051cd4ff5d261b46a5237d84496d4ca284af084a492e14
- clm_19f58047b4b99221f073f6d7dc26569123c7ba80507fb7dfb645ed33cf625183
- clm_1f452482d459dd2daa950150229f9c172a02906230f3beb49f31ddcad4b06ae1
- clm_3e0adbd6ce51b05c6f2d4d1f6234706c1011a17c36a8530edefbd67001bdb400
- clm_4b31bb09421f7fd4a18d467167ae822772ff4a3546a6a76301388ffa285661b1
- clm_882610b9676cf4753adab4f2c626c4225531e12cc5205089b5e0efb0d26b6048
- clm_8a5ded1a1c5b93ca80c76384e555bc464ac45aeebf72322a9a6605fb24a0f77e
- clm_8ade5080eaf55fd5d31ad6fa69138bf5b3a981a0fab3661047f7d99e6b6efcd6
- clm_8c7d255f2686db133ffc6430b5e57137d9ff644101c1a5efb4e457729e319c5c
- clm_946e9862b151210f9e8e21927e398d7321c285fe58037da8ce21403c3ad7eb2e
- clm_97ee62fef9916269e668e2a36f42572e7a030d34e3e231b5138b45c402cc8c28
- clm_a133509c1534db3799addcdf629d5139f7dd41f5ada37c9dd1cb8038e7e4c7f6
- clm_a37ac9b968663d997b15d6d4b41befb623754fd2f6ad7a1d146a64c157e241d8
- clm_e3923c2064cf33c4bb6802dd198b485082c3ef9c22f63b33bb819cb503afe6d1
- clm_f5c2440557548e283a75276e3dceb87733471b3fa63efe430c3e7da4856609a7
- clm_f675a67985250349fafd70ccc92c0370485350ded68446fc7c749e17a1dcc20b
maturity: draft
page_id: pg_9d9a92c604ba54b8aeb3bab9f6eef81a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_57e5fe2c807c5815812977626e431470
title: 1jehuang/jcode/README.md @ 37159430c3d0
updated_at: '2026-09-14T01:58:38Z'
---

# 1jehuang/jcode/README.md @ 37159430c3d0

<!-- rcw:begin owner=source:src_57e5fe2c807c5815812977626e431470 block=evidence -->
- The author wrote a separate Rust mermaid rendering library (mermaid-rs-renderer) with no browser or TypeScript dependency, claimed to render diagrams 1800x faster. [@claim:clm_01af36b892d1797872911d773e5ba85d9fa61e41494b21d224e51f3322be7088]
- Updates run via /update in the TUI or `jcode update`; dev builds compare the running binary's Git commit against the release tag and stop rather than risk a downgrade when ancestry cannot be verified. [@claim:clm_0385d37866a63894f262dca3a002077ddb37e023ae5803fe01bd8c9bc847f5ab]
- jcode currently supports only stdio (command-based) MCP servers; HTTP/SSE entries are recognized and skipped with a log line. [@claim:clm_0dc258fa4732a92229eba3bc9faa2d4ba08da316ae3d719c4f3030657196a529]
- User input is interleaved with the working agent as soon as it can be sent without breaking the KV cache; shift-enter instead queues the message until the agent finishes its turn. [@claim:clm_17707422749be4f1f2051cd4ff5d261b46a5237d84496d4ca284af084a492e14]
- The README reports self-measured benchmarks: jcode at 14.0 ms time-to-first-frame and 48.7 ms time-to-first-input versus slower figures for Codex CLI, Claude Code, OpenCode, Cursor Agent, and others, across 10 interactive PTY launches on one Linux machine. [@claim:clm_19f58047b4b99221f073f6d7dc26569123c7ba80507fb7dfb645ed33cf625183]
- MCP servers are configured in ~/.jcode/mcp.json (global) and .jcode/mcp.json (project-local); Claude Code config files (~/.claude.json, .mcp.json, .claude/mcp.json) are read live, and a one-time import from ~/.codex/config.toml is performed. [@claim:clm_1f452482d459dd2daa950150229f9c172a02906230f3beb49f31ddcad4b06ae1]
- Multiple agents spawned in the same repo are managed by a server: when one agent edits a file another has read, the server notifies the reader, which can ignore it or check the diff; agents can DM, broadcast, or message repo-scoped peers. [@claim:clm_3e0adbd6ce51b05c6f2d4d1f6234706c1011a17c36a8530edefbd67001bdb400]
- Smooth partial-line scrolling is not possible with jcode's custom scrollback in normal terminals due to a terminal-level limitation; the author's separate Handterm terminal with a native scroll API is a work in progress addressing this. [@claim:clm_4b31bb09421f7fd4a18d467167ae822772ff4a3546a6a76301388ffa285661b1]
- Besides passive background recall, jcode provides explicit memory tools for active search/store, plus session search performing traditional RAG over previous sessions. [@claim:clm_882610b9676cf4753adab4f2c626c4225531e12cc5205089b5e0efb0d26b6048]
- jcode offers built-in login flows via `jcode login --provider <id>` for providers including claude, openai, gemini, copilot, azure, fireworks, novita, minimax, lmstudio, ollama, and custom OpenAI-compatible endpoints. [@claim:clm_8a5ded1a1c5b93ca80c76384e555bc464ac45aeebf72322a9a6605fb24a0f77e]
- Each conversation turn is embedded as a semantic vector and queried against a memory graph via cosine similarity; hits are injected into the conversation, optionally after verification by a memory sideagent. [@claim:clm_8ade5080eaf55fd5d31ad6fa69138bf5b3a981a0fab3661047f7d99e6b6efcd6]
- Memories are extracted by a memory sideagent at triggers such as semantic drift, a K-turn interval, or session end, and added to the memory graph. [@claim:clm_8c7d255f2686db133ffc6430b5e57137d9ff644101c1a5efb4e457729e319c5c]
- Skills are not all loaded at startup; embedding hits on the conversation inject relevant skills automatically, and skills can also be activated manually via a skill tool or slash commands. [@claim:clm_946e9862b151210f9e8e21927e398d7321c285fe58037da8ce21403c3ad7eb2e]
- A memory-scaling comparison reports ~9.9-10.4 MB extra PSS per added jcode session versus larger figures for competing tools, with tested versions listed (e.g. jcode v0.9.1888-dev, codex-cli 0.120.0, Claude Code 2.1.86). [@claim:clm_97ee62fef9916269e668e2a36f42572e7a030d34e3e231b5138b45c402cc8c28]
- Agents have a swarm tool to autonomously spawn teammates for parallel work, turning the main agent into a coordinator; groups, messaging channels, and completion statuses are managed automatically, headed or headless. [@claim:clm_a133509c1534db3799addcdf629d5139f7dd41f5ada37c9dd1cb8038e7e4c7f6]
- An 'agent grep' tool augments grep output with file structure information (function lists, offsets) and adaptively truncates results based on what the agent has already seen to save context. [@claim:clm_a37ac9b968663d997b15d6d4b41befb623754fd2f6ad7a1d146a64c157e241d8]
- Headless OAuth is supported via --no-browser (printing auth URL/QR for manual paste), and a two-step --print-auth-url / --callback-url or --auth-code pattern exists for openai, gemini, claude, and antigravity. [@claim:clm_e3923c2064cf33c4bb6802dd198b485082c3ef9c22f63b33bb819cb503afe6d1]
- The side panel can display files updated in real time, receive agent-written content, act as a diff viewer, and render mermaid diagrams inline in both panel and chat. [@claim:clm_f5c2440557548e283a75276e3dceb87733471b3fa63efe430c3e7da4856609a7]
- An ambient mode periodically consolidates memories, reorganizing them and checking for staleness and conflicts. [@claim:clm_f675a67985250349fafd70ccc92c0370485350ded68446fc7c749e17a1dcc20b]
<!-- rcw:end owner=source:src_57e5fe2c807c5815812977626e431470 block=evidence -->

## Researcher notes

