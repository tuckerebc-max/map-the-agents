# Aperant (`aperant`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: AndyMik90
- License: AGPL-3.0
- Language: TypeScript (Electron desktop app)
- Interface: platforms=Autonomous; install=binary
- Model providers: Anthropic/Claude (requires Claude Pro/Max subscription)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: yes (requires Claude Code CLI) (yes)
  - subagents: yes (up to 12 parallel agent terminals) (yes)
  - hooks: unknown (unknown)
  - plan_mode: yes (agents autonomously plan, implement, and validate tasks) (yes)

Repository map entry: [andymik90/aperant](../../repos/andymik90/aperant.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Autonomous multi-agent coding framework that plans, builds, and validates software using Claude Code. It runs up to 12 parallel agents in isolated git worktrees with self-validating QA loops, AI-powered merge conflict resolution, and a Kanban board for visual task management.

(captured site page body (agents/aperant.md), not a verified repo-code finding)
Aperant (formerly Auto Claude) addresses the throughput ceiling of single-agent coding: it decomposes a goal into tasks, runs them concurrently in isolated worktrees, validates each with automated QA, and merges results with AI-assisted conflict resolution, holding session memory across runs and integrating GitHub, GitLab, and Linear. It drives the Claude Code CLI rather than bundling its own model access, so users need a Claude Pro/Max subscription. The AGPL-3.0 desktop app is free with prebuilt binaries for all three platforms; version 3.0 is a ground-up rebuild in a separate repo with cloud features, placing 2.x in maintenance mode with code PRs paused. Around 14.5k stars and an active Discord community, with docs in the repo guides/ and at aperant.com.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/aperant.md)
