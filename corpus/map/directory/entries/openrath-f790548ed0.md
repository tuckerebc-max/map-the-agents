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
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
