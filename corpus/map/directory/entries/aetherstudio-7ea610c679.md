# AetherStudio (`aetherstudio`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aetherstudio-cn
- License: MIT
- Language: Rust
- Interface: platforms=Desktop, IDE; install=cargo build -p aether-win32 --bin aether-app --release
- Model providers: DeepSeek, Kimi
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aetherstudio-cn/aetherstudio](../../repos/aetherstudio-cn/aetherstudio.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native Windows code editor built with Rust + Win32 API using Direct2D rendering and a Piece Table text buffer. Features multi-cursor editing, Tree-sitter, LSP/DAP, SSH remote development, ConPTY terminal, and CJK IME support. Includes an aether-plugin crate for plugin extensions and AI-assisted coding via DeepSeek/Kimi.

(captured site page body (agents/aetherstudio.md), not a verified repo-code finding)
AetherStudio (牧羊人编辑器) starts from a performance complaint: Electron-based editors cost memory and input latency on Windows, so it renders with Direct2D/DirectWrite through the Win32 API in Rust, using a Piece Table buffer for multi-cursor editing at native speed. It is a complete editor rather than a demo — Tree-sitter highlighting, LSP and DAP clients, SSH remote development, ConPTY terminal, and CJK IME support for Chinese users. The AI layer integrates DeepSeek and Kimi presets for code explanation, rewriting, and inline suggestions, and can feed agent tool results back into the loop. Windows users who want native responsiveness with Chinese-market AI presets are the audience; the project is MIT-licensed and actively developed by Song Diyang.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/aetherstudio.md)
