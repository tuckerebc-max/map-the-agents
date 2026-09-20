# Ai-Agent-Security (`ai-agent-security`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: SecurityLab-UCD
- License: unknown
- Language: Python
- Interface: install=source ./env.sh && pip install -r requirements.txt && cd HE_data && python HE_data.py && cd ../
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [securitylab-ucd/ai-agent-security](../../repos/securitylab-ucd/ai-agent-security.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Agents that handle sensitive data leak it through prompts and context, and this repository explores one defensive idea: run the agent's reasoning over homomorphically encrypted values so the LLM never
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
