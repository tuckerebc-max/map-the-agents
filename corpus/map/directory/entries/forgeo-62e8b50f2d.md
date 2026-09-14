# forgeo (`forgeo`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: lucaGazzola
- License: MIT
- Language: Python 3.11+
- Interface: install=brew install lucaGazzola/forgeo/forgeo (macOS/Linux); or curl -fsSL https://forgeo.org/install.sh | bash (Linux/macOS/Windows); or pipx install forgeo-cli
- Model providers: Agent-agnostic - works with any coding agent CLI (Claude Code, Codex, opencode named)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [lucagazzola/forgeo](../../repos/lucagazzola/forgeo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Scheduled, agent-driven software factory layer on top of any coding-agent CLI; maintain a plain-JSON backlog and the daemon autonomously picks tasks, runs the agent, commits directly to main (no branches, no PRs), retries transient failures, and runs a refactoring pass when idle; only escalates to a human for genuine decisions; everything stored in inspectable plain files with automatic backup/restore; supports ...

(captured site page body (agents/forgeo.md), not a verified repo-code finding)
forgeo serves maintainers who accumulate more well-specified tasks than attention: it reads a backlog from a JSON file or a Jira/GitHub/GitLab/HTTP tracker, selects the oldest OPEN task whose dependencies are complete, and runs the configured agent CLI on it — optionally inside a Docker sandbox with the network off by default — committing the result directly to main. When the backlog empties, the daemon switches to refactoring passes instead of idling. Transient agent failures retry automatically while persistent failures and genuine human decisions escalate via BLOCKER.md. Operationally it stays lightweight: \`forgeo validate\` dry-runs the configuration, backlogs are snapshotted automatically, multiple instances per repository feed one aggregate web dashboard, and a token-protected web UI exposes run status for solo maintainers and small teams.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/forgeo.md)
