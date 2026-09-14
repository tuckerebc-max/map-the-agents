# Zellij (`zellij`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: zellij-org
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=OS package, prebuilt binary from GitHub releases, or cargo install --locked zellij
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [zellij-org/zellij](../../repos/zellij-org/zellij.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=multiplexer, page=other

## Description

Highlight (site page `what_makes_it_special`): Terminal workspace/multiplexer aimed at developers with layouts, floating and stacked panes, multiplayer collaboration, a built-in web-client, and a WebAssembly plugin system (plugins can be written in any language compiling to WASM). Not a coding agent harness; a terminal multiplexer. ~35k stars.

(captured site page body (agents/zellij.md), not a verified repo-code finding)
Zellij rebuilds the terminal multiplexer concept that tmux and GNU screen have held for decades around modern development habits. It ships friendly default keybindings with on-screen hints so new users are productive without reading documentation, supports layout files that recreate a multi-pane workspace on demand, and allows panes to float above or stack within the tiling grid. Its plugin system compiles to WebAssembly, so extensions written in Rust or any other WASM-targeting language run in a sandbox with a stable API instead of shelling out to arbitrary scripts. Two features go beyond what classic multiplexers offer: multiplayer sessions, where several people attach to the same workspace and interact collaboratively, and a built-in web client that exposes the session in a browser. Rust and Cargo-based build tooling keep the core self-contained, and distribution covers cargo install, prebuilt binaries, and OS packages. Developers running long-lived terminal sessions — including those hosting terminal coding agents — use it to organize panes, persist work across disconnects, and share sessions with teammates.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zellij.md)
