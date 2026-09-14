# mng-dev-ai/agentrove -- full detail

[Back to orientation](agentrove.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mng-dev-ai/agentrove/53ef8fc0dea3a29005d341ad1031014aa07e56b8/7ceeacd8ec0fc1b5.json](../../../wiki/dossiers/mng-dev-ai/agentrove/53ef8fc0dea3a29005d341ad1031014aa07e56b8/7ceeacd8ec0fc1b5.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Agents are run through ACP adapters, and each workspace gets its own Docker or host sandbox. -- evidence: [README.md#L14-L22](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L14-L22) (`clm_3e8ff4c49e097a084ac2dd6c255fdebdac747699473276d5520e622be0657cf8`)
- [observation/documented] The stack is React 19, TypeScript, Vite, Tailwind, Monaco, and xterm.js on the frontend; FastAPI, SQLAlchemy, SQLite, and Redis on the backend; ACP with Docker or host sandboxes at runtime. -- evidence: [README.md#L158-L160](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L158-L160) (`clm_08fb405b72b2c0bb16a3104a6e87a82a3a492af034239a62dfddca91a2d4ebba`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building the iOS app from source requires macOS with Xcode, Rust iOS targets via rustup, and CocoaPods; a helper script (npm run ios:install) builds, signs, exports, and installs using APPLE_DEVELOPMENT_TEAM. -- evidence: [README.md#L118-L121](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L118-L121), [README.md#L123-L127](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L123-L127), [README.md#L88-L89](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L88-L89) (`clm_5671a3f6ef07539da294b8bf459da43366c346462e0b584465486c03275d2679`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Agentrove is a self-hosted AI coding workspace that runs and orchestrates Antigravity, Claude Code, Codex, Copilot, Cursor, Grok, and OpenCode agents from one interface. -- evidence: [README.md#L3-L3](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L3-L3) (`clm_9ff72cbbd858ddf1a4252b7188d80a8108325f7741d8a8928bbd7bbba5615ad5`)
- [observation/documented] The workspace combines chat, code editor, terminal, file tree, diffs, secrets, and git tools, and streams agent sessions with cancellation, permission prompts, queued follow-ups, file mentions, slash commands, and attachments. -- evidence: [README.md#L14-L22](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L14-L22) (`clm_35d36aec574f8d37576229b63f62e777349d4ae371fb4c05366f06739cc1aabd`)
- [observation/documented] Ships as a Docker web app, a macOS desktop app built with Tauri (bundled Python backend sidecar on a local port), and a native iOS thin client that talks to an already-hosted instance over https/wss. -- evidence: [README.md#L82-L86](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L82-L86), [README.md#L69-L69](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L69-L69), [README.md#L14-L22](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L14-L22) (`clm_0acec8cdfb88ff976cc741d744f39dba0536401929f99dd575c56dfe8042c604`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (4 claim(s))

- [observation/documented] A bundled MCP server exposes the instance as tools such as send_message, get_messages, list_models, and list_personas, letting any chat's agent act as an orchestrator that decomposes work and reviews results. -- evidence: [README.md#L26-L26](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L26-L26) (`clm_f3bc6146ff4637351677567c2cf95d90e80fe989ee9cdcba1f2635bab51e3d11`)
- [observation/documented] Sub-threads created via send_message(parent_chat_id=...) are worker chats grouped under the lead in the same workspace and branch, and stay flat with no nesting. -- evidence: [README.md#L30-L34](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L30-L34) (`clm_2acbee0e8a939871a5c82c573cfeab37ea6a3aa1331b464966774c28c80ad3eb`)
- [observation/documented] Workers can run on any installed agent, model, and persona; worktree=true gives a worker its own git worktree so parallel workers edit concurrently without conflicts. -- evidence: [README.md#L30-L34](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L30-L34) (`clm_4a1120b3227eba79da191c605a69e8f2f334eb309fd540e8d64e98c65a5329b2`)
- [observation/documented] The lead polls get_messages until a worker's turn completes, judges results against the code, and sends rework to the worker's thread; follow-ups inherit prior model, persona, and reasoning settings. -- evidence: [README.md#L30-L34](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L30-L34) (`clm_c77b49d113a6933f2730bc3722886aec4c4fa81fea79a2bc3125442267fa16e6`)

## tools-permissions (1 claim(s))

- [observation/documented] Orchestrated turns run in the agent's full-execution mode, so workers finish without permission prompts. -- evidence: [README.md#L30-L34](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L30-L34) (`clm_1dfbfe277a7c842f13110017175d273c64fe52071a8f9a42946d4a6a39c6e9cb`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Quick start requires Docker and Docker Compose, cloning the repo, copying .env.example to .env, and setting SECRET_KEY before docker compose up -d; the app is served at localhost:3000. -- evidence: [README.md#L51-L51](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L51-L51), [README.md#L45-L49](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L45-L49), [README.md#L59-L61](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L59-L61), [README.md#L63-L63](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L63-L63), [README.md#L42-L43](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L42-L43) (`clm_f5df732c136864cdf27d5792aff39630d5e6a1ba46458ccf8b5900c872f874cd`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

