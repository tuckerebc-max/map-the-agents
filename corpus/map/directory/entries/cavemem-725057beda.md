# cavemem (`cavemem`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: JuliusBrussee
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=npm
- Model providers: local, ollama, openai (embeddings)
- Feature flags (directory-reported):
  - mcp_support: yes (stdio) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [juliusbrussee/cavemem](../../repos/juliusbrussee/cavemem.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Cross-agent persistent memory for coding assistants. Hooks fire at session boundaries, compress observations with caveman grammar (~75% fewer prose tokens, code/paths preserved byte-for-byte, round-trip expandable), write to local SQLite. Agents query their own history via stdio MCP server (search, timeline, get_observations, list_sessions, enrich). Hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd (Claude Code); partial for Codex, Copilot, Augment; query-only for Cursor/Gemini CLI/Antigravity/IBM ...

(captured site page body (agents/cavemem.md), not a verified repo-code finding)
cavemem exists because coding agents lose context between sessions, forcing them to re-derive decisions and repeat mistakes. It installs hook handlers across nine coding assistants — Claude Code, OpenCode, Codex CLI, GitHub Copilot, and Augment get full capture, while Cursor, Gemini CLI, Antigravity, and IBM Bob get query-only access — and fires at session boundaries to compress observations before writing them to a local SQLite database. Agents retrieve their own history through an MCP server exposing search, timeline, and observation tools, with hybrid FTS5 keyword and vector search over the store. All data stays local by default, with embeddings handled by a local provider, Ollama, or OpenAI, and private blocks redacted before compression. The project froze in August 2026, with its compressed-memory core carried forward in the author's actively developed caveman repository.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/cavemem.md)
