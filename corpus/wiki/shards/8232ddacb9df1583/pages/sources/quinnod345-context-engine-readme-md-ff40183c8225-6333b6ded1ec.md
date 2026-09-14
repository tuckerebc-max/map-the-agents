---
access: public
aliases: []
claim_ids:
- clm_0ee1877b255298700fc3ceab20ffa98073ad6bd574c91d49654b0c572b04179a
- clm_172ff492b6da7011519f6f386e6da314825e9c1fe8172b12c6515ce5a5beed24
- clm_3375bd7d96c37283510074684d048f80fb8eadb3e7139066606bd023050a3f76
- clm_393e16452ac0102fa33cdb383582e16a025092145c30b744f6bf2ffb51581cfd
- clm_62ac101334cc26dc67708e0ca602d248c3ffd7410fed72b2908d6e438b4343df
- clm_a834fc855c29950e54cd13bb89643557b957fc3492d8223c4ce589c95dcb712b
- clm_c3e0f3cecb7c769c587ee060ea186b6ee29890340a1e1adf613b58012535a04a
- clm_c925389e44174a63b1ec3ee249137b688005b76fa8d38638435e34281f21adcf
- clm_d1c9ea2c49ed3db2b097bb569eecc7c5e2290c8818bf50b1dbcb221bfd8fed4f
- clm_d45a47f23e8857fcadb8367e30be2c8eae6ca6ed5cf4bd0fabe7c64048406dbc
- clm_d70d0317c3cd9762ab4916376e83f6bae00080a6381467626055aedb2db5ffdc
- clm_ed3a3be63b906075cb697552bc7f8c1f44a5bf1d5b1cf016a9fe43b4859d0b50
maturity: draft
page_id: pg_9cd462541156550e9af86333b6ded1ec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2249690a32225f4ba85618e6a039b162
title: Quinnod345/context-engine/README.md @ ff40183c8225
updated_at: '2026-09-14T04:17:15Z'
---

# Quinnod345/context-engine/README.md @ ff40183c8225

<!-- rcw:begin owner=source:src_2249690a32225f4ba85618e6a039b162 block=evidence -->
- The project positions itself for agents needing real-time situational awareness, semantic search over structured event streams, and quick prototypes with built-in temporal decay and deduplication. [@claim:clm_0ee1877b255298700fc3ceab20ffa98073ad6bd574c91d49654b0c572b04179a]
- Default embeddings use TF-IDF with locality-sensitive hashing projected to 128 dimensions, deterministic and network-free; an optional OpenAI text-embedding-3-small provider offers 1536-dimensional semantic search. [@claim:clm_172ff492b6da7011519f6f386e6da314825e9c1fe8172b12c6515ce5a5beed24]
- The README reports benchmarks on Apple Silicon with local TF-IDF and in-memory SQLite: roughly 0.1ms per ingest, 0.1ms per query across 1000 events, and about 20MB heap. [@claim:clm_3375bd7d96c37283510074684d048f80fb8eadb3e7139066606bd023050a3f76]
- Repository development practice: contributors clone the repo, run npm install, npm run build to compile TypeScript, npm test for the test suite, and npm run dev for watch mode. [@claim:clm_393e16452ac0102fa33cdb383582e16a025092145c30b744f6bf2ffb51581cfd]
- An MCP server example lets MCP-compatible clients such as Claude Desktop, Cursor, and Windsurf call ingest_event, query_context, get_recent, and clear_context as native tools. [@claim:clm_62ac101334cc26dc67708e0ca602d248c3ffd7410fed72b2908d6e438b4343df]
- The npm package context-engine-ai lets AI agents ingest events from any source and query them in natural language, returning ranked, time-decayed results without a vector database, API keys, or configuration. [@claim:clm_a834fc855c29950e54cd13bb89643557b957fc3492d8223c4ce589c95dcb712b]
- Query ranking multiplies cosine similarity by relevance and an exponential half-life decay factor 0.5^(age/halfLife), with a configurable decayHours defaulting to 24 hours. [@claim:clm_c3e0f3cecb7c769c587ee060ea186b6ee29890340a1e1adf613b58012535a04a]
- The HTTP server mode exposes REST endpoints including POST /ingest, GET /context?q=..., GET /recent, GET /count, DELETE /events, and GET /health, startable via ctx.serve(3334) or an npx CLI command. [@claim:clm_c925389e44174a63b1ec3ee249137b688005b76fa8d38638435e34281f21adcf]
- Requirements are Node.js >= 18 with no external services in default configuration; PostgreSQL with the pgvector extension and an OpenAI API key are optional for production scale and higher-quality embeddings. [@claim:clm_d1c9ea2c49ed3db2b097bb569eecc7c5e2290c8818bf50b1dbcb221bfd8fed4f]
- The README states the tool is not the right fit for searching large documents or PDFs, for months-long persistent memory, or for indexing millions of documents, suggesting RAG frameworks or dedicated vector databases instead. [@claim:clm_d45a47f23e8857fcadb8367e30be2c8eae6ca6ed5cf4bd0fabe7c64048406dbc]
- Ingest deduplicates events whose cosine similarity exceeds a configurable threshold (default 0.95) within a time window (default 60s), merging timestamps, boosting relevance, and tracking a _mergeCount field. [@claim:clm_d70d0317c3cd9762ab4916376e83f6bae00080a6381467626055aedb2db5ffdc]
- By default the engine runs in-memory with events lost on restart; passing dbPath persists events to a standard SQLite file that survives restarts and can be inspected with SQLite tools. [@claim:clm_ed3a3be63b906075cb697552bc7f8c1f44a5bf1d5b1cf016a9fe43b4859d0b50]
<!-- rcw:end owner=source:src_2249690a32225f4ba85618e6a039b162 block=evidence -->

## Researcher notes

