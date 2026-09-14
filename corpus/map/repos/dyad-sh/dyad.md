# dyad-sh/dyad

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0c8403662504 @ 73f45ce23df314b3

## Summary (orientation draft, not independently verified)

Dyad is a local, open-source Electron-based AI app builder whose LLM workflow uses XML-like dyad tags rendered in the UI and applied by a main-process response processor, with a newer local agent loop in src/pro. Evidence also covers i18n design, tool-permission settings, and contributor/CLA practices.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Dyad is a local, open-source AI app builder where users describe an app in plain language and the AI generates code with a live preview on their machine, with local-first operation as the core differentiator. -- evidence: [PRODUCT.md#L13-L13](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/PRODUCT.md#L13-L13), [README.md#L3-L3](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/README.md#L3-L3)
  - [observation/documented] The primary users are non-technical builders with no coding background running Dyad locally on Mac or Windows; a secondary audience brings their own API keys and local models. -- evidence: [PRODUCT.md#L9-L9](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/PRODUCT.md#L9-L9)
- components (2 claim(s)):
  - [observation/documented] Dyad is an Electron app with a React renderer process (sandboxed) and a privileged Node.js main process that accesses the filesystem, communicating via IPC. -- evidence: [docs/architecture.md#L11-L11](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L11-L11), [docs/architecture.md#L7-L7](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L7-L7)
  - [observation/documented] The local agent's core loop lives in src/pro/main/ipc/handlers/local_agent/local_agent_handler.ts, calling the LLM until it stops making tool calls or hits a per-turn maximum step count; tool_definitions.ts lists the agent's tools. -- evidence: [docs/agent_architecture.md#L5-L6](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L5-L6)
- design-choices (3 claim(s)):
  - [observation/documented] Dyad historically simulated tool calling with custom XML-like tags instead of models' formal tool calling, citing the ability to batch many calls and evidence that JSON code output hurts quality; a newer agent architecture moves toward standard tool calling. -- evidence: [docs/agent_architecture.md#L3-L3](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L3-L3), [docs/architecture.md#L27-L27](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L27-L27), [docs/architecture.md#L31-L32](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L31-L32)
  - [observation/documented] By default each LLM request includes the entire codebase plus a system prompt instructing XML-like responses; Smart Context uses smaller models to filter important files, and agentic iterative search is avoided mainly for cost reasons. -- evidence: [docs/architecture.md#L50-L50](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L50-L50), [docs/architecture.md#L17-L19](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L17-L19), [docs/architecture.md#L52-L52](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/architecture.md#L52-L52)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors add tools in the local_agent/tools directory, register them in tool_definitions.ts, render their XML tag in DyadMarkdownParser.tsx, and can add E2E tests modeled on e2e-tests/local_agent*.spec.ts with tool-call fixtures. -- evidence: [docs/agent_architecture.md#L20-L20](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L20-L20), [docs/agent_architecture.md#L14-L14](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L14-L14), [docs/agent_architecture.md#L12-L12](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L12-L12), [docs/agent_architecture.md#L18-L18](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L18-L18), [docs/agent_architecture.md#L10-L10](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/agent_architecture.md#L10-L10)
  - [observation/documented] Repository development practice: English locale files are the source of truth, other locales must mirror their key structure with automatic English fallback, and a CI check warns on missing keys; contributions fall under a CLA granting Dyad Tech, Inc. copyright and patent licenses. -- evidence: [CLA.md#L21-L21](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/CLA.md#L21-L21), [docs/i18n.md#L396-L396](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L396-L396), [docs/i18n.md#L391-L392](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/docs/i18n.md#L391-L392), [CLA.md#L40-L40](https://github.com/dyad-sh/dyad/blob/0c8403662504264f911242504fc2d2b07895c6ad/CLA.md#L40-L40)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
More evidence: [full detail](dyad.detail.md)

Metadata and full claim list: [full detail](dyad.detail.md)
Human notes ([notes](dyad.notes.md), never overwritten by build)

[Back to map index](../../index.md)
