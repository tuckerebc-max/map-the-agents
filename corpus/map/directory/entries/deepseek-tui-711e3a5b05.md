# DeepSeek-TUI (`deepseek-tui`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Independent
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=Download prebuilt binaries from GitHub Releases (.7z for Windows x64, .dmg for macOS ARM64)
- Model providers: DeepSeek (default), NVIDIA NIM, Fireworks, SGLang, vLLM
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [deepseek-tui/deepseek-tui](../../repos/deepseek-tui/deepseek-tui.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal coding agent for DeepSeek V4 models. Streams reasoning blocks, edits local workspaces with approval gates, reads/edits files, runs shell commands, searches the web, manages git, and coordinates sub-agents. Includes auto mode that selects model and thinking level per turn. Has Plan (read-only investigation), Agent, and YOLO modes. MCP support and a Skills system for composable, installable instruction packs from ...

(captured site page body (agents/deepseek-tui.md), not a verified repo-code finding)
deepseek-tui was a terminal coding agent built around DeepSeek V4 models: it streamed the models' reasoning blocks into the terminal, edited local workspaces behind approval gates, ran shell commands, searched the web, managed git, and coordinated subagents from a TUI. The project attracted an ecosystem — a Homebrew tap, Windows install tutorials, desktop re-implementations, and DeepSeek Harness TUI distributions such as seektty and cocode — indicating real adoption at its peak. The canonical repository at github.com/deepseek-tui/deepseek-tui now returns 404, confirmed via GitHub's API, so the original source is no longer available. Users who want comparable tooling must rely on the surviving fork/companion projects, which complicates provenance and security review.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepseek-tui.md)
