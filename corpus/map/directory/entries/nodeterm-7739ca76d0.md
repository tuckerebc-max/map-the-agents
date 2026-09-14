# nodeterm (`nodeterm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: eneskirca
- License: BUSL-1.1
- Language: TypeScript
- Interface: platforms=CLI, Desktop, Web; install=binary
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes — subagent cards with live transcripts; agents can spawn teams and verify each other's work via canvas-control CLI (yes)
  - hooks: yes — hook-driven status system (pulsing badges, OS notifications, permission prompts, push notifications from SSH hosts) (yes)
  - plan_mode: no (no)

Repository map entry: [eneskirca/nodeterm](../../repos/eneskirca/nodeterm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Spatial infinite canvas for terminals and AI coding agents as draggable nodes; dual canvas/kanban view where cards are live running sessions; three surfaces (desktop, browser Server Edition, iOS companion) sharing the same live tmux sessions.

(captured site page body (agents/nodeterm.md), not a verified repo-code finding)
nodeterm rethinks agent management as spatial layout rather than stacked terminal tabs, placing terminals, agent sessions, editors, and diff views as nodes on a shared canvas. Every project is tmux-backed, so sessions survive app restarts and machine reboots, and group nodes bind to git worktrees to give each agent its own branch. A hook-driven status system surfaces which sessions need attention through badges, notifications, and permission prompts answered in-node, and agents can drive the canvas itself through a built-in control CLI. The same renderer runs as a desktop app, a self-hosted browser server, and an iOS companion over an encrypted relay. Licensing is BUSL-1.1, converting to MIT four years after each release.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nodeterm.md)
