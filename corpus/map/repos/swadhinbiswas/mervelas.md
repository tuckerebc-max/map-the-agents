# swadhinbiswas/mervelas

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1aa7b039e521 @ 0619a7e59a3a7e60

## Summary (orientation draft, not independently verified)

Mervelas is an open-source, local-first AI coding CLI built with Bun, currently unpublished to NPM and requiring local compilation. Evidence covers its README-described commands, provider configuration, session storage, and contributor rules.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [inference/documented] The CLI appears to render its terminal UI with a custom React Ink abstraction compiled natively via Bun, per the README's performance description. -- evidence: [README.md#L30-L33](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L30-L33)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors must not import ink directly from npm; UI layout components must be routed through src/ink.ts. -- evidence: [README.md#L132-L134](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L132-L134)
  - [observation/documented] Repository development practice: contributors should run strict type checking via npm run typecheck (tsc --noEmit) and use lazy load: () => import(...) for tools and execute loops. -- evidence: [README.md#L132-L134](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L132-L134)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes slash commands including /config, /context, /agents, /mcp, /status, and /login for provider setup, context inspection, agent switching, and MCP integration. -- evidence: [README.md#L101-L106](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L101-L106)
  - [observation/documented] Providers can be configured via environment variables such as MERVELAS_API_PROVIDER, OPENAI_API_KEY, and OPENROUTER_API_KEY for headless and CI setups. -- evidence: [README.md#L121-L124](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L121-L124), [README.md#L112-L112](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L112-L112), [README.md#L116-L118](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L116-L118)
- memory-state (1 claim(s)):
  - [observation/documented] Conversational session history is written locally to ~/.mervelas/projects/ in JSONL format, per the README's privacy description. -- evidence: [README.md#L30-L33](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L30-L33)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The project is built with Bun and requires Bun to compile and run locally. -- evidence: [README.md#L13-L14](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L13-L14), [README.md#L72-L72](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L72-L72)
  - [observation/documented] The README claims out-of-the-box support for OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, and locally hosted models. -- evidence: [README.md#L30-L33](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L30-L33)
- limitations (1 claim(s)):
  - [observation/documented] The project is in active development, has not been published to NPM, and users must build it locally and supply their own API keys. -- evidence: [README.md#L16-L16](https://github.com/swadhinbiswas/Mervelas/blob/1aa7b039e52186f646d2bc472e4dbbe68e812625/README.md#L16-L16)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](mervelas.detail.md) for every claim.)

Metadata and full claim list: [full detail](mervelas.detail.md)
Human notes ([notes](mervelas.notes.md), never overwritten by build)

[Back to map index](../../index.md)
