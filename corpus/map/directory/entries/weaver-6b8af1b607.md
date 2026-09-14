# Weaver (`weaver`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: sean35mm
- License: MIT
- Language: TypeScript
- Interface: install=curl -fsSL https://raw.githubusercontent.com/sean35mm/weaver/main/install.sh | sh (installs binary to ~/.local/bin/weaver); then run weaver init (project or global). macOS/Linux arm64/x64; Windows via WSL2.
- Model providers: Claude Code, Codex, OpenCode, Pi (any agent that can run shell commands)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [sean35mm/weaver](../../repos/sean35mm/weaver.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-only, serverless coordination layer for multiple AI coding agents in the same repo. Provides cross-agent presence, advisory file claims, durable notes that survive context compaction, recent activity tracking, and live views — all via a small CLI over local SQLite files (~/.weaver/). No telemetry, no account, no network calls. Git remains source of truth; claims are advisory, never blocking. Explicitly ...

(captured site page body (agents/weaver.md), not a verified repo-code finding)
Weaver solves the problem of multiple AI coding agents (Claude Code, Codex, OpenCode, Pi, or plain terminals) colliding in the same repository without any cloud service. It provides a coordination-lite loop — status, task, claim, done — where advisory, TTL-bound file claims detect overlap (exit 1 signals overlap) and git remains authoritative for code. State lives in a per-repo SQLite database under ~/.weaver/, supplemented by durable Repository Facts that survive context compaction, optional Markdown scratchpads, a loopback-only web dashboard, and a preflight command that verifies claims before commit or push. The CLI installs protocol blocks into CLAUDE.md/AGENTS.md and optional Claude Code hooks or OpenCode plugins. It targets developers running several agents in parallel on one repo, fully locally.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/weaver.md)
