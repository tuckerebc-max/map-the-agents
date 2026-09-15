# agent-deck (`agent-deck`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: asheshgoplani
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl install script, brew, go
- Model providers: Claude, Gemini, OpenCode, Codex, Copilot, Crush, Cursor, DeepSeek Harness; custom endpoints via env vars (e.g., GLM via ANTHROPIC_BASE_URL)
- Feature flags (directory-reported):
  - mcp_support: yes (built-in MCP Manager with socket pooling; stdio; 85-90% memory reduction) (yes)
  - plugin_support: yes (Skills Manager; managed pool workflow; materializes into .claude/skills) (yes)
  - claude_code_plugin: yes (/plugin marketplace add asheshgoplani/agent-deck; /plugin install agent-deck@agent-deck) (yes)
  - subagents: partial (Conductor: persistent supervisor agents orchestrate/monitor sessions, launch child sessions with parent linkage, auto-respond, escalate via Telegram/Slack) (reported)
  - hooks: yes (Claude Code hook integration for cost tracking; Codex notify hooks; transition notifier daemon) (yes)
  - plan_mode: no (no)

Repository map entry: [asheshgoplani/agent-deck](../../repos/asheshgoplani/agent-deck.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal session manager / mission control for AI coding agents — manage multiple AI agent sessions (Claude Code, Gemini CLI, OpenCode, Codex, Copilot, Cursor, Crush, Hermes Agent) from a single TUI. AI-aware status detection, session forking with inherited context, Conductor orchestration (auto-respond, escalate to phone via Telegram/Slack), MCP socket pooling (85-90% memory reduction), git worktree integration, Docker sandboxing, cost tracking ...

(captured site page body (agents/agent-deck.md), not a verified repo-code finding)
agent-deck is for developers whose screen is a grid of agent terminals: it puts every Claude Code, Codex, OpenCode, Copilot, or Gemini CLI session into one Bubble Tea TUI with per-session status detection, forking with inherited context, and git worktree or Docker sandbox isolation. A Conductor layer runs supervisor sessions that monitor workers, auto-respond, and escalate to Telegram or Slack when a human is needed, and watchers consume GitHub webhooks or ntfy events. Operational features — MCP socket pooling that cuts server memory 85–90%, cost dashboards with budget caps, Docker sandboxing, remote SSH instances, a web UI mode — make it infrastructure for people running agents as a fleet. Solo developers and small teams on macOS, Linux, or WSL are the users.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/agent-deck.md)
