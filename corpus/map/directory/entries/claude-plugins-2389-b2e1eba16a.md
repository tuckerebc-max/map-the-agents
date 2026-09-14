# 2389 Claude Plugins (`claude-plugins-2389`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: JavaScript
- Interface: platforms=IDE; install=/plugin marketplace add 2389-research/claude-plugins
- Model providers: Claude (via Claude Code)
- Feature flags (directory-reported):
  - mcp_support: yes (includes MCP servers) (yes)
  - plugin_support: yes (28 plugins and MCP servers) (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (multi-agent orchestration plugin) (yes)
  - hooks: yes (TDD, iterative refinement, structured decisions) (yes)
  - plan_mode: yes (structured decision plugins) (yes)

Repository map entry: [2389-research/claude-plugins](../../repos/2389-research/claude-plugins.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Collection of 28 plugins and MCP servers for Claude Code covering TDD, multi-agent orchestration, iterative refinement, binary reverse engineering, structured decisions, and more. Install any skill in one command via the Claude Code plugin marketplace.

(captured site page body (agents/claude-plugins-2389.md), not a verified repo-code finding)
2389 Research's claude-plugins repo is a curated marketplace entry point for their Claude Code ecosystem: 28 plugins and MCP servers installable with a single \`/plugin marketplace add\` command. The collection spans TDD workflows, multi-agent orchestration, iterative refinement (Simmer), binary reverse engineering, structured decision-making, and specialized tools — each running inside Claude Code's existing agent loop rather than defining its own. Individual plugins like Thrifty, Simmer, and Binary RE have their own repos and census entries; this repo is the umbrella that makes them installable as a set. Developers browsing the marketplace pick the skills they need, and Claude Code's plugin system handles discovery, installation, and invocation.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-plugins-2389.md)
