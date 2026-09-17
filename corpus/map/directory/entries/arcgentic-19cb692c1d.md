# Arcgentic (`arcgentic`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: agent
- Provider/maker: Arch1eSUN
- License: MIT
- Language: Python, JavaScript
- Interface: install=npm install -g arcgentic; pipx install arcgentic; /plugin marketplace add Arch1eSUN/Arcgentic; git clone + scripts/install-codex-local.sh
- Model providers: OpenAI (Codex), Anthropic (Claude Code)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [arch1esun/arcgentic](../../repos/arch1esun/arcgentic.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Ad-hoc prompting of coding agents produces drift: silent scope changes, skipped tests, and unverified done claims. Arcgentic is a layer installed into Codex or Claude Code that structures each session
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
