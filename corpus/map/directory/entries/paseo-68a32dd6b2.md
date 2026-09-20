# Paseo (`paseo`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: multiplexer
- Provider/maker: getpaseo
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Claude Code, Codex, GitHub Copilot, OpenCode, Pi
- Feature flags (directory-reported):
  - mcp_support: yes (packages/server includes an MCP server; transport not specified) (yes)
  - plugin_support: partial (plugin-examples/ directory; skills system for extensibility) (reported)
  - claude_code_plugin: yes (.claude/skills/ directory; Claude Code is a supported agent) (yes)
  - subagents: yes (/paseo-advisor and /paseo-committee skills spin up additional agents) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [getpaseo/paseo](../../repos/getpaseo/paseo.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Paseo exists because coding agents strand work in a single terminal on a single machine: sessions die when the laptop closes and there is no way to supervise several agents at once. Its self-hosted da
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
