# Prime Agent (`prime-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: PrimeIntellect-ai
- License: MIT
- Language: TypeScript (TUI), Python (agent runtime)
- Interface: platforms=Autonomous, CLI, IDE; install=binary
- Model providers: subscription and API-key (BYOK) providers via /login
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (skills as importable Python packages) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (rlm(...) spawns child agents for parallel/background work) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [primeintellect-ai/prime-agent](../../repos/primeintellect-ai/prime-agent.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Prime Agent exists because long tasks break harnesses that hold all context in a shrinking window: it instead puts the model in a persistent IPython REPL where the prompt is a variable, tools are func
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
