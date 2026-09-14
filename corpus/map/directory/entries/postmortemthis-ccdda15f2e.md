# postmortemthis (`postmortemthis`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Softeria
- License: MIT
- Language: Rust, Shell
- Interface: platforms=CLI; install=Paste a prompt into your coding agent (Claude Code, Codex, etc.) to create a /postmortemthis skill that downloads postmortemthis.cmd from GitHub Releases; run via echo '...' | sh postmortemthis.cmd. Supports Windows, macOS, Linux.
- Model providers: Claude Code, Codex, Antigravity, Qwen, Vibe, Grok, Gemini, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [softeria/postmortemthis](../../repos/softeria/postmortemthis.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): One tiny script with zero setup runs every major coding agent simultaneously in read-only mode to cross-review your diff and deliver a unified ship/no-ship verdict; no server, no MCP, uses your own provider logins. Antigravity (which lacks a read-only switch) enforces read-only via plan mode.

(captured site page body (agents/postmortemthis.md), not a verified repo-code finding)
Postmortemthis starts from the observation that the agent which wrote your code is the worst judge of it, so a diff deserves review by models that had no hand in producing it. Piping one prompt into its small Rust launcher fans the review out to Claude Code, Codex, Antigravity, Qwen, Vibe, and Grok in parallel, each forced read-only through its own CLI flags so the working tree cannot change mid-run. There is deliberately no server, no MCP, and no resold access: agents you are logged into review directly, and OpenRouter covers the rest through a setup subcommand. Results aggregate into a single ship or no-ship call before a real postmortem happens. It is aimed at developers who already run several agent CLIs and want cross-model second opinions with zero setup.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/postmortemthis.md)
