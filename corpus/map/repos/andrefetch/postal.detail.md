# andrefetch/postal -- full detail

[Back to orientation](postal.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/andrefetch/postal/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/d2cc8dfe1c666ebc.json](../../../wiki/dossiers/andrefetch/postal/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/d2cc8dfe1c666ebc.json)

## specifications (1 claim(s))

- [observation/documented] Postal is an open-source AI coding agent that runs in the terminal, planning, editing, running, and reviewing code with any model available on OpenRouter. -- evidence: [README.md#L5-L8](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L5-L8) (`clm_c3c004344870d75995fb61ee5a9f00dbdf81acd0c03bd6fafd805376e707e3c9`)

## components (2 claim(s))

- [observation/documented] Built-in tools include file operations (read, write, edit, apply_patch, grep, glob, list_directories), bash, a plan todo-list tool, DuckDuckGo-backed web search, URL fetching, and cross-session key-value memory. -- evidence: [docs/tools.md#L27-L27](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L27-L27), [docs/tools.md#L38-L38](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L38-L38), [docs/tools.md#L23-L23](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L23-L23), [docs/tools.md#L9-L17](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L9-L17), [docs/tools.md#L31-L34](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L31-L34), [README.md#L86-L96](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L86-L96) (`clm_e8f9155826918265d0ad81b68611780ed6b6007bf7a3dbb963166ea15183ae55`)
- [observation/documented] The main agent can delegate to five specialized sub-agents (codebase_investigator, code_reviewer, software_architect, test_writer, debugger), each running its own loop with a narrowed tool set and turn cap; sub-agent runs are never checkpointed. -- evidence: [docs/tools.md#L44-L50](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L44-L50), [README.md#L86-L96](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L86-L96), [docs/tools.md#L42-L42](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L42-L42) (`clm_09ab4cfcdae81b1ed767c2a3e3c2cc7d3a879a94748cda7c9e45ce9f299020f5`)

## design-choices (1 claim(s))

- [observation/documented] Context handling uses two loop-side mechanisms: pruning clears stale tool outputs to reclaim tokens, and compaction summarizes history into a continuation brief when the context window fills, instead of erroring out. -- evidence: [README.md#L77-L82](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L77-L82), [docs/tools.md#L62-L62](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L62-L62), [docs/tools.md#L64-L65](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/tools.md#L64-L65) (`clm_17d251135130b3e5c741a1c668b4f49c9d629b534c35a798b1cb6e707e0e0be9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcomed in any size and prospective contributors are directed to CONTRIBUTING.md and the open issue tracker to get started. -- evidence: [README.md#L185-L185](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L185-L185) (`clm_2652587a085c37a9090de740dbe375f2ea2a67a9f176a85f6b4eb395e7acb6b2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI offers single-shot mode via a prompt argument, --cwd to target another directory, --continue/--resume for sessions, and a sessions subcommand; the interactive mode is a full-screen TUI. -- evidence: [README.md#L50-L56](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L50-L56), [README.md#L42-L46](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L42-L46), [README.md#L86-L96](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L86-L96) (`clm_15ae26b832dded8f5abd24fb4ee2c7b062e80cb0d28d2721352cc165076ed2c2`)
- [observation/documented] The TUI supports slash commands including /model, /approval, /thinking, /clear, /stats, /tools, /mcp, /sessions, /resume, /checkpoint, /rewind and /exit, with autocomplete as the user types. -- evidence: [README.md#L119-L119](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L119-L119), [README.md#L100-L117](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L100-L117) (`clm_86b78ec86694be8834b2cfd7acd0c43942a0004ebda5145cc6a4ad1a3cca5e0f`)

## memory-state (2 claim(s))

- [observation/documented] Conversations are checkpointed to disk after every turn under ~/.config/postal/sessions/<id>/ as JSONL transcripts plus meta.json; /rewind restores a checkpoint's conversation but does not revert files already written to disk. -- evidence: [README.md#L154-L154](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L154-L154), [README.md#L123-L123](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L123-L123), [README.md#L152-L152](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L152-L152) (`clm_9d7226fa038ffaf0ca2d42d9d1e96fb9bcc80a07bb8c3a41777027f768512ef1`)
- [observation/documented] Resuming a session rebuilds the system prompt from current config and tool set rather than restoring it, so resumed sessions pick up later model, approval, or AGENTS.md changes. -- evidence: [README.md#L133-L133](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L133-L133) (`clm_e9bc32a4197cb5abb03dc6ceabda40e78400c0b34cae0b19d82576f9e81754cd`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Six approval policies govern mutating actions: on_request (default), auto_edit, auto, on_fail (currently identical to auto), never (read-only), and yolo; read-only tools never prompt. -- evidence: [docs/approvals.md#L9-L16](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/approvals.md#L9-L16), [README.md#L158-L158](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L158-L158), [README.md#L160-L167](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L160-L167) (`clm_86e8f2900261b629e153cd1dde98953fa87e3276d94a1f53b2e2d80915c0a5ee`)
- [observation/documented] Two rules override any policy except yolo: dangerous commands (e.g. rm -rf /, mkfs, curl piped to bash) are rejected, and anything touching paths outside the working directory requires confirmation (or is rejected under never). -- evidence: [README.md#L169-L169](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L169-L169), [docs/approvals.md#L22-L23](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/docs/approvals.md#L22-L23), [README.md#L171-L172](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L171-L172) (`clm_8796e11e418c56d54480904700c96f54ff83e4ae1f8771d328fe3dccfdd2f116`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is built on Python with Rich, Click, Pydantic, the OpenAI SDK, and MCP, and also uses Docker per its README badges; requirements.txt pins packages such as openai 2.45.0, pydantic 2.13.4, rich 15.0.0, and mcp 1.28.1. -- evidence: [README.md#L20-L30](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/README.md#L20-L30), [requirements.txt#L1-L98](https://github.com/andrefetch/postal/blob/240622b0c2dcbfd1e3ba5e3d60d38193059881f5/requirements.txt#L1-L98) (`clm_b3e3ac1ef38641a9b20fd658575ff401581d28567cb057239d134a4aed3e6283`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

