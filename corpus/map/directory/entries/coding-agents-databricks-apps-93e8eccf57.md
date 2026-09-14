# coding-agents-databricks-apps (`coding-agents-databricks-apps`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: datasciencemonkey
- License: MIT
- Language: Python
- Interface: install=GitHub template to Databricks Custom App, or local: git clone + uv run python app.py
- Model providers: Anthropic, OpenAI, Google, NousResearch
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [datasciencemonkey/coding-agents-databricks-apps](../../repos/datasciencemonkey/coding-agents-databricks-apps.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Zero-setup browser terminal running 5 coding agents (Claude Code, Codex, Gemini CLI, Hermes Agent, OpenCode) on Databricks Apps with enterprise integration: Unity Catalog governance, AI Gateway centralized model routing, automatic MLflow tracing of every session, auto-rotating short-lived PATs, parallel agent setup, WebSocket real-time I/O, and auto-sync to Databricks Workspace on every git commit.

(captured site page body (agents/coding-agents-databricks-apps.md), not a verified repo-code finding)
Enterprises want developers using coding agents, but agents running on laptops sit outside governance boundaries, and data teams need audit trails and central model billing. CoDA packages five coding agent CLIs into a browser-terminal Databricks App: an xterm.js frontend over a Flask/Gunicorn PTY server, with an entrypoint script that installs and preconfigures the agent CLIs at boot and wires all model calls through the Databricks AI Gateway for central governance. Unity Catalog governs what the agents can access, MLflow traces every session, personal access tokens rotate automatically, and 39 skills plus 2 MCP servers (DeepWiki, Exa) ship preconfigured. Data platform teams deploy it from a GitHub template to give developers governed browser access to agents; the project has moved to the databrickslabs organization, where development continues.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coding-agents-databricks-apps.md)
