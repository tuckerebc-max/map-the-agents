# deepclaude (`deepclaude`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: aattaran
- License: MIT
- Language: Shell
- Interface: platforms=Autonomous; install=binary
- Model providers: DeepSeek, OpenRouter, Fireworks AI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aattaran/deepclaude](../../repos/aattaran/deepclaude.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Swaps Claude Code's model backend while keeping its full autonomous agent loop (file editing, bash, git, subagents), achieving the same UX at ~17x lower cost with DeepSeek. Features live mid-session model switching via slash commands and automatic DeepSeek context caching.

(captured site page body (agents/deepclaude.md), not a verified repo-code finding)
deepclaude addresses the cost problem of running Claude Code for heavy daily use: it leaves the agent's loop, tools, and subagent machinery untouched and routes the model calls to DeepSeek V4 Pro through a local proxy, cutting output-token cost from $15/M to about $0.87/M. A localhost proxy (port 3200) intercepts requests, supports switching between DeepSeek, OpenRouter, Fireworks, and Anthropic mid-session via slash commands or keybindings, and exposes cost and benchmark endpoints. Users keep Claude Code's file editing, bash, git, and subagent behavior while trading away vision input, MCP server tools, and some complex-reasoning quality. It appeals to individual developers and teams running large volumes of agentic sessions who want the Claude Code UX without Anthropic pricing.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepclaude.md)
