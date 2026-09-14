# cherryhq/cherry-studio

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 61cac30ece4d @ c0035cf5a75c4323

## Summary (orientation draft, not independently verified)

Cherry Studio is an AGPL-3.0 desktop LLM client for Windows/Mac/Linux with an Electron multi-process architecture, extensive internal reference documentation, and a documented contributor workflow including branching strategy and release runbooks. Evidence coverage: 112 of 250 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 141 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Cherry Studio is a desktop client supporting multiple LLM providers, available on Windows, Mac, and Linux. -- evidence: [README.md#L37-L37](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L37-L37)
  - [observation/documented] The app supports cloud LLM services such as OpenAI, Gemini, and Anthropic, plus local models via Ollama and LM Studio. -- evidence: [README.md#L55-L57](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L55-L57)
- design-choices (3 claim(s)):
  - [observation/documented] The architecture follows an Electron process model with main, renderer, shared, and utility-process layers, each with documented dependency rules. -- evidence: [docs/README.md#L55-L62](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L55-L62)
  - [observation/documented] The file domain splits into FileManager for persistent FileEntry records and DirectoryTreeManager for in-memory directory mirrors, which do not automatically join. -- evidence: [docs/references/file/architecture.md#L15-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/references/file/architecture.md#L15-L16), [docs/references/file/architecture.md#L18-L19](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/references/file/architecture.md#L18-L19)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributions follow a documented branching strategy with pull request guidelines and version tag management targeting main. -- evidence: [docs/README.md#L7-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L7-L16), [README.md#L148-L148](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L148-L148)
  - [observation/documented] Repository development practice: a maintainer runbook covers preparing, validating, hotfixing, publishing, and synchronizing release branches, and a Test Plan process governs beta and rc testing. -- evidence: [docs/README.md#L7-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L7-L16)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A local HTTP API gateway exposes OpenAI, Anthropic, Gemini, Cherry REST, and MCP-compatible client endpoints. -- evidence: [docs/README.md#L49-L51](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L49-L51)
  - [observation/documented] A LAN transfer protocol specification covers desktop-mobile sync using mDNS discovery, a TCP handshake, and file transfer. -- evidence: [docs/README.md#L179-L181](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L179-L181)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Linux packaging uses pinned better-sqlite3 prebuilds, with documented build commands and prebuild update steps. -- evidence: [docs/README.md#L7-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L7-L16)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](cherry-studio.detail.md) for every claim.)

Metadata and full claim list: [full detail](cherry-studio.detail.md)
Human notes ([notes](cherry-studio.notes.md), never overwritten by build)

[Back to map index](../../index.md)
