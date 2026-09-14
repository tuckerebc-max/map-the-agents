# SymDex (`symdex`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: husnainpk
- License: MIT
- Language: Python
- Interface: install=pip install symdex (or uv tool install symdex / uvx symdex); optional extras: symdex\[local\], symdex\[voyage\], symdex\[voyage-multimodal\]
- Model providers: Local sentence-transformers, Voyage, OpenAI-compatible /embeddings, Gemini Embedding (embedding backends)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: n/a (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [husnainpk/symdex](../../repos/husnainpk/symdex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Repo-local symbolic indexing engine turning a checked-out repo into a local SQLite knowledge base of symbols, routes, relations, docs, tests, and context. Provides 21 MCP tools, HTTP route extraction across 10+ frameworks, call graph traversal, token-budgeted context packs, and ROI/token-savings reporting via both CLI and MCP without requiring a hosted index.

(captured site page body (agents/symdex.md), not a verified repo-code finding)
SymDex exists because agents burn context reading whole files when they need one definition or call site. It indexes a checked-out repository into a local SQLite database: exact symbols with byte offsets, file and repo outlines, HTTP routes extracted across a dozen web frameworks, caller/callee graphs, docs, and tests, spanning roughly 20 language surfaces via tree-sitter. Agents reach it through an MCP server (21 tools, stdio or HTTP) or a CLI, and an installable skill teaches agents to query the index instead of browsing files; retrieval is token-budgeted so a context pack fits the model's budget, and everything runs locally with optional sentence-transformers or Voyage embeddings. Reports of token savings and index ROI are built in. Developers wiring their own agents to precise, hosted-service-free codebase retrieval are the intended users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/symdex.md)
