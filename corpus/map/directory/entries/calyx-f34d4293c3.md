# Calyx (`calyx`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: yuuichieguchi
- License: MIT
- Language: Swift
- Interface: platforms=CLI, Desktop; install=brew tap yuuichieguchi/calyx && brew install --cask calyx; or manual download from latest release
- Model providers: Claude Code, Codex, OpenCode, Hermes, Grok, pi
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [yuuichieguchi/calyx](../../repos/yuuichieguchi/calyx.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native macOS terminal (built on Ghostty) for running and supervising multiple coding agents (Claude Code, Codex, OpenCode, Hermes, Grok, pi) in parallel. Provides one approval inbox, live agent status sidebar, persistent sessions, agent-readable command history, inline diff review, IPC between agents, LSP proxy, and browser scripting.

(captured site page body (agents/calyx.md), not a verified repo-code finding)
Calyx exists because running several coding agents in parallel in ordinary terminals means juggling tabs, missing permission prompts, and losing track of which agent is blocked. Built on Ghostty as a native macOS app, it hosts Claude Code, Codex, OpenCode, Hermes, Grok, and pi in panes with a sidebar showing live status, unread badges, and subagent state, while a single approval inbox queues permission requests from every pane for one-by-one review. An agent-readable command history (with secrets redacted) and an MCP server for inter-agent messaging let agents discover and talk to each other; git integration supports inline diff review with comments routed back into the originating agent's pane. Persistent daemon-backed sessions survive restarts, and an LSP proxy plus scriptable browser commands round out the toolkit. It targets developers running agent fleets on macOS who want supervision without leaving the terminal, is distributed via Homebrew cask, and accepts issues but not external pull requests.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/calyx.md)
