# Unpeel (`unpeel`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: unknown
- License: unknown
- Language: Swift, Rust
- Interface: platforms=CLI, Desktop; install=Download macOS app from website; also ships a CLI/TUI (e.g. unpeel --host ssh://your-box)
- Model providers: Anthropic (Claude Code), OpenAI (Codex), Google (Gemini CLI), Moonshot (Kimi), Cline, Cursor, Kiro
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Terminal-first workspace that runs AI agent sessions as persistent hosted processes on your own machine; iPhone remote control via QR pairing; multi-agent orchestration via local Unpeel Sessions MCP; browser automation via your existing Chrome; session forking and markdown export

(captured site page body (agents/unpeel.md), not a verified repo-code finding)
Unpeel exists because long agent runs are fragile: close the terminal or laptop lid and the session dies, and there is no way to check on or approve an agent's work from away from the desk. It hosts agent sessions (Claude Code, Codex, Gemini CLI, Cursor Agent, Kimi, Cline, Kiro) as processes independent of the UI, so quitting the app leaves them running, while a sidebar dashboard shows busy/done/needs-you status and a menu-bar item pulses on activity. A paired iPhone provides live terminals, input, approvals, and push notifications, with screenshots annotatable and returned into the agent's context; workspaces can also run on any SSH-reachable machine. Developers who step away from their desk — or manage several agents across machines — use it to supervise runs remotely; the app and TUI are free, with the Unpeel Link encrypted relay sold separately, and all state lives in plain files under ~/.unpeel.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/unpeel.md)
