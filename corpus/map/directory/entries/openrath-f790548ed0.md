# OpenRath (`openrath`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: Rath-Team
- License: BSD-3-Clause
- Language: Python
- Interface: install=pip
- Model providers: OpenAI, Anthropic (OpenAI-compatible providers)
- Feature flags (directory-reported):
  - mcp_support: yes — stdio MCP tools adapted into the loop as FlowToolCall instances (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes — multi-agent collaboration; agents share session state; sessions can be forked/merged across agents with lineage tracking (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [rath-team/openrath](../../repos/rath-team/openrath.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=

## Description

(published index `description`, not a verified repo-code finding)
Multi-agent frameworks typically ask developers to express workflows in graphs or YAML, which hides control flow behind DSLs and makes state hard to inspect. OpenRath instead imports PyTorch's vocabul
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
