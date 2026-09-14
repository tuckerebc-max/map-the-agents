# zap-coding-agent/zap-coding-agent -- full detail

[Back to orientation](zap-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zap-coding-agent/zap-coding-agent/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/e16dd8e1241033bc.json](../../../wiki/dossiers/zap-coding-agent/zap-coding-agent/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/e16dd8e1241033bc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] A documented domain map lists modules including agent_core, llm_client, tools with permission_manager and shell_runner, context_manager, code_index, mcp, persistence, skill_manager, and remote session sharing. -- evidence: [README.md#L115-L125](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L115-L125) (`clm_db5e90f1f143c0e21a75cfdd920a931e1fc29f0de292f09282d0346c854690d8`)
- [observation/documented] The AST code index is built at startup with tree-sitter and SQLite, stored at .zap/code.db, supports Rust, Python, TypeScript, JavaScript, Go, and Java, and reindexes edited files before the next LLM turn. -- evidence: [README.md#L365-L365](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L365-L365), [README.md#L267-L267](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L267-L267), [README.md#L279-L279](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L279-L279), [README.md#L233-L233](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L233-L233) (`clm_31ca53605b9ffa5e977bdd5f2fa1b0d79a8db1e1fa219394e3bc8c90ff791fca`)

## design-choices (1 claim(s))

- [observation/documented] ZAP is a terminal-first, local AI coding agent written in Rust, distributed as a single statically-linked binary with no runtime dependency on Python, Node.js, or Docker. -- evidence: [README.md#L9-L9](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L9-L9), [README.md#L430-L434](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L430-L434), [README.md#L428-L428](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L428-L428) (`clm_90214120fc7c6c43456a3c439bbafaa64df0858f5b31ea0370771579741c66a8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (3 claim(s))

- [observation/documented] ZAP uses a skill system of markdown files injected only when triggered: always-on skills (e.g. karpathy-guidelines) fire every turn, while triggered skills like rust, git, or security fire on keyword matches in the user's message. -- evidence: [README.md#L150-L150](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L150-L150), [README.md#L161-L172](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L161-L172), [README.md#L154-L157](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L154-L157) (`clm_1498106074384681347da2843fe5328e05416eb8f52482ec873661a6ae3a16a3`)
- [observation/documented] Skills resolve by priority: project-level .zap/skills/ overrides personal ~/.zap/skills/, which overrides built-in defaults compiled into the binary; same-name custom skills override built-ins. -- evidence: [README.md#L187-L187](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L187-L187), [README.md#L218-L218](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L218-L218), [README.md#L212-L216](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L212-L216) (`clm_437bc316111fa639905d9ef1f01b02ba11e20b0d58eca3a8f0700980d973dd07`)
- [observation/documented] Slash commands manage skills, including /skill list, show, export, create, and capture, the last of which extracts instructions from the current session into a reusable skill. -- evidence: [README.md#L220-L227](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L220-L227) (`clm_631282014c8209c51c393c78a6d12ab03ff84cbfb48f1af94e14e7f18fae2e74`)

## interfaces (1 claim(s))

- [observation/documented] Index-backed tools include code_map, find_definition, find_references, who_calls, file_imports, where_imported, find_subtypes/supertypes, pack_context, ripple_analysis, get_diagnostics, lsp_definition, and lsp_type_at. -- evidence: [README.md#L283-L296](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L283-L296) (`clm_b47aa5719529611de33ff28e629038b70b6ef95b0d773e78ac8e61d6727c0978`)

## memory-state (1 claim(s))

- [observation/documented] ZAP maintains four context files (ZAP.md, .zap/understanding.md, .zap/context.md, .zap/session_log.md) updated at defined times and loaded on demand via read_file rather than pre-loaded into context. -- evidence: [README.md#L81-L86](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L81-L86), [README.md#L88-L88](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L88-L88) (`clm_d79d9ee3e5e097013e2922a6f27049a5b22d0170005b88d0d25946628c4af597`)

## orchestration (1 claim(s))

- [observation/documented] MCP servers stay pending at startup with only a lightweight mcp_connect stub in context; the server process is spawned and its real tool schemas fetched only when the model calls mcp_connect. -- evidence: [README.md#L470-L475](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L470-L475), [README.md#L468-L468](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L468-L468), [README.md#L459-L459](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L459-L459) (`clm_0cbadcc8047e32e3963c954f3489b3da7a3337759c1bc723495f9c02f6481fc3`)

## tools-permissions (2 claim(s))

- [observation/documented] ZAP has three permission modes — ask (default, prompts before writes and shell), auto, and deny (read-only) — switchable via /permissions, plus a shell sandbox with workdir and container (Docker/Podman, network disabled) modes. -- evidence: [README.md#L496-L501](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L496-L501), [README.md#L511-L511](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L511-L511), [README.md#L513-L513](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L513-L513), [README.md#L505-L509](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L505-L509) (`clm_8271009ffd6728d4cec7df24567777d0afd05ba58c2218f451f4bab9b8712a4c`)
- [observation/documented] Before content is sent to a cloud LLM, a secret scanner checks patterns including API keys, VCS tokens, AWS/GCP credentials, PEM blocks, and JWTs, blocking matches with a redacted warning; every tool call is appended to ~/.zap/audit.jsonl. -- evidence: [README.md#L529-L529](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L529-L529), [README.md#L525-L525](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L525-L525), [README.md#L519-L523](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L519-L523), [README.md#L517-L517](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L517-L517) (`clm_2d46bb3a2ee2ab34a435799916aacc0d0fa234728a33e36364e961b58b1ac404`)

## evaluation (1 claim(s))

- [observation/documented] The README reports a token-efficiency comparison claiming ZAP sends task-specific prompts (1,889 vs 1,661 tokens for Spring Boot vs React) versus identical static prompts from Gemini CLI and OpenCode, with methodology in a linked evidence file. -- evidence: [README.md#L54-L54](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L54-L54), [README.md#L42-L46](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L42-L46), [README.md#L56-L57](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L56-L57) (`clm_402d827ddfa00ffec9ef659ce16cfce5f421717d11e0af792f5e9ba0ef730ab2`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

