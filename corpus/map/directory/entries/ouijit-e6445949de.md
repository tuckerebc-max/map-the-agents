# ouijit (`ouijit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: ouijit
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=CLI; install=Download prebuilt releases (macOS Apple Silicon/Intel, Linux x64) or build from source (git clone + npm install + npm start; requires Node.js 20+, git, C/C++ build tools)
- Model providers: none (launches whatever agent CLI is configured via hooks, e.g. claude, codex, opencode)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [ouijit/ouijit](../../repos/ouijit/ouijit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Git worktree-based task and terminal session manager for agentic coding; Kanban board, live agent status with notifications, automatic worktree management for parallel workstreams, VM sandboxing for untrusted code, session-aware CLI with JSON output.

(captured site page body (agents/ouijit.md), not a verified repo-code finding)
Parallel agent work on one repository collides over worktrees, ports, and context, and most managers solve it with configuration overhead. Ouijit takes the kanban route: starting a task creates an isolated git worktree via copy-on-write clone that preserves node_modules, attaches a terminal to the card, and provides dev-server runners, web previews, and markdown plan panels alongside. Integration with Claude Code, Codex, Pi, and OpenCode requires no setup because Ouijit shadows the agent binaries on PATH to inject lifecycle hooks, and agents themselves can move cards, create tasks, comment on diffs, and open panels through a session-aware ouijit CLI and local REST API. Per-terminal sandboxing runs commands inside a Lima VM or Seatbelt/Landlock via nono, and all state stays in local SQLite with no account or telemetry. Prebuilt releases cover macOS 13+ and Linux x64 under AGPL-3.0. Developers running parallel agent workstreams who want visual task tracking with sandboxing are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ouijit.md)
