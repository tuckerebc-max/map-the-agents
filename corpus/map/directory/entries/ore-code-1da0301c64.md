# ore-code (`ore-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: 233i
- License: MIT
- Language: TypeScript, Rust
- Interface: platforms=Desktop; install=Download macOS .dmg from GitHub Releases; or build from source via pnpm install && pnpm dev (Tauri 2 build)
- Model providers: DeepSeek, Mimo, Ark Coding, custom endpoints
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [233i/ore-code](../../repos/233i/ore-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): DeepSeek-first coding agent with a native desktop shell (Tauri/Rust) providing a secure OS boundary for file, shell, process, Git, keychain, artifact, and MCP operations; long-context features including history compression, context briefing, checkpoint summaries, and provider-aware request shaping

(captured site page body (agents/ore-code.md), not a verified repo-code finding)
Desktop coding agents typically hand the model broad shell access, which makes accidental filesystem or process damage hard to contain. Ore Code structures the problem differently: a Tauri 2.x shell with a Rust layer mediates every sensitive operation — file, shell, process, Git, keychain, artifact, and MCP calls — while a TypeScript agent runtime and React frontend drive the workflow above it. The agent targets DeepSeek first (with Mimo, Ark Coding, or custom endpoints supported) and includes long-context features such as history compression and checkpoint summaries for extended sessions, plus project-aware chat, diff review, task-change restore, a skills system, and MCP server support. Configuration lives in ~/.ore-code/config.toml with API keys stored in the OS keychain. It is early — v0.1.1, 39 commits, macOS Apple Silicon only with an ad-hoc-signed DMG and Windows pending — so it is best treated as a promising architecture preview for developers invested in the DeepSeek ecosystem.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ore-code.md)
