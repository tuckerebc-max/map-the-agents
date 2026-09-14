# terminal (`terminal`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: bbarit
- License: unknown
- Language: Rust (backend), TypeScript/React 19 (frontend); Tauri v2
- Interface: platforms=CLI, Desktop, IDE; install=Download latest release build for macOS or Windows; launch and sign in with GitHub. Auto-updates via Tauri updater.
- Model providers: OpenAI, Anthropic, Google, Mistral, AWS Bedrock, Azure, Ollama, and more (37 providers / 1,000+ models)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: n/a (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [bbarit/terminal](../../repos/bbarit/terminal.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unified AI vibe-coding IDE: native terminal, code editor, and coding agent in one desktop app built 100% in Rust (Tauri). Broker Agent is a one-click autonomous AI dev\<-\>review pair with a mechanical (zero-LLM-cost) broker mediating the full design-\>build-\>test-\>review-\>merge loop on isolated git worktrees. Keeps all projects and terminals on a single screen, runs multiple AI coding CLIs side by side ...

(captured site page body (agents/terminal.md), not a verified repo-code finding)
BBARIT Terminal (formerly Octo Terminal, built by Tenmiles Inc.) collapses the terminal, the code editor, and the coding agent into one desktop application written entirely in Rust on Tauri. Its built-in agent works with an enforced verification loop — tests or builds must pass before a task can complete — alongside line-anchored safe edits, automatic rollback snapshots, and blocking of catastrophic commands, and a Broker Agent stages autonomous developer/reviewer pairs (for example Claude writing while Codex reviews) mediated by a deterministic, non-LLM broker that costs no tokens. The same screen hosts multiple real PTY terminals running other AI CLIs side by side (Claude Code, Codex, Gemini, Kimi, Qwen, OpenCode), a Monaco editor, git worktree panels with Kanban/Gantt views, an embedded Chromium browser, and remote access through a web terminal. MCP integration adds external tools, and 37 model providers (plus local Ollama) cover inference; GitHub sign-in suffices for the free app. Solo developers who want an all-in-one agentic workspace, particularly on Apple Silicon, are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/terminal.md)
