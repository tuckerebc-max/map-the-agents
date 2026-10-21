# Loopsy (`loopsy`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: leox255
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI, Mobile; install=npm (loopsy); relay self-hosted via npx @loopsy/deploy-relay
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [leox255/loopsy](../../repos/leox255/loopsy.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): It pairs a Flutter mobile app with a machine-resident daemon over a self-hostable Cloudflare Worker relay (npx @loopsy/deploy-relay, no port forwarding), giving full PTY terminal control of Claude Code, Codex, or any shell from a phone, plus an mDNS-paired LAN mode where agents exchange commands, files, and context across machines over MCP.

(captured site page body (agents/loopsy.md), not a verified repo-code finding)
Long-running agent sessions strand developers at their desks, and loopsy solves the away-from-keyboard problem: a daemon on the workstation bridges to the user's phone through a Cloudflare relay that can be the maintainer's or self-hosted on the free tier in about thirty seconds. The mobile client renders a real PTY terminal with ANSI, scrollback, and resize, so TUI-based agents work normally, and sessions survive phone locks and signal loss. Its second mode is agent-to-agent: daemons discover each other via mDNS on a LAN, pair with a 6-digit code, and expose MCP tools so an agent on one machine can run commands, transfer files, or share key/value context on another - for example, dispatching an iOS build to a Mac Studio from a laptop session. Developers running Claude Code, Codex, or Gemini CLI across multiple machines use it as the connective layer.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/loopsy.md)
