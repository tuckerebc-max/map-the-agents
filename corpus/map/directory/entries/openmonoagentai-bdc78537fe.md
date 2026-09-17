# OpenMonoAgent.ai (`openmonoagentai`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: StartupHakk
- License: AGPL-3.0
- Language: C# / .NET 10
- Interface: platforms=CLI; install=binary - one-command curl install script
- Model providers: Local llama.cpp (default), OpenAI (WIP), Anthropic (WIP), Ollama (WIP)
- Feature flags (directory-reported):
  - mcp_support: yes - stdio; auto-detects code-review-graph MCP server, configurable in settings.json (yes)
  - plugin_support: yes - Playbooks (YAML workflows) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes - 5 specialist sub-agents (Explore, Plan, Coder, Verify, general-purpose) (yes)
  - hooks: yes - pre/post hooks in 12-step tool pipeline (yes)
  - plan_mode: yes - plan-mode guard + dedicated Plan sub-agent (yes)

Repository map entry: [startuphakk/openmonoagent.ai](../../repos/startuphakk/openmonoagent.ai.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Local-first coding agents usually stop at supporting whatever inference server the user happens to run, leaving setup as the user's problem. OpenMono bundles the whole stack: a .NET 10 CLI paired with
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
