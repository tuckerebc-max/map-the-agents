# claude-orchestration (`claude-orchestration`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: mbruhler
- License: MIT
- Language: unknown
- Interface: install=/plugin marketplace add mbruhler/claude-orchestration; /plugin install orchestration@mbruhler
- Model providers: Anthropic (via Claude Code)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mbruhler/claude-orchestration](../../repos/mbruhler/claude-orchestration.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Multi-agent workflow orchestration plugin for Claude Code; chain AI agents to automate complex tasks using natural language or declarative .flow syntax. Markdown-based plugin with built-in agents (Explore, Plan, general-purpose), custom agents importable from ~/.claude/agents/, temp agents.

(captured site page body (agents/claude-orchestration.md), not a verified repo-code finding)
The plugin brings data-pipeline ergonomics to agent work: instead of re-prompting Claude Code through each step of a multi-stage task, users describe a workflow in natural language or .flow syntax, and the plugin decomposes it into chained sub-agent invocations with captured outputs feeding later steps. Temp agents handle concrete steps like scraping or database queries; @review checkpoints pause for human input; state snapshots let crashed workflows resume; and .flow.test files allow dry-run unit testing of workflows. Everything runs through the Claude Code plugin system with no separate runtime. Developers automating scraping, reporting, and multi-repo chores install it from the plugin marketplace.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/claude-orchestration.md)
