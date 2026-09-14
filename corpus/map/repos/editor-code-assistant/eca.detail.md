# editor-code-assistant/eca -- full detail

[Back to orientation](eca.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/editor-code-assistant/eca/e30026331ad698d0748d52dc403e4a7d481d241e/6543b15215023cac.json](../../../wiki/dossiers/editor-code-assistant/eca/e30026331ad698d0748d52dc403e4a7d481d241e/6543b15215023cac.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The server is written in Clojure with a layered layout: handlers.clj receives all JSON-RPC requests, db.clj holds in-memory state, llm_api.clj is the LLM facade, and llm_providers/ holds vendor adapters. -- evidence: [README.md#L43-L43](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L43-L43), [docs/development.md#L18-L56](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L18-L56) (`clm_cc6f81e534358cc1add6c2cfaba0c304997b1d8654e23a187fac6f7e41eb3612`)
- [observation/documented] The documented request flow is: client/editor → stdin JSON-RPC → handlers → features → llm_api → llm_provider, with results streamed back via messenger. -- evidence: [docs/development.md#L60-L60](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L60-L60) (`clm_58069c3585076b2b2d16173260158378e67d1a445e64939f04dac93538e92d0d`)

## design-choices (2 claim(s))

- [observation/documented] ECA places a server between editors and LLMs to centralize tool-call management, multi-LLM interaction, telemetry, and a single configuration shared across editors. -- evidence: [README.md#L45-L50](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L45-L50) (`clm_dbf5003be61d4eb18234969493881dc5e366c687a57e421a870f21f14719789a`)
- [observation/documented] Configuration is centralized and resolved from multiple sources: global config, local config, environment variables, and initializationOptions. -- evidence: [docs/development.md#L18-L56](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L18-L56) (`clm_dc297a72bf081d7431be1cf606dbf20e3aa81f9aca554cea28643cd311290f09`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run unit tests with `bb test` (CI runs the same task), single namespaces via kaocha focus, and integration tests with `bb integration-test`, which spawns the server over JSON-RPC with mocked LLM and MCP servers. -- evidence: [docs/development.md#L74-L76](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L74-L76), [docs/development.md#L70-L70](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L70-L70), [docs/development.md#L80-L80](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L80-L80), [docs/development.md#L72-L72](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L72-L72) (`clm_fe481f51f9018c41875141329e76601e840885d80e441d8f5022c3529712ce9c`)
- [observation/documented] Repository development practice: a local debug binary is built with `bb debug-cli` (requires babashka), and contributors can attach to the nREPL port printed on stderr to modify the running ECA process. -- evidence: [docs/development.md#L92-L95](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L92-L95), [docs/development.md#L9-L10](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L9-L10) (`clm_9bba2c9d7fbacad909f4c7adea10fc9cb6e0c9dc690ad9484c53a06d4ab0b505`)
- [observation/documented] Repository development practice: contributions are welcomed via issue discussion or pull request with developer details in the development docs, and new-editor integrations follow a UX-consistency checklist. -- evidence: [docs/development.md#L99-L99](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L99-L99), [docs/development.md#L103-L133](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L103-L133), [README.md#L99-L100](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L99-L100) (`clm_4241fbeac06d3e97c164183b8465546028cd82147fed26bbac5c926376569049`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are SKILL.md folders following the agentskills standard, searched in ~/.config/eca/skills, .eca/skills, and .agents/skills; only name and description are sent to the LLM, which loads a skill via the `eca__skill` tool. -- evidence: [docs/config/skills.md#L9-L10](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L9-L10), [docs/config/skills.md#L12-L12](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L12-L12) (`clm_019a6d1b9241994c986dbbcc918fea4e0ec992c4ef898a4938edf78e9aafa185`)
- [observation/documented] Skills can be parameterized as slash commands using $ARGS, $ARGUMENTS, and positional variables; when arguments are given, ECA substitutes them into the skill body instead of using the eca__skill tool. -- evidence: [docs/config/skills.md#L110-L110](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L110-L110), [docs/config/skills.md#L92-L92](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L92-L92), [docs/config/skills.md#L90-L90](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L90-L90) (`clm_4e4d1d0f957eabf056848f842ee69da2d9a1060de36538c50b9379a62b37c164`)

## interfaces (3 claim(s))

- [observation/documented] Editors spawn the server via `eca server` and communicate over stdin/stdout using a JSON-RPC protocol inspired by LSP, so any editor can integrate. -- evidence: [README.md#L43-L43](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L43-L43), [README.md#L54-L54](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L54-L54) (`clm_bcaa4dd7944a227363f2f5b75e98e84d92c9f50f8b84ff41ee7bdb5f209112e4`)
- [observation/documented] MCP servers are configured via an `mcpServers` key supporting stdio commands and HTTP (streamable or SSE) URLs, with OAuth discovery, static Authorization headers, and a `disabled` flag. -- evidence: [docs/config/tools.md#L38-L46](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L38-L46), [docs/config/tools.md#L21-L32](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L21-L32), [docs/config/tools.md#L219-L219](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L219-L219), [docs/config/tools.md#L34-L34](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L34-L34), [docs/config/tools.md#L17-L17](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L17-L17), [docs/config/tools.md#L98-L99](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L98-L99) (`clm_0eab46df40bddd7555e009676fe811f0cf24613ad4038b8be85e26296b909ab8`)
- [observation/documented] The new-editor checklist documents protocol methods including initialize/initialized, exit/shutdown, chat/prompt, chat/contentReceived, chat/queryContext, chat/toolCallApprove/Reject, and chat/queryCommands. -- evidence: [docs/development.md#L103-L133](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L103-L133) (`clm_dd26149171401eb9d477820d0a500ae91440461cb0627f210095ffea76fef8f2`)

## memory-state (2 claim(s))

- [observation/documented] All runtime state — sessions, chats, and tool servers — lives in an in-memory atom (`db*`) in db.clj. -- evidence: [docs/development.md#L18-L56](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L18-L56) (`clm_df94f3c9cc1b97bc1ae558e66262dfab16bb3bf7cb5251c037875bdd52f5f621`)
- [observation/documented] Locally, ECA stores config in ~/.config/eca/config.json, auth tokens in ~/.cache/eca/db.transit.json, and per-workspace conversation history plus truncated tool outputs auto-deleted after 7 days, respecting XDG paths. -- evidence: [PRIVACY.md#L31-L31](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L31-L31), [PRIVACY.md#L23-L29](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L23-L29) (`clm_bcffd2f1369425f3d43da287d372c0c299c641b3f439ce02cf5f2a0415e23d13`)

## orchestration (1 claim(s))

- [observation/documented] ECA supports configuring multiple agents/subagents, each with different models, tools, and behaviors. -- evidence: [README.md#L31-L37](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L31-L37) (`clm_5c6b83246d050c5a920f328a5e560024391d0bf578276efe022c78151e4d191e`)

## tools-permissions (3 claim(s))

- [observation/documented] ECA supports three tool types: native tools (edit_file, write_file, read, etc.), configured MCP servers, and user-defined custom CLI tools. -- evidence: [docs/config/tools.md#L11-L13](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L11-L13), [docs/config/tools.md#L9-L9](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L9-L9) (`clm_d6e51bd0e157050c65bac269326ace240333014f81612bda305d3a63d2e4461d`)
- [observation/documented] Tool-call approval is configurable globally or per agent with allow/deny rules and argsMatchers, e.g. denying `eca__skill` globally while allowing a specific skill name for one agent. -- evidence: [docs/config/skills.md#L50-L51](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L50-L51), [docs/config/skills.md#L55-L76](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L55-L76) (`clm_dd1571767c47fb08c21ec0b4c007f6a644525053b30c9e4e428bc7c5a24118c4`)
- [observation/documented] Custom tools are defined in config with a description, a command string containing {{argument_name}} placeholders replaced by LLM-supplied values, and a schema of parameters. -- evidence: [docs/config/tools.md#L239-L243](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L239-L243), [docs/config/tools.md#L245-L245](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L245-L245), [docs/config/tools.md#L235-L235](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L235-L235), [docs/config/tools.md#L237-L237](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/tools.md#L237-L237) (`clm_53d48f2581e309b150970a6e2ae6a2b9a4c64cfddc8c3acaf2d93c273d0cc84a`)

## evaluation (1 claim(s))

- [inference/documented] No evidence in this snapshot describes benchmarks or success-rate evaluation of the agent; the only test-related material is the repository's own unit and integration test suites. -- evidence: [docs/development.md#L70-L70](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L70-L70), [docs/development.md#L80-L80](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L80-L80) (`clm_8f7c14c99f4f427934720a2d66c6a69b3d3b1dc9f6878121068a9ad5b7f3b6d0`)

## dependencies (2 claim(s))

- [observation/documented] The project builds with Babashka tasks (bb.edn) and Clojure deps.edn including a native GraalVM image target; the server wires together via jsonrpc4clj. -- evidence: [docs/development.md#L18-L56](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L18-L56) (`clm_c1250660aa7f98281ad294ecb84885b03eece47645ec19e5fdff809bb4499d82`)
- [observation/documented] Documented providers include Anthropic, OpenAI, GitHub Copilot, Google Gemini, Azure OpenAI, DeepSeek, OpenRouter, xAI, and locally running Ollama, plus custom providers. -- evidence: [PRIVACY.md#L77-L77](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L77-L77), [PRIVACY.md#L65-L75](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L65-L75) (`clm_49283325dde0ef9b2855f4e8d28c1ee9f2e4f8de53273c89474436b3984c4dca`)

## limitations (1 claim(s))

- [observation/documented] Per its privacy policy, ECA runs entirely locally with no hosted service, no accounts, no analytics or tracking, and ships with no MCP servers enabled by default. -- evidence: [PRIVACY.md#L81-L86](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L81-L86), [PRIVACY.md#L7-L7](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L7-L7), [PRIVACY.md#L41-L41](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L41-L41), [PRIVACY.md#L3-L3](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/PRIVACY.md#L3-L3) (`clm_410b6a3eb93f3428668a9f23bf20cd1f32dd150b1e63ab94d2bb4fd93c567ecd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

