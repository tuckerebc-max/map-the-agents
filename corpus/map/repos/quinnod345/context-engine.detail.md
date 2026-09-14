# quinnod345/context-engine -- full detail

[Back to orientation](context-engine.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/quinnod345/context-engine/ff40183c8225ed7dd0946ea31bdbb3d56a894684/0674eb88612e7123.json](../../../wiki/dossiers/quinnod345/context-engine/ff40183c8225ed7dd0946ea31bdbb3d56a894684/0674eb88612e7123.json)

## specifications (1 claim(s))

- [observation/documented] The npm package context-engine-ai lets AI agents ingest events from any source and query them in natural language, returning ranked, time-decayed results without a vector database, API keys, or configuration. -- evidence: [README.md#L5-L5](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L5-L5), [README.md#L7-L7](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L7-L7) (`clm_a834fc855c29950e54cd13bb89643557b957fc3492d8223c4ce589c95dcb712b`)

## components (1 claim(s))

- [observation/documented] Storage adapters include SQLiteStorage built on better-sqlite3 with brute-force JS cosine search suited to roughly 10,000 events, and PostgresStorage using pgvector's cosine-distance operator for production scale. -- evidence: [docs/architecture.md#L75-L78](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L75-L78), [docs/architecture.md#L68-L71](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L68-L71) (`clm_c80934970d1b411abe7318837ce23bd19b65bd4e2444b9ecc746e350818a20e4`)

## design-choices (3 claim(s))

- [observation/documented] Default embeddings use TF-IDF with locality-sensitive hashing projected to 128 dimensions, deterministic and network-free; an optional OpenAI text-embedding-3-small provider offers 1536-dimensional semantic search. -- evidence: [README.md#L486-L486](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L486-L486), [README.md#L490-L490](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L490-L490), [README.md#L432-L432](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L432-L432) (`clm_172ff492b6da7011519f6f386e6da314825e9c1fe8172b12c6515ce5a5beed24`)
- [observation/documented] Query ranking multiplies cosine similarity by relevance and an exponential half-life decay factor 0.5^(age/halfLife), with a configurable decayHours defaulting to 24 hours. -- evidence: [README.md#L459-L465](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L459-L465), [docs/architecture.md#L101-L103](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L101-L103), [docs/architecture.md#L105-L108](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L105-L108), [README.md#L411-L413](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L411-L413) (`clm_c3e0f3cecb7c769c587ee060ea186b6ee29890340a1e1adf613b58012535a04a`)
- [observation/documented] Ingest deduplicates events whose cosine similarity exceeds a configurable threshold (default 0.95) within a time window (default 60s), merging timestamps, boosting relevance, and tracking a _mergeCount field. -- evidence: [docs/architecture.md#L114-L114](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L114-L114), [README.md#L459-L465](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L459-L465), [docs/architecture.md#L116-L120](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/docs/architecture.md#L116-L120), [README.md#L405-L405](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L405-L405) (`clm_d70d0317c3cd9762ab4916376e83f6bae00080a6381467626055aedb2db5ffdc`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm install, npm run build to compile TypeScript, npm test for the test suite, and npm run dev for watch mode. -- evidence: [README.md#L662-L669](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L662-L669) (`clm_393e16452ac0102fa33cdb383582e16a025092145c30b744f6bf2ffb51581cfd`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The HTTP server mode exposes REST endpoints including POST /ingest, GET /context?q=..., GET /recent, GET /count, DELETE /events, and GET /health, startable via ctx.serve(3334) or an npx CLI command. -- evidence: [README.md#L249-L256](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L249-L256), [README.md#L213-L215](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L213-L215), [README.md#L206-L209](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L206-L209) (`clm_c925389e44174a63b1ec3ee249137b688005b76fa8d38638435e34281f21adcf`)
- [observation/documented] An MCP server example lets MCP-compatible clients such as Claude Desktop, Cursor, and Windsurf call ingest_event, query_context, get_recent, and clear_context as native tools. -- evidence: [README.md#L239-L243](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L239-L243), [README.md#L219-L219](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L219-L219) (`clm_62ac101334cc26dc67708e0ca602d248c3ffd7410fed72b2908d6e438b4343df`)

## memory-state (1 claim(s))

- [observation/documented] By default the engine runs in-memory with events lost on restart; passing dbPath persists events to a standard SQLite file that survives restarts and can be inspected with SQLite tools. -- evidence: [README.md#L188-L191](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L188-L191), [README.md#L471-L471](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L471-L471) (`clm_ed3a3be63b906075cb697552bc7f8c1f44a5bf1d5b1cf016a9fe43b4859d0b50`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports benchmarks on Apple Silicon with local TF-IDF and in-memory SQLite: roughly 0.1ms per ingest, 0.1ms per query across 1000 events, and about 20MB heap. -- evidence: [README.md#L438-L442](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L438-L442), [README.md#L436-L436](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L436-L436) (`clm_3375bd7d96c37283510074684d048f80fb8eadb3e7139066606bd023050a3f76`)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Node.js >= 18 with no external services in default configuration; PostgreSQL with the pgvector extension and an OpenAI API key are optional for production scale and higher-quality embeddings. -- evidence: [README.md#L653-L656](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L653-L656) (`clm_d1c9ea2c49ed3db2b097bb569eecc7c5e2290c8818bf50b1dbcb221bfd8fed4f`)

## limitations (1 claim(s))

- [observation/documented] The README states the tool is not the right fit for searching large documents or PDFs, for months-long persistent memory, or for indexing millions of documents, suggesting RAG frameworks or dedicated vector databases instead. -- evidence: [README.md#L134-L137](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L134-L137) (`clm_d45a47f23e8857fcadb8367e30be2c8eae6ca6ed5cf4bd0fabe7c64048406dbc`)

## relevance (1 claim(s))

- [observation/documented] The project positions itself for agents needing real-time situational awareness, semantic search over structured event streams, and quick prototypes with built-in temporal decay and deduplication. -- evidence: [README.md#L127-L132](https://github.com/Quinnod345/context-engine/blob/ff40183c8225ed7dd0946ea31bdbb3d56a894684/README.md#L127-L132) (`clm_0ee1877b255298700fc3ceab20ffa98073ad6bd574c91d49654b0c572b04179a`)

