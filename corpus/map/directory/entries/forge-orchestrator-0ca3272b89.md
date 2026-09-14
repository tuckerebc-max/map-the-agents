# forge-orchestrator (`forge-orchestrator`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: tarunms7
- License: MIT
- Language: Python
- Interface: install=curl -fsSL https://raw.githubusercontent.com/tarunms7/forge-orchestrator/main/install.sh | sh
- Model providers: Anthropic, OpenAI
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [tarunms7/forge-orchestrator](../../repos/tarunms7/forge-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-evolving multi-agent orchestrator built on Claude Code. Plans tasks, runs parallel agents in isolated git worktrees, 5-gate review pipeline (build/lint/test/LLM review/contracts), Contract Builder generates binding API specs before coding. Self-evolving learning captures lessons from failures and applies them cross-pipeline. Real-time cost tracking with budget limits, multi-repo workspaces, health monitor for stuck tasks.

(captured site page body (agents/forge-orchestrator.md), not a verified repo-code finding)
FORGE addresses the failure mode of running several coding agents at once: duplicated work, conflicting interfaces, and diffs nobody reviewed. A planner reads the codebase, asks clarifying questions, and produces a task DAG the user edits and approves; binding API/type contracts are generated before coding begins; one agent per git worktree executes in parallel with a health monitor watching for stuck tasks. Every change passes five gates (build, lint, test, LLM review, contract check) before auto-rebase, merge, and a single pull request via the GitHub CLI. Lessons captured from failed-then-retried tasks persist across pipelines, per-stage model routing balances cost and quality, and a Textual TUI plus Next.js dashboard expose state. Solo maintainers and small teams using Claude Code as their main harness are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/forge-orchestrator.md)
