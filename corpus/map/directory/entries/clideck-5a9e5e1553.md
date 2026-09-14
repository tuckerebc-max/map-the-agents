# CliDeck (`clideck`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: rustykuntz
- License: MIT
- Language: JavaScript
- Interface: platforms=CLI, IDE, Web; install=npm install -g clideck or npx clideck (Node 18+)
- Model providers: Claude Code, Codex, Gemini CLI, OpenCode, Pi (any terminal CLI)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [rustykuntz/clideck](../../repos/rustykuntz/clideck.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local dashboard for running and coordinating multiple AI CLI coding agents (Claude Code, Codex, Gemini CLI, OpenCode, Pi) in one browser window with chat-style sidebar, live status detection, session resume, inter-agent communication, autopilot routing between agents, projects grouping, prompt library, and an E2E encrypted mobile relay - without sitting between agents rewriting prompts.

(captured site page body (agents/clideck.md), not a verified repo-code finding)
CliDeck rethinks the tmux pane grid as a chat-style interface: agents keep running in their real terminals, but the dashboard groups them by project, shows live working/idle/waiting status, previews messages, and resumes sessions, all while explicitly not sitting in the middle of the conversation. The ask-another-session feature injects a message into a target agent's terminal and returns the response, giving lightweight cross-agent consultation without an orchestration layer. Everything is local with no data leaving the machine, and a plugin API covers voice input and autopilot. Developers who run several CLIs but dislike pane-based multiplexers are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/clideck.md)
