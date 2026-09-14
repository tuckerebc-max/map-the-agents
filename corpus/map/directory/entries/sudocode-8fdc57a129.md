# sudocode (`sudocode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: sudoprivacy
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/sudoprivacy/sudocode/main/install.sh | sh
- Model providers: Anthropic, OpenAI, xAI, Gemini, proxy/mock (model-agnostic)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [sudoprivacy/sudocode](../../repos/sudoprivacy/sudocode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native, pipe-composable, scrollback-safe CLI coding agent for heavy users. Inline-only (never hijacks terminal), model-agnostic, headless-first, local-first (zero telemetry by default), open source. Designed as an interchangeable agent unit for multi-agent orchestration via the nexus VFS chat-with-me mailbox.

(captured site page body (agents/sudocode.md), not a verified repo-code finding)
sudocode was built by the Sudo Privacy community in explicit reaction to Claude Code's beginner-oriented direction, and its design choices follow from that audience: output renders inline so tmux, ssh, and terminal scrollback stay intact; JSON output pipes into jq like any Unix tool; and sessions are stored as readable, forkable jsonl files with zero telemetry by default. The same binary runs as a REPL, a one-shot command, or a headless ACP server for editors and web clients, with MCP servers mounted alongside built-in tools. It is deliberately positioned as an agent unit rather than an orchestrator — fleets of 7-10 or 100+ instances coordinate through a nexus VFS mailbox under the broader Sudowork platform. Releases are gated on dogfooding, and everything is configuration files: sessions as jsonl, config as .scode.json, docs as markdown.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sudocode.md)
