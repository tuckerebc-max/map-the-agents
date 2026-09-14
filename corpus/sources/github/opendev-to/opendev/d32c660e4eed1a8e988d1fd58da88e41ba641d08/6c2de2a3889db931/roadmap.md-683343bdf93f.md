# OpenDev Roadmap

This document outlines OpenDev's development priorities. It describes direction, not commitments — there are no fixed dates, and priorities shift with community feedback. Contributions and feedback are welcome: [open an issue](https://github.com/opendev-to/opendev/issues) to discuss anything here.

**Last updated: 2026-07**

---

## ✅ Recently Completed

- **Full Rust Rewrite**: The entire agent was rewritten from Python to Rust — a 20-crate workspace with a ratatui terminal UI (`opendev-tui`), an axum WebSocket web backend (`opendev-web`), and a React/Vite web frontend (`web-ui/`). Result: ~4 ms startup, ~9 MB memory, single 18 MB binary
- **Compound AI Architecture**: Main agent plus specialized subagents, with independent model bindings for the Normal, Thinking, Compact, Self-Critique, and VLM workflow slots
- **Multi-Provider Support**: 9 providers (OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, Azure OpenAI) via provider adapters in `crates/opendev-http/src/adapters/`
- **Streaming Tool Executor**: Tools begin executing while the model is still streaming its response ([#66](https://github.com/opendev-to/opendev/pull/66))
- **XDG Base Directory Support**: Config and data files follow the XDG spec ([#45](https://github.com/opendev-to/opendev/issues/45))
- **Offline Built-in Provider Defaults**: OpenDev starts and configures providers without network access to the models registry ([#42](https://github.com/opendev-to/opendev/issues/42))
- **Security Hardening**: An ongoing automated audit pass has fixed dozens of TOCTOU/atomic-write and related filesystem vulnerabilities across the workspace (e.g. [#198](https://github.com/opendev-to/opendev/pull/198), [#199](https://github.com/opendev-to/opendev/pull/199))
- **Web UI Performance**: A sustained series of frontend optimizations — memoized filtering, deferred search, precompiled regexes, layout-thrashing fixes (e.g. [#197](https://github.com/opendev-to/opendev/pull/197), [#200](https://github.com/opendev-to/opendev/pull/200))
- **Provider Streaming Fixes**: Community-contributed fixes such as Kimi streaming response parsing ([#192](https://github.com/opendev-to/opendev/pull/192))
- **30+ Built-in Tools**: File ops, bash, edit, search, browser, web fetch, LSP queries, AST symbol navigation, memory, todos, subagents, and more (`crates/opendev-tools-impl`)
- **LSP + Symbol Navigation**: Language server integration (`opendev-tools-lsp`) and AST-based symbol tools (`opendev-tools-symbol`)
- **MCP Integration**: Dynamic tool discovery via the Model Context Protocol (`opendev-mcp`)
- **Session Persistence & Concurrent Sessions**: Save/resume sessions, multiple independent agent sessions in parallel (`opendev-history`)

---

## 🚧 In Progress

- **Web UI / TUI Feature Parity and Remote Sessions**: Bring the Web UI up to the TUI's feedback richness (subagent trees, streaming thinking, diff rendering, plan tracking) through a shared event protocol, and support remote sessions so tasks can be started away from the terminal (see [docs/prd-web-ui-sync.md](docs/prd-web-ui-sync.md))
- **Telegram Channel**: Interact with OpenDev via a Telegram bot, built on the channel router in `opendev-channels`
- **Ongoing Security and Performance Passes**: The automated Sentinel (security) and Bolt (web-ui performance) audit series continue to land fixes on `main`

---

## 🗺️ Planned / Exploring

These reflect intent; none have committed timelines.

- **More Messaging Channels**: The `opendev-channels` router abstraction is designed for additional integrations (WhatsApp, Slack, Discord) beyond Telegram — exploring
- **Codebase Indexing & Multi-Root Workspaces**: Better whole-repo understanding and support for working across multiple repositories ([#8](https://github.com/opendev-to/opendev/issues/8)) — exploring, building on `opendev-tools-symbol` and the memory system in `opendev-agents`
- **Release Engineering Improvements**: More robust installer/checksum verification and release automation ([#41](https://github.com/opendev-to/opendev/issues/41), [#84](https://github.com/opendev-to/opendev/issues/84))
- **Improved Sandboxed Execution**: Continued work on isolated command execution in `opendev-sandbox`

---

## 🤝 Community Contributions Welcome

Development is active, and external PRs get reviewed and merged (recent examples: [#192](https://github.com/opendev-to/opendev/pull/192), [#90](https://github.com/opendev-to/opendev/pull/90), [#91](https://github.com/opendev-to/opendev/pull/91)). Areas where help is genuinely wanted, with pointers to where the code lives:

- **Codebase indexing & multi-root workspaces** ([#8](https://github.com/opendev-to/opendev/issues/8)) — foundations exist in `crates/opendev-tools-symbol` (AST symbol navigation) and the memory system in `crates/opendev-agents`
- **ChatGPT-subscription authentication design** ([#49](https://github.com/opendev-to/opendev/issues/49)) — provider auth lives in `crates/opendev-http/src/auth.rs` alongside the adapters in `crates/opendev-http/src/adapters/`
- **First-run provider setup UX** ([#109](https://github.com/opendev-to/opendev/issues/109)) — the welcome/API-key panel is in `crates/opendev-tui/src/widgets/welcome_panel/`
- **TUI polish** ([#61](https://github.com/opendev-to/opendev/issues/61)) — e.g. input line wrapping and other terminal UX fixes in `crates/opendev-tui`
- **Release engineering** ([#41](https://github.com/opendev-to/opendev/issues/41), [#84](https://github.com/opendev-to/opendev/issues/84)) — installer and checksum reliability; see [RELEASE_FLOW.md](RELEASE_FLOW.md)

To get started, see [DEVELOPMENT.md](DEVELOPMENT.md) for the local build/test workflow, then open an issue or pull request.

---

## 💡 Community Ideas

Have a feature request? [Open an issue](https://github.com/opendev-to/opendev/issues) and let's discuss.
