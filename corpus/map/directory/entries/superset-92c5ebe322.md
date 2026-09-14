# Superset (`superset`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: multiplexer
- Provider/maker: superset-sh
- License: Elastic License 2.0 (ELv2)
- Language: TypeScript (Bun, React, Electron)
- Interface: platforms=CLI, IDE; install=brew
- Model providers: OpenRouter, Bedrock, Vertex, Vercel AI Gateway (BYO providers); Claude, OpenAI/Codex, Gemini, Grok, Mistral, Kimi
- Feature flags (directory-reported):
  - mcp_support: yes (MCP server; transport not specified) (yes)
  - plugin_support: yes (custom agents, skills, terminal presets, themes) (yes)
  - claude_code_plugin: yes (fully supported agent; .claude-plugin and .claude directories present) (yes)
  - subagents: yes (.agents directory; built-in orchestration skills for parallel agents) (yes)
  - hooks: yes (setup/teardown/run scripts) (yes)
  - plan_mode: yes (inline tool approvals and plan review) (yes)

Repository map entry: [superset-sh/superset](../../repos/superset-sh/superset.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Superset is structured around the workflow of running many CLI agents at once: every agent works in its own git worktree with an isolated branch and terminal, the app provides diff viewing, in-app bro
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
