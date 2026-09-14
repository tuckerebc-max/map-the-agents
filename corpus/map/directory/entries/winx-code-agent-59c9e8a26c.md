# winx-code-agent (`winx-code-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: gabrielmaialva33
- License: MIT
- Language: Rust
- Interface: install=cargo install winx-code-agent (Rust 1.88+); also GitHub Release .tar.gz bundles and build from source
- Model providers: None — MCP tool server for any MCP client (Claude Code, Codex, Cursor, ChatGPT)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: True (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: no (no)

Repository map entry: [gabrielmaialva33/winx-code-agent](../../repos/gabrielmaialva33/winx-code-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native Rust (not a Python wrapper) remote MCP runtime for coding agents with durable daemon architecture (winxd + winx-guardian per session). Sessions survive HTTP disconnects, client restarts, and adapter upgrades. Agent-native terminal semantics (real PTY, Ctrl+C, interactive TUIs), tree-sitter code navigation across 11 languages, robust SEARCH/REPLACE editing tolerant of LLM mistakes, token-budgeted output compression, and secret redaction by default.

(captured site page body (agents/winx-code-agent.md), not a verified repo-code finding)
winx-code-agent provides durable, remote-first tool access for coding agents that connect over MCP: real PTY shell sessions survive HTTP disconnects, client restarts, and adapter upgrades because a separate winxd daemon and per-session winx-guardian process own the shell. It exposes a configurable tool catalog (BashCommand, ReadFiles, EditFiles with search_replace/line_patch/undo, tree-sitter CodeMap across 13 languages, ContextSave, ReadImage) over Streamable HTTP for hosted agents or stdio for local clients like Claude Code and Cursor, with workspace modes ranging from full access to read-only architect mode. Beginning as a Rust port of WCGW, it is hardened with fuzz tests, loom model checking, SBOM attestations, secret redaction, and an opt-in Landlock sandbox. It is a tool server for agents rather than an agent itself, MIT-licensed, and installable via cargo.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/winx-code-agent.md)
