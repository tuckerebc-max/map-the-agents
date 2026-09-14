---
access: public
aliases: []
claim_ids:
- clm_00eae0f8d64346c3586edbbd51f6a00d1cbc755d551d5bf6c936f0f1a85f5e67
- clm_089ea0040d451ad7b64b7381919c204da583f0ac7cd08ad10e4aa561b7ccc679
- clm_08c31351ad595ea9812a87d8ab50015879184bc417cb36adf2573a5e23c540e3
- clm_0e6f1f7b99ed565085621d43ee3cbec4a7787efef7ea919cb62736264e85c814
- clm_35a5d6b1d650ac960ce1cf0ccd0f2fc1cdd81f09323db43c9397ec65b3bff83c
- clm_49d2c60655195a255a1ce915e76e746cd8783da3252247fb5a34028793dd123a
- clm_4c6a0c1bea34b440959609435f47c8abed84054eabd139cfcc40a67b541406a8
- clm_54c6366498d4def7fc5f511f2a3b68c42018d63c87ebbe846a2c0a6c00ba7447
- clm_5fc56691298269bc57cecbf43633e8f69fcf3e71c305c46b4d22e528a66b86e5
- clm_73275af1f59ee353b86e494a61583791cf7002e146f64847455c3ceedbb979c6
- clm_822c8dcc69e6e583f4941aebb04e369e0886e984599898196fe24568d054d1a2
- clm_86e0faadae3537376403d61d2793ffd32125a2e291fdc90b687ff778a07a0c3a
- clm_95b05bd687c241cc3ac3f4af54bdbb6c3b3a99a26c4a06463a4db33341fb6ee8
- clm_a290eae041ada055a8661e1e3c8b31a04d326d6fadf1c1abbf59dbf64674f743
- clm_b95e15240a16ea0435d682f5db24433bfad078e95fafadb3ead3e660a1940b78
- clm_cbb2323c20895ee52d28a26ff0e6c7412e53764d3d22d8632c31e65f8bee8c3c
- clm_e7550ac01d291827ea20791a91618b2bc81ae16ada5c0e65273d16d1ade99b36
- clm_ee22d46a1d91999e100a62ef57f57d410edd1e14a9ba9a13aaac86a62f24acf8
maturity: draft
page_id: pg_7ecc1ad274595b0989541aada37f06a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3fe97386ba0f5755ac042e1a14e827ec
title: atomgit-atomcode/atomcode/README.md @ 287bff70f940
updated_at: '2026-09-14T01:59:39Z'
---

# atomgit-atomcode/atomcode/README.md @ 287bff70f940

