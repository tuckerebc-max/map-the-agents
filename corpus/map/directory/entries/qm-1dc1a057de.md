# qm (`qm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
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

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): A 'multiplayer agent harness for work': each employee gets an isolated workspace (own memory, files, keychain view, crons, durable sandbox) while collaborating through shared Slack channels and projects, with the agent loop itself pluggable across Pi, OpenCode, Codex, or Claude Code. Contributions are accepted as written ADRs, not code — maintainers implement proposals themselves.

(captured site page body (agents/qm.md), not a verified repo-code finding)
qm is built for companies that want one agent platform shared across employees rather than a personal CLI: each person gets an isolated workspace with their own memory, files, keychain view, permissions, and durable sandbox, while shared scopes cover Slack channels, group messages, and team projects. The headless TypeScript core runs an agent loop over a fixed tool surface — notably an execute tool confined to each scope's sandbox — with Postgres storing sessions, memory, and queue state, and the web UI, admin panel, and Slack integration all plugins over its HTTP API. Which underlying harness (Pi, OpenCode, Codex, or Claude Code) drives the loop is an org-level configuration, behind interfaces swapped through one wiring file. Security postures range from per-tool human approval to a classifier-screened auto mode, with hard denials for destructive commands in all postures and auditing throughout. Organizations self-host it in their own Fly or AWS accounts, and contribute architectural proposals as written ADRs that maintainers implement.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qm.md)
