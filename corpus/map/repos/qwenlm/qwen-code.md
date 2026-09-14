# qwenlm/qwen-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7e0beb9d1823 @ 0429dc14353565eb

## Summary (orientation draft, not independently verified)

Qwen Code is an open-source, multi-protocol AI coding agent distributed as an npm package with terminal, headless, daemon, SDK, and IDE surfaces; the snapshot includes README product docs, an architecture overview, and a daemon side-channel coordination design doc. Evidence coverage: 110 of 329 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 827 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Key monorepo packages: `packages/cli` (executable, arg parsing, Ink TUI, headless output, ACP entry, `qwen serve`), `packages/core` (agent orchestration, tools, permissions, sessions, memory), and `packages/acp-bridge` (ACP channel lifecycle, session multiplexing, permission mediation). -- evidence: [docs/developers/architecture.md#L80-L95](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L80-L95)
- design-choices (3 claim(s)):
  - [observation/documented] The core runtime owns the agent loop — model requests, conversation context, tool dispatch, permission policy — while display and transport decisions are deliberately kept in the CLI, bridge, SDK, and UI layers. -- evidence: [docs/developers/architecture.md#L127-L129](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L127-L129), [docs/developers/architecture.md#L120-L125](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L120-L125)
  - [observation/documented] In daemon mode with multi-workspace sessions, each live workspace runtime owns its own bridge and `qwen --acp` child, with filesystem access, environment overlays, MCP transports, and sessions scoped to that runtime. -- evidence: [docs/developers/architecture.md#L185-L189](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L185-L189)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are directed to CONTRIBUTING.md for guidelines. -- evidence: [README.md#L206-L206](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L206-L206)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product offers multiple invocation surfaces: an interactive `qwen` TUI started in a project directory, headless `qwen -p "..."` for scripts/CI, and an experimental `qwen serve` daemon exposing HTTP + SSE (ACP). -- evidence: [README.md#L71-L74](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L71-L74), [docs/developers/architecture.md#L17-L21](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/docs/developers/architecture.md#L17-L21), [README.md#L105-L107](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L105-L107)
  - [observation/documented] SDKs exist for TypeScript, Python, and Java; the Python SDK exposes an async `query()` taking a cwd and path to the qwen executable, streaming messages from which result messages are printed. -- evidence: [README.md#L118-L125](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L118-L125), [README.md#L127-L129](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L127-L129), [README.md#L115-L115](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L115-L115), [README.md#L105-L107](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L105-L107)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports a SWE-bench Verified evaluation (500 cases, 3 trials per version, model Qwen 3.7 Max) with average scores between roughly 76.4% and 77.8% across seven Qwen Code versions. -- evidence: [README.md#L162-L170](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L162-L170), [README.md#L174-L182](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L174-L182)
- dependencies (1 claim(s)):
  - [observation/documented] NPM installation requires Node.js 22+; the project was originally based on Google Gemini CLI v0.8.2 but stopped syncing upstream starting from Qwen Code v0.1. -- evidence: [README.md#L53-L53](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L53-L53), [README.md#L3-L6](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L3-L6), [README.md#L210-L210](https://github.com/QwenLM/qwen-code/blob/7e0beb9d18233b0395dd7c203cb2e60a88de30aa/README.md#L210-L210)
More evidence: [full detail](qwen-code.detail.md)

Metadata and full claim list: [full detail](qwen-code.detail.md)
Human notes ([notes](qwen-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
