# qwenlm/qwen-code -- full detail

[Back to orientation](qwen-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/qwenlm/qwen-code/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/0429dc14353565eb.json](../../../wiki/dossiers/qwenlm/qwen-code/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/0429dc14353565eb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Key monorepo packages: `packages/cli` (executable, arg parsing, Ink TUI, headless output, ACP entry, `qwen serve`), `packages/core` (agent orchestration, tools, permissions, sessions, memory), and `packages/acp-bridge` (ACP channel lifecycle, session multiplexing, permission mediation). -- evidence: [docs/developers/architecture.md#L80-L95](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L80-L95) (`clm_ba678e712368f880bc4037da02af772d1e5c5aab114626cc48b30580e2e968fd`)

## design-choices (3 claim(s))

- [observation/documented] The core runtime owns the agent loop — model requests, conversation context, tool dispatch, permission policy — while display and transport decisions are deliberately kept in the CLI, bridge, SDK, and UI layers. -- evidence: [docs/developers/architecture.md#L127-L129](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L127-L129), [docs/developers/architecture.md#L120-L125](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L120-L125) (`clm_39be8499f6049f7de9d74a1031bfb54c3919074de076ba21029a6c507251d9ff`)
- [observation/documented] In daemon mode with multi-workspace sessions, each live workspace runtime owns its own bridge and `qwen --acp` child, with filesystem access, environment overlays, MCP transports, and sessions scoped to that runtime. -- evidence: [docs/developers/architecture.md#L185-L189](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L185-L189) (`clm_08d2e35bb045bb91e815fa67d94fae91be0691738d13f973553a59e88ddd6232`)
- [observation/documented] A daemon side-channel coordination design doc specifies that in-session model changes are demuxed from `extNotification()` while approval-mode changes use the ACP `current_mode_update` sessionUpdate, since no `current_model_update` ACP type exists. -- evidence: [docs/design/daemon-sidechannel-coordination/design.md#L56-L59](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/design/daemon-sidechannel-coordination/design.md#L56-L59), [docs/design/daemon-sidechannel-coordination/design.md#L115-L118](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/design/daemon-sidechannel-coordination/design.md#L115-L118), [docs/design/daemon-sidechannel-coordination/design.md#L157-L157](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/design/daemon-sidechannel-coordination/design.md#L157-L157) (`clm_99f38ef03d95427a3ef5cbefaf52bf96b869e3dbe35dea01b1159a008c70eab8`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are directed to CONTRIBUTING.md for guidelines. -- evidence: [README.md#L206-L206](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L206-L206) (`clm_110a3814d4d12db7b301a02be5711930193930f1730ac15a4b35f6e90ddcae23`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product offers multiple invocation surfaces: an interactive `qwen` TUI started in a project directory, headless `qwen -p "..."` for scripts/CI, and an experimental `qwen serve` daemon exposing HTTP + SSE (ACP). -- evidence: [README.md#L71-L74](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L71-L74), [docs/developers/architecture.md#L17-L21](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L17-L21), [README.md#L105-L107](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L105-L107) (`clm_254bea1c00a829fc129a389f13de362f4c10ee854fbfdd18b64958c24034b408`)
- [observation/documented] SDKs exist for TypeScript, Python, and Java; the Python SDK exposes an async `query()` taking a cwd and path to the qwen executable, streaming messages from which result messages are printed. -- evidence: [README.md#L118-L125](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L118-L125), [README.md#L127-L129](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L127-L129), [README.md#L115-L115](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L115-L115), [README.md#L105-L107](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L105-L107) (`clm_ea38d7ebb4fdafa5771e94f673c8eb20e4362289e183ac1bb1dd18d6796e71de`)
- [observation/documented] The agent supports multiple model protocols — OpenAI, Anthropic, Gemini, and Qwen APIs — plus third-party or local providers (Ollama/vLLM), switchable at runtime. -- evidence: [README.md#L26-L29](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L26-L29) (`clm_8e0cb7db4b61a63442af47fb149dede015d4c3bfecf21cc08189cabeb5a57040`)
- [observation/documented] Inside a session, `/auth` configures the provider and API key; the CLI is started by running `qwen` in a project directory. -- evidence: [README.md#L71-L74](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L71-L74), [README.md#L76-L76](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L76-L76) (`clm_5e578832269ca9d7a4f80cefa8da12ade2d771e104b97f986b1ab9a323cbda68`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports a SWE-bench Verified evaluation (500 cases, 3 trials per version, model Qwen 3.7 Max) with average scores between roughly 76.4% and 77.8% across seven Qwen Code versions. -- evidence: [README.md#L162-L170](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L162-L170), [README.md#L174-L182](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L174-L182) (`clm_cda91ac3d6e68c0fe48d71a3c99e331cf3416a0f6c067eb357cdfd29248ae0c2`)

## dependencies (1 claim(s))

- [observation/documented] NPM installation requires Node.js 22+; the project was originally based on Google Gemini CLI v0.8.2 but stopped syncing upstream starting from Qwen Code v0.1. -- evidence: [README.md#L53-L53](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L53-L53), [README.md#L3-L6](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L3-L6), [README.md#L210-L210](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L210-L210) (`clm_087625134d58de08f29b7d6db36d59d42238b63c6209f66d7963572e6ca75ff6`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Qwen Code is positioned as an open-source AI coding agent for terminal, editor, desktop, browser, and chat, aiming for feature parity with Claude Code plus multi-protocol and daemon-mode extras. -- evidence: [README.md#L141-L156](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L141-L156), [README.md#L10-L10](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L10-L10), [README.md#L139-L139](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L139-L139) (`clm_d93e84acb57184c6b602b37a0466ed377676b55cf30dc20766760a81754e90d4`)

