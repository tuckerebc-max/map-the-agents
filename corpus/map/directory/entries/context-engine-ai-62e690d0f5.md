# context-engine-ai (`context-engine-ai`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Quinnod345
- License: MIT
- Language: TypeScript
- Interface: install=npm install context-engine-ai
- Model providers: OpenAI (embeddings), Local TF-IDF, Anthropic (via MCP clients)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [quinnod345/context-engine](../../repos/quinnod345/context-engine.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight context engine for AI agents that ingests events from any source and builds semantic context with ranked, time-decayed results; requires no vector database or API keys by default; runs as an MCP tool server for Claude Desktop, Cursor, and Windsurf; pluggable storage/embedding adapters

(captured site page body (agents/context-engine-ai.md), not a verified repo-code finding)
Agents that operate over hours lose track of what happened earlier, and the conventional fix - a vector database plus an embedding API - adds infrastructure many projects cannot justify. context-engine-ai packages agent memory as a TypeScript library: callers ingest typed events, query in natural language, and receive ranked, time-decayed results together with a summary string formatted for direct injection into a system prompt. The default stack is SQLite with local TF-IDF embeddings, requiring no vector database, no API keys, and no network access; optional adapters swap in PostgreSQL with pgvector and OpenAI embeddings. The same engine is exposed through a CLI, an HTTP server, and an example MCP server wired for Claude Desktop, Cursor, and Windsurf. Developers building agent memory without infrastructure overhead are the target users, though the project is new with minimal adoption.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/context-engine-ai.md)
