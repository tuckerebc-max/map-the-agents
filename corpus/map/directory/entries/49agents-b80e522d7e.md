# 49IDE (`49agents`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: alpbahadur
- License: BSL-1.1 (free for individuals and small teams; converts to MIT 2030-02-26)
- Language: JavaScript
- Interface: platforms=Desktop, Web; install=Self-host via ./49ctl setup and ./49ctl start (localhost:1071), or download the macOS desktop app (.dmg)
- Model providers: delegates to the connected agent CLIs
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [alpbahadur/49agents](https://github.com/alpbahadur/49agents) (source: backing, field: `source_code_url`) now resolves to [alpbahadur/49-ide](../../repos/alpbahadur/49-ide.md) (github id 1168100167, verified [https://github.com/alpbahadur/49-IDE](https://github.com/alpbahadur/49-IDE)).

## Description

Highlight (site page `what_makes_it_special`): The first 2D agentic IDE: an infinite zoomable canvas where terminals, agents, files, git graphs, and issue tables are panes you place anywhere, running real tmux sessions via ttyd, with broadcast input typing into many terminals at once and multi-machine agents connecting over WebSocket through a relay with no SSH.

(captured site page body (agents/49agents.md), not a verified repo-code finding)
49Agents bills itself as the first 2D agentic IDE — all agents, all terminals, all projects, all machines, one unified space. Instead of tabs and splits, panes live on an infinite zoomable canvas you arrange freely with the layout persisting: real tmux sessions served through ttyd run Claude Code, Codex, and other agent CLIs in their native form, alongside a Monaco editor, git graphs, Beads interactive issue tables, and markdown notes. Broadcast input types once into many terminals simultaneously, which is the key move for steering a fleet of agents, and agents on different machines — MacBook, PC, cloud VMs — all connect through a WebSocket relay with a HUD showing CPU, RAM, and API usage across machines, reachable from phone, tablet, or laptop via Tailscale, LAN, or the hosted relay with no terminal data stored server-side. It ships as a self-hosted Node/TypeScript web stack, a macOS desktop app, or an upcoming hosted version at 49agents.com.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json); [site page @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/agents/49agents.md)
