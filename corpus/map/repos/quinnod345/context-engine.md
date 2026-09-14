# quinnod345/context-engine

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ff40183c8225 @ 0674eb88612e7123

## Summary (orientation draft, not independently verified)

The npm package context-engine-ai lets AI agents ingest events from any source and query them in natural language, returning ranked, time-decayed results without a vector database, API keys, or configuration. The HTTP server mode exposes REST endpoints including POST /ingest, GET /context?q=..., GET /recent, GET /count, DELETE /events, and GET /health, startable via ctx.serve(3334) or an npx CLI command. Evidence coverage: 161 of 326 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The npm package context-engine-ai lets AI agents ingest events from any source and query them in natural language, returning ranked, time-decayed results without a vector database, API keys, or configuration. -- evidence: [README.md#L5-L5](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L5-L5), [README.md#L7-L7](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] Storage adapters include SQLiteStorage built on better-sqlite3 with brute-force JS cosine search suited to roughly 10,000 events, and PostgresStorage using pgvector's cosine-distance operator for production scale. -- evidence: [docs/architecture.md#L75-L78](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L75-L78), [docs/architecture.md#L68-L71](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L68-L71)
- design-choices (3 claim(s)):
  - [observation/documented] Default embeddings use TF-IDF with locality-sensitive hashing projected to 128 dimensions, deterministic and network-free; an optional OpenAI text-embedding-3-small provider offers 1536-dimensional semantic search. -- evidence: [README.md#L486-L486](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L486-L486), [README.md#L490-L490](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L490-L490), [README.md#L432-L432](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L432-L432)
  - [observation/documented] Query ranking multiplies cosine similarity by relevance and an exponential half-life decay factor 0.5^(age/halfLife), with a configurable decayHours defaulting to 24 hours. -- evidence: [README.md#L459-L465](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L459-L465), [docs/architecture.md#L101-L103](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L101-L103), [docs/architecture.md#L105-L108](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L105-L108), [README.md#L411-L413](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L411-L413)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install, npm run build to compile TypeScript, npm test for the test suite, and npm run dev for watch mode. -- evidence: [README.md#L662-L669](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L662-L669)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The HTTP server mode exposes REST endpoints including POST /ingest, GET /context?q=..., GET /recent, GET /count, DELETE /events, and GET /health, startable via ctx.serve(3334) or an npx CLI command. -- evidence: [README.md#L249-L256](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L249-L256), [README.md#L213-L215](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L213-L215), [README.md#L206-L209](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L206-L209)
  - [observation/documented] An MCP server example lets MCP-compatible clients such as Claude Desktop, Cursor, and Windsurf call ingest_event, query_context, get_recent, and clear_context as native tools. -- evidence: [README.md#L239-L243](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L239-L243), [README.md#L219-L219](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L219-L219)
- memory-state (1 claim(s)):
  - [observation/documented] By default the engine runs in-memory with events lost on restart; passing dbPath persists events to a standard SQLite file that survives restarts and can be inspected with SQLite tools. -- evidence: [README.md#L188-L191](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L188-L191), [README.md#L471-L471](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L471-L471)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](context-engine.detail.md)

Metadata and full claim list: [full detail](context-engine.detail.md)
Human notes ([notes](context-engine.notes.md), never overwritten by build)

[Back to map index](../../index.md)
