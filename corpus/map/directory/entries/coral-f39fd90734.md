# CORAL (`coral`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: Human-Agent-Society
- License: Apache-2.0
- Language: Python
- Interface: platforms=Autonomous; install=pip
- Model providers: LiteLLM gateway (custom models); supported agents: Claude Code, Codex, Cursor, Kiro, OpenCode
- Feature flags (directory-reported):
  - mcp_support: no — explicitly described as a skills-first bundle (no MCP) (no)
  - plugin_support: yes — plugin system installable in Claude Code and Codex; marketplace Human-Agent-Society/CORAL (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes — coral-task-author (autonomously scaffolds tasks) and coral-run-doctor (triages stuck runs) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [human-agent-society/coral](../../repos/human-agent-society/coral.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Running one coding agent against a benchmark is straightforward; running populations of agents that build on each other's results without contaminating evaluation is not, and CORAL supplies that subst
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
