---
access: public
aliases: []
claim_ids:
- clm_09ab4cfcdae81b1ed767c2a3e3c2cc7d3a879a94748cda7c9e45ce9f299020f5
- clm_15ae26b832dded8f5abd24fb4ee2c7b062e80cb0d28d2721352cc165076ed2c2
- clm_17d251135130b3e5c741a1c668b4f49c9d629b534c35a798b1cb6e707e0e0be9
- clm_2652587a085c37a9090de740dbe375f2ea2a67a9f176a85f6b4eb395e7acb6b2
- clm_86b78ec86694be8834b2cfd7acd0c43942a0004ebda5145cc6a4ad1a3cca5e0f
- clm_86e8f2900261b629e153cd1dde98953fa87e3276d94a1f53b2e2d80915c0a5ee
- clm_8796e11e418c56d54480904700c96f54ff83e4ae1f8771d328fe3dccfdd2f116
- clm_9d7226fa038ffaf0ca2d42d9d1e96fb9bcc80a07bb8c3a41777027f768512ef1
- clm_b3e3ac1ef38641a9b20fd658575ff401581d28567cb057239d134a4aed3e6283
- clm_c3c004344870d75995fb61ee5a9f00dbdf81acd0c03bd6fafd805376e707e3c9
- clm_e8f9155826918265d0ad81b68611780ed6b6007bf7a3dbb963166ea15183ae55
- clm_e9bc32a4197cb5abb03dc6ceabda40e78400c0b34cae0b19d82576f9e81754cd
maturity: draft
page_id: pg_34314bbff34057af9028ce449dad2f31
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_22f56ca5b9c9557a873e173ad92b5905
title: andrefetch/postal/README.md @ 240622b0c2dc
updated_at: '2026-09-14T01:33:24Z'
---

# andrefetch/postal/README.md @ 240622b0c2dc

<!-- rcw:begin owner=source:src_22f56ca5b9c9557a873e173ad92b5905 block=evidence -->
- The main agent can delegate to five specialized sub-agents (codebase_investigator, code_reviewer, software_architect, test_writer, debugger), each running its own loop with a narrowed tool set and turn cap; sub-agent runs are never checkpointed. [@claim:clm_09ab4cfcdae81b1ed767c2a3e3c2cc7d3a879a94748cda7c9e45ce9f299020f5]
- The CLI offers single-shot mode via a prompt argument, --cwd to target another directory, --continue/--resume for sessions, and a sessions subcommand; the interactive mode is a full-screen TUI. [@claim:clm_15ae26b832dded8f5abd24fb4ee2c7b062e80cb0d28d2721352cc165076ed2c2]
- Context handling uses two loop-side mechanisms: pruning clears stale tool outputs to reclaim tokens, and compaction summarizes history into a continuation brief when the context window fills, instead of erroring out. [@claim:clm_17d251135130b3e5c741a1c668b4f49c9d629b534c35a798b1cb6e707e0e0be9]
- Repository development practice: contributions are welcomed in any size and prospective contributors are directed to CONTRIBUTING.md and the open issue tracker to get started. [@claim:clm_2652587a085c37a9090de740dbe375f2ea2a67a9f176a85f6b4eb395e7acb6b2]
- The TUI supports slash commands including /model, /approval, /thinking, /clear, /stats, /tools, /mcp, /sessions, /resume, /checkpoint, /rewind and /exit, with autocomplete as the user types. [@claim:clm_86b78ec86694be8834b2cfd7acd0c43942a0004ebda5145cc6a4ad1a3cca5e0f]
- Six approval policies govern mutating actions: on_request (default), auto_edit, auto, on_fail (currently identical to auto), never (read-only), and yolo; read-only tools never prompt. [@claim:clm_86e8f2900261b629e153cd1dde98953fa87e3276d94a1f53b2e2d80915c0a5ee]
- Two rules override any policy except yolo: dangerous commands (e.g. rm -rf /, mkfs, curl piped to bash) are rejected, and anything touching paths outside the working directory requires confirmation (or is rejected under never). [@claim:clm_8796e11e418c56d54480904700c96f54ff83e4ae1f8771d328fe3dccfdd2f116]
- Conversations are checkpointed to disk after every turn under ~/.config/postal/sessions/<id>/ as JSONL transcripts plus meta.json; /rewind restores a checkpoint's conversation but does not revert files already written to disk. [@claim:clm_9d7226fa038ffaf0ca2d42d9d1e96fb9bcc80a07bb8c3a41777027f768512ef1]
- The project is built on Python with Rich, Click, Pydantic, the OpenAI SDK, and MCP, and also uses Docker per its README badges; requirements.txt pins packages such as openai 2.45.0, pydantic 2.13.4, rich 15.0.0, and mcp 1.28.1. [@claim:clm_b3e3ac1ef38641a9b20fd658575ff401581d28567cb057239d134a4aed3e6283]
- Postal is an open-source AI coding agent that runs in the terminal, planning, editing, running, and reviewing code with any model available on OpenRouter. [@claim:clm_c3c004344870d75995fb61ee5a9f00dbdf81acd0c03bd6fafd805376e707e3c9]
- Built-in tools include file operations (read, write, edit, apply_patch, grep, glob, list_directories), bash, a plan todo-list tool, DuckDuckGo-backed web search, URL fetching, and cross-session key-value memory. [@claim:clm_e8f9155826918265d0ad81b68611780ed6b6007bf7a3dbb963166ea15183ae55]
- Resuming a session rebuilds the system prompt from current config and tool set rather than restoring it, so resumed sessions pick up later model, approval, or AGENTS.md changes. [@claim:clm_e9bc32a4197cb5abb03dc6ceabda40e78400c0b34cae0b19d82576f9e81754cd]
<!-- rcw:end owner=source:src_22f56ca5b9c9557a873e173ad92b5905 block=evidence -->

## Researcher notes

