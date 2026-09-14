# cline/cline -- full detail

[Back to orientation](cline.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cline/cline/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/ebde58e88eff80d7.json](../../../wiki/dossiers/cline/cline/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/ebde58e88eff80d7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository ships several products: an SDK, a CLI, a VS Code extension, a native macOS/Windows desktop app (Tauri shell, Bun sidecar, Next.js UI), and docs; the JetBrains plugin is not open-sourced. -- evidence: [README.md#L125-L132](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L125-L132) (`clm_a1d75f5dc152d0af92a2c04f55654d4279a5d377a96cee4c1b5ec64117f612d9`)

## design-choices (1 claim(s))

- [observation/documented] Cline offers Plan and Act modes: Plan mode explores the codebase and proposes a strategy, Act mode executes, and every file edit and terminal command requires user approval unless auto-approve is toggled. -- evidence: [README.md#L144-L144](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L144-L144) (`clm_c73caeb46327c64d7614220398aff12b28c6b88b7bc05a0d3954334771124eaf`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to start with the Contributing Guide (CONTRIBUTING.md) and join the #contributors Discord channel. -- evidence: [README.md#L231-L231](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L231-L231) (`clm_54f38b09322b5a051f001d517e9d52f9e6c40a293aca04698fbd9125742bcfbf`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are modular instruction sets loaded on demand (unlike always-active rules): metadata loads at startup (~100 tokens), full SKILL.md instructions load when triggered via the use_skill tool or slash commands, and resources load as needed. -- evidence: [docs/customization/skills.mdx#L25-L25](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L25-L25), [docs/customization/skills.mdx#L9-L9](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L9-L9), [docs/customization/skills.mdx#L19-L23](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L19-L23), [docs/customization/skills.mdx#L31-L33](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L31-L33), [docs/customization/skills.mdx#L7-L7](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L7-L7) (`clm_97bb50af6163a9968c5c1b9d984ae6ad1db9d866f035235bdfc8f404ce19b03d`)
- [observation/documented] A skill is a directory containing a required SKILL.md with YAML frontmatter (name matching the directory, description up to 1024 chars), optionally with docs/ and scripts/ subdirectories; skills are discovered from .cline/skills/ or ~/.cline/skills/. -- evidence: [docs/customization/skills.mdx#L39-L39](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L39-L39), [docs/customization/skills.mdx#L89-L89](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L89-L89), [docs/customization/skills.mdx#L68-L70](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L68-L70), [docs/customization/skills.mdx#L41-L48](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L41-L48) (`clm_d06d78d5cd8373f0f6a24f03099e854573e204cacd03f44603974b67687a0e1c`)

## interfaces (4 claim(s))

- [observation/documented] The CLI installs via `npm i -g cline` and supports interactive chat or fully headless mode for CI/CD and scripting, including JSON output and piped input. -- evidence: [README.md#L221-L221](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L221-L221), [README.md#L50-L52](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L50-L52), [README.md#L46-L48](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L46-L48), [README.md#L223-L227](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L223-L227) (`clm_8c22eb9ee4a201647dc88eb2cb86ee050b39f8e4fbe8fa9c3d92b22ad5d2a161`)
- [observation/documented] The Cline API requires a Bearer token in the Authorization header, with two auth methods: API keys created in the web dashboard and account auth tokens generated automatically on sign-in. -- evidence: [docs/api/authentication.mdx#L60-L60](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L60-L60), [docs/api/authentication.mdx#L7-L7](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L7-L7), [docs/api/authentication.mdx#L13-L16](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L13-L16) (`clm_a1128ff581601d5289b832527018075de09885afd1e86ef6b24f37ec560c2e45`)
- [observation/documented] The CLI exposes commands including `cline auth` for sign-in, `cline mcp` for MCP server management, and `cline connect` for messaging integrations such as Telegram and Slack. -- evidence: [docs/api/authentication.mdx#L66-L66](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L66-L66), [README.md#L214-L214](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L214-L214), [README.md#L212-L212](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L212-L212), [README.md#L216-L217](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L216-L217), [README.md#L183-L185](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L183-L185) (`clm_06c0c8d808e3415b0079d5265ddab81b741eb2f0db99d365c49e55aec0c1d94f`)
- [observation/documented] The SDK (`@cline/sdk`) exposes the agent core programmatically, allowing custom tools via createTool and plugins with lifecycle hooks, and powers the CLI, desktop app, VS Code extension, and JetBrains plugin. -- evidence: [README.md#L109-L111](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L109-L111), [README.md#L169-L169](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L169-L169), [README.md#L174-L181](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L174-L181), [README.md#L107-L107](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L107-L107), [README.md#L183-L185](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L183-L185) (`clm_0e8e01b736a37147daf48c02dbd9f84b6dbb2d743192fde4f9f674bdc7658823`)

## memory-state (2 claim(s))

- [observation/documented] Configuration lives in two scopes: global `~/.cline/` (with data/settings, teams, sessions, SQLite databases, workflows, rules, hooks, skills, agents, plugins, cron) and per-workspace `.cline/`; a custom directory can be set via CLINE_DATA_DIR. -- evidence: [docs/getting-started/config.mdx#L9-L10](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L9-L10), [docs/getting-started/config.mdx#L109-L117](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L109-L117), [docs/getting-started/config.mdx#L16-L33](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L16-L33), [docs/getting-started/config.mdx#L96-L99](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L96-L99), [docs/getting-started/config.mdx#L47-L55](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L47-L55) (`clm_b349330bcd7c830e7aec3560106bd0ae829bd972a279b7bbdb33d99a7660bae0`)
- [observation/documented] In multi-agent teams, team state persists across sessions so work can be resumed, and scheduled cron agents persist across restarts and run independently of any terminal session. -- evidence: [README.md#L189-L189](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L189-L189), [README.md#L197-L197](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L197-L197) (`clm_fccf4c08bf006e90479704661f754874ea704b5f43fb901a69cd238bf991c0bf`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Shell command execution can be restricted at runtime via the CLINE_COMMAND_PERMISSIONS environment variable, a JSON policy with allow/deny glob patterns where deny overrides allow, plus an allowRedirects option defaulting to false. -- evidence: [docs/getting-started/config.mdx#L128-L128](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L128-L128), [docs/getting-started/config.mdx#L109-L117](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L109-L117), [docs/getting-started/config.mdx#L136-L142](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L136-L142), [docs/getting-started/config.mdx#L130-L132](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L130-L132), [docs/getting-started/config.mdx#L146-L148](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L146-L148) (`clm_e19b334c79f94df6bbfd1f0dccdbd94d688298ce17ac9cdeb66f5a139ce50c8b`)
- [observation/documented] Sandbox mode can be enabled via the CLINE_SANDBOX environment variable, with sandbox session storage configurable through CLINE_SANDBOX_DATA_DIR. -- evidence: [docs/getting-started/config.mdx#L109-L117](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L109-L117) (`clm_763d40f53afb4d9336220bf23ccd58ad63d9f143823ab3e6911520e75807f8d4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Cline supports multiple model providers including Anthropic, OpenAI, Google, OpenRouter (200+ models), AWS Bedrock, Azure/GCP Vertex, Cerebras/Groq, Ollama/LM Studio for local models, and any OpenAI-compatible API. -- evidence: [README.md#L154-L165](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L154-L165) (`clm_12c7b18a122f2b80a8518ffe771b0312576d9877f370f3ae54617b29c10330cd`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

