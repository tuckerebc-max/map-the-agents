# clu (`clu`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Arjia-Labs
- License: MIT
- Language: Go
- Interface: platforms=Autonomous, CLI; install=go install github.com/arjia-labs/clu/cmd/clu@latest (or make install from clone)
- Model providers: Agent-agnostic (any CLI agent can claim and work issues)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [arjia-labs/clu](../../repos/arjia-labs/clu.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): SQLite-backed issue tracker for coordinating AI coding agents on a single machine. Atomic claims (racing agents get different issues), dependency graphs with cascading cancel, bulk graph instantiation via clu batch, context inheritance for agents, workflow templates with human-approval gates, and an in-process local Web UI. No daemon, no server, no network. Includes an integration pattern using Claude Code's Monitor tool ...

(captured site page body (agents/clu.md), not a verified repo-code finding)
clu fills the gap between having several agent processes and having anywhere durable for them to pick up work: issues live in one SQLite file with no daemon or network, claims are atomic SQL updates so two agents never take the same task, and cancel cascades walk the dependency graph so downstream work never runs on cancelled premises. Workflow templates encode human-approval checkpoints for risky steps, a mailbox lets agents communicate, and a local web dashboard exposes kanban, graph, and approval views. It deliberately excludes an agent runtime, positioning itself as the coordination substrate beneath any harness, and its design favors single-machine, local-first setups over distributed orchestration.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/clu.md)
