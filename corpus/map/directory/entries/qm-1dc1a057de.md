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
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
