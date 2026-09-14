# husu/loom -- full detail

[Back to orientation](loom.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/husu/loom/905416f838bff228dab4018ad6e190d5ab49e992/a6063738faa5e442.json](../../../wiki/dossiers/husu/loom/905416f838bff228dab4018ad6e190d5ab49e992/a6063738faa5e442.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The documented project structure includes an agents system with tool calling and conversation memory, an LLM client for DeepSeek/OpenAI, agent tools for schema generation/validation and file operations, an Ink-based TUI, a Fastify web viewer with React SPA frontend, and a mock server with dynamic route registration. -- evidence: [README.en.md#L343-L383](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L343-L383), [README.en.md#L511-L515](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L511-L515) (`clm_4e50f0c47ca654055650cbfbfb6f58e4f13b932b748d9e67d8a5b48f54567291`)

## design-choices (2 claim(s))

- [observation/documented] Loom uses a custom JSON Schema format (draft-07) for API docs, with module title/description, an endpoints array carrying path, HTTP method, optional request schema (headers, params, query, body), and responses keyed by status code. -- evidence: [README.en.md#L291-L297](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L291-L297), [README.md#L290-L296](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L290-L296), [README.md#L241-L241](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L241-L241), [README.en.md#L244-L288](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L244-L288) (`clm_0cc22999768ecbfd8096dc73e7e316f6c60de8631a3ec21ee0dbb0ecbe600249`)
- [observation/documented] Reusable entity schemas live in docs/entities/*.entity.schema.json and are referenced from endpoint schemas via an x-entity-ref keyword, in either string form or object form with an entity name and a pick list of properties. -- evidence: [README.en.md#L303-L305](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L303-L305), [README.md#L323-L323](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L323-L323), [README.md#L302-L304](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L302-L304), [README.md#L336-L338](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L336-L338), [README.en.md#L337-L339](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L337-L339), [README.en.md#L324-L324](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L324-L324) (`clm_9307c05ca67ae3a6af1a4f98e3359c9c422b671b7fb61239a5237d2d9afde464`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are asked to fork, create a feature branch, commit, push, and open a PR; development guidelines say to use strict-mode TypeScript, follow existing code style, add tests for new functionality, and update documentation. -- evidence: [README.en.md#L491-L491](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L491-L491), [README.en.md#L493-L497](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L493-L497), [README.en.md#L500-L503](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L500-L503) (`clm_76bea33e5d443d9237b0b1c0c9aadde6be76fa7d5e167da3c769e71aa5f50d64`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Inside `loom chat`, slash commands include /help, /reset, /list, /mock, /view, /scan <dir> (with resume/reset), /abort, and /exit; Tab autocompletes commands and arrow keys navigate persisted history. -- evidence: [README.md#L152-L161](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L152-L161) (`clm_70706102a347bfa0e4ec04f4243998cfaeb8d7ce272a1c4c9e448e74fe85a1b6`)
- [observation/documented] The combined `loom serve` mode serves the web viewer at /, documentation APIs at /api/docs, /api/schemas, /api/entities, and mock routes under /mock/... on one port. -- evidence: [README.md#L214-L219](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L214-L219) (`clm_ea66851a2d093998e6d8f2191322194f1958b586b62b98cb03d1ac872791ffc2`)

## memory-state (2 claim(s))

- [observation/documented] Chat input history is persisted globally at ~/.loom/history.jsonl (capped at 100 entries) and is navigable across sessions with arrow keys; configuration lives at ~/.loom/config.json while docs/ stays per-project. -- evidence: [README.md#L44-L46](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L44-L46), [README.en.md#L456-L472](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L456-L472), [README.md#L79-L79](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L79-L79), [README.md#L353-L369](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L353-L369), [README.en.md#L80-L80](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L80-L80), [README.en.md#L44-L46](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L44-L46) (`clm_2486e910279353cd73e356bc0171c3705ee659602ef47d8ae019c342d30d13f3`)
- [observation/documented] The /scan feature caches LLM output keyed by file content hash in <outDir>/.loom-scan-cache.json, skipping unchanged files on incremental rescans; cache invalidation is driven by source-hash plus per-entry shape checks rather than a global version wipe. -- evidence: [README.md#L346-L350](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L346-L350), [README.en.md#L456-L472](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L456-L472), [README.en.md#L449-L453](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L449-L453), [README.md#L353-L369](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L353-L369) (`clm_6ffcba04acd6d33c02fac2bd5540bc52358c2e38e0f882d25de54e7cb66fdb73`)

## orchestration (1 claim(s))

- [observation/documented] The mock and web-viewer services can be started, stopped, and restarted from within the TUI via /mock and /view commands, or run together on one port via `loom serve`. -- evidence: [README.md#L92-L94](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L92-L94), [README.md#L152-L161](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L152-L161), [README.en.md#L204-L204](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L204-L204), [README.md#L203-L203](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L203-L203), [README.en.md#L93-L95](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L93-L95), [README.en.md#L153-L162](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L153-L162) (`clm_70f66d52fa98c4f8eff66aabc108ce0e3ff51d225ef08a83835a66b2df07e295`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project requires Node.js >= 18 and a DeepSeek API key, and credits Fastify, React, mock-json-schema, and Ink as key libraries; the mock server reportedly uses mock-json-schema for data generation. -- evidence: [README.md#L28-L30](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L28-L30), [README.en.md#L511-L515](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L511-L515), [README.md#L196-L200](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L196-L200), [README.en.md#L28-L30](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.en.md#L28-L30), [README.md#L391-L395](https://github.com/husu/loom/blob/905416f838bff228dab4018ad6e190d5ab49e992/README.md#L391-L395) (`clm_d67ab1f1f4238b0e7dce67e22b04b478749e1ebc935bb1b938862a2fee248ba0`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

