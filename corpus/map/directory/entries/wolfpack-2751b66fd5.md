# Wolfpack (`wolfpack`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: almogdepaz
- License: MIT
- Language: TypeScript, JavaScript (Bun), Rust (PTY broker)
- Interface: platforms=Autonomous, CLI, Desktop, Web; install=curl -fsSL https://raw.githubusercontent.com/almogdepaz/wolfpack/main/install.sh | bash; or bunx wolfpack-bridge@latest; or npx --yes wolfpack-bridge@latest. Verify with wolfpack doctor. Uninstall with wolfpack uninstall --yes
- Model providers: Claude Code, Codex, Gemini, arbitrary shell/custom commands on PATH
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [almogdepaz/wolfpack](../../repos/almogdepaz/wolfpack.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted browser terminal manager for AI coding agents; persistent PTY-backed sessions live in a Rust broker (not the web server) so server restarts/upgrades don't kill running agents; fully self-hosted with direct private Tailnet access and no Wolfpack-hosted relay or account; multi-machine control room with handshake-verified peers; phone PWA, desktop terminal grid, and direct wolfpack attach; Agent Skills (wolfpack-tailnet-control) and Pi ...

(captured site page body (agents/wolfpack.md), not a verified repo-code finding)
Wolfpack gives developers a self-hosted control room for AI coding agents running on their own machines, reachable from a desktop browser or phone PWA over a private Tailscale network with no hosted relay or account. Its two-part design separates the web server from a Rust PTY broker that owns sessions, so restarting the web server or closing the browser does not kill running agents. The dashboard shows live session previews, needs-input states, and handshake-verified Wolfpack peers on the Tailnet, with harness choices including Claude Code, Codex, Gemini CLI, Cursor, and Pi. Parent and child agent spawning with a task gateway supports orchestration, and Agent Skills (wolfpack-tailnet-control, wolfpack-pi-task-delegation) extend external harnesses. It installs via a curl setup wizard with Tailscale-based private access and JWT/ACL options.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/wolfpack.md)
