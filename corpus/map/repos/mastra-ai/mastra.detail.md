# mastra-ai/mastra -- full detail

[Back to orientation](mastra.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mastra-ai/mastra/f04f724c6c587463424232e777266fdcc316f3f6/4a191eb4e779b79d.json](../../../wiki/dossiers/mastra-ai/mastra/f04f724c6c587463424232e777266fdcc316f3f6/4a191eb4e779b79d.json)

## specifications (1 claim(s))

- [observation/documented] Mastra is documented as a TypeScript framework for building AI-powered applications and agents, integrating with React, Next.js, and Node or deployable as a standalone server. -- evidence: [README.md#L11-L11](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L11-L11), [README.md#L13-L13](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L13-L13) (`clm_31ae4f4ee582f19c2969e09354956672374ac89757f93b34ea3874edb15ebb16`)

## components (1 claim(s))

- [observation/documented] Documented capabilities include model routing to 40+ providers, autonomous agents, a graph-based workflow engine, human-in-the-loop suspend/resume, memory and RAG context management, MCP server authoring, and built-in evals and observability. -- evidence: [README.md#L23-L23](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L23-L23), [README.md#L21-L21](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L21-L21), [README.md#L35-L35](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L35-L35), [README.md#L33-L33](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L33-L33), [README.md#L27-L27](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L27-L27), [README.md#L29-L29](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L29-L29), [README.md#L25-L25](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L25-L25) (`clm_70715d4cfe85ab6d7d28475a9780ac4309b0076106819a9dae7a3d01b863f44a`)

## design-choices (1 claim(s))

- [observation/documented] The repository uses dual licensing: Apache-2.0 for most code, while any directory named ee/ (e.g., packages/core/src/auth/ee/) falls under the Mastra Enterprise License, free for development/testing but requiring a license for production use. -- evidence: [README.md#L100-L101](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L100-L101), [README.md#L98-L98](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L98-L98) (`clm_6e902f92e265f05afa8d442deda91b061daead240772a952e530bcfee6a498fe`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: contributors need Node.js v22.13.0+, pnpm v10.18.0+ (enabled via corepack), and optionally Docker for a subset of tests; setup uses pnpm run setup to install dependencies and build the CLI package. -- evidence: [DEVELOPMENT.md#L7-L9](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L7-L9), [DEVELOPMENT.md#L22-L22](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L22-L22), [DEVELOPMENT.md#L30-L32](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L30-L32), [DEVELOPMENT.md#L34-L34](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L34-L34) (`clm_93816dff1c7a4a0dad4c9622f94c5f5aab4828c642ece3cc6caeb880da61b1de`)
- [observation/documented] Repository development practice: testing uses Vitest with pnpm test and per-package scripts; some tests require environment variables such as OPENAI_API_KEY and a local PostgreSQL DB_URL, with services started via pnpm run dev:services:up. -- evidence: [DEVELOPMENT.md#L130-L130](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L130-L130), [DEVELOPMENT.md#L132-L149](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L132-L149), [DEVELOPMENT.md#L155-L162](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L155-L162), [DEVELOPMENT.md#L151-L151](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L151-L151), [DEVELOPMENT.md#L166-L168](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L166-L168) (`clm_cfbf1c9e310f12bd94bba745795457633bb28dbd75dc734c0528308d601e379c`)
- [observation/documented] Repository development practice: PRs must link a relevant issue (e.g., Fixes #1234) or be closed; Coderabbit and Mastra Platform automatically comment on PRs, and contributors are asked to address all review comments. -- evidence: [DEVELOPMENT.md#L194-L194](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L194-L194), [CONTRIBUTING.md#L35-L35](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/CONTRIBUTING.md#L35-L35), [DEVELOPMENT.md#L196-L196](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L196-L196), [CONTRIBUTING.md#L31-L31](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/CONTRIBUTING.md#L31-L31) (`clm_c3eeeda604e6165440d2b77504966437332ee5982c721648c815c82540582abf`)
- [observation/documented] Repository development practice: feature PRs can only be opened when the feature request issue lacks the 'status: needs triage' or 'status: needs approval' labels; otherwise the PR is automatically closed. -- evidence: [CONTRIBUTING.md#L39-L40](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/CONTRIBUTING.md#L39-L40) (`clm_7e94c8c2490a2203bfae488c989e4cb2deb719801bdabb0ae61945b9cb28c352`)
- [observation/documented] Repository development practice: AGENTS.md instructs agents to use the most-specific AGENTS.md, place deterministic input/output constraints in schemas rather than execute, and keep runtime/external checks (authorization, existence, conflicts) in execute. -- evidence: [AGENTS.md#L6-L8](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/AGENTS.md#L6-L8), [AGENTS.md#L3-L4](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/AGENTS.md#L3-L4) (`clm_856ba7e9b7382153e546791e728f7dd8bfe659d5de14da7e659905deb414271f`)
- [observation/documented] Repository development practice: bug reports should include a minimal reproduction—a simplified project with only the packages and code needed to demonstrate the bug—published to a public GitHub repo and linked in the issue. -- evidence: [CONTRIBUTING.md#L73-L75](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/CONTRIBUTING.md#L73-L75), [CONTRIBUTING.md#L56-L56](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/CONTRIBUTING.md#L56-L56), [CONTRIBUTING.md#L106-L112](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/CONTRIBUTING.md#L106-L112) (`clm_164d997c1b8f66c76b5f36e3b6cb7d8b98ad7dfa6a1a68475994abb654f2e57a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The workflow engine's documented control-flow syntax includes methods such as .then(), .branch(), and .parallel() for orchestrating multi-step processes. -- evidence: [README.md#L25-L25](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L25-L25) (`clm_dea4cdd59b2ea7d72708bba8f2d71d613e14cceeb9b60068632f42b07edaa0da`)
- [observation/documented] Mastra Studio is presented as a web interface at http://localhost:4111 for building, testing, and managing agents, workflows, and tools after starting the dev server. -- evidence: [README.md#L65-L65](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L65-L65), [README.md#L67-L67](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L67-L67) (`clm_d9b432f90d2de20983246f880b759c632ec2307a24cfa98e8ced68f678a22c98`)

## memory-state (1 claim(s))

- [observation/documented] Suspended agents or workflows use storage to remember execution state, allowing indefinite pausing and later resumption where execution left off. -- evidence: [README.md#L27-L27](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L27-L27) (`clm_55c2c3a59f3034c484ebc42b1b8086c9f6f4dcfbc72a3c90f912812d1019b7ff`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The model router is documented to connect to 40+ providers through one standard interface, naming OpenAI, Anthropic, and Gemini among supported model sources. -- evidence: [README.md#L21-L21](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L21-L21) (`clm_1b985c126853df7260d22911d90fe9de9fb3c4661729cf736bc014c9b10d7cd5`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

