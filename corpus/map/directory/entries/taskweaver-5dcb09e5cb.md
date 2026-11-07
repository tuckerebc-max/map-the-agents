# TaskWeaver (`taskweaver`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: microsoft
- License: MIT
- Language: Python
- Interface: install=pip, docker
- Model providers: OpenAI, Azure OpenAI, local LLMs
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [microsoft/taskweaver](../../repos/microsoft/taskweaver.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Code-first agent framework for data analytics: it interprets user requests through code snippets and orchestrates plugins (functions) to execute analytics tasks in a stateful manner. Preserves both chat history AND code execution history including in-memory data (e.g., DataFrames), verifies generated code before execution, supports reflective execution, and runs code in isolated containers by default. Repository was archived by the owner ...

(captured site page body (agents/taskweaver.md), not a verified repo-code finding)
Microsoft's TaskWeaver addressed data-analytics automation by making generated code the medium of planning and execution: user requests became Python snippets orchestrated with YAML-defined plugins, executed in stateful sessions that retained DataFrames and other in-memory results across turns. Execution defaulted to an isolated Docker container, generated code was verified before running, and a reflective loop corrected failures; multi-agent extension, experience memory, and AgentOps observability rounded out the framework. It served data scientists and analysts running analytics pipelines — SQL pulls, anomaly detection, forecasting with libraries like yfinance — through CLI, web UI, or library embedding. The repository was archived on March 23, 2026 and is read-only, so the project is no longer developed; it remains a reference implementation of the code-first agent pattern.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/taskweaver.md)
