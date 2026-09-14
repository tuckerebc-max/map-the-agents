# pocketshell (`pocketshell`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Big-Pony
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/Big-Pony/pocketshell/main/install.sh | sh; or download binary from Releases; or build from source with Bun
- Model providers: whatever agents the user runs on the host (Claude Code, Codex, opencode, Kimi CLI)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [big-pony/pocketshell](../../repos/big-pony/pocketshell.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted mobile-first remote terminal for running CLI/TUI AI coding agents (Claude Code, Codex, opencode, Kimi CLI) or plain shell/vim/htop from a phone browser; resilient sessions with precise replay on reconnect, push notifications when an agent finishes or needs input, single zero-dependency binary, end-to-end encryption (Noise IK).

(captured site page body (agents/pocketshell.md), not a verified repo-code finding)
pocketshell exists for the moment a long-running coding agent needs attention while the developer is away from the desk: it turns a phone browser into a resilient terminal onto the dev machine's tmux sessions, where agents like Claude Code, Codex, opencode, or Kimi CLI run alongside plain shell, vim, and htop. Sessions persist server-side, so a dropped connection loses nothing — on reconnect the terminal replays exactly the missing gap of output — and push notifications arrive even with the phone locked when an agent finishes or blocks on input. Setup is a single Bun-built binary plus a pairing string with a 300-second TTL; optional integration writes hook/notify entries into each agent's config (Claude Code settings, etc.) for finish-and-notify events, and delivery spans Web Push and webhooks to WeCom, Feishu, Slack, and Discord. Security got attention the hard way: a web admin page was removed in v1.8.0 over an anonymous-access vulnerability, with audit guidance for older deployments. Self-hosting developers who want phone-based agent supervision without a cloud relay are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pocketshell.md)
