# ORCH (`orch`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: oxgeneral
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @oxgeneral/orch
- Model providers: none (drives existing CLI agents: Claude Code, OpenCode, Codex, Pi, Cursor, Grok, Antigravity, plus a generic Shell adapter)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [oxgeneral/orch](../../repos/oxgeneral/orch.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Coordinates multiple AI agents (and any CLI tool) in parallel on one project with isolated git worktrees, a state machine (todo -\> in_progress -\> review -\> done) with mandatory code review, zero infrastructure (no database, no cloud, no Docker), file-based state, and pre-built team templates for engineering and non-engineering workflows. Includes /orch skill for Claude Code.

(captured site page body (agents/orch.md), not a verified repo-code finding)
Orchestrating several AI agents on one repository usually introduces infrastructure: queues, databases, dashboards. ORCH keeps everything in the repo: an orchestrating CTO agent decomposes a goal into tasks, worker agents (Claude Code, Codex, Pi, Cursor, OpenCode, Grok, Antigravity, or a generic Shell adapter) execute in parallel inside isolated git worktrees, and a review gate blocks merging until a reviewer agent approves. State lives in .orchestry/ as plain YAML/JSON/JSONL — no database, no Docker, no accounts — with auto-retry, zombie detection, and inter-agent messaging handled by the CLI. Beyond code, the same Shell adapter runs editorial, sales, analytics, security, and DevOps workflows, and a headless orch serve daemon supports 24/7 operation under pm2 or systemd. Install is one npm global with Node 20+ on macOS, Linux, or WSL2, MIT-licensed with roughly 1,950 tests. Solo operators and small teams running agent fleets without infrastructure are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/orch.md)
