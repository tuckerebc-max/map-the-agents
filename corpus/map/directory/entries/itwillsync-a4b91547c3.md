# itwillsync (`itwillsync`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: shrijayan
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE, Web; install=npx itwillsync \<command\> (Node.js 20+)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [shrijayan/itwillsync](../../repos/shrijayan/itwillsync.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Syncs any terminal-based AI coding agent to your phone over a local network (WiFi/Tailscale/localhost); privacy-first E2E encrypted with per-session NaCl secretbox tokens, zero cloud/accounts/telemetry; multi-session dashboard with attention detection and sleep prevention; agent-agnostic (works with Claude Code, Aider, Codex, Goose, Cline, Copilot CLI, or any terminal tool).

(captured site page body (agents/itwillsync.md), not a verified repo-code finding)
itwillsync answers a small but constant pain: your agent is working, but you are not at the desk. It wraps the agent command in a PTY, streams the terminal over an encrypted WebSocket, and renders it in a mobile browser after a QR scan — approve prompts, type commands, and watch output from a phone. A hub daemon tracks all running sessions with attention detection and can keep the machine awake during long runs. Everything stays on the local network or Tailscale, encrypted end-to-end with per-session NaCl keys and no accounts. It is deliberately agent-agnostic plumbing rather than an agent itself.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/itwillsync.md)
