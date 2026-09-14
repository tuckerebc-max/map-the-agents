# Warp (`warp`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: warpdotdev
- License: MIT (UI framework), AGPL-3.0 (rest)
- Language: Rust
- Interface: platforms=CLI, Desktop; install=Download from https://www.warp.dev/download, or build from source (./script/bootstrap && ./script/run)
- Model providers: OpenAI, supports external agents (Claude Code, Codex, Gemini CLI)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [warpdotdev/warp](../../repos/warpdotdev/warp.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic development environment born from the terminal. Combines a modern terminal with AI-powered coding agent capabilities and support for external CLI agents (Claude Code, Codex, Gemini CLI). Client codebase is open source.

(captured site page body (agents/warp.md), not a verified repo-code finding)
Warp began as a modern terminal and grew into an agentic development environment for running fleets of coding agents across the software lifecycle. Work is defined as factories-as-code — factory.yaml plus agent files specifying triggers, agent types, models, permissions, and approval gates — and work flows in from Slack, Teams, Linear, Jira, and GitHub, with runs steerable from web, mobile, terminal, or IDE. A quality loop runs evals on a team's own work, cross-model benchmarks, and self-improvement in which observer agents open PRs against the factory config itself. Warp supports MCP servers in both local and cloud agents, exposes its own MCP server, and works with any MCP-capable harness including Claude Code and Codex. Pricing is credit-based per agent run across Free, Build ($20), Max, Business, and Enterprise tiers, with self-hosted-VPC options.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/warp.md)
