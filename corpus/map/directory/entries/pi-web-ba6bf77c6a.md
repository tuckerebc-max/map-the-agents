# pi-web (`pi-web`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: jmfederico
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=npm
- Model providers: whatever the host pi runtime supports (multi-provider via pi)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [jmfederico/pi-web](../../repos/jmfederico/pi-web.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Keeps Pi Coding Agent sessions persistently alive in real workspaces on your machine or server; sessions survive browser disconnects; supervise multiple parallel sessions from any browser/device; remote-first design with fleet/machine management

(captured site page body (agents/pi-web.md), not a verified repo-code finding)
pi-web addresses the fragility of terminal-based coding agents: close the laptop and the session dies, and supervising several parallel runs means juggling terminals. The server hosts pi sessions in real workspaces on the user's machine or server, so browser disconnects never interrupt the agent, and any browser or device can attach to a running session or start a new one. Fleet management treats other pi-web runtimes as remote machines, proxying projects, files, git state, terminals, and settings through one control surface; access runs over private networks, SSH tunnels, or trusted reverse proxies since the system is explicitly not a multi-tenant sandbox. Trusted browser plugins and sessiond-backed workspace providers extend the platform. Developers running pi on headless boxes or across several machines use it as the durable control surface for those sessions.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-web.md)
