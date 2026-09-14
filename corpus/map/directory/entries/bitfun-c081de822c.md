# BitFun (`bitfun`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: GCWing
- License: MIT
- Language: Rust
- Interface: platforms=Desktop; install=binary
- Model providers: BYOK (model-agnostic, choose provider and enter API key)
- Feature flags (directory-reported):
  - mcp_support: yes (L2 customization tier includes MCP for connecting external tools) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (Codex-hook compatible, existing hook scripts work as-is) (yes)
  - plan_mode: yes (yes)

Repository map entry (renamed): original lead [gcwing/bitfun](https://github.com/gcwing/bitfun) (source: backing, field: `source_code_url`) now resolves to [gcwing/openbitfun](../../repos/gcwing/openbitfun.md) (github id 1147866277, verified [https://github.com/GCWing/OpenBitFun](https://github.com/GCWing/OpenBitFun)).

## Description

Highlight (site page `what_makes_it_special`): Combines a high-performance Rust agent runtime with a polished desktop app featuring Agentic Mini Apps (each task gets its own dedicated UI bound to live conversation state), self-hosted zero-knowledge multi-device relay, 98.67% KV cache hit rate via byte-stable prompt assembly, and flashgrep for 36x faster repo search.

(captured site page body (agents/bitfun.md), not a verified repo-code finding)
BitFun pairs a Rust agent runtime with a Tauri desktop app, positioning itself around the idea that a chat transcript is the wrong interface for many agent tasks. When the agent builds a chart, board, form, or panel, that interface persists as a mini app bound to the conversation's live state, and a public gallery hosts shareable examples. The runtime is tuned for long-horizon work: byte-stable prompt assembly keeps KV-cache hit rates at 98.67% on SWE-Bench-Pro runs, and a resident flashgrep index speeds repository search roughly 36x on Chromium-scale codebases. Customization runs through four tiers — custom agents, MCP/skills/hooks, mini apps, and source-level changes — with Codex-compatible hooks so existing scripts work unmodified. Multi-device use runs through a self-hosted, zero-knowledge relay (Argon2id and AES-GCM client-side key derivation), keeping sessions off vendor infrastructure. The project is MIT-licensed, spare-time research rather than a commercial product, and actively developed with 3,400+ commits.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bitfun.md)
