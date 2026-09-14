# pawanosman/opencursor -- full detail

[Back to orientation](opencursor.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pawanosman/opencursor/e94886325f765dc4f98f49b20e3b44af05a2f3d1/4d702a4dae4114d6.json](../../../wiki/dossiers/pawanosman/opencursor/e94886325f765dc4f98f49b20e3b44af05a2f3d1/4d702a4dae4114d6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The agent ships a suite of 25 tools including read/write/edit, shell, grep/glob, semantic search, web search/fetch, notebooks, todos, subagents, and MCP. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54) (`clm_5c535319a5999f7395dc6d4a6f638c05ce614dd5e58cc80d85e2ffca75a5137a`)
- [observation/documented] Local AI support includes built-in llama.cpp management (spawning llama-server with control over context size, GPU layers, flash attention, etc.) and zero-config Ollama integration. -- evidence: [README.md#L23-L26](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L23-L26) (`clm_54fc169ee2e371772e284ade7e9ac5bd5f9ef57b1be69a80d7eb267128291f1a`)
- [observation/documented] Semantic codebase search uses an on-device ONNX MiniLM embedding model, with an option to point at any OpenAI-compatible /embeddings endpoint instead. -- evidence: [README.md#L32-L32](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L32-L32), [README.md#L23-L26](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L23-L26) (`clm_c925998b6f15efe5ad7b675f697a318f7f62a86746b5d1c771a0b5b06e7bab57`)

## design-choices (2 claim(s))

- [observation/documented] Edits get per-hunk Keep/Undo CodeLenses for inline review, and the README states this works without requiring git. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54) (`clm_b3c684dd546ea77944b3b851c385593f71a7094889d3be76f89f62c2d86242ef`)
- [observation/documented] Shell commands run in their own child shell and kill child processes on termination, and denied commands are checked per sub-command to prevent chaining-based bypasses. -- evidence: [CHANGELOG.md#L111-L119](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L111-L119) (`clm_ce47e5c2fedfcb09ff4c69ca7391b07f168ee9d1a2b43cef400c6978e78aa6d6`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: build from source with pnpm install and pnpm run compile (or watch), press F5 for the Extension Development Host, and package with pnpm run vsix; issues and PRs are welcome. -- evidence: [README.md#L80-L80](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L80-L80), [README.md#L76-L76](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L76-L76), [README.md#L69-L74](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L69-L74) (`clm_be5f88ffd89336c03248baad6878131b5f40a2c4c9afe80d58776b0cff435d16`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] OpenCursor is a VS Code extension installable from the Marketplace or as a .vsix, providing a multi-tab sidebar chat with @-mentions of files, folders, docs, commits, diffs, terminals, and rules. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54), [README.md#L58-L63](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L58-L63) (`clm_b7b1984a225d7099c9afc38c6091bf9446b7c0863dc8f33d897d3bf9773502e8`)
- [observation/documented] Providers include OAuth sign-in for Claude Code, OpenAI Codex, and Google Antigravity accounts, API-key presets (OpenAI, Anthropic, Gemini, OpenRouter), and custom OpenAI-compatible or Anthropic-style endpoints usable simultaneously. -- evidence: [README.md#L38-L41](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L38-L41) (`clm_c04769895b45c6190bd889342816bb12694e1a568c632f87f98d2b38296393f3`)

## memory-state (2 claim(s))

- [observation/documented] The semantic index persists across VS Code restarts, re-indexes incrementally on changed files, and auto-indexes new/modified files via a workspace file watcher; indexing can be fully disabled in settings. -- evidence: [CHANGELOG.md#L257-L262](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L257-L262) (`clm_ef6bc5e03dbaf197aa74ba4e3ec924b5254b884add5de1b693bd6e815e26b825`)
- [observation/documented] Context management includes auto-compaction with a verbatim tail, lossless persisted chat history for export, and latest-wins deduplication of older tool results for the same target. -- evidence: [CHANGELOG.md#L164-L170](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L164-L170) (`clm_8a09a8bd0ed738df9e74ee1516d0cfc4a8cd5626da635d01bc633af9d8a76def`)

## orchestration (2 claim(s))

- [observation/documented] Project mode lets the agent act as a project lead delegating to a team of subagents (TeamDef presets), with subagents running on isolated history so the parent only receives the final Task result. -- evidence: [CHANGELOG.md#L266-L269](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L266-L269), [CHANGELOG.md#L81-L86](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L81-L86) (`clm_bfc36574fabb6a845417e597142d0f07c6be8a6cf3ba6020812f19bfd4ec19b0`)
- [observation/documented] The changelog documents per-tool hard timeouts, abort-signal support so Stop cancels mid-work, and configurable per-tool timeout seconds in Settings. -- evidence: [CHANGELOG.md#L233-L235](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L233-L235), [CHANGELOG.md#L214-L219](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L214-L219) (`clm_18a92481fcd303acc77449a11fedf537f35e4e4dd2b223dc62ea76b7814d3f74`)

## tools-permissions (1 claim(s))

- [observation/documented] A per-action approval policy supports allow/ask/review/deny with risk heuristics (e.g. rm -rf, sudo, .env, secrets) and wildcard allow/deny lists. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54) (`clm_26a0b7a181ead46788ab7c62b8b61b64d2c4609d2a3134aebce2fef5e884f38c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Heavy native runtime dependencies such as ONNX runtime and image processing are downloaded on first activation with integrity checks rather than shipped in the VSIX. -- evidence: [README.md#L65-L65](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L65-L65) (`clm_6e95d34490d42431b652fc70f354c78150ae10e5b832468d95fdfefeb1bd9aeb`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

