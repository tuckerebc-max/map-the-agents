# MicroCodex (`microcodex`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: paoloanzn
- License: Apache-2.0
- Language: C++
- Interface: platforms=CLI; install=curl -fsSL https://github.com/paoloanzn/microcodex/releases/latest/download/install.sh | sh
- Model providers: locked
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [paoloanzn/microcodex](../../repos/paoloanzn/microcodex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An ultra-lightweight Codex-compatible terminal coding agent written in C++23 with no runtime dependencies beyond libcurl and OpenSSL on Linux — it authenticates with your ChatGPT plan via OAuth and reuses Codex skills from the filesystem, without being a Codex distribution.

(captured site page body (agents/microcodex.md), not a verified repo-code finding)
MicroCodex is an independently written C++ client for the OpenAI Codex service: a terminal coding agent offering one-shot prompts and an interactive TUI, local coding tools for file read/write/edit, bash execution, and glob, durable conversations, and automatic context compaction. It logs in with your ChatGPT plan through OAuth (including device-auth for headless machines), stores credentials alongside Codex's own under ~/.codex, and discovers Codex skills installed under $CODEX_HOME/skills, so an existing Codex user's setup carries over. The bash tool runs behind a lexical safety gate that blocks destructive commands like rm -f and git reset --hard — explicitly not a sandbox — and MCP support is not yet implemented. It builds for macOS (Apple Silicon and Intel) and Linux, and targets developers who want a tiny, dependency-light alternative frontend to the Codex service.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/microcodex.md)
