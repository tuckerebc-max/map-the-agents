# Datasette Agent (`datasette-agent`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: datasette
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI, Web; install=datasette install datasette-agent
- Model providers: OpenAI, Anthropic, Google Gemini, and any tool-calling model with an LLM plugin, including local models
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [datasette/datasette-agent](../../repos/datasette/datasette-agent.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): It works with hundreds of tool-calling models, any model with an LLM plugin, and other Datasette plugins can register extra tools for it. With the Datasette Apps plugin installed alongside it, it can also build HTML applications that run in sandboxed frames against your databases.

(captured site page body (agents/datasette-agent.md), not a verified repo-code finding)
Datasette Agent is an open-source plugin that puts a conversational assistant inside Datasette, the tool for exploring and publishing SQLite databases. Installed next to Datasette, it serves a chat at /-/agent and a \`datasette agent chat\` mode in the terminal, where the model calls tools to inspect schemas, write and run SQL, and save what it wrote as a Datasette stored query. Write statements and saved queries are shown in full and run only after the person approves them, through Datasette's own permissions, and explorer reports and background agents run toward a goal without further input. Announced in May 2026 and still in alpha releases, it is aimed at people who already keep data in Datasette and want to ask questions of it without leaving the browser.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/datasette-agent.md)
