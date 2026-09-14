# context-engine-ai Launch Plan

Everything below is ready to copy-paste. Submit in this order for maximum effect.

---

## 1. Hacker News (Show HN)

**Title:** `Show HN: Context Engine – Give your AI agent a memory with zero config`

**URL:** `https://github.com/Quinnod345/context-engine`

**Comment (post immediately after submitting):**

```
I built this because every AI agent I was building needed the same thing: a way to know what's happening right now. Not RAG over documents — real-time context. What app is the user in? Who messaged them? What's coming up?

Most solutions require OpenAI keys + Pinecone/Weaviate + Postgres just to start. I wanted something that works in 3 lines with zero config.

context-engine-ai uses SQLite + local TF-IDF embeddings by default — no API keys, no cloud, no database to set up. You can upgrade to pgvector + OpenAI embeddings when you need production scale.

Core API is three methods:
- ctx.ingest({ type, data }) — feed in events
- ctx.query('what is the user doing?') — semantic search with temporal decay
- ctx.recent(10) — get latest events

Try it: npx context-engine-ai demo

Benchmarks: ~0.1ms per ingest, ~0.1ms per query (local TF-IDF + SQLite, 1000 events). 20MB heap. The context layer shouldn't be the bottleneck when your agent is running a tight loop.

Tech: TypeScript, SQLite (better-sqlite3), optional pgvector, local TF-IDF or OpenAI embeddings. MIT licensed. ~64KB unpacked.

Happy to answer questions about the architecture, the temporal decay math, or use cases.
```

**Submit at:** https://news.ycombinator.com/submit
**Best time:** Tuesday-Thursday, 8-10am EST

---

## 2. Reddit

### r/programming

**Title:** `I built a zero-config context engine for AI agents — ingest events, query with natural language`

**Body:**

```
I kept rebuilding the same "what is the user doing right now?" layer for every AI agent project. So I extracted it into a standalone package.

context-engine-ai gives you semantic context in 3 lines:

    const ctx = new ContextEngine()
    await ctx.ingest({ type: 'app_switch', data: { app: 'VS Code', file: 'main.ts' } })
    const result = await ctx.query('what is the user working on?')

Features:
- Zero config default: SQLite + local TF-IDF embeddings (no API keys)
- Semantic querying with temporal decay
- Auto-dedup and auto-pruning
- Optional pgvector + OpenAI for production
- HTTP server / CLI / library modes
- Full TypeScript

Try it: `npx context-engine-ai demo`

GitHub: https://github.com/Quinnod345/context-engine
npm: https://www.npmjs.com/package/context-engine-ai

Benchmarks: ~0.1ms per ingest, ~0.1ms per query. 20MB heap. 14 tests passing.

MIT licensed, feedback welcome.
```

### r/node

**Title:** `context-engine-ai: Zero-config semantic context for AI agents (TypeScript, SQLite, pgvector)`

**Body:** (same as above, but add at the end)

```
Built with TypeScript, better-sqlite3, Express 5, and optional pgvector + OpenAI. Sub-millisecond ingest and query. 14 tests passing. ~64KB unpacked. Feedback on the API design welcome.
```

### r/MachineLearning

**Title:** `[P] Context Engine — lightweight real-time context for AI agents with local TF-IDF or OpenAI embeddings`

**Body:**

```
Open source library for giving AI agents real-time contextual awareness. The core idea: instead of RAG over documents, you ingest a stream of events (app switches, messages, calendar, terminal commands, etc.) and query them semantically with temporal decay.

Default mode uses local TF-IDF with LSH (128-dim vectors) — no API calls, instant, deterministic. Can upgrade to OpenAI text-embedding-3-small for higher quality.

Storage: SQLite (in-memory or file) by default, pgvector for production.

Key design decisions:
- Temporal decay: recent events rank higher (configurable half-life)
- Auto-deduplication via cosine similarity threshold
- Auto-pruning when event limit is hit

GitHub: https://github.com/Quinnod345/context-engine
Paper/approach inspiration: TF-IDF with random hyperplane LSH for the local embedding provider.
```

### r/artificial

**Title:** `Open source: Give your AI agent a memory — context-engine-ai`

**Body:** (shorter version of r/programming post)

### r/SideProject

**Title:** `I built a context engine for AI agents — zero config, semantic queries, temporal decay`

**Body:** (same as r/programming)

---

## 3. Product Hunt

**Product Name:** context-engine-ai

**Tagline:** Give your AI agent a memory. Zero config.

**Description:**

```
A lightweight context engine for AI agents. Ingest events from any source (app switches, messages, calendar, terminal, git commits), then query with natural language: "what is the user working on?"

Works out of the box with SQLite + local embeddings — no API keys, no cloud, no database setup. Upgrade to pgvector + OpenAI when you need production scale.

Three methods, that's it:
- ingest() — feed in events
- query() — semantic search with temporal decay
- recent() — get latest events

Try it: npx context-engine-ai demo

TypeScript. MIT licensed. Built for developers building AI agents.
```

**Topics:** Developer Tools, Artificial Intelligence, Open Source

**Submit at:** https://www.producthunt.com/posts/new

---

## 4. Awesome Lists — Open PRs

### awesome-ai (sindresorhus/awesome)
Not a direct fit — look for more specific lists.

### awesome-rag
Search for: https://github.com/search?q=awesome+rag&type=repositories

### awesome-llm-apps
https://github.com/Shubhamsaboo/awesome-llm-apps
Add under "Tools" or "Context/Memory"

### awesome-ai-agents
https://github.com/e2b-dev/awesome-ai-agents
Add as infrastructure/tooling

### awesome-typescript
https://github.com/dzharii/awesome-typescript
Add under "Libraries"

### awesome-nodejs
https://github.com/sindresorhus/awesome-nodejs
Add under "AI" or relevant section

**PR template for awesome-lists:**

```
Add context-engine-ai to [section]

[context-engine-ai](https://github.com/Quinnod345/context-engine) - Lightweight context engine for AI agents. Ingest events, query with natural language. Zero config with SQLite + local embeddings.
```

---

## 5. Other Channels

### Dev.to Article
Write a post: "Building Real-Time Context for AI Agents Without a Vector Database"
- Walk through the problem
- Show the 3-line solution
- Explain temporal decay and dedup
- Link to GitHub

### Twitter/X
```
I built context-engine-ai — give your AI agent a memory in 3 lines.

const ctx = new ContextEngine()
await ctx.ingest({ type: 'message', data: { from: 'Alice', text: 'PR ready' } })
await ctx.query('any messages?')

Zero config. No API keys. SQLite + local embeddings.

Try it: npx context-engine-ai demo

github.com/Quinnod345/context-engine
```

### Discord
Post in AI/dev Discord servers:
- Vercel Discord (#showcase)
- Anthropic Discord
- LangChain Discord
- TheAIExchange

---

## Timeline

| Day | Action |
|-----|--------|
| Today | Post to HN (Show HN), r/programming, r/node |
| Day 2 | Post to r/MachineLearning, r/artificial, r/SideProject |
| Day 3 | Submit to Product Hunt |
| Day 4 | Open awesome-list PRs (2-3) |
| Day 5 | Write Dev.to article |
| Day 6 | Twitter thread, Discord posts |
| Week 2 | Follow up on awesome-list PRs, engage with comments |
