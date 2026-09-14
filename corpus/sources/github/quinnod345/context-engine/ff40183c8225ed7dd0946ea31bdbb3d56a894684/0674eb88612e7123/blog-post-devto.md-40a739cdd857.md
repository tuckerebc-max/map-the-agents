---
title: "Building Real-Time Context for AI Agents Without a Vector Database"
published: true
description: "How I built context-engine-ai — a zero-config context engine that gives AI agents situational awareness using SQLite and local embeddings. Now with MCP server support."
tags: ai, typescript, opensource, tutorial
cover_image: https://opengraph.githubassets.com/1/Quinnod345/context-engine
canonical_url: https://github.com/Quinnod345/context-engine
---

# Building Real-Time Context for AI Agents Without a Vector Database

Every AI agent I built needed the same thing: to know what's happening *right now*.

Not document search. Not RAG over PDFs. Real-time situational awareness — what app is the user in, who messaged them, what's on their calendar, what errors are firing.

## The Problem

If you're building an AI agent that responds to a user, you need context. The user says "what should I focus on?" and the agent needs to know:

- They're in VS Code editing `auth.ts`
- 3 tests are failing
- There's a Slack message about staging being down
- Sprint planning starts in 15 minutes

Your options today:

**Vector database + embedding API.** Set up Pinecone or Weaviate, get an OpenAI key, build the retrieval pipeline, handle rate limits. This works, but you're now maintaining infrastructure for what should be a function call.

**Stuff everything in the prompt.** Append raw events to the system prompt. This breaks when you hit 50+ events. No relevance ranking. No temporal awareness — an event from yesterday looks the same as one from 5 seconds ago.

**Build it yourself.** Event store, embedding logic, similarity search, temporal decay, deduplication. A week of work before you write any agent logic.

## What I Built

