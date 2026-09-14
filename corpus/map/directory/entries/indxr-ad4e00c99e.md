# indxr (`indxr`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: bahdotsh
- License: MIT
- Language: Rust
- Interface: install=cargo install indxr --features wiki (via crates.io), or build from source via git clone + cargo build
- Model providers: Anthropic, OpenAI
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [bahdotsh/indxr](../../repos/bahdotsh/indxr.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fast codebase indexer and self-updating knowledge wiki for AI agents, backed by a structural index (tree-sitter AST parsing for 8 languages + regex for 19 more). Provides 26 MCP tools plus 9 wiki MCP tools, token-aware progressive truncation, git structural diffing, dependency graphs, complexity hotspot analysis, monorepo support, and one-command setup for multiple AI agents. Agents can record failure patterns ...

(captured site page body (agents/indxr.md), not a verified repo-code finding)
indxr gives coding agents durable knowledge instead of forcing them to re-derive a codebase every session. The structural index combines tree-sitter ASTs with regex extraction for 27 languages, exposing symbol lookup, caller tracing, and complexity hotspots through MCP. On top sits a Markdown wiki in .indxr/wiki/ that agents both read and write: \`wiki_record_failure\` logs mistakes so later agents avoid them, and \`wiki_compound\` merges new findings into existing pages. Watch mode regenerates pages automatically using Anthropic or OpenAI keys. One-command setup wires it into Claude Code, Cursor, Windsurf, and Codex CLI.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/indxr.md)
