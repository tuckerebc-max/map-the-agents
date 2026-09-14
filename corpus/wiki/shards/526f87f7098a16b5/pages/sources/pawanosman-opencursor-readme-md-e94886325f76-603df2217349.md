---
access: public
aliases: []
claim_ids:
- clm_26a0b7a181ead46788ab7c62b8b61b64d2c4609d2a3134aebce2fef5e884f38c
- clm_54fc169ee2e371772e284ade7e9ac5bd5f9ef57b1be69a80d7eb267128291f1a
- clm_5c535319a5999f7395dc6d4a6f638c05ce614dd5e58cc80d85e2ffca75a5137a
- clm_6e95d34490d42431b652fc70f354c78150ae10e5b832468d95fdfefeb1bd9aeb
- clm_b3c684dd546ea77944b3b851c385593f71a7094889d3be76f89f62c2d86242ef
- clm_b7b1984a225d7099c9afc38c6091bf9446b7c0863dc8f33d897d3bf9773502e8
- clm_be5f88ffd89336c03248baad6878131b5f40a2c4c9afe80d58776b0cff435d16
- clm_c04769895b45c6190bd889342816bb12694e1a568c632f87f98d2b38296393f3
- clm_c925998b6f15efe5ad7b675f697a318f7f62a86746b5d1c771a0b5b06e7bab57
maturity: draft
page_id: pg_2ad13a4dd9bc52e59666603df2217349
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a00f40e6ce875bf5abb76b6f64af9231
title: PawanOsman/OpenCursor/README.md @ e94886325f76
updated_at: '2026-09-14T02:30:07Z'
---

# PawanOsman/OpenCursor/README.md @ e94886325f76

<!-- rcw:begin owner=source:src_a00f40e6ce875bf5abb76b6f64af9231 block=evidence -->
- A per-action approval policy supports allow/ask/review/deny with risk heuristics (e.g. rm -rf, sudo, .env, secrets) and wildcard allow/deny lists. [@claim:clm_26a0b7a181ead46788ab7c62b8b61b64d2c4609d2a3134aebce2fef5e884f38c]
- Local AI support includes built-in llama.cpp management (spawning llama-server with control over context size, GPU layers, flash attention, etc.) and zero-config Ollama integration. [@claim:clm_54fc169ee2e371772e284ade7e9ac5bd5f9ef57b1be69a80d7eb267128291f1a]
- The agent ships a suite of 25 tools including read/write/edit, shell, grep/glob, semantic search, web search/fetch, notebooks, todos, subagents, and MCP. [@claim:clm_5c535319a5999f7395dc6d4a6f638c05ce614dd5e58cc80d85e2ffca75a5137a]
- Heavy native runtime dependencies such as ONNX runtime and image processing are downloaded on first activation with integrity checks rather than shipped in the VSIX. [@claim:clm_6e95d34490d42431b652fc70f354c78150ae10e5b832468d95fdfefeb1bd9aeb]
- Edits get per-hunk Keep/Undo CodeLenses for inline review, and the README states this works without requiring git. [@claim:clm_b3c684dd546ea77944b3b851c385593f71a7094889d3be76f89f62c2d86242ef]
- OpenCursor is a VS Code extension installable from the Marketplace or as a .vsix, providing a multi-tab sidebar chat with @-mentions of files, folders, docs, commits, diffs, terminals, and rules. [@claim:clm_b7b1984a225d7099c9afc38c6091bf9446b7c0863dc8f33d897d3bf9773502e8]
- Repository development practice: build from source with pnpm install and pnpm run compile (or watch), press F5 for the Extension Development Host, and package with pnpm run vsix; issues and PRs are welcome. [@claim:clm_be5f88ffd89336c03248baad6878131b5f40a2c4c9afe80d58776b0cff435d16]
- Providers include OAuth sign-in for Claude Code, OpenAI Codex, and Google Antigravity accounts, API-key presets (OpenAI, Anthropic, Gemini, OpenRouter), and custom OpenAI-compatible or Anthropic-style endpoints usable simultaneously. [@claim:clm_c04769895b45c6190bd889342816bb12694e1a568c632f87f98d2b38296393f3]
- Semantic codebase search uses an on-device ONNX MiniLM embedding model, with an option to point at any OpenAI-compatible /embeddings endpoint instead. [@claim:clm_c925998b6f15efe5ad7b675f697a318f7f62a86746b5d1c771a0b5b06e7bab57]
<!-- rcw:end owner=source:src_a00f40e6ce875bf5abb76b6f64af9231 block=evidence -->

## Researcher notes

