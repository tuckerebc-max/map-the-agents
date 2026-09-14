# pixtuoid (`pixtuoid`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: IvanWng97
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=Homebrew (brew install pixtuoid), npm (npm install -g pixtuoid), Cargo, prebuilt binaries, or Debian .deb
- Model providers: Claude Code, Codex CLI, Antigravity, DeepSeek-Reasonix, CodeWhale, Copilot CLI, opencode, Cursor CLI, Hermes Agent, Oh My Pi, OpenClaw, Grok Build, Kimi Code CLI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [ivanwng97/pixtuoid](../../repos/ivanwng97/pixtuoid.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal pixel-art office TUI that visualizes AI coding agents as pixel-art coworkers at desks; agents type while working, raise ? when waiting for permission, and sleep when done; A*-routed pathfinding, office pets, lofi soundtrack, floating desktop window mode, local-only privacy

(captured site page body (agents/pixtuoid.md), not a verified repo-code finding)
pixtuoid addresses the visibility gap that opens up when several coding-agent sessions run at once: nothing shows at a glance which agent is working, blocked on a permission prompt, or finished. The tool watches sessions read-only — through a hook shim and JSONL transcript tails for Claude Code, Codex, and roughly a dozen other CLIs — and renders each as a pixel-art character at a desk: typing while working, raising a ? when waiting for approval, sleeping when done. Characters walk between desks via A* pathfinding, office pets wander the floor, and a lofi soundtrack plays, with a floating desktop-window mode keeping the office visible during real work. Everything stays local with no telemetry; state arrives through the hook shim and transcript files rather than any agent integration, so pixtuoid never touches the agents themselves. Built in Rust and distributed via Homebrew, npm, and Cargo, it targets developers running multiple agent sessions who want ambient, glanceable status.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pixtuoid.md)
