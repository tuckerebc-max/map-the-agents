# sourcegraph/cody-public-snapshot

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8e20ac6c1460 @ 04923e036f317313

## Summary (orientation draft, not independently verified)

Evidence covers the README of a public snapshot of Sourcegraph's Cody AI coding assistant (VS Code/JetBrains/web), plus contributor-facing AGENT.md, ARCHITECTURE.md, and a manual QA checklist (TESTING.md), and a Storybook story file for agentic tool-output UI cells. Product claims are drawn from README/TESTING descriptions; build, style, and telemetry conventions are development practice.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] Documented features include chat with codebase context, single- and multi-line autocomplete, inline edit/refactor, and customizable prompts such as Document, Explain, and Generate Unit Tests. -- evidence: [README.md#L45-L50](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L45-L50)
  - [observation/documented] The edit workflow applies changes with code lenses for Show diff, Accept All, Retry, Undo, Accept, and Reject, and shows a 'Cody is working...' notification while edits apply. -- evidence: [TESTING.md#L43-L55](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/TESTING.md#L43-L55)
- design-choices (2 claim(s)):
  - [observation/documented] Cody retrieves context from local and remote codebases via advanced/semantic search, and supports @-mentioning files to target specific context. -- evidence: [README.md#L37-L37](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L37-L37), [README.md#L45-L50](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L45-L50)
  - [observation/documented] The product advertises swappable LLMs, naming Anthropic Claude Sonnet 4, OpenAI GPT-4o, Mixtral, and Gemini 1.5 among supported models. -- evidence: [README.md#L45-L50](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L45-L50)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: AGENT.md lists build (pnpm build), lint/format via Biome, and unit, integration, and E2E test commands such as pnpm test:unit and pnpm -C vscode run test:integration. -- evidence: [AGENT.md#L4-L10](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/AGENT.md#L4-L10)
  - [observation/documented] Repository development practice: AGENT.md prescribes code style including 4-space indentation, 105-character lines, avoiding 'as' casts outside tests, and telemetry event names of the form cody.<feature>. -- evidence: [AGENT.md#L13-L25](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/AGENT.md#L13-L25)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Cody is available as a VS Code extension, a JetBrains plugin, and a web chat client. -- evidence: [README.md#L39-L39](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L39-L39)
  - [observation/documented] The editor extensions work with Sourcegraph Cloud and self-hosted Sourcegraph Enterprise Server instances on version 5.1 or later. -- evidence: [README.md#L91-L92](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L91-L92)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Individual usage currently requires a free Sourcegraph.com account, which the README says exists to prevent abuse of free Anthropic/OpenAI LLM usage. -- evidence: [README.md#L81-L81](https://github.com/sourcegraph/cody-public-snapshot/blob/8e20ac6c1460c08b0db581c0204658112a246eda/README.md#L81-L81)
- limitations (1 claim(s)):
More evidence: [full detail](cody-public-snapshot.detail.md)

Metadata and full claim list: [full detail](cody-public-snapshot.detail.md)
Human notes ([notes](cody-public-snapshot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
