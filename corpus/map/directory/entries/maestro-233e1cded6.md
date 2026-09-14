# maestro (`maestro`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: its-maestro-baby
- License: MIT
- Language: Rust, TypeScript
- Interface: platforms=CLI; install=binary
- Model providers: Anthropic (Claude Code), Google (Gemini CLI), OpenAI (Codex)
- Feature flags (directory-reported):
  - mcp_support: yes (stdio) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [its-maestro-baby/maestro](../../repos/its-maestro-baby/maestro.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Cross-platform desktop application that orchestrates 1-6 AI coding assistants (Claude Code, Gemini CLI, OpenAI Codex) in parallel, running each session simultaneously in its own isolated git worktree to enable true parallel development without merge conflicts. Plugin Marketplace supports Skills, Commands, and MCP servers.

(captured site page body (agents/maestro.md), not a verified repo-code finding)
Parallel agent work usually means juggling terminal tabs and manual branch hygiene, so Maestro provides a Tauri-based desktop grid where each cell is a CLI session bound to its own git worktree, eliminating merge conflicts between concurrent agents on one repository. A visual git graph with diffs shows what each agent changed, quick actions cover running the app, committing, or firing custom prompts at a session, and a plugin marketplace adds skills, commands, and MCP servers. Developers running multiple Claude Code, Gemini CLI, or Codex sessions against the same repository - the 'Bloomberg terminal for CLI agents' workflow - are the target user.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/maestro.md)
