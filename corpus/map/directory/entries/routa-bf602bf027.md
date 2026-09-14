# routa (`routa`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: phodal
- License: MIT
- Language: TypeScript
- Interface: platforms=Desktop, Web; install=npm
- Model providers: BYOK (normalized through adapters)
- Feature flags (directory-reported):
  - mcp_support: yes (MCP, ACP, A2A, AG-UI, A2UI, REST, SSE) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (webhooks and schedules for automation) (yes)
  - plan_mode: yes (yes)

Repository map entry: [phodal/routa](../../repos/phodal/routa.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Workspace-first multi-agent coordination platform that uses a Kanban board as both planning surface and coordination bus, with each lane backed by a different specialist prompt with increasingly strict evidence contracts. The review boundary is a real gate. Works in local-first desktop mode or self-hosted web mode.

(captured site page body (agents/routa.md), not a verified repo-code finding)
Routa treats software delivery as a board rather than a chat: work enters as cards, moves through Backlog, Todo, Dev, Review, and Done lanes, and each lane's agent operates under the constraints and evidence requirements that lane defines. Sessions stream live, can be reconnected after interruption, and expose traces for inspection, while worktree management keeps parallel agents from colliding in one checkout. Schedules, webhooks, and background tasks drive unattended runs, and GitHub repositories can be imported as virtual workspaces without a local clone. Teams use it to enforce stage discipline on multi-agent delivery — the coordinator splits work, crafters implement, and verifiers gate the merge — with MIT-licensed desktop and web builds.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/routa.md)
