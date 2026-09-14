# hax (`hax`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: OleksandrChekhovskyi
- License: MIT
- Language: C
- Interface: platforms=CLI; install=Homebrew: brew install oleksandrchekhovskyi/hax/hax; AUR (Arch Linux); prebuilt static binary from releases; or build from source (make)
- Model providers: OpenAI (+compatible), Anthropic (+compatible), Codex (via ChatGPT subscription), OpenRouter, OpenCode Zen/Go, llama.cpp, Ollama, custom endpoints
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [oleksandrchekhovskyi/hax](../../repos/oleksandrchekhovskyi/hax.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A minimalist, terminal-native coding agent written in C — single lightweight binary with small memory footprint, local models as first-class citizens, respects the terminal (preserves scrollback, no TUI takeover), fully inspectable transcripts, and uses Unix-style subprocess composition instead of plugins/MCP/IDE panels.

(captured site page body (agents/hax.md), not a verified repo-code finding)
hax is a coding agent built as a single small C binary with minimal dependencies, aimed at developers who want agent capability without a heavyweight runtime. It supports interactive REPL, one-shot, and stdin-piped modes with session continuation and resume, and connects to OpenAI-compatible and Anthropic-compatible endpoints, OpenRouter, Codex subscriptions, and local llama.cpp or Ollama servers — with llama.cpp auto-discovery requiring no configuration. The interface respects the terminal it runs in: streaming Markdown reflows in place, tool output stays inline, and native scrollback is preserved rather than replaced. Config is plain text under XDG paths, transcripts are inspectable (Ctrl+T shows exactly what was sent and received), and capabilities extend through subprocess composition rather than a plugin system. It suits terminal-focused developers, local-model users, and environments where memory footprint and auditability matter.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hax.md)
