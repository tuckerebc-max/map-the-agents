# tlbx (`tlbx`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: tlbx-ai
- License: AGPL-3.0
- Language: .NET 10 Native AOT, TypeScript, xterm.js
- Interface: platforms=CLI, Desktop, Web; install=curl -fsSL https://get.tlbx.ai/install.sh | bash (macOS/Linux); irm https://get.tlbx.ai/install.ps1 | iex (Windows); npx @tlbx-ai/midterm for ephemeral trial
- Model providers: Agent CLIs (Codex, Claude Code, Gemini CLI, Grok Build, OpenCode, Copilot CLI, Antigravity CLI)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [tlbx-ai/tlbx](../../repos/tlbx-ai/tlbx.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Browser is the control surface, not the runtime-agents, PTYs, tests, and servers persist across browser disconnects/device changes; one independent instance per host; works with any terminal app not just agents; private remote access via Tailscale/WireGuard (no cloud relay); runs multiple agents simultaneously on same project

(captured site page body (agents/tlbx.md), not a verified repo-code finding)
tlbx (formerly MidTerm) is a self-hosted terminal multiplexer whose browser UI is only a control surface: close the tab, switch devices, or lose connectivity and the underlying PTYs, tests, servers, and agent sessions keep running on the host, ready to reattach from any device. Each host runs one independent instance, so there is no central cloud — remote access goes over the user's own network path, with Tailscale or WireGuard recommended and Cloudflare Tunnel or plain LAN also supported, keeping repositories and credentials on the host. Two session types coexist in a workspace: real persistent PTYs running any shell or terminal program, and Agent Controller sessions that give structured UI (turns, tool calls, diffs, approvals) to ACP-speaking coding agents such as Codex, Grok Build, OpenCode, Gemini CLI, and Copilot CLI, while multiple agents can work the same project concurrently. The implementation is .NET 10 Native AOT with an xterm.js frontend, AGPL-3.0 licensed with commercial licensing available, and installers cover macOS, Linux, and Windows. Developers who run long-lived agent sessions across several machines and refuse to route them through a vendor cloud are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tlbx.md)
