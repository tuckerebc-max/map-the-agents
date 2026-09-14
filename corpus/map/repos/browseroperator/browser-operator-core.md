# browseroperator/browser-operator-core

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 85da86c2a942 @ 0ff1a873cb718770

## Summary (orientation draft, not independently verified)

Browser Operator is described as an open-source, privacy-focused AI browser for research, analysis, and automation that runs locally, with releases for macOS and Windows. Stated system requirements are macOS 10.15+ or Windows 10 64-bit, 8GB RAM (16GB recommended), and 2GB free disk space; the project is licensed under BSD-3-Clause.

## Source coverage

Source coverage (partial): 4 of 4 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Browser Operator is described as an open-source, privacy-focused AI browser for research, analysis, and automation that runs locally, with releases for macOS and Windows. -- evidence: [README.md#L9-L9](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/README.md#L9-L9), [README.md#L5-L7](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/README.md#L5-L7), [README.md#L19-L19](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/README.md#L19-L19)
  - [observation/documented] Stated system requirements are macOS 10.15+ or Windows 10 64-bit, 8GB RAM (16GB recommended), and 2GB free disk space; the project is licensed under BSD-3-Clause. -- evidence: [README.md#L21-L21](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/README.md#L21-L21), [README.md#L75-L75](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/README.md#L75-L75)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] LLM configuration uses a three-tier model scheme (Main for agent execution, Mini for lightweight operations, Nano for simple tasks) with configuration precedence of override first, then localStorage fallback. -- evidence: [MODEL-CONFIGS.md#L10-L14](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L10-L14), [MODEL-CONFIGS.md#L107-L108](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L107-L108)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use gclient sync and npm install, build via npm run build, run Karma/Mocha unit tests, Puppeteer webtests, and ESLint, and must add tests and pass lint before PRs reviewed by maintainers. -- evidence: [CLAUDE.md#L22-L25](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CLAUDE.md#L22-L25), [CLAUDE.md#L15-L18](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CLAUDE.md#L15-L18), [CONTRIBUTING.md#L96-L98](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CONTRIBUTING.md#L96-L98), [CONTRIBUTING.md#L37-L40](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CONTRIBUTING.md#L37-L40), [CONTRIBUTING.md#L145-L149](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CONTRIBUTING.md#L145-L149), [CLAUDE.md#L50-L55](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CLAUDE.md#L50-L55), [CONTRIBUTING.md#L85-L92](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CONTRIBUTING.md#L85-L92)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] An evaluation protocol defines JSON-RPC methods including 'configure_llm' for persistent LLM configuration and 'evaluate' requests that can carry per-request model, provider, API key, and endpoint overrides. -- evidence: [MODEL-CONFIGS.md#L289-L305](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L289-L305), [MODEL-CONFIGS.md#L114-L121](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L114-L121), [MODEL-CONFIGS.md#L165-L187](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L165-L187), [MODEL-CONFIGS.md#L269-L286](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L269-L286)
- memory-state (1 claim(s)):
  - [observation/documented] Provider, model, and API-key settings are persisted in localStorage under keys such as ai_chat_provider, ai_chat_model_selection, ai_chat_mini_model, ai_chat_nano_model, and per-provider API key/endpoint keys. -- evidence: [MODEL-CONFIGS.md#L17-L21](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L17-L21), [MODEL-CONFIGS.md#L24-L32](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L24-L32)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The product supports four LLM providers (LiteLLM, OpenAI, Groq, OpenRouter) per MODEL-CONFIGS.md, with LiteLLM enabling local models via Ollama; CLAUDE.md additionally lists cerebras and anthropic providers. -- evidence: [MODEL-CONFIGS.md#L10-L14](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L10-L14), [CLAUDE.md#L147-L150](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/CLAUDE.md#L147-L150), [README.md#L25-L30](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/README.md#L25-L30)
- limitations (1 claim(s)):
  - [observation/documented] The configuration rollout notes agent-server support for persistent configuration and comprehensive tests/performance testing as still pending (marked in-progress), while earlier phases are marked completed. -- evidence: [MODEL-CONFIGS.md#L347-L350](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L347-L350), [MODEL-CONFIGS.md#L353-L356](https://github.com/BrowserOperator/browser-operator-core/blob/85da86c2a9421c44d682af0e627243b76d3df0ef/MODEL-CONFIGS.md#L353-L356)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](browser-operator-core.detail.md)

Metadata and full claim list: [full detail](browser-operator-core.detail.md)
Human notes ([notes](browser-operator-core.notes.md), never overwritten by build)

[Back to map index](../../index.md)
