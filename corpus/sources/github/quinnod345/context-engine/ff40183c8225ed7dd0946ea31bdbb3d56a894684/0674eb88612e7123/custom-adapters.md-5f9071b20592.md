# Custom Adapters

You can implement custom storage backends and embedding providers by implementing the `StorageAdapter` and `EmbeddingProvider` interfaces.

## Custom Storage Adapter

Implement the `StorageAdapter` interface:

```ts
import type { StorageAdapter, StoredEvent } from 'context-engine-ai'

class MyStorage implements StorageAdapter {
  async init(): Promise<void> {
    // Initialize your database, create tables, etc.
  }

  async insert(event: StoredEvent): Promise<void> {
    // Store the event
  }

  async search(embedding: number[], limit: number): Promise<StoredEvent[]> {
    // Find the most similar events by embedding
    // Return them sorted by similarity * relevance
  }

  async recent(limit: number): Promise<StoredEvent[]> {
    // Return the most recent events by timestamp
  }

  async count(): Promise<number> {
    // Return total event count
  }

  async prune(maxEvents: number): Promise<number> {
    // Delete the least relevant/oldest events if count > maxEvents
    // Return the number of events deleted
  }

  async findSimilar(
    embedding: number[],
    timeWindowMs: number,
    threshold: number
  ): Promise<StoredEvent | null> {
    // Find an event within timeWindowMs that has cosine similarity >= threshold
    // Return it, or null if none found
  }

  async updateRelevance(id: string, relevance: number): Promise<void> {
    // Update the relevance score of an event
  }

  async close(): Promise<void> {
    // Clean up connections
  }
}
```

## Custom Embedding Provider

Implement the `EmbeddingProvider` interface:

```ts
import type { EmbeddingProvider } from 'context-engine-ai'

class MyEmbedder implements EmbeddingProvider {
  dimensions = 256  // your embedding dimensions

  async embed(text: string): Promise<number[]> {
    // Convert text to a vector of `this.dimensions` length
    // Return the vector as a number[]
  }
}
```

## Using Custom Adapters Directly

Since `ContextEngine` currently accepts `'sqlite' | 'postgres'` for storage and `'local' | 'openai'` for embeddings, you'll use the lower-level APIs to wire custom adapters:

```ts
import { cosineSimilarity, computeDecay, eventToText } from 'context-engine-ai'
import { v4 as uuid } from 'uuid'

const storage = new MyStorage()
await storage.init()

const embedder = new MyEmbedder()

// Ingest
const text = eventToText('app_switch', { app: 'Firefox' })
const embedding = await embedder.embed(text)
await storage.insert({
  id: uuid(),
  type: 'app_switch',
  data: { app: 'Firefox' },
  timestamp: Date.now(),
  embedding,
  relevance: 1.0,
})

// Query
const queryEmb = await embedder.embed('what browser is open?')
const results = await storage.search(queryEmb, 10)

// Apply decay
const now = Date.now()
const decayed = results.map(e => ({
  ...e,
  relevance: e.relevance * computeDecay(e.timestamp, now, 24),
}))
decayed.sort((a, b) => b.relevance - a.relevance)
```

## Utility Functions

The package exports these helpers:

### `cosineSimilarity(a: number[], b: number[]): number`

Compute cosine similarity between two vectors. Returns a value between -1 and 1.

### `computeDecay(timestamp: number, now: number, halfLifeHours: number): number`

Compute temporal decay factor. Returns a value between 0 and 1.

### `eventToText(type: string, data: Record<string, unknown>): string`

Serialize an event to a searchable text string. Format: `event:type key1:value1 key2:value2`.