I extracted the pattern into a standalone library: [context-engine-ai](https://github.com/Quinnod345/context-engine).

```js
import { ContextEngine } from 'context-engine-ai'

const ctx = new ContextEngine()

await ctx.ingest({ type: 'app_switch', data: { app: 'VS Code', file: 'auth.ts' } })
await ctx.ingest({ type: 'slack',      data: { from: 'Sarah', text: 'staging is down' } })
await ctx.ingest({ type: 'calendar',   data: { event: 'Sprint planning', in: '15min' } })

const result = await ctx.query('what needs attention?')
// result.summary → "[slack] from: Sarah, text: staging is down | [app_switch] app: VS Code, file: auth.ts | ..."
```

That's the full API. Three methods: `ingest`, `query`, `recent`.

No API keys required. No database to set up. Zero config.

## How It Works Under the Hood

### Embeddings without an API

The default embedding provider uses TF-IDF with locality-sensitive hashing, projected into 128 dimensions. Every event gets converted to text (`"event:slack from:Sarah text:staging is down"`), then embedded locally.

It's deterministic, instant, and free. No network calls. Benchmarked at ~0.1ms per embed on Apple Silicon.

When you need higher semantic quality — for ambiguous queries or complex natural language — you swap in OpenAI embeddings with one config change:

```js
const ctx = new ContextEngine({
  embeddingProvider: 'openai',
  openaiApiKey: process.env.OPENAI_API_KEY,
})
```

### Temporal Decay

This was the key insight. In a context engine, *recency matters as much as relevance*.

If the user asks "what's going on?", an event from 2 minutes ago should outrank an identical event from yesterday. Standard vector search treats them equally.

context-engine-ai applies exponential decay based on a configurable half-life (default: 24 hours). The math:

```
finalScore = cosineSimilarity(query, event) × relevance × decay(age, halfLife)
```

A 5-minute-old event gets nearly full weight. A 24-hour-old event gets half. A 48-hour-old event gets a quarter. This means the context naturally "forgets" old events without any cleanup logic.

### Deduplication

If a user switches between VS Code and Chrome 50 times, you don't want 50 events. The engine checks incoming events against recent events using cosine similarity — if the new event is >95% similar to something in the last 60 seconds, it merges them instead of creating a duplicate.

Both the threshold (0.95) and the time window (60s) are configurable.

### Performance

With local embeddings and SQLite, the whole pipeline — embed, dedup check, store — runs in ~0.1ms per event. Queries across 1000 events take ~0.1ms. Memory footprint is ~20MB heap. These aren't theoretical numbers; I benchmarked the actual library on Apple Silicon.

This matters because if your agent is running a tight loop (poll every few seconds, ingest, think, respond), the context layer can't be the bottleneck.

### Auto-pruning

When the event count exceeds your limit (default: 1000), the lowest-relevance, oldest events are automatically removed. No cron jobs, no maintenance.

## Real Use Cases

### 1. AI Agent with Claude

The most direct use case — feed context into an LLM's system prompt:

```js
import Anthropic from '@anthropic-ai/sdk'
import { ContextEngine } from 'context-engine-ai'

const ctx = new ContextEngine({ dbPath: './agent-context.db' })
const claude = new Anthropic()

// Events stream in throughout the day
await ctx.ingest({ type: 'terminal', data: { command: 'npm test', output: '3 failed' } })
await ctx.ingest({ type: 'error',   data: { service: 'auth', error: 'TokenExpiredError', count: 47 } })

// When the agent responds, get relevant context
const context = await ctx.query('what needs attention?', 5)

const response = await claude.messages.create({
  model: 'claude-sonnet-4-6',
  max_tokens: 1024,
  system: `You are a developer assistant. Current context:\n${context.summary}`,
  messages: [{ role: 'user', content: 'What should I focus on?' }]
})
```

The `summary` field is pre-formatted for prompt injection — drop it in and it works.

### 2. Webhook Aggregation

Receive webhooks from GitHub, Slack, PagerDuty. Query the combined stream in natural language instead of checking each service:

```js
app.post('/webhook/github', async (req, res) => {
  await ctx.ingest({
    type: 'github_pr',
    data: { action: req.body.action, title: req.body.pull_request?.title }
  })
  res.sendStatus(200)
})

// One query across all sources
const result = await ctx.query('what happened in the last hour?')
```

### 3. Desktop Activity Tracker

Track what you're doing across apps. Deduplication handles the noise:

```js
setInterval(async () => {
  const app = execSync(
    `osascript -e 'tell app "System Events" to get name of first process whose frontmost is true'`,
    { encoding: 'utf-8' }
  ).trim()
  await ctx.ingest({ type: 'window_focus', data: { app } })
}, 5000)
```

## MCP Server (Claude Desktop, Cursor, Windsurf)

One more use case worth calling out: you can run context-engine as an [MCP](https://modelcontextprotocol.io) (Model Context Protocol) tool server. This lets Claude Desktop, Cursor, or any MCP-compatible client call `ingest_event`, `query_context`, `get_recent`, and `clear_context` as native tools.

```bash
npm install @modelcontextprotocol/sdk zod
node examples/mcp-server.js
```

Point your MCP client at the process and the agent can ingest and query context natively. Full setup in [`examples/mcp-server.js`](https://github.com/Quinnod345/context-engine/blob/main/examples/mcp-server.js).

---

## When NOT to Use This

Honesty matters more than marketing:

- **Document search / RAG** — Use LangChain, LlamaIndex, or a proper RAG framework. context-engine-ai is for *events*, not documents.
- **Long-term memory** — If you need months of history, use a proper vector database. This is designed for ephemeral, real-time context.
- **Millions of records** — The SQLite backend handles thousands well. For millions, use pgvector directly.

## Try It

```bash
npx context-engine-ai demo
```

No API keys. No setup. Runs a simulated developer workflow and shows the query results.

Or install it:

```bash
npm install context-engine-ai
```

GitHub: [github.com/Quinnod345/context-engine](https://github.com/Quinnod345/context-engine)
npm: [npmjs.com/package/context-engine-ai](https://www.npmjs.com/package/context-engine-ai)

MIT licensed. TypeScript. 64KB unpacked. Sub-millisecond latency. Feedback welcome — especially if you have ideas for new storage adapters or embedding providers.
