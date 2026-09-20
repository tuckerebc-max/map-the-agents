# agent-deck (`agent-deck`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
agent-deck is for developers whose screen is a grid of agent terminals: it puts every Claude Code, Codex, OpenCode, Copilot, or Gemini CLI session into one Bubble Tea TUI with per-session status detec
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
