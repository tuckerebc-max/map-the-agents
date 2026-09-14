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
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/freshell.md)
