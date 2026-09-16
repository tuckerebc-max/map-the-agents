# small-opencode-orchestrator (`small-opencode-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: agent
- Provider/maker: tempont
- License: MIT
- Language: TypeScript
- Interface: install=Clone to ~/.config/opencode, then npm install
- Model providers: DeepSeek V4 Pro / GLM 5.2 (primary agents), DeepSeek V4 Flash (subagents)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [tempont/small-opencode-orchestrator](../../repos/tempont/small-opencode-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
The project is a configuration rather than a binary: cloned into ~/.config/opencode, it defines an orchestrator agent that routes work to plan-runner, code-executor, test-verifier, code-reviewer, docs
Sources: [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
