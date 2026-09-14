# codebase-index-cli (`codebase-index-cli`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: dudufcb1
- License: MIT
- Language: TypeScript
- Interface: install=git clone + run platform install script (./scripts/install.sh on Linux)
- Model providers: OpenAI, OpenAI-compatible (LM Studio, Nebius AI Studio, Together AI), Ollama
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [dudufcb1/codebase-index-cli](../../repos/dudufcb1/codebase-index-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight semantic code indexing engine for AI coding assistants lacking native semantic search; real-time file watching, git commit tracking with LLM analysis, dual storage (SQLite-vec / Qdrant), tree-sitter parsing for 29+ languages, per-vector-store embedder configuration, and Claude Code integration via SessionStart hook.

(captured site page body (agents/codebase-index-cli.md), not a verified repo-code finding)
Codebase-index-cli exists because most coding assistants locate code through text matching, which fails on semantic queries like 'where is rate limiting enforced.' It watches a workspace continuously, parses files with tree-sitter across 29+ languages, and maintains vector indexes in either SQLite-vec for local single-user use or Qdrant for larger deployments, with embedders configurable per store (OpenAI, OpenAI-compatible endpoints such as LM Studio or Together, or Ollama). An experimental layer analyzes git commit history with an LLM, indexing the semantic meaning of changes including retroactive indexing of historical commits. Integration targets Claude Code specifically through a SessionStart hook that launches indexing at session start, and the author ships a companion MCP server so MCP-capable IDEs can query the indexes. The project is small and self-described as experimental, derived from Roo Code's indexer.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codebase-index-cli.md)
