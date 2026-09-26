# Archon (`archon`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: coleam00
- License: MIT
- Language: TypeScript
- Interface: install=binary (curl install script), brew, docker
- Model providers: Claude, Codex, Pi
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (platform adapters: Web, CLI, Telegram, Slack, Discord, GitHub Webhooks) (yes)
  - claude_code_plugin: yes (ships a Claude Code skill; .claude directory; Claude Code is a prerequisite) (yes)
  - subagents: yes (multi-agent workflows, parallel reviewers, adversarial dev) (yes)
  - hooks: yes (validation gates, type-check hooks, approval gates) (yes)
  - plan_mode: yes (explicit plan nodes; archon-plan-to-pr workflow) (yes)

Repository map entry: [coleam00/archon](../../repos/coleam00/archon.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): The first open-source harness builder for AI coding; makes AI coding deterministic and repeatable by encoding development processes as YAML workflows with isolated git worktrees per run, parallel execution, human approval gates, and composable deterministic + AI nodes.

(captured site page body (agents/archon.md), not a verified repo-code finding)
Archon, by cole medin (coleam00), tackles the problem that AI coding agents behave nondeterministically: the same prompt can produce different results on different runs. It encodes development processes as YAML workflow definitions - planning, implementation, validation, review, and PR creation as reusable stages - so the same process runs deterministically each time, with isolated git worktrees per run enabling parallel execution. Runs can start from the CLI, web UI, Slack, Telegram, Discord, or GitHub webhooks, and 19 default workflows ship out of the box (fix-github-issue, idea-to-pr, plan-to-pr, comprehensive PR review). Claude Code is the primary assistant, with Codex and Pi also supported, and the MIT-licensed TypeScript (Bun) codebase is under very active development. Teams use it to standardize how coding agents execute repeatable engineering processes rather than hoping a prompt works.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/archon.md)
