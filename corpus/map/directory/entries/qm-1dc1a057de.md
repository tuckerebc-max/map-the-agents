# qm (`qm`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: yc-software
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Web; install=npm exec --yes --package=@yc-software/qm@latest -- qm init . --org \<slug\> --target \<fly-or-aws\>
- Model providers: Harness-agnostic: the agent loop drives Pi, OpenCode, Codex, or Claude Code as swappable 'substrates'; models are admin-configured per org
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [yc-software/qm](../../repos/yc-software/qm.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=

## Description

(published index `description`, not a verified repo-code finding)
qm is built for companies that want one agent platform shared across employees rather than a personal CLI: each person gets an isolated workspace with their own memory, files, keychain view, permissio
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
