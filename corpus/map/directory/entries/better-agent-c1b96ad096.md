# Better Agent (`better-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: ofekron
- License: Source-available (non-commercial)
- Language: Python, JavaScript
- Interface: platforms=CLI, Web; install=One-liner scripts (macOS/Linux), PowerShell (Windows), Homebrew (brew tap ofekron/better-agent && brew install better-agent), or from source (git clone + ./run.sh)
- Model providers: Claude, Codex, Antigravity, Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ofekron/better-agent](../../repos/ofekron/better-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unifies multiple coding agents (Claude, Codex, Gemini, Antigravity) into one durable local workspace with persistent sessions, detached agents surviving restarts, offline-first capture, local inspection of all traces/tool calls, and multi-agent orchestration accessible from browser, desktop, or mobile.

(captured site page body (agents/better-agent.md), not a verified repo-code finding)
Better Agent addresses a practical pain point: developers running several AI coding agents in parallel lose sessions on restart, lose context across terminals, and have no unified surface to inspect what each agent did. It provides one durable local workspace where Claude Code, Codex, Gemini, and Antigravity agents run as detached processes with persistent sessions that survive restarts, and it captures work offline-first so results survive connectivity loss. Local inspection and reattachment let developers review and resume agent work across restarts. It is a workspace/session multiplexer rather than a coding agent - it manages agents rather than writing code itself. The project is a small free open-source utility, actively iterated, suited to developers running multiple agent CLIs locally.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/better-agent.md)
