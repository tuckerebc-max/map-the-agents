# ai-doc-gen (`ai-doc-gen`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: agent
- Provider/maker: divar-ir
- License: MIT
- Language: Python
- Interface: install=Claude Code plugin install, pip (uv sync), docker
- Model providers: any OpenAI-compatible (OpenAI, Anthropic-compatible gateways, OpenRouter, local models)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Claude Code plugin) (yes)
  - claude_code_plugin: yes (/plugin marketplace add divar-ir/ai-doc-gen; /plugin install ai-doc-gen@divar) (yes)
  - subagents: yes (5 specialized analysis agents: code structure, data flow, dependencies, request flow, APIs; coordinated by AnalyzerAgent via worker pool) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [divar-ir/ai-doc-gen](../../repos/divar-ir/ai-doc-gen.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Documentation and AI-assistant config files go stale the moment a codebase changes, and most generators produce one-shot summaries with no intermediate evidence. ai-doc-gen runs five specialized analy
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
