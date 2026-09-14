# lsp-mcp (`lsp-mcp`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: jonrad
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=docker run -i --rm docker.io/jonrad/lsp-mcp:0.3.1 (recommended); or npx -y --silent git+https://github.com/jonrad/lsp-mcp
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [jonrad/lsp-mcp](../../repos/jonrad/lsp-mcp.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): MCP server bridging LSP to MCP, giving AI agents real language-aware code analysis (scope, types, shadowing, etc.) instead of relying on text parsing. Dynamically generates supported LSP methods from JSON schema and supports multiple language servers simultaneously; works with Claude Desktop, Cursor, and MCP CLI Client.

(captured site page body (agents/lsp-mcp.md), not a verified repo-code finding)
AI coding agents working through text search miss the type information, scope analysis, and diagnostics that language servers already compute. lsp-mcp bridges that gap over MCP: agents call tools that proxy into real LSP servers, getting symbol-accurate answers about definitions, references, and errors instead of grep approximations. Because the tool definitions are generated from the LSP JSON Schema, supporting an additional language is configuration rather than new code, and multiple language servers can run side by side with lazy initialization. Claude Desktop, Cursor, and MCP CLI clients are the documented consumers. The author labels it a proof of concept, and development has been minimal since early 2025.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/lsp-mcp.md)
