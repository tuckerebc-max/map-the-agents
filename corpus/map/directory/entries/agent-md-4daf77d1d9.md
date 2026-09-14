# agent-md (`agent-md`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: iamfakeguru
- License: MIT
- Language: Shell (Bash)
- Interface: platforms=Autonomous, IDE; install=binary
- Model providers: agent-agnostic (Claude Code, Codex, Cursor, Windsurf, Aider)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes — extensive hook system for Claude Code, Codex, and Git hooks (destructive command blocking, stop-verify, state-enforcement, visual evidence) (yes)
  - plan_mode: no (no)

Repository map entry: [iamfakeguru/agent-md](../../repos/iamfakeguru/agent-md.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Portable contracts for coding agents — single source-of-truth rules file, repo-local hooks, persistent task state, and helper scripts so AI agents verify their work rather than guess. Multi-agent portable (Claude Code, Codex, Cursor, Windsurf, Aider).

(captured site page body (agents/agent-md.md), not a verified repo-code finding)
Rules written in prose get ignored the moment a model rationalizes around them, so agent-md moves everything that can be forgotten into things that cannot: an installer lays down a single AGENT.md source of truth, generates per-tool variants (AGENTS.md, CLAUDE.md), and wires repo-local hooks for Claude Code, Codex, and git pre-commit that block destructive commands and force stop-verify steps. Task state lives in memory files — plan, progress, verify — so commitments survive across sessions instead of being re-derived from chat. Helper scripts add a doctor check and Playwright screenshot capture for visual evidence. Teams running Claude Code, Codex, Cursor, Windsurf, or Aider over the same repo use it to make all of them obey the same contract.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agent-md.md)
