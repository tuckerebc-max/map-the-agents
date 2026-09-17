# Galley (`galley`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: multiplexer
- Provider/maker: shinpr
- License: MIT
- Language: Go
- Interface: platforms=CLI, IDE; install=Plugin marketplace (/plugin marketplace add shinpr/galley), or curl installer script, or go install github.com/shinpr/galley/cmd/galley@latest
- Model providers: Claude Code, OpenAI Codex, GLM (Z.AI), Kimi, Grok
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [shinpr/galley](../../repos/shinpr/galley.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Unattended agent work fails when the same model both writes and grades the code. Galley is a Go CLI and daemon that takes a task YAML with acceptance criteria, runs an executor backend — Claude Code,
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
