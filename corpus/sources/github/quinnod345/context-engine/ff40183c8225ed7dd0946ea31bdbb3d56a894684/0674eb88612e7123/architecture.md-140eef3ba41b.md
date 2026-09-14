# Architecture

## Overview

`context-engine-ai` is structured as a small set of composable modules:

```
ContextEngine
├── StorageAdapter (SQLite or PostgreSQL)
├── EmbeddingProvider (Local TF-IDF or OpenAI)
├── Deduplication (cosine similarity within time window)
├── Temporal Decay (exponential half-life)
└── HTTP Server (Express, optional)
```

## Data Flow

### Ingest

```
EventInput { type, data }
    ↓
eventToText()         — serialize to searchable text
    ↓
embedder.embed()      — generate embedding vector
    ↓
findSimilar()         — check for duplicates in recent window
    ↓  (duplicate found)        ↓  (new event)
merge + updateRelevance()    insert() + prune()
    ↓                           ↓
StoredEvent                  StoredEvent
```

1. The event is serialized to text using `eventToText(type, data)`.
2. The text is embedded into a vector using the configured embedding provider.
3. The storage adapter checks for similar events within the deduplication window.
4. If a duplicate is found (cosine similarity >= threshold), the existing event is merged: timestamp updated, relevance boosted, data merged.
5. If it's a new event, it's inserted and the storage is pruned if over `maxEvents`.

### Query

```
query string
    ↓
embedder.embed()          — embed the query
    ↓
storage.search()          — vector similarity search
    ↓
computeDecay()            — apply temporal decay to relevance scores
    ↓
sort by decayed relevance
    ↓
build summary text
    ↓
ContextResult { summary, events, query, timestamp }
```

1. The query string is embedded.
2. The storage adapter performs vector similarity search.
3. Each result's relevance is multiplied by a temporal decay factor: `relevance * 0.5^(age / halfLife)`.
4. Results are re-sorted by decayed relevance.
5. A summary string is built from the top 5 events.

## Storage Adapters

### SQLite (`SQLiteStorage`)

- Uses `better-sqlite3` for synchronous, fast SQLite access.
- Embeddings stored as JSON text columns.
- Similarity search is brute-force (scan + cosine similarity in JS).
- Good for up to ~10,000 events. Beyond that, use PostgreSQL.

### PostgreSQL (`PostgresStorage`)

- Uses `pg` with the `pgvector` extension.
- Embeddings stored as native `vector` columns.
- Similarity search uses pgvector's `<=>` (cosine distance) operator with index support.
- Good for production, multi-process, and large-scale deployments.

## Embedding Providers

### Local (`LocalEmbeddingProvider`)

- TF-IDF with locality-sensitive hashing.
- 128-dimensional vectors.
- Maintains an in-memory vocabulary and document frequency table.
- Deterministic for the same instance (vocabulary grows with use).
- No network calls, no API keys, instant.

### OpenAI (`OpenAIEmbeddingProvider`)

- Uses `text-embedding-3-small` (1536-dimensional).
- Higher quality semantic similarity.
- Requires an API key and network access.
- Better for complex natural language queries.

## Temporal Decay

Events lose relevance over time using exponential decay:

```
decayed_relevance = base_relevance * 0.5^(age_ms / halflife_ms)
```

With the default `decayHours: 24`:
- An event 24 hours old has 50% of its original relevance.
- An event 48 hours old has 25%.
- An event 1 hour old has ~97%.

This means recent events naturally dominate query results without manually managing event lifecycle.

## Deduplication

When a new event is ingested, the engine checks recent events (within `deduplicationWindow` ms) for cosine similarity above `deduplicationThreshold`.

If a match is found:
- The existing event's timestamp is updated to now.
- Relevance is boosted by 0.1 (capped at 1.0).
- Data fields are merged (new values overwrite).
- A `_mergeCount` field tracks how many times the event was deduplicated.

This prevents flooding from repeated identical events (e.g., the user staying in the same app).
