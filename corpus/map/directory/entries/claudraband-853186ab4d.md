# Claudraband (`claudraband`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: halfwhey
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm (@halfwhey/claudraband)
- Model providers: Anthropic (via bundled Claude Code)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [halfwhey/claudraband](../../repos/halfwhey/claudraband.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Power-user wrapper around the Claude Code TUI (CLI: cband): sessions run in a first-class tmux backend so they persist and can be resumed, pending permission prompts can be answered programmatically (cband prompt --select N), non-interactive runs support sessions like claude -p, an HTTP daemon (cband serve) enables headless remote control, and an ACP server lets editors such as Zed drive ...

(captured site page body (agents/claudraband.md), not a verified repo-code finding)
The project exists because Claude Code's TUI is interactive-first: sessions die with the terminal, and automation means re-prompting by hand. claudraband keeps real Claude Code sessions alive in tmux, records their state under ~/.claudraband, and exposes operations - answer this pending prompt, resume this session, run this prompt non-interactively - as CLI commands, an HTTP API, an ACP server, and a TypeScript library. Nothing about the agent is re-implemented or patched; the bundled Claude Code handles authentication and behavior, which keeps the wrapper robust across upstream changes at the cost of depending on its release cadence. It is experimental, MIT-licensed, and aimed at individual power users rather than SDK users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claudraband.md)
