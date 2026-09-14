# supaterm (`supaterm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: supabitapp
- License: Elastic License 2.0
- Language: Swift
- Interface: platforms=CLI
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [supabitapp/supaterm](../../repos/supabitapp/supaterm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A terminal designed for the coding agents age. Integrates with Claude Code, Codex, and Pi coding agents via a hook-based settings bridge (Claude/Codex) and extension package (Pi). Injects pane context into terminal processes, routes structured agent events through the 'sp' CLI over a socket, and manages UI state (tab activity, notifications, session binding). Features terminal phase detection and session-identity model ...

(captured site page body (agents/supaterm.md), not a verified repo-code finding)
supaterm rethinks the terminal for developers whose primary 'applications' are coding agents. Rather than embedding agents, it bridges into them: hook-based settings injection for Claude Code and Codex, an extension package for Pi, and a shared session-identity model so the terminal can bind panes to agent sessions, track phase (working, waiting, done), and surface notifications and tab activity accordingly. Agents receive pane context injected through settings bridges, and structured events flow back to the app over a socket controlled by the sp CLI. Theming, session management, and integration docs live in the repository, and the same team ships the supacode worktree manager. Development is fast-moving (2,500+ commits) under the Elastic License 2.0.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/supaterm.md)
