# freshell (`freshell`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: danshapiro
- License: MIT
- Language: TypeScript, Rust
- Interface: platforms=IDE; install=git clone --branch v0.7.5, npm install, npm run serve (Node.js 18+, 20+ recommended)
- Model providers: Claude Code, Codex, OpenCode, Gemini, Kimi, Amplifier
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [danshapiro/freshell](../../repos/danshapiro/freshell.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): The 'loving child of tmux and Claude Code': an agentic IDE that unifies coding agents, shells, editors, and browsers into a tabbed/paned workspace across desktop, laptop, and phone (VPN/Tailscale); cross-device session resumption ('speak with the dead' - resume any Claude/Codex/OpenCode session from any device); Freshclaude interactive alternative to Claude CLI with rich chat UI; Stream Deck hardware integration; extension system ...

(captured site page body (agents/freshell.md), not a verified repo-code finding)
Agent CLI sessions are normally trapped in one terminal on one machine, which breaks when work spans a desk machine, a laptop, and a phone. Freshell is a self-hosted web workspace (React front end over node-pty) that hosts Claude Code, Codex, OpenCode, Gemini, and Kimi sessions alongside shells, editors, and browser panes, indexes their session histories, and lets any device resume a session where it left off. Agents can configure the workspace themselves through an extension API that creates tabs, panes, browsers, and subagents programmatically, and a Freshclaude chat UI wraps the Claude CLI with a richer interface. It is MIT-licensed, installed from source with Node 18+, and used by developers who juggle several agent CLIs across devices.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/freshell.md)
