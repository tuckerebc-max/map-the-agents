# Forge (`forge`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: LucasDuys
- License: MIT
- Language: JavaScript
- Interface: platforms=Autonomous, IDE; install=claude plugin marketplace add LucasDuys/forge then claude plugin install forge@forge-marketplace (requires Claude Code v1.0.33+)
- Model providers: Anthropic (Claude only)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [lucasduys/forge](../../repos/lucasduys/forge.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): 5-phase autonomous loop (brainstorm-\>plan-\>execute-\>review+verify-\>backprop); state persisted on disk in .forge/ not conversation memory; crash-recoverable via lock file + checkpoints; per-task git worktrees with TDD and atomic squash-merge; hard token budgets; backpropagation turns runtime failures into new acceptance criteria + regression tests; multiplayer mode via distributed claim queue.

(captured site page body (agents/forge.md), not a verified repo-code finding)
Forge turns Claude Code into a brainstorm-to-commit pipeline built for long, token-hungry runs: an idea becomes an R-numbered spec with testable acceptance criteria, a dependency-ordered task DAG, TDD execution in per-task git worktrees, then review and four-level verification (existence, substantive, wired, runtime). Because state lives in .forge/ on disk instead of the context window, crashes and context resets resume from checkpoints, and a backprop phase converts runtime failures into new acceptance criteria plus regression tests that re-enter the loop. Seven hooks enforce token budgets, trim Bash output, cache reads, and compress tool output, which the project measures at roughly 29% real-token savings on filterable workloads. Approval-gated by default with a full mode for trusted runs, it appeals to Claude Code subscribers running multi-hour feature development.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/forge.md)
