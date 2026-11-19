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
Sources: [backing feed @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/_data/agents.json)
