# squarebox (`squarebox`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: SquareWaveSystems
- License: MIT
- Language: Shell
- Interface: platforms=CLI; install=curl -fsSL https://github.com/SquareWaveSystems/squarebox/releases/latest/download/install.sh | bash (Linux/macOS); irm install.ps1 | iex (Windows PowerShell); docker compose up -d (server)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [squarewavesystems/squarebox](../../repos/squarewavesystems/squarebox.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Curated set of modern CLI/TUI tools and AI coding assistants packaged in a single Docker/Podman container with batteries included, one-line install, interactive first-run setup, and sensible defaults. Run the same box anywhere (desktop, VPS, Codespace) and SSH in from any device. Bundles Claude Code, Copilot CLI, Gemini CLI, Codex CLI, opencode, Pi, Oh My Pi.

(captured site page body (agents/squarebox.md), not a verified repo-code finding)
squarebox solves environment drift for people who work across laptops, servers, and cloud shells: a one-line installer pulls a digest-verified image, runs an interactive wizard to pick optional AI assistants (Claude Code, Copilot CLI, Gemini CLI, Codex, opencode, Pi), editors, TUIs, and mise-managed SDKs, then mounts host code from ~/squarebox/workspace with persistent state in a Docker volume. The box suspends on exit and resumes on start, SSH in from any device, and sqrbx-update upgrades in place while sqrbx-rebuild replaces the image wholesale. Security posture is explicit — checksum-pinned downloads, fail-closed digest verification, a documented trust model. It is MIT-licensed and designed to be forked as a personal base image; at roughly 900 MB plus optional toolchains it trades disk for reproducibility.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/squarebox.md)
