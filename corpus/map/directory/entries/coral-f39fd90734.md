# CORAL (`coral`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Human-Agent-Society
- License: Apache-2.0
- Language: Python
- Interface: platforms=Autonomous; install=pip
- Model providers: LiteLLM gateway (custom models); supported agents: Claude Code, Codex, Cursor, Kiro, OpenCode
- Feature flags (directory-reported):
  - mcp_support: no — explicitly described as a skills-first bundle (no MCP) (no)
  - plugin_support: yes — plugin system installable in Claude Code and Codex; marketplace Human-Agent-Society/CORAL (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes — coral-task-author (autonomously scaffolds tasks) and coral-run-doctor (triages stuck runs) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [human-agent-society/coral](../../repos/human-agent-society/coral.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Infrastructure for autonomous AI agent organizations running experiments, sharing knowledge, and continuously improving solutions; multi-agent self-evolution in parallel git worktrees with shared .coral/public/ state; grader daemon scores every commit; accepted at COLM 2026.

(captured site page body (agents/coral.md), not a verified repo-code finding)
Running one coding agent against a benchmark is straightforward; running populations of agents that build on each other's results without contaminating evaluation is not, and CORAL supplies that substrate. Each agent works in an isolated git worktree, shared state (attempts, notes, skills) lives in a .coral/public/ directory symlinked into every worktree so agents see each other's progress in real time, and a grader daemon scores each commit so progress is measured rather than claimed. A manager agent injects heartbeat prompts - reflect, consolidate, pivot - to steer long runs, and multi-island runs with migration support evolution-style experiments across isolated agent populations. Docker isolation keeps agents from reading grader answer keys, and rubric-based LLM judges score open-ended tasks. Research groups studying self-improving agent systems use it; the project ships as a pip/uv install with a Claude Code plugin for authoring tasks.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coral.md)
