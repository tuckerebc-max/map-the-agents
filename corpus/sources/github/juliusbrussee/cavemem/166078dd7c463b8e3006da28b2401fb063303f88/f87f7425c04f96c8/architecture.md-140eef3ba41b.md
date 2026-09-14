# Architecture

## Flow

```
IDE ── hooks ──▶ CLI `hook run`
                     │
                     ▼
              MemoryStore (core)
            ┌──────────┴──────────┐
            ▼                     ▼
       compress (prose)      Storage (SQLite + FTS5 + embeddings)
                                   ▲
                                   │
IDE ── MCP stdio ──▶ mcp-server ───┘
Browser ── HTTP ──▶ worker (Hono) ─┘
```

## Write path

1. Hook receives input from IDE.
2. CLI invokes `runHook(name, input)`.
3. `redactPrivate` strips `<private>` content.
4. `compress` transforms prose; technical tokens pass through.
5. `Storage.insertObservation` commits to SQLite; FTS5 is updated via triggers.
6. Embedding, when enabled, is computed out-of-band by the worker.

## Read path

- **Model (MCP)**: compact search → `get_observations(expand: true)` returns readable text.
- **Human (viewer)**: worker serves expanded text over HTTP on `127.0.0.1:37777`.

## Invariants

- Only `MemoryStore` may write observations.
- Only `@cavemem/storage` may open the database.
- Hooks do no I/O beyond the `MemoryStore` call.
- Worker binds to loopback only.
