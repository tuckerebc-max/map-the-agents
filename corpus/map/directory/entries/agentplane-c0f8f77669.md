# AgentPlane (`agentplane`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: basilisk-labs
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm i -g agentplane
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [basilisk-labs/agentplane](../../repos/basilisk-labs/agentplane.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Git-native control plane for coding agents that wraps agents like Claude Code, Codex, Cursor, and Aider in an approved, verifiable repository workflow with bounded authority, approval gates, supervisor-observed proof, verification, and closure. Features Task lifecycle management, Agent Change Records (ACR), local context management, recipes (TDD, security review, docs update), two workflow modes (direct and branch_pr), DCO-compliant multi-author commits, SLSA provenance, ...

(captured site page body (agents/agentplane.md), not a verified repo-code finding)
Teams adopting coding agents need an enforceable record of who did what, not chat transcripts. AgentPlane divides responsibility three ways: humans set outcomes and approve material risk, coding agents do semantic work inside bounded episodes, and the CLI (semantically blind, mechanically authoritative) owns task state, Git/PR routing, and evidence. Each task advance emits a packet with an objective, writable scope, context, and a typed result schema; agents cannot perform lifecycle transitions or claim formal approvals. Workflows run in direct mode for solo reversible work or branch_pr mode with worktrees, branches, and hosted checks. The tool is aimed at engineering teams that want Git itself to be the durable review surface for agent-driven changes.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentplane.md)
