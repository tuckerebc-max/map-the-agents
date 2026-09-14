# agentsync (`agentsync`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: dallay
- License: MIT
- Language: Rust, TypeScript
- Interface: platforms=CLI; install=npm install -g @dallay/agentsync; or cargo install agentsync; or GitHub Releases binaries
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [dallay/agentsync](../../repos/dallay/agentsync.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fast portable CLI that synchronizes AI agent configurations and MCP servers across multiple AI coding assistants (Claude Code, Gemini CLI, Cursor, Copilot, Codex, OpenCode) using symlinks from a single source of truth in .agents/.

(captured site page body (agents/agentsync.md), not a verified repo-code finding)
Teams running several AI assistants must keep CLAUDE.md, .cursor/rules, copilot-instructions.md, and per-tool MCP configs in sync by hand. AgentSync makes .agents/ the single source of truth — agentsync.toml, AGENTS.md, commands, skills, and prompts — and generates each tool's native files from it, with MCP servers defined once and emitted as .mcp.json, .codex/config.toml, .gemini/settings.json, and equivalents. Symlink-based targets (symlink, symlink-contents, nested-glob for monorepos, module-map) mean edits take effect without re-running a copy step, and existing files are backed up before replacement. A Rust core ships as a single static binary behind an npm wrapper, with commands for init, apply, status, clean, doctor, and skill management. Cross-platform support includes a documented Windows symlink setup path.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentsync.md)
