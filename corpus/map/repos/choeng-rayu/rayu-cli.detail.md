# choeng-rayu/rayu-cli -- full detail

[Back to orientation](rayu-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/choeng-rayu/rayu-cli/c16466f3b068732e0be23698155c00a97cccf41c/f8841530529d555b.json](../../../wiki/dossiers/choeng-rayu/rayu-cli/c16466f3b068732e0be23698155c00a97cccf41c/f8841530529d555b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is a monorepo of four services plus a deploy stack: a TypeScript/Bun/Ink CLI, a NestJS/Prisma/MySQL accounts API, a Go/chi/Redis AI gateway, and a Next.js 15 website, with Docker Compose + Caddy for deployment. -- evidence: [README.md#L112-L112](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L112-L112), [README.md#L114-L120](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L114-L120) (`clm_8ff4f6c20b31733d436aa12c83dc90103433908a649aef0e9ece4cc53bf3d866`)

## design-choices (1 claim(s))

- [observation/documented] The README claims a custom React/Ink terminal renderer with zero-GC cell buffers and a Go gateway with sub-millisecond routing overhead, with time-to-first-token under 500ms for cached sessions. -- evidence: [README.md#L57-L59](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L57-L59) (`clm_6903522209cb84f5619861bd8e8cf7862cac297085674097993e482b78f616d3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are directed to a Contributing Guide covering issues, code formatting, and pull requests, and the project adopts a Contributor Covenant 2.1 code of conduct with a correction/warning/ban enforcement ladder and GitHub-based reporting. -- evidence: [CODE_OF_CONDUCT.md#L57-L58](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L57-L58), [CODE_OF_CONDUCT.md#L78-L78](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L78-L78), [CODE_OF_CONDUCT.md#L72-L72](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L72-L72), [README.md#L137-L137](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L137-L137), [CODE_OF_CONDUCT.md#L90-L90](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L90-L90), [CODE_OF_CONDUCT.md#L100-L100](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L100-L100), [CODE_OF_CONDUCT.md#L84-L84](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L84-L84), [CODE_OF_CONDUCT.md#L96-L96](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L96-L96) (`clm_2607a16fbd2b6bdcbc7671aedbb0a916f93d572735438875cea79b4e78616ef1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI is distributed as the npm package @rayu-dev/rayu-cli, installable globally via npm, runnable via npx, or via curl/PowerShell install scripts that the README says require no Node, npm, or sudo. -- evidence: [README.md#L80-L81](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L80-L81), [README.md#L102-L104](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L102-L104), [README.md#L7-L11](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L7-L11), [README.md#L96-L98](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L96-L98), [README.md#L85-L86](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L85-L86), [README.md#L76-L76](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L76-L76) (`clm_1b2915ca7f513bb5c07da25cf265a93ad9a4b2ab5f9675ad0eab07dc8c4c5d55`)
- [observation/documented] The CLI exposes slash commands including /model for mid-session model switching, /connect for provider setup, /sessions and /switch for Telegram bridge sessions, and /banner, /mascot, /brandmark for branding display. -- evidence: [CHANGELOG.md#L67-L74](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L67-L74), [README.md#L70-L70](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L70-L70), [README.md#L106-L106](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L106-L106), [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20), [CHANGELOG.md#L142-L144](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L142-L144) (`clm_96c3735dbe748530c1d6eff3cad51502356ee5f541fe68705d84f0a6136c4823`)
- [observation/documented] The CLI includes a Telegram bridge for remote access with multi-session support, health monitoring showing connected/reconnecting/disconnected states, and a remote uninstall gated by local opt-in, device targeting, and single-use confirmation tokens. -- evidence: [CHANGELOG.md#L26-L27](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L26-L27), [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20) (`clm_4cd34d5551947c70c023e60edaea599eaf455d047999ce9b7367700f5b8de850`)

## memory-state (1 claim(s))

- [observation/documented] The changelog describes a secure IPC layer using a Unix socket protocol with per-session token auth, enabling cross-session routing and multi-session coordination. -- evidence: [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20) (`clm_61492d9f3e9f75f75f39469e3f7c26a8b584acb6e188c5e64006f166e0d1f833`)

## orchestration (2 claim(s))

- [observation/documented] The changelog documents an External Agent Orchestrator with an /agent command and ExternalAgent tool to launch and coordinate other agentic CLIs (Codex, Claude Code, OpenCode, ACP agents), with parallel/sequential/race/retry/fallback policies, git worktree isolation, and crash recovery. -- evidence: [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20) (`clm_633cb0ad6019c0e33f7cf664d07e08be157d85ae54a5e8155c60e3dbddb9b37d`)
- [observation/documented] The changelog describes a planner subagent dispatching parallel Explore subagents, a collaborator swarm with persistent agent memory syncing, and /ultraplan and /ultrareview commands that run parallel planning/review subagents on the user's own provider. -- evidence: [CHANGELOG.md#L133-L136](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L133-L136), [CHANGELOG.md#L174-L180](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L174-L180) (`clm_cb8f0051563e620716136601473d9fcac79d6dacb92ec17441b849c7fe9db806`)

## tools-permissions (1 claim(s))

- [observation/documented] The changelog references product permission modes, including a fix to the Ask User Question tool in 'full manage (full-control) permission mode' and brokered permissions in the external agent orchestrator. -- evidence: [CHANGELOG.md#L35-L35](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L35-L35), [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20) (`clm_b7a2d291f0141e3c5eb708aa713843124630d8401b7073f3b9f7e0bc140cb83d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README lists supported LLM providers including Anthropic, OpenAI, DeepSeek, Google Gemini, Kimi, and locally hosted models via Ollama/LM Studio, connectable via BYOK API keys or a Rayu-hosted connection. -- evidence: [README.md#L70-L70](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L70-L70), [README.md#L106-L106](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L106-L106), [README.md#L65-L67](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L65-L67) (`clm_75bf046c7638b7cf34ed5f7d79e5b33f5afd868ca1d92c96264fe00845082c80`)

## limitations (1 claim(s))

- [inference/documented] The README's performance and competitor-comparison claims (sub-500ms responses, superiority over other CLI agents) appear to be marketing assertions without cited benchmarks in the provided evidence, so they should be treated as unverified. -- evidence: [README.md#L37-L37](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L37-L37), [README.md#L43-L50](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L43-L50), [README.md#L57-L59](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L57-L59) (`clm_ab618ed4391846bd3f2388ee3744be8b970961ab16d4dbf268663014e9afaf2f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

