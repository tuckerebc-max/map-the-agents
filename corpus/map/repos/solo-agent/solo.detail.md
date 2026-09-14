# solo-agent/solo -- full detail

[Back to orientation](solo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/solo-agent/solo/9d58e66769ed2479c089b531705f09223d37fff3/e6a9f00ed7f2beb8.json](../../../wiki/dossiers/solo-agent/solo/9d58e66769ed2479c089b531705f09223d37fff3/e6a9f00ed7f2beb8.json)

## specifications (1 claim(s))

- [observation/documented] Solo is described as an open-source, local-first workspace for humans and AI coding agents, coordinating multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. -- evidence: [README.md#L7-L10](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L7-L10) (`clm_0b514cbb947b741ec1c797a425cf3505288d34db966a872ed76c58c3151ad3ae`)

## components (3 claim(s))

- [observation/documented] Solo runs three local layers: a Go API server on :8080 with WebSocket hub, auth, and PostgreSQL persistence; a daemon on :8081 that registers the machine and manages agent subprocesses; and the installed agent CLI driven over stdin/stdout. -- evidence: [README.md#L140-L142](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L140-L142), [README.md#L138-L138](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L138-L138) (`clm_15cf1d0db2c4cccc6a46acb0b76d7eea0f05ff41c1f47ce920fe75484f6fe990`)
- [observation/documented] Core concepts include channels, long-lived agents, Kanban tasks with states todo/in_progress/in_review/done/closed, channel-scoped teams, memory, an inbox for mentions and DMs, and reviewable artifacts. -- evidence: [README.md#L126-L134](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L126-L134) (`clm_69e89c53c4d73c4f32d2e4d9de00c0621bc0ee727d3010877336d69043771a7a`)
- [observation/documented] Solo supports remote deployment: the web app, API, PostgreSQL, attachments, and artifacts can run on a remote server while agent runtimes and credentials stay local, with one-time pairing tokens and a `solo` CLI for daemon management. -- evidence: [CHANGELOG.md#L29-L35](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/CHANGELOG.md#L29-L35) (`clm_3fb7485119e0352cb1f6ee6406d436717ccabe1e2f97fb79f4b3baefd729929e`)

## design-choices (1 claim(s))

- [observation/documented] Solo is intentionally a workspace rather than a company simulator, where agents can be mentioned, assigned, reviewed, remembered, and trusted with visible work. -- evidence: [README.md#L55-L55](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L55-L55) (`clm_670bee5f77ec370c6c4236289435da15ba5154dedf31b53a8195ad5232edaf3c`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributor rules require a complete architecture design before implementation, whole-project review of changes, and E2E validation using real frontend, API server, and PostgreSQL with no mocks for HTTP routes, services, or database behavior. -- evidence: [AGENTS.md#L3-L9](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/AGENTS.md#L3-L9) (`clm_8150547612d9e2bf75eb8866f1b671801024ceccf12cf4fc9980a43cfd3cd6ed`)
- [observation/documented] Repository development practice: agents may restart the frontend, API server, and daemon only via `make rebuild` from the repo root, and must never use launchctl, direct binaries, go run, npm run dev, nohup, or custom background commands. -- evidence: [AGENTS.md#L13-L15](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/AGENTS.md#L13-L15) (`clm_5b760d4977d82ca2ac227b16909fbb9e1341fb7b80980924261609bed3f5b9f1`)
- [observation/documented] Repository development practice: `make dev` bootstraps the project by creating .env, installing frontend dependencies, starting PostgreSQL, running migrations, and launching the app, which is then opened at http://localhost:3000. -- evidence: [README.md#L69-L69](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L69-L69), [README.md#L61-L65](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L61-L65), [README.md#L67-L67](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L67-L67) (`clm_a14beaeebf55d3dda63ff2a22a9253c1a555836c3f8768eade844eab6891d946`)
- [observation/documented] Repository development practice: the changelog reports real end-to-end test coverage for workspaces, multi-daemon execution, automations, token accounting, remote uploads, governance, wake coalescing, and runtime capability detection. -- evidence: [CHANGELOG.md#L45-L45](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/CHANGELOG.md#L45-L45), [CHANGELOG.md#L23-L23](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/CHANGELOG.md#L23-L23) (`clm_2c98d456627272e3e128f2df6d724ee230d45bbae284c9036c1f36e71276d13d`)

## skills-patterns (1 claim(s))

- [observation/documented] Agent team templates let users choose an official workflow or describe a goal to Lucy, preview roles and working relationships, and create agents scoped to one channel with post-creation tuning. -- evidence: [README.md#L88-L88](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L88-L88) (`clm_0e957804a6fde39af42bbf63f7dc13f496b87342bfb7d049e61f83cdced2bcb8`)

## interfaces (2 claim(s))

- [observation/documented] Agent backends are auto-detected from PATH at daemon startup: Claude Code via stream-json, Codex CLI via JSON-RPC, and OpenCode, Hermes, and OpenClaw via ACP. -- evidence: [README.md#L114-L120](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L114-L120), [README.md#L112-L112](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L112-L112) (`clm_1d9f9ac6866d63bc8298d126deccc1fecaa2ce7c96b9b9f2073635243c8be4b6`)
- [observation/documented] The runtime topology is Browser (Next.js :3000) to Server (Go :8080) over WebSocket, Server to Daemon over HTTP/SSE, and Daemon to Agent CLI over stdin/stdout. -- evidence: [README.md#L144-L147](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L144-L147) (`clm_529591f0951196d4ec30731b943fa0fbfc9915c5fbd0fcaba7ecc87e32c497a3`)

## memory-state (1 claim(s))

- [observation/documented] Agents keep agent-specific MEMORY.md context that is loaded into future sessions, and the comparison table says agents retain long-term memory, their own environment, and a fixed workspace. -- evidence: [README.md#L126-L134](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L126-L134), [README.md#L45-L45](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L45-L45) (`clm_362ac9079c62f9f7df5383f7988b6472e0f438c10aa6f0bfa2870bb41dce21ff`)

## orchestration (1 claim(s))

- [observation/documented] The changelog documents deterministic agent wake-up routing with idempotency, acknowledgements, durable offline recovery, send-time freshness checks, and wake coalescing for busy agents while preserving distinct messages. -- evidence: [CHANGELOG.md#L7-L12](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/CHANGELOG.md#L7-L12), [CHANGELOG.md#L29-L35](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/CHANGELOG.md#L29-L35) (`clm_db18ff26dbe334f9fd3cdb06e19553e9325018cf2c89471aef795a9702b2cad7`)

## tools-permissions (1 claim(s))

- [observation/documented] Each agent can override system_prompt, model_name, custom_env, and custom_args, and agents are described as having roles and tool access. -- evidence: [README.md#L122-L122](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L122-L122), [README.md#L126-L134](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L126-L134) (`clm_83f03932f1c26383f2cd62a57e6b019e7a3ba2c6c83f56b1d781a1518a84318e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running Solo requires Go 1.25+, Node.js 20+, npm, Docker, and at least one supported agent CLI on PATH; README badges also display Go 1.22+ and Node 20+. -- evidence: [README.md#L59-L59](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L59-L59), [README.md#L16-L20](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L16-L20) (`clm_74bd9c399e6905f97facddea1770f4494115d76e1207fb9a91e0e7a413f7c395`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

