---
access: public
aliases: []
claim_ids:
- clm_04d08ece3e59789e2123736bd0be72b93e3aa34ff53d91a6b01a689cfe1e4ad7
- clm_08645cf940261c73a8ca3456e070460e7304f72a72951d88369390f182ee166f
- clm_2b6ad02d2676386c1605fc8e4caefab386d742f10aa740c46abf7fe901633200
- clm_2ccf0cc1810d8b21b293ba31acfef57dc1cd325ffc4097959cfd7e39aed03dca
- clm_417cdff9cb1fb7401495ead4fb2d106bb82922ce1beaf903f85af3be8fbe5b6d
- clm_691a52f2580adc08639655701c876431c5dfc948220c486c9175eb04fba15791
- clm_b502023c83300e2516d2a13d7084bab111158fc3a64c1a2a1e6ac27308de8618
- clm_c12ebc788c4fab2c9191876d5b65f2fdd3723ad1837703a063e03cbc4c81d403
maturity: draft
page_id: pg_65a0ca1c853c51409ed8546bc1f1734d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b91a8fc98a015822b63b5babccdb5ccc
title: sudoprivacy/sudocode/docs/acp.md @ a67bb90f5c4b
updated_at: '2026-09-14T04:40:28Z'
---

# sudoprivacy/sudocode/docs/acp.md @ a67bb90f5c4b

<!-- rcw:begin owner=source:src_b91a8fc98a015822b63b5babccdb5ccc block=evidence -->
- scode speaks the Agent Communication Protocol natively over two transports sharing one handler chain: `scode acp` over stdio and `scode acp serve --port N` over WebSocket. [@claim:clm_04d08ece3e59789e2123736bd0be72b93e3aa34ff53d91a6b01a689cfe1e4ad7]
- Sessions persist as JSONL under `<cwd>/.scode/sessions/<workspace-fingerprint>/`; session/load restores transcript, model, compaction state and fork lineage, but not permission-mode overrides, background commands, or MCP servers not passed in the request. [@claim:clm_08645cf940261c73a8ca3456e070460e7304f72a72951d88369390f182ee166f]
- Automatic compaction trims oversized tool text (over 8,192 code points) to a head/tail with marker before running a checkpoint pipeline; successful replacement archives the original transcript as `<transcript>.before-compact-<timestamp>`. [@claim:clm_2b6ad02d2676386c1605fc8e4caefab386d742f10aa740c46abf7fe901633200]
- The WebSocket server exposes JSON-RPC at ws://localhost:8080/ws plus an embedded interactive Web UI at http://localhost:8080/; both transports share streaming, tool use, elicitation and permission prompting. [@claim:clm_2ccf0cc1810d8b21b293ba31acfef57dc1cd325ffc4097959cfd7e39aed03dca]
- A session/prompt starting with `/` runs as a slash command (e.g. /help, /status, /cost, /model, /compact, /diff, /doctor), and the agent advertises the command table via a session/update notification after session/new or session/load. [@claim:clm_417cdff9cb1fb7401495ead4fb2d106bb82922ce1beaf903f85af3be8fbe5b6d]
- Per-session memory is controlled via `_meta.sudocode.memory`; 'disabled' means the session neither reads nor writes the persistent memory directory, and disabling never deletes existing entries. [@claim:clm_691a52f2580adc08639655701c876431c5dfc948220c486c9175eb04fba15791]
- Forking via `session/new` with `_meta.sudocode.forkFrom` copies the source transcript into a new first-class session under the new cwd; the source is read, never modified, and the initialize response advertises sessionFork for feature detection. [@claim:clm_b502023c83300e2516d2a13d7084bab111158fc3a64c1a2a1e6ac27308de8618]
- ACP sessions accept `_meta.sudocode.systemPrompt` (replaces built-in static system-prompt blocks) and `appendSystemPrompt` (appended after them); non-string or empty values are rejected with invalid_params (-32602). [@claim:clm_c12ebc788c4fab2c9191876d5b65f2fdd3723ad1837703a063e03cbc4c81d403]
<!-- rcw:end owner=source:src_b91a8fc98a015822b63b5babccdb5ccc block=evidence -->

## Researcher notes

