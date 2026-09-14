# husu/loom

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 905416f838bf @ a6063738faa5e442

## Summary (orientation draft, not independently verified)

Inside `loom chat`, slash commands include /help, /reset, /list, /mock, /view, /scan <dir> (with resume/reset), /abort, and /exit; Tab autocompletes commands and arrow keys navigate persisted history. The combined `loom serve` mode serves the web viewer at /, documentation APIs at /api/docs, /api/schemas, /api/entities, and mock routes under /mock/... on one port.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The documented project structure includes an agents system with tool calling and conversation memory, an LLM client for DeepSeek/OpenAI, agent tools for schema generation/validation and file operations, an Ink-based TUI, a Fastify web viewer with React SPA frontend, and a mock server with dynamic route registration. -- evidence: [README.en.md#L343-L383](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L343-L383), [README.en.md#L511-L515](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L511-L515)
- design-choices (2 claim(s)):
  - [observation/documented] Loom uses a custom JSON Schema format (draft-07) for API docs, with module title/description, an endpoints array carrying path, HTTP method, optional request schema (headers, params, query, body), and responses keyed by status code. -- evidence: [README.en.md#L291-L297](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L291-L297), [README.md#L290-L296](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L290-L296), [README.md#L241-L241](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L241-L241), [README.en.md#L244-L288](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L244-L288)
  - [observation/documented] Reusable entity schemas live in docs/entities/*.entity.schema.json and are referenced from endpoint schemas via an x-entity-ref keyword, in either string form or object form with an entity name and a pick list of properties. -- evidence: [README.en.md#L303-L305](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L303-L305), [README.md#L323-L323](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L323-L323), [README.md#L302-L304](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L302-L304), [README.md#L336-L338](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L336-L338), [README.en.md#L337-L339](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L337-L339), [README.en.md#L324-L324](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L324-L324)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are asked to fork, create a feature branch, commit, push, and open a PR; development guidelines say to use strict-mode TypeScript, follow existing code style, add tests for new functionality, and update documentation. -- evidence: [README.en.md#L491-L491](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L491-L491), [README.en.md#L493-L497](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L493-L497), [README.en.md#L500-L503](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L500-L503)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Inside `loom chat`, slash commands include /help, /reset, /list, /mock, /view, /scan <dir> (with resume/reset), /abort, and /exit; Tab autocompletes commands and arrow keys navigate persisted history. -- evidence: [README.md#L152-L161](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L152-L161)
  - [observation/documented] The combined `loom serve` mode serves the web viewer at /, documentation APIs at /api/docs, /api/schemas, /api/entities, and mock routes under /mock/... on one port. -- evidence: [README.md#L214-L219](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L214-L219)
- memory-state (2 claim(s)):
  - [observation/documented] Chat input history is persisted globally at ~/.loom/history.jsonl (capped at 100 entries) and is navigable across sessions with arrow keys; configuration lives at ~/.loom/config.json while docs/ stays per-project. -- evidence: [README.md#L44-L46](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L44-L46), [README.en.md#L456-L472](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L456-L472), [README.md#L79-L79](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L79-L79), [README.md#L353-L369](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L353-L369), [README.en.md#L80-L80](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L80-L80), [README.en.md#L44-L46](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L44-L46)
More evidence: [full detail](loom.detail.md)

Metadata and full claim list: [full detail](loom.detail.md)
Human notes ([notes](loom.notes.md), never overwritten by build)

[Back to map index](../../index.md)
