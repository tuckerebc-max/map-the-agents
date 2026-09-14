# dog-qiuqiu/invincat -- full detail

[Back to orientation](invincat.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dog-qiuqiu/invincat/8a026ea3579aaff800c1be989ffc79c09cba79e4/aeb151f89aa5de23.json](../../../wiki/dossiers/dog-qiuqiu/invincat/8a026ea3579aaff800c1be989ffc79c09cba79e4/aeb151f89aa5de23.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The runtime is a Textual TUI over a DeepAgents/LangGraph agent: cli assembles startup, agent builds the agent with tools/middleware/backend/system prompt, textual_adapter converts agent streams to UI messages, and widgets render chat, tool calls, approvals, and selectors. -- evidence: [doc/ARCHITECTURE_EN.md#L9-L15](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L9-L15), [doc/ARCHITECTURE.md#L9-L15](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L9-L15) (`clm_c389cfa7030c09cd1461982c9f298920b67c3b35af8b413438c42436db3b840b`)
- [observation/documented] Middleware includes approve_plan and ask_user interrupt protocols, auto memory refresh, project-scoped file management tools (file_info, mkdir, move_file, copy_file, delete_file), micro_compaction of old messages, and token state tracking. -- evidence: [doc/ARCHITECTURE_EN.md#L152-L160](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L152-L160), [doc/ARCHITECTURE.md#L152-L160](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L152-L160) (`clm_b5aae266459120dffad5efd8b7c0f413115035e6d15e1751c689f99fb4482685`)
- [observation/documented] The scheduler subsystem parses natural-language time expressions into cron/once schedules, stores tasks in SQLite with schema migrations, exposes schedule tools via ScheduleMiddleware, and supports WeCom delivery of scheduled results. -- evidence: [doc/ARCHITECTURE.md#L294-L312](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L294-L312), [doc/ARCHITECTURE_EN.md#L294-L312](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L294-L312) (`clm_d5403586f8815c3d71e206417782d5cc64957cc4425109b42b43f0ab1618339f`)
- [inference/documented] The architecture docs indicate sandboxing is pluggable: a sandbox provider protocol and factory exist, with cloud providers including AWS Bedrock AgentCore and LangSmith sandboxes. -- evidence: [doc/ARCHITECTURE.md#L374-L419](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L374-L419) (`clm_50c7b2d60fa403a472432d1fdce9d4a4dcf8f7b757fd67dd54cfaf32afea78a1`)

## design-choices (2 claim(s))

- [observation/documented] Model selection is per-call switchable through LangGraph runtime context via configurable_model, and model profiles persist as TOML configuration with thread-level model preferences. -- evidence: [doc/ARCHITECTURE_EN.md#L250-L265](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L250-L265), [doc/ARCHITECTURE.md#L250-L265](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L250-L265) (`clm_c19110a154cc7f2e96fccca5068880a5cdb5189932ff81c9932858a6d6915b94`)
- [observation/documented] MCP integration includes server loading/connection, tool wrapping, and an MCP server trust policy module (mcp/trust.py). -- evidence: [doc/ARCHITECTURE.md#L269-L275](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L269-L275), [doc/ARCHITECTURE_EN.md#L269-L275](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L269-L275) (`clm_70e242a815658fb666d835516dcef64a98452e034e82f6e5d82d3828b2b7dd71`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are capability packs loaded when a task matches their description; built-in skills include docx, pdf, pptx, xlsx, and skill-creator, and custom skills can live at user, user-shared, project, or project-shared scope with project overriding user and custom overriding built-in. -- evidence: [README.md#L180-L182](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L180-L182), [README.md#L197-L203](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L197-L203), [README.md#L205-L207](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L205-L207), [README.md#L184-L190](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L184-L190) (`clm_dc54b40da60aaaeff5c4da4938890019d36e5084f2602970f2a6c13efcda5157`)

## interfaces (4 claim(s))

- [observation/documented] The product exposes slash commands including /model, /plan, /goal, /memory, /schedule, /mcp, /threads, and /help, plus a wecombot subcommand to start the WeCom daemon. -- evidence: [README.md#L249-L252](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L249-L252), [README.md#L95-L104](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L95-L104) (`clm_9cb53f6cc8cd933fb2d8a7a81deaa2bc555b30356c9d0e9aa8427eb36029fec9`)
- [observation/documented] Model configuration is done via a /model manager (Ctrl+N to register provider, model name, API key, optional base URL) or through provider environment variables such as OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, DEEPSEEK_API_KEY, and OPENROUTER_API_KEY. -- evidence: [README.md#L66-L66](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L66-L66), [README.md#L68-L74](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L68-L74), [README.md#L62-L64](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L62-L64) (`clm_a8b2614e58bba5b8f0daac26b84143b28a6d1aad8bcdd4c683e195f2f1aa0648`)
- [observation/documented] The WeCom bot daemon is configured with WECOM_BOT_ID and WECOM_BOT_SECRET environment variables, optionally overrides WECOM_WS_URL (default wss://openws.work.weixin.qq.com), and runs project-scoped remote turns and scheduled-task delivery. -- evidence: [README.md#L244-L245](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L244-L245), [README.md#L239-L242](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L239-L242), [README.md#L235-L235](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L235-L235) (`clm_52ad87263acd07224c23139442359f3f3061e9e49731509cd6db89420a1a8187`)
- [observation/documented] The package supports both interactive Textual TUI and non-interactive runtime paths, plus a local LangGraph server mode and ACP startup wiring, selected from parsed CLI arguments. -- evidence: [doc/ARCHITECTURE_EN.md#L43-L51](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE_EN.md#L43-L51), [doc/ARCHITECTURE.md#L43-L51](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/doc/ARCHITECTURE.md#L43-L51) (`clm_70318a9f4bd124c571269dc995a5b6d5d9f3ade61602339fb46c698f1d01cf53`)

## memory-state (2 claim(s))

- [observation/documented] Durable memory has two scopes: user memory at ~/.invincat/<agent>/memory_user.json and project memory at .invincat/memory_project.json; a background memory agent extracts updates after non-trivial turns, and /memory opens a manager UI. -- evidence: [README.md#L138-L142](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L138-L142), [README.md#L133-L136](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L133-L136), [README.md#L144-L147](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L144-L147) (`clm_f0c6f0df1b9ccdf7d261d6ffd8473726cc046075128dc4a0e6916a4a8dd051ed`)
- [observation/documented] An optional dedicated memory model can be set with /model 2 <provider:model> for post-turn memory extraction; otherwise extraction uses the current primary model. -- evidence: [README.md#L138-L142](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L138-L142), [README.md#L91-L91](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L91-L91) (`clm_2f77c31d3b465ee14e9fdd6c78b9cf5d48c530c3cefcddc8b08c313b7bf24917`)

## orchestration (2 claim(s))

- [observation/documented] Plan mode (/plan) first produces an execution checklist for user approval; the planner is restricted to read/planning tools, and implementation tools are reserved for post-approval execution by the main agent. -- evidence: [README.md#L156-L160](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L156-L160), [README.md#L151-L154](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L151-L154) (`clm_20e987f0de1883b2c80c8be614b0764db59c2af4906e7bf97b5a49a719d643ff`)
- [observation/documented] Built-in subagents callable via the task tool include explorer (read-only codebase exploration), worker (bounded implementation), researcher (external research), and document-worker (document parsing/extraction for PDF, DOCX, PPTX, XLSX, Markdown, CSV, JSON). -- evidence: [README.md#L167-L172](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L167-L172), [README.md#L164-L165](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L164-L165) (`clm_9c6ff3f6c070b0cdf691928bac878cdfd0fae1952203d800d4d1dd18a35e6c2d`)

## tools-permissions (1 claim(s))

- [observation/documented] File reads, edits, creation, and shell command execution are approval-gated, with shell commands running under configurable safety controls. -- evidence: [README.md#L11-L11](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L11-L11), [README.md#L15-L21](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L15-L21) (`clm_9db1c58409ca0c3ed001fccbe1746aa7d23f303cb899e8938945888468f58adc`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The package is distributed on PyPI as invincat-cli, requires Python 3.11+, and can also be installed from source via an editable pip install. -- evidence: [README.md#L35-L35](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L35-L35), [README.md#L43-L47](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L43-L47), [README.md#L3-L7](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L3-L7), [README.md#L37-L39](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L37-L39) (`clm_cdc2529264955c6e45527d768d01f4c9147d82f6fa24ecdc9b71bb329420dd3a`)
- [observation/documented] Document-oriented skills rely on optional extras (invincat-cli[pdf], [office], [all-skills]) and may need system tools such as LibreOffice, Poppler, Tesseract, or Node.js packages. -- evidence: [README.md#L213-L217](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L213-L217), [README.md#L219-L221](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L219-L221), [README.md#L209-L211](https://github.com/dog-qiuqiu/invincat/blob/8a026ea3579aaff800c1be989ffc79c09cba79e4/README.md#L209-L211) (`clm_5537d5302129a49ebc86a9e3ce5655bf575f7ccd3d03a77e52aa7fb3bdecf9d8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

