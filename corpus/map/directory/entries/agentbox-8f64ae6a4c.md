# AgentBox (`agentbox`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: madarco
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE, Web; install=npm -g install @madarco/agentbox, then agentbox install
- Model providers: Claude Code, Codex, OpenCode (agent CLIs hosted per box)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [madarco/agentbox](../../repos/madarco/agentbox.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runs multiple coding agents in parallel in sandboxed VMs/containers with one command; teleports entire project (skills, plugins, settings) into dedicated VM/container; sub-second startup from checkpoints; full computer per box (browser, screen sharing, persistent shells, warmed-up VS Code/Cursor); git credentials stay local with permission-gated pushes; supports local Docker and multiple cloud providers (Hetzner, Daytona, Vercel, E2B, DigitalOcean).

(captured site page body (agents/agentbox.md), not a verified repo-code finding)
Running three coding agents on one laptop means shared credentials, clobbered working trees, and contention, so AgentBox gives each agent its own box: a sandboxed VM or container created with one command and loaded with the project's skills, plugins, and settings via a teleport step. Checkpoints make box startup sub-second and auto-pause idle boxes, each box is a full computer with a browser, persistent shells, screen sharing over noVNC, and warmed-up VS Code or Cursor, while git credentials stay on the host with pushes gated behind permissions. Boxes run on local Docker or OrbStack or on cloud providers including Hetzner, Daytona, Vercel, E2B, and DigitalOcean. Developers running several agents in parallel who want isolation without workflow friction are the users.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agentbox.md)
