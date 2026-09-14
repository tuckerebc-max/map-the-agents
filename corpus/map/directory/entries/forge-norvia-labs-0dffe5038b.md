# Forge (Norvia Labs) (`forge-norvia-labs`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: NorviaLabs
- License: MIT
- Language: Rust
- Interface: platforms=CLI, IDE; install=Prebuilt installer: curl --proto '=https' --tlsv1.2 -LsSf https://raw.githubusercontent.com/NorviaLabs/forge/main/install/forge-installer.sh | sh; Windows PowerShell: irm https://raw.githubusercontent.com/NorviaLabs/forge/main/install/forge-installer.ps1 | iex; Build from source: cargo build --release --locked --package forge-cli
- Model providers: OpenAI, Anthropic, xAI Grok, OpenAI Codex (via device login), OpenCode Go, OpenCode Zen, Ollama
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [norvialabs/forge](../../repos/norvialabs/forge.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unifies AI agent, code editor, file explorer, shell, approvals, diffs, and durable sessions in one keyboard-driven TUI workspace. Every shell command runs inside an OS-level sandbox (macOS Seatbelt, Linux bubblewrap, WSL2) with network egress filtering via an allow-list proxy. Durable SQLite session journals allow resuming after interruption. Vim-style editing built in.

(captured site page body (agents/forge-norvia-labs.md), not a verified repo-code finding)
Forge unifies what terminal-agent users normally stitch together — an AI agent, a Vim-style editor, a file explorer, and a shell — into one Rust-based TUI workspace. Its security model replaces the usual approve-every-command dance with OS-level confinement: commands run inside Seatbelt or bubblewrap with writes restricted to the workspace, network egress flows through a filtering proxy with an empty default allow-list, and the program refuses to start rather than run unsandboxed. Sessions journal durably to SQLite for crash-resilient resume, tools cover files, patches, Git, search, and web, and MCP servers extend capability with prompting. A forge bench headless mode supports automation and benchmarking. It remains alpha software with a small user base.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/forge-norvia-labs.md)
