# limecloud/lime -- full detail

[Back to orientation](lime.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/limecloud/lime/580022b574cb23acc3c44614566ed05ffb4f6180/abaebea4bce76cc8.json](../../../wiki/dossiers/limecloud/lime/580022b574cb23acc3c44614566ed05ffb4f6180/abaebea4bce76cc8.json)

## specifications (1 claim(s))

- [observation/documented] Lime is described as an open-source full-stack desktop AI agent for coding, files, terminals, tools, research, content, multimodal work, and multi-agent workflows. -- evidence: [README.md#L9-L9](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L9-L9), [README.md#L11-L11](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L11-L11), [README.md#L49-L49](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L49-L49) (`clm_e1c9520a081f1d62730db7ac860de41d7c1ea4e1887527aaa249c03372da5a53`)

## components (2 claim(s))

- [observation/documented] The stack comprises an Electron desktop shell, a Rust App Server speaking JSON-RPC, a React/TypeScript/Vite frontend, and local capabilities including filesystem, processes, workspaces, artifacts, and persisted state. -- evidence: [README.md#L173-L178](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L173-L178), [README.en.md#L175-L180](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.en.md#L175-L180) (`clm_45e1eafa3e3523020f2b42abd0adb12eb2d061372202ed0910b9c9dfd61d5a51`)
- [observation/documented] FEATURE-MAP assigns ownership across crates: agent-runtime/agent for turn lifecycle and orchestration, model-provider for catalog/routing/retry, and tool-runtime for tool definitions, permissions, sandbox, dispatch, processes and MCP; the main-chain diagram lists thread-store/repository for persistence and projection. -- evidence: [FEATURE-MAP.md#L76-L84](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L76-L84), [FEATURE-MAP.md#L24-L33](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L24-L33) (`clm_5a540c3290e1bd6954b0a094e070993e17536264b22f78f2b71e9b3608ef4c9d`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: minimal documentation checks are `npm run docs:boundary`, relative-link validation, and `git diff --check`, with `npm run governance:legacy-report` added when governance categories change. -- evidence: [FEATURE-MAP.md#L101-L106](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L101-L106) (`clm_4b77d48813e64244206c481d888475847d7b5130b866fd7c5fa9ba36891006f1`)
- [observation/documented] Repository development practice: FEATURE-MAP maintenance rules require updating code and the architecture doc first, then syncing the map after owner confirmation, and readiness is judged by code, protocol, and corresponding evidence levels rather than roadmap claims or single test results. -- evidence: [FEATURE-MAP.md#L101-L106](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L101-L106), [FEATURE-MAP.md#L17-L20](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L17-L20) (`clm_8d04121bcac26cde224365e9233ca72c37ffa60e7e9ebdac20347af6a2c36cc5`)

## skills-patterns (1 claim(s))

- [observation/documented] Recurring procedures can be encoded as Skills that the agent discovers and runs through MCP or controlled capabilities instead of repeating instructions in every prompt. -- evidence: [README.md#L95-L95](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L95-L95) (`clm_279a5804c7833f721acff616e8d7be6d4de39fd8158bb008f11b4b6385aa236b`)

## interfaces (1 claim(s))

- [observation/documented] Desktop GUI business capabilities enter the Rust runtime only through App Server JSON-RPC; Electron IPC is limited to windows, file selection, system permissions, notifications, updates, native views, and sidecar lifecycle. -- evidence: [FEATURE-MAP.md#L46-L46](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L46-L46) (`clm_32790b7ead9a4948841858e4a3aa090513de616cf7c825c12f7e994a99e8dde0`)

## memory-state (1 claim(s))

- [observation/documented] Work is projected as Thread, Turn, Item, and reusable artifacts so tasks can be paused, reviewed, restored, and continued; project materials, conversation history, and configuration are kept locally by default. -- evidence: [README.md#L194-L194](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L194-L194), [README.md#L55-L58](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L55-L58) (`clm_e2afe9e63891272fa23b5b474f6eb0d30ce488b14f6c70dbb26d94d89b34d243`)

## orchestration (1 claim(s))

- [observation/documented] Multi-agent collaboration lets users delegate research, implementation, testing, and documentation to different agents while the main Thread keeps shared context, permissions, and review boundaries. -- evidence: [README.md#L99-L99](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L99-L99) (`clm_39d1d62bd3871c69e00cf9a2fb9d62b6bb92a23ff39b6f9a27c46aad1145182f`)

## tools-permissions (1 claim(s))

- [observation/documented] Within permissions the user grants, the agent can read and edit files, run terminal commands and tests, and call tools, with high-risk actions requiring review or approval. -- evidence: [README.md#L190-L190](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L190-L190), [README.md#L163-L167](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L163-L167) (`clm_6ccd9e3ef46b0cd441776719f50bc33356d2ad4ff9d792e66f5a9c08ad7d9b2c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Lime does not ship AI models itself; users must configure a provider, model, and credential, and model capabilities come from third-party AI service providers configured by the user. -- evidence: [README.md#L214-L214](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L214-L214), [README.md#L186-L186](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L186-L186) (`clm_1e16cdb2004756b9c25df182aa71559c097d5b3bd48925b4ecd1153aba3bf84f`)

## limitations (2 claim(s))

- [observation/documented] Only macOS and Windows builds are published; Linux desktop builds are paused, and the Windows installer may trigger SmartScreen because it is unsigned or lacks signing reputation. -- evidence: [README.md#L149-L152](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L149-L152) (`clm_7822e03f0fe0aa2203eb976f3345e6a83e938a7843ba3c156638ed4724ee9d6a`)
- [observation/documented] The project is provided for learning and research purposes only, with users responsible for their own use and risk. -- evidence: [README.md#L212-L212](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L212-L212) (`clm_4d05830e36ac252827a2ddad612dbe7c65ce80e3ccb614cda60eedceb2013a61`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

