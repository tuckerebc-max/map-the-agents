# dyad-sh/dyad -- full detail

[Back to orientation](dyad.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dyad-sh/dyad/0c8403662504264f911242504fc2d2b07895c6ad/73f45ce23df314b3.json](../../../wiki/dossiers/dyad-sh/dyad/0c8403662504264f911242504fc2d2b07895c6ad/73f45ce23df314b3.json)

## specifications (2 claim(s))

- [observation/documented] Dyad is a local, open-source AI app builder where users describe an app in plain language and the AI generates code with a live preview on their machine, with local-first operation as the core differentiator. -- evidence: [PRODUCT.md#L13-L13](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/PRODUCT.md#L13-L13), [README.md#L3-L3](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/README.md#L3-L3) (`clm_e82e778498dbe870ef3a7075d7f2118b79cbc920ccc1990e88bb611d4908286a`)
- [observation/documented] The primary users are non-technical builders with no coding background running Dyad locally on Mac or Windows; a secondary audience brings their own API keys and local models. -- evidence: [PRODUCT.md#L9-L9](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/PRODUCT.md#L9-L9) (`clm_9229067de4508db47853798c2b748aa1d4e0659b732b217895fe52767ae25398`)

## components (2 claim(s))

- [observation/documented] Dyad is an Electron app with a React renderer process (sandboxed) and a privileged Node.js main process that accesses the filesystem, communicating via IPC. -- evidence: [docs/architecture.md#L11-L11](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L11-L11), [docs/architecture.md#L7-L7](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L7-L7) (`clm_b09bc830f2a70cc6465620b593cf964c2e0fa59edf489ad8e23e7a38504202b2`)
- [observation/documented] The local agent's core loop lives in src/pro/main/ipc/handlers/local_agent/local_agent_handler.ts, calling the LLM until it stops making tool calls or hits a per-turn maximum step count; tool_definitions.ts lists the agent's tools. -- evidence: [docs/agent_architecture.md#L5-L6](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L5-L6) (`clm_5d803da96a1b00b2cc5d01f83b6d3de993dcd7a20a2b91c6d1d3877eda713fea`)

## design-choices (3 claim(s))

- [observation/documented] Dyad historically simulated tool calling with custom XML-like tags instead of models' formal tool calling, citing the ability to batch many calls and evidence that JSON code output hurts quality; a newer agent architecture moves toward standard tool calling. -- evidence: [docs/agent_architecture.md#L3-L3](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L3-L3), [docs/architecture.md#L27-L27](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L27-L27), [docs/architecture.md#L31-L32](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L31-L32) (`clm_6c09f7f3268f9571d5ef067bd4b16aa0b7d99a7dda9b97b0f7b95ea7a8bde254`)
- [observation/documented] By default each LLM request includes the entire codebase plus a system prompt instructing XML-like responses; Smart Context uses smaller models to filter important files, and agentic iterative search is avoided mainly for cost reasons. -- evidence: [docs/architecture.md#L50-L50](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L50-L50), [docs/architecture.md#L17-L19](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L17-L19), [docs/architecture.md#L52-L52](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L52-L52) (`clm_4c65b4db85feb487fadaf1cf896b9e78c5694531131908bb1ee4bfa6eec7913f`)
- [observation/documented] Dyad deliberately keeps a simple agentic loop—usually a single AI request, with optional auto-fix of TypeScript compiler errors—to keep costs low compared to more agentic tools. -- evidence: [docs/architecture.md#L40-L40](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L40-L40), [docs/architecture.md#L42-L42](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L42-L42) (`clm_b0e4cd46aefc75a2605ffd866daf5a42f1aa0da8abfd4652d0eddd991cae5599`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors add tools in the local_agent/tools directory, register them in tool_definitions.ts, render their XML tag in DyadMarkdownParser.tsx, and can add E2E tests modeled on e2e-tests/local_agent*.spec.ts with tool-call fixtures. -- evidence: [docs/agent_architecture.md#L20-L20](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L20-L20), [docs/agent_architecture.md#L14-L14](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L14-L14), [docs/agent_architecture.md#L12-L12](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L12-L12), [docs/agent_architecture.md#L18-L18](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L18-L18), [docs/agent_architecture.md#L10-L10](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L10-L10) (`clm_276f6a53f22536c65aa73f2270fdabd2966b5b977fa02760bb63035850c9bbeb`)
- [observation/documented] Repository development practice: English locale files are the source of truth, other locales must mirror their key structure with automatic English fallback, and a CI check warns on missing keys; contributions fall under a CLA granting Dyad Tech, Inc. copyright and patent licenses. -- evidence: [CLA.md#L21-L21](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/CLA.md#L21-L21), [docs/i18n.md#L396-L396](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L396-L396), [docs/i18n.md#L391-L392](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L391-L392), [CLA.md#L40-L40](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/CLA.md#L40-L40) (`clm_97b65571e0a43b62007d14db24bf4efe2de8432d59c674d4fd10addef21a9a36`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The LLM responds with <dyad-*> tags (e.g. <dyad-write path=...>) that a specialized Markdown parser renders in the UI, and a response processor in the main process applies after user approval—writing or deleting files, adding NPM packages, etc. -- evidence: [docs/architecture.md#L17-L19](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L17-L19), [docs/architecture.md#L21-L21](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L21-L21) (`clm_7a4359e0ce5debf9d1744e4fa427e19066036f4b785f2750d248c7595fe1f42c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product includes agent built-in tool permission settings with per-tool options: Ask, Always allow, and Never allow. -- evidence: [docs/i18n.md#L69-L94](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L69-L94) (`clm_9b3c91818d60f5530bbde12d7e4b1ad5c8a88965c585a1bc5edbd93204c5e575`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The i18n design specifies react-i18next and i18next (installed via npm) for translations with bundled locale JSON and no HTTP backend, and notes date-fns as an existing dependency for locale-aware date formatting. -- evidence: [docs/i18n.md#L350-L350](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L350-L350), [docs/i18n.md#L26-L26](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L26-L26), [docs/i18n.md#L22-L24](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L22-L24), [docs/i18n.md#L9-L9](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L9-L9) (`clm_fdcfbd7d59c5b1635f2773858dceaf4b5e18246abde4a3e1d7adf1f499c4986b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

