# atomgit-atomcode/atomcode -- full detail

[Back to orientation](atomcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/atomgit-atomcode/atomcode/287bff70f9400c24f4afd8fcf4762fbab63d8efa/21b0b17abcf968f4.json](../../../wiki/dossiers/atomgit-atomcode/atomcode/287bff70f9400c24f4afd8fcf4762fbab63d8efa/21b0b17abcf968f4.json)

## specifications (1 claim(s))

- [observation/documented] AtomCode is described as an open-source terminal AI coding agent written in Rust, positioned as an alternative to Claude Code / Cursor Agent that connects to any OpenAI-compatible API. -- evidence: [README.md#L47-L47](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L47-L47), [README.md#L11-L13](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L11-L13) (`clm_0e6f1f7b99ed565085621d43ee3cbec4a7787efef7ea919cb62736264e85c814`)

## components (1 claim(s))

- [observation/documented] The project is a layered Rust workspace with crates for kernel (agent loop), capabilities (providers/tools/MCP/skills/sessions/memory), coding, review, TUI, CLI, and daemon (HTTP/SSE/WebSocket transport). -- evidence: [README.md#L629-L639](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L629-L639) (`clm_cbb2323c20895ee52d28a26ff0e6c7412e53764d3d22d8632c31e65f8bee8c3c`)

## design-choices (1 claim(s))

- [observation/documented] Stated design principles include tech-stack agnosticism via descriptor-file detection (package.json, Cargo.toml, etc.), a single CodingRuntime owner, tool safety, token-budget-aware context windowing, and directed dependencies keeping the kernel neutral. -- evidence: [README.md#L650-L650](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L650-L650), [README.md#L652-L652](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L652-L652), [README.md#L648-L648](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L648-L648), [README.md#L654-L654](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L654-L654), [README.md#L646-L646](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L646-L646) (`clm_b95e15240a16ea0435d682f5db24433bfad078e95fafadb3ead3e660a1940b78`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source requires Rust 1.88+ and Git; the webui frontend must be built with npm before the Rust build (webui/dist is gitignored and embedded), and cargo clean -p atomcode-daemon is needed after frontend rebuilds. -- evidence: [README.md#L187-L191](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L187-L191), [README.md#L678-L680](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L678-L680), [README.md#L203-L207](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L203-L207) (`clm_e7550ac01d291827ea20791a91618b2bc81ae16ada5c0e65273d16d1ade99b36`)

## skills-patterns (1 claim(s))

- [observation/documented] Users can define custom slash commands as Markdown template files with frontmatter (name, description, args) in global, project-level, or plugin directories; project-level overrides global, but custom commands cannot shadow built-ins. -- evidence: [README.md#L564-L564](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L564-L564), [README.md#L568-L572](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L568-L572), [README.md#L623-L623](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L623-L623), [README.md#L590-L592](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L590-L592) (`clm_822c8dcc69e6e583f4941aebb04e369e0886e984599898196fe24568d054d1a2`)

## interfaces (4 claim(s))

- [observation/documented] Built-in tools include file/shell operations (read_file, edit_file, bash, grep, glob), web search/fetch, code-graph tools (list_symbols, trace_callers, blast_radius), auto_fix, and use_skill. -- evidence: [README.md#L77-L79](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L77-L79), [README.md#L83-L84](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L83-L84), [README.md#L71-L73](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L71-L73) (`clm_08c31351ad595ea9812a87d8ab50015879184bc417cb36adf2573a5e23c540e3`)
- [observation/documented] The CLI offers persistent sessions (--continue, /resume), AtomGit OAuth login, SSO login, headless single-prompt mode, and a daemon exposing an HTTP API with SSE streaming chat. -- evidence: [README.md#L103-L107](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L103-L107) (`clm_5fc56691298269bc57cecbf43633e8f69fcf3e71c305c46b4d22e528a66b86e5`)
- [observation/documented] A /webui command launches a local browser UI bound to 127.0.0.1 with a one-time token; /app enables mobile remote access via a reverse WSS relay with QR-code pairing and bidirectional sync. -- evidence: [README.md#L129-L135](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L129-L135), [README.md#L123-L125](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L123-L125) (`clm_35a5d6b1d650ac960ce1cf0ccd0f2fc1cdd81f09323db43c9397ec65b3bff83c`)
- [observation/documented] Configuration lives at ~/.atomcode/config.toml with provider entries (type, api_key, model, base_url, context_window); /reload picks up manual edits without restart, and a first-run wizard guides provider setup. -- evidence: [README.md#L353-L354](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L353-L354), [README.md#L374-L375](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L374-L375), [README.md#L339-L339](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L339-L339), [README.md#L359-L365](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L359-L365) (`clm_4c6a0c1bea34b440959609435f47c8abed84054eabd139cfcc40a67b541406a8`)

## memory-state (2 claim(s))

- [observation/documented] Memory commands let users save facts (/remember, with --global scope), remove them (/forget), and list them (/memory); sessions are persisted and resumable. -- evidence: [README.md#L520-L524](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L520-L524), [README.md#L103-L107](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L103-L107) (`clm_a290eae041ada055a8661e1e3c8b31a04d326d6fadf1c1abbf59dbf64674f743`)
- [observation/documented] A .atomcode.md file in the project root provides persistent context included in the system prompt; AGENTS.md is supported as an alternative, with .atomcode.md taking priority if both exist. -- evidence: [README.md#L670-L670](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L670-L670), [README.md#L658-L658](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L658-L658) (`clm_00eae0f8d64346c3586edbbd51f6a00d1cbc755d551d5bf6c936f0f1a85f5e67`)

## orchestration (1 claim(s))

- [observation/documented] The agent loop features autonomous multi-step execution, a verification loop with syntax checks, a dynamic step budget scaled to edited files, loop detection, and 3-layer JSON repair of malformed tool-call arguments. -- evidence: [README.md#L53-L58](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L53-L58) (`clm_089ea0040d451ad7b64b7381919c204da583f0ac7cd08ad10e4aa561b7ccc679`)

## tools-permissions (2 claim(s))

- [observation/documented] Destructive commands (rm -rf, git push --force, DROP TABLE) require explicit approval; writes outside the workspace, sensitive paths, and source-file deletion get stronger confirmation rules, with per-session grants and /undo rollback. -- evidence: [README.md#L139-L145](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L139-L145) (`clm_ee22d46a1d91999e100a62ef57f57d410edd1e14a9ba9a13aaac86a62f24acf8`)
- [observation/documented] In headless mode (-p), approval-required bash calls are auto-approved and logged to stderr, while other approval-required tools are denied. -- evidence: [README.md#L397-L397](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L397-L397), [README.md#L103-L107](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L103-L107) (`clm_86e0faadae3537376403d61d2793ffd32125a2e291fdc90b687ff778a07a0c3a`)

## evaluation (1 claim(s))

- [inference/documented] The turn-level datalog is described as supporting replay, debugging, and eval harnesses, suggesting the product provides structured logs intended for evaluation use. -- evidence: [README.md#L53-L58](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L53-L58) (`clm_49d2c60655195a255a1ce915e76e746cd8783da3252247fb5a34028793dd123a`)

## dependencies (2 claim(s))

- [observation/documented] The agent supports multiple LLM providers via OpenAI function-calling, including Claude, OpenAI, DeepSeek, Zhipu GLM, Qwen, SiliconFlow, Ollama (partial), and any OpenAI-compatible API. -- evidence: [README.md#L90-L99](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L90-L99), [README.md#L88-L88](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L88-L88) (`clm_54c6366498d4def7fc5f511f2a3b68c42018d63c87ebbe846a2c0a6c00ba7447`)
- [observation/documented] Building from source requires Rust 1.88+ because older Cargo versions cannot parse the current lockfile; runtime needs an API key from a supported provider or an AtomGit account. -- evidence: [README.md#L282-L285](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L282-L285) (`clm_73275af1f59ee353b86e494a61583791cf7002e146f64847455c3ceedbb979c6`)

## limitations (1 claim(s))

- [observation/documented] The CodingPlan request signer is closed-source and only present in official builds; self-built binaries cannot sign requests, so /login cannot claim free CodingPlan models, though own API providers work without it. -- evidence: [README.md#L237-L242](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L237-L242), [README.md#L230-L235](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L230-L235) (`clm_95b05bd687c241cc3ac3f4af54bdbb6c3b3a99a26c4a06463a4db33341fb6ee8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

