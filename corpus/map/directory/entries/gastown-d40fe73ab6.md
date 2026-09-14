# gastown (`gastown`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: gastownhall
- License: MIT
- Language: Go
- Interface: install=brew
- Model providers: claude, gemini, codex, kiro, cursor, auggie, amp, opencode, copilot, pi, omp; custom agents configurable
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (plugins/ directory and plugin-system design doc) (yes)
  - claude_code_plugin: yes (Claude Code is a primary runtime; uses .claude/settings.json hooks) (yes)
  - subagents: yes (Polecats — worker agents with persistent identity, spawned for tasks) (yes)
  - hooks: yes (git worktree-based persistent storage; lifecycle hooks for session events) (yes)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [steveyegge/gastown](https://github.com/steveyegge/gastown) (source: backing, field: `source_code_url`) now resolves to [gastownhall/gastown](../../repos/gastownhall/gastown.md) (github id 1117184424, verified [https://github.com/gastownhall/gastown](https://github.com/gastownhall/gastown)).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent orchestration system that coordinates 20-30+ AI coding agents working on different tasks simultaneously, using git-backed hooks for persistent work state that survives agent crashes and restarts, with built-in merge queue, scheduling, escalation, and federation features.

(captured site page body (agents/gastown.md), not a verified repo-code finding)
Coordinating dozens of coding agents by hand collapses quickly: sessions die, work is lost, and nobody merges anything. Gastown, from steveyegge and now under gastownhall, organizes a workspace into Rigs staffed by persistent worker agents (Polecats) and a Mayor — typically a Claude Code instance — that decomposes work into convoys tracked in the Beads issue ledger. State is git-backed so crashes and restarts lose nothing, a Refinery merge queue serializes landing, and Witness/Deacon watchdogs plus scheduling and federation (Wasteland via DoltHub) handle the operational surface. It is Go, MIT-licensed, installable via brew or go install, and at 17.8k stars with 7,770 commits it is one of the most active multi-agent orchestrators in the ecosystem.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gastown.md)