<!-- rcw:begin owner=source:src_3fe97386ba0f5755ac042e1a14e827ec block=evidence -->
- A .atomcode.md file in the project root provides persistent context included in the system prompt; AGENTS.md is supported as an alternative, with .atomcode.md taking priority if both exist. [@claim:clm_00eae0f8d64346c3586edbbd51f6a00d1cbc755d551d5bf6c936f0f1a85f5e67]
- The agent loop features autonomous multi-step execution, a verification loop with syntax checks, a dynamic step budget scaled to edited files, loop detection, and 3-layer JSON repair of malformed tool-call arguments. [@claim:clm_089ea0040d451ad7b64b7381919c204da583f0ac7cd08ad10e4aa561b7ccc679]
- Built-in tools include file/shell operations (read_file, edit_file, bash, grep, glob), web search/fetch, code-graph tools (list_symbols, trace_callers, blast_radius), auto_fix, and use_skill. [@claim:clm_08c31351ad595ea9812a87d8ab50015879184bc417cb36adf2573a5e23c540e3]
- AtomCode is described as an open-source terminal AI coding agent written in Rust, positioned as an alternative to Claude Code / Cursor Agent that connects to any OpenAI-compatible API. [@claim:clm_0e6f1f7b99ed565085621d43ee3cbec4a7787efef7ea919cb62736264e85c814]
- A /webui command launches a local browser UI bound to 127.0.0.1 with a one-time token; /app enables mobile remote access via a reverse WSS relay with QR-code pairing and bidirectional sync. [@claim:clm_35a5d6b1d650ac960ce1cf0ccd0f2fc1cdd81f09323db43c9397ec65b3bff83c]
- The turn-level datalog is described as supporting replay, debugging, and eval harnesses, suggesting the product provides structured logs intended for evaluation use. [@claim:clm_49d2c60655195a255a1ce915e76e746cd8783da3252247fb5a34028793dd123a]
- Configuration lives at ~/.atomcode/config.toml with provider entries (type, api_key, model, base_url, context_window); /reload picks up manual edits without restart, and a first-run wizard guides provider setup. [@claim:clm_4c6a0c1bea34b440959609435f47c8abed84054eabd139cfcc40a67b541406a8]
- The agent supports multiple LLM providers via OpenAI function-calling, including Claude, OpenAI, DeepSeek, Zhipu GLM, Qwen, SiliconFlow, Ollama (partial), and any OpenAI-compatible API. [@claim:clm_54c6366498d4def7fc5f511f2a3b68c42018d63c87ebbe846a2c0a6c00ba7447]
- The CLI offers persistent sessions (--continue, /resume), AtomGit OAuth login, SSO login, headless single-prompt mode, and a daemon exposing an HTTP API with SSE streaming chat. [@claim:clm_5fc56691298269bc57cecbf43633e8f69fcf3e71c305c46b4d22e528a66b86e5]
- Building from source requires Rust 1.88+ because older Cargo versions cannot parse the current lockfile; runtime needs an API key from a supported provider or an AtomGit account. [@claim:clm_73275af1f59ee353b86e494a61583791cf7002e146f64847455c3ceedbb979c6]
- Users can define custom slash commands as Markdown template files with frontmatter (name, description, args) in global, project-level, or plugin directories; project-level overrides global, but custom commands cannot shadow built-ins. [@claim:clm_822c8dcc69e6e583f4941aebb04e369e0886e984599898196fe24568d054d1a2]
- In headless mode (-p), approval-required bash calls are auto-approved and logged to stderr, while other approval-required tools are denied. [@claim:clm_86e0faadae3537376403d61d2793ffd32125a2e291fdc90b687ff778a07a0c3a]
- The CodingPlan request signer is closed-source and only present in official builds; self-built binaries cannot sign requests, so /login cannot claim free CodingPlan models, though own API providers work without it. [@claim:clm_95b05bd687c241cc3ac3f4af54bdbb6c3b3a99a26c4a06463a4db33341fb6ee8]
- Memory commands let users save facts (/remember, with --global scope), remove them (/forget), and list them (/memory); sessions are persisted and resumable. [@claim:clm_a290eae041ada055a8661e1e3c8b31a04d326d6fadf1c1abbf59dbf64674f743]
- Stated design principles include tech-stack agnosticism via descriptor-file detection (package.json, Cargo.toml, etc.), a single CodingRuntime owner, tool safety, token-budget-aware context windowing, and directed dependencies keeping the kernel neutral. [@claim:clm_b95e15240a16ea0435d682f5db24433bfad078e95fafadb3ead3e660a1940b78]
- The project is a layered Rust workspace with crates for kernel (agent loop), capabilities (providers/tools/MCP/skills/sessions/memory), coding, review, TUI, CLI, and daemon (HTTP/SSE/WebSocket transport). [@claim:clm_cbb2323c20895ee52d28a26ff0e6c7412e53764d3d22d8632c31e65f8bee8c3c]
- Repository development practice: building from source requires Rust 1.88+ and Git; the webui frontend must be built with npm before the Rust build (webui/dist is gitignored and embedded), and cargo clean -p atomcode-daemon is needed after frontend rebuilds. [@claim:clm_e7550ac01d291827ea20791a91618b2bc81ae16ada5c0e65273d16d1ade99b36]
- Destructive commands (rm -rf, git push --force, DROP TABLE) require explicit approval; writes outside the workspace, sensitive paths, and source-file deletion get stronger confirmation rules, with per-session grants and /undo rollback. [@claim:clm_ee22d46a1d91999e100a62ef57f57d410edd1e14a9ba9a13aaac86a62f24acf8]
<!-- rcw:end owner=source:src_3fe97386ba0f5755ac042e1a14e827ec block=evidence -->

## Researcher notes

