# coding_agent_session_search (`coding-agent-session-search`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Dicklesworthstone
- License: MIT
- Language: Rust
- Interface: platforms=CLI, IDE; install=brew, binary
- Model providers: Local only (MiniLM all-minilm-l6-v2, FNV-1a hash fallback)
- Feature flags (directory-reported):
  - mcp_support: yes (HTTP) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [dicklesworthstone/coding_agent_session_search](../../repos/dicklesworthstone/coding_agent_session_search.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unified TUI that aggregates and indexes local coding agent history across 24+ agents (Claude Code, Codex, Cursor, Gemini, Aider, ChatGPT, etc.) into a single searchable timeline. Fully local/private with hybrid BM25+vector search, multi-machine SSH sync, self-documenting robot API, token-budgeted answer packs for agent handoffs, and atomic index swaps for crash safety.

(captured site page body (agents/coding-agent-session-search.md), not a verified repo-code finding)
Developers running coding agents accumulate thousands of sessions across different CLIs, and the solutions, dead ends, and context in those sessions become unreachable because each tool stores history in its own format. cass indexes them all into one SQLite-backed archive on the local machine and serves lexical, semantic, and hybrid search through a Rust terminal UI and CLI. Semantic search runs a local MiniLM model with a hash-based fallback, so the index works without network access or API keys, and multi-machine search extends the corpus over SSH and rsync. A JSON robot mode exposes the archive to agents themselves, letting a coding agent query how similar problems were solved before. Individual developers and teams auditing agent activity are the users; the project is in alpha but developed intensively.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coding-agent-session-search.md)
