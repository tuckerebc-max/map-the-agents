# zerostack (`zerostack`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: gi-dellav
- License: GPL-3.0-only
- Language: Rust
- Interface: install=binary - install.sh, Cargo, Homebrew, or Nix
- Model providers: OpenRouter (default), OpenAI-compatible, Anthropic, Gemini, Ollama, custom providers
- Feature flags (directory-reported):
  - mcp_support: yes - optional compile-time feature (yes)
  - plugin_support: no - custom prompts via Markdown files (no)
  - claude_code_plugin: n/a - Claude Code hook-compatible settings.json schema; loads CLAUDE.md (reported)
  - subagents: yes - parallel/fast subagents for codebase exploration (yes)
  - hooks: yes - gated hooks feature; lifecycle hooks for tool calls, prompts, sessions; CC-compatible (yes)
  - plan_mode: yes - built-in /prompt modes including plan (planning-only) (yes)

Repository map entry: [gi-dellav/zerostack](../../repos/gi-dellav/zerostack.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
zerostack began as an argument about budgets: if a coding agent mostly shells out and edits text, it should not need hundreds of megabytes of RAM. Written in Rust in roughly two weeks and inspired by
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
