# agent-os (`agent-os`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: saadnvd1
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE, Web; install=npm install -g @saadnvd1/agent-os; or curl -fsSL https://raw.githubusercontent.com/saadnvd1/agent-os/main/scripts/install.sh | bash; desktop app downloads; or manual git clone
- Model providers: agent CLIs bring their own providers (Claude Code, Codex, Aider, Gemini CLI, Amp, Pi, OpenCode, Cursor CLI)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Mobile-first web UI for managing AI coding sessions (Claude Code, Codex, Aider, Gemini CLI, Amp, Pi); multi-pane parallel terminals (up to 4 side-by-side), voice-to-text dictation, git integration, session orchestration via MCP Conductor/worker model.

(captured site page body (agents/agent-os.md), not a verified repo-code finding)
Agent sessions keep running after you step away from the desk, but checking on them usually means SSH from a phone with a tiny keyboard. AgentOS serves a mobile-first web UI over self-hosted sessions of Claude Code, Codex, Aider, Gemini CLI, Amp, Pi, and other CLIs, with up to four terminal panes side by side, voice-to-text for dictating prompts, and git integration covering status, diffs, commits, PRs, and worktrees. Session orchestration follows a Conductor/worker model over MCP, a Tauri desktop app wraps the same UI for desktop use, and a hosted cloud option exists at runagentos.com. Developers who kick off long agent runs and check in from phones or other machines are the users.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agent-os.md)
