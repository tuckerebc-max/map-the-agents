# agentic-coding-tool-eval (`agentic-coding-tool-eval`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: disler
- License: No license file is declared in the repository
- Language: Vue
- Interface: platforms=IDE; install=git clone; use custom slash command /trees in Claude Code (or manual git worktrees)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [disler/agentic-coding-tool-eval](../../repos/disler/agentic-coding-tool-eval.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Hands-on micro apps to compare and evaluate agentic coding tools (Claude Code, Gemini CLI, Codex CLI) in a standardized way. Uses a custom /trees slash command to spin up parallel git worktrees.

(captured site page body (agents/agentic-coding-tool-eval.md), not a verified repo-code finding)
Choosing between Claude Code, Gemini CLI, and Codex CLI is usually based on demos and marketing, so this repository provides a controlled hands-on alternative: one small UI-component challenge that every candidate tool attempts under the same prompts. Each tool runs in an isolated git worktree so the attempts never interfere, and the /trees slash command creates those worktrees in one step. The tools are deliberately run in permissionless mode (claude --dangerously-skip-permissions, gemini --yolo, codex --dangerously-auto-approve-everything) so permission friction does not skew the comparison. It is aimed at developers who want to judge tool quality on a realistic task they can inspect themselves rather than on published benchmark numbers.
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agentic-coding-tool-eval.md)
