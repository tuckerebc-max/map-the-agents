# LocoOperator (`locooperator`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: agent
- Provider/maker: LocoreMind
- License: MIT
- Language: Python
- Interface: install=git clone + uv sync; requires Claude Code (npm install -g @anthropic-ai/claude-code), llama.cpp, and an OpenRouter API key
- Model providers: OpenRouter (cloud fallback); local llama.cpp (GGUF)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: yes (yes)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [locoremind/locooperator](../../repos/locoremind/locooperator.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
The project targets the cost profile of Claude Code sessions, where every cheap exploration subagent still bills API tokens. A local proxy intercepts Claude Code's subagent dispatches (which would oth
Sources: [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
