# zykjshadow/async -- full detail

[Back to orientation](async.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zykjshadow/async/2c18a43c0711d1f991a6eabd913831f9c82794b0/b8601518a228cb3a.json](../../../wiki/dossiers/zykjshadow/async/2c18a43c0711d1f991a6eabd913831f9c82794b0/b8601518a228cb3a.json)

## specifications (1 claim(s))

- [observation/documented] Async IDE is an open-source, agent-first desktop workspace combining Agent, editor, Git, and terminal, licensed Apache 2.0, local-first with BYOK model access. -- evidence: [README.md#L290-L290](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L290-L290), [README.md#L33-L33](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L33-L33), [README.md#L7-L10](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L7-L10) (`clm_d8727f401d90c41b4239a85badb49140e61e0990e207e57a8f1b920e14dc0719`)

## components (1 claim(s))

- [observation/documented] The main process contains agentLoop.ts (multi-round tool calls, partial JSON streaming, tool repair, aborts), toolExecutor, LLM adapters, gitService, threadStore, settingsStore, LSP session, and PTY terminal. -- evidence: [README.md#L142-L155](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L142-L155), [README.md#L182-L224](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L182-L224), [README.md#L173-L178](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L173-L178) (`clm_25dedae062db33f48b086cf033d401372ff7b4b961011193e3ff2d92757f434b`)

## design-choices (1 claim(s))

- [observation/documented] The app is built from scratch on Electron + React + Monaco and is explicitly not a VS Code fork, with a deliberately lean two-process architecture and clear IPC boundaries. -- evidence: [README.md#L29-L29](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L29-L29), [README.md#L173-L178](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L173-L178) (`clm_3bd926cec47597347e1d73170fc26ff710f62d56582fc9e0d1bdee8f8c075a1c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: docs/llm-wiki is a structured knowledge layer for humans and agents, with maintenance conventions like link-first navigation, code-over-docs conflict resolution, and recording contradictions in a dedicated page. -- evidence: [docs/llm-wiki/README.md#L3-L5](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/README.md#L3-L5), [docs/README.md#L5-L6](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/README.md#L5-L6), [docs/llm-wiki/README.md#L9-L13](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/README.md#L9-L13), [docs/llm-wiki/README.md#L103-L105](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/README.md#L103-L105) (`clm_9b85594aa89880b575f21ae443e041f6af248061e6ed4ea2d0172aced96ee736`)
- [observation/documented] Repository development practice: the repo can be run with npm install then npm run desktop, with dev, dev:debug, and icons scripts; the macOS test guide documents building unsigned packages via npm run release:mac:unsigned. -- evidence: [README.md#L248-L253](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L248-L253), [docs/mac-mini-auto-update-test.md#L99-L102](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/mac-mini-auto-update-test.md#L99-L102), [README.md#L266-L270](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L266-L270) (`clm_151fecd3080948373995600bdc6cb29b510fa7a749b800a779195f456ede6f6d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Composer offers four modes: Agent (full auto), Plan (review before run), Ask (read-only Q&A), and Debug (systematic troubleshooting). -- evidence: [README.md#L39-L46](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L39-L46), [docs/llm-wiki/project-overview.md#L22-L25](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/project-overview.md#L22-L25) (`clm_1192ffa2a0b37a5f49036b982808435da98179b1ba564a4060a730681bc54fd9`)
- [observation/documented] The app bridges to Telegram, Slack, Discord, and Feishu bots; inbound messages run through botRuntime, reusing the same agentLoop and teamOrchestrator paths as the desktop Composer, with per-integration model, workspace, and allowlist config. -- evidence: [README.md#L129-L134](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L129-L134) (`clm_1dcdc63e0b306bc32504e6487a26dff5b33cb09c14ff7288268066fa044792ef`)

## memory-state (1 claim(s))

- [observation/documented] Threads, settings, and plans persist locally as JSON/Markdown under Electron userData (threads.json, settings.json, .async/plans/); threads.json is the authoritative conversation source. -- evidence: [README.md#L230-L232](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L230-L232), [README.md#L234-L234](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L234-L234), [README.md#L228-L228](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L228-L228), [README.md#L173-L178](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L173-L178) (`clm_6955a29490e77e71088d227e93fe5d0786620084183b10016f28d4c783a84cc6`)

## orchestration (1 claim(s))

- [observation/documented] Team mode provides multi-agent collaboration with a Lead planning, specialist execution, reviewer verification, and plan-approval workflows; nested and background sub-agents are supported. -- evidence: [README.md#L39-L46](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L39-L46), [docs/llm-wiki/project-overview.md#L22-L25](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/project-overview.md#L22-L25), [README.md#L105-L109](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L105-L109) (`clm_45fcb1e2be6be76bde1a434255bf5684a9000faa50e24bd3d425e63561ac18d0`)

## tools-permissions (1 claim(s))

- [observation/documented] Sensitive operations such as shell commands and file writes pass through approval gates, and the renderer's access to main-process capabilities is bounded by a preload whitelist. -- evidence: [README.md#L39-L46](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L39-L46), [README.md#L105-L109](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L105-L109), [docs/llm-wiki/project-overview.md#L50-L52](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/project-overview.md#L50-L52) (`clm_da09fcdeff3423c53e946475022543cc61c9be01abc1ef595ad4091e7dc83b33`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tech stack includes Electron 41, React 19, TypeScript 5.9, Monaco 0.52, xterm.js, OpenAI/Anthropic/Gemini SDKs, MCP SDK, and node-pty. -- evidence: [README.md#L159-L171](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L159-L171) (`clm_e507b5c7998c2f0f364ad1da2f9472da73c332808025439167c2af55d341a5ed`)

## limitations (1 claim(s))

- [observation/documented] The macOS build is unsigned, so electron-updater cannot auto-install updates; the app instead downloads the ZIP to ~/Downloads and prompts manual installation, while Windows builds auto-install. -- evidence: [docs/mac-mini-auto-update-test.md#L7-L10](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/mac-mini-auto-update-test.md#L7-L10), [docs/mac-mini-auto-update-test.md#L247-L251](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/mac-mini-auto-update-test.md#L247-L251) (`clm_d6d93e4f6ef214281b5521151b52e4b76f813957151e99a791a8c7898c698ea6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

