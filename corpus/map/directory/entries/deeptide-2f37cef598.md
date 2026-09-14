# deeptide (`deeptide`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: paean-ai
- License: MIT
- Language: Rust, TypeScript, Swift
- Interface: platforms=Desktop; install=binary, npm
- Model providers: DeepSeek (default), BYOK to any Anthropic-protocol-compatible endpoint (OpenAI, Anthropic, Ollama, Gemini, Zhipu GLM, Volcengine, Moonshot, Qwen, self-hosted)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [paean-ai/deeptide](../../repos/paean-ai/deeptide.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Built specifically for DeepSeek models with three flavors (native macOS app, TypeScript/Bun CLI, Rust CLI+GUI) that share configuration, sessions, and tools via a shared interface contract (tide-spec). Includes a local DeepSeek inference runtime (Metal engine + OpenAI/Anthropic-compatible gateway). Hooks engine for pre/post tool, user-prompt, session, and compaction shell hooks.

(captured site page body (agents/deeptide.md), not a verified repo-code finding)
Deeptide exists because DeepSeek users otherwise have to run general-purpose harnesses tuned for other providers. The three form factors deliberately share one interface contract (tide-spec), so configuration, sessions, and tools carry across the native macOS app, the Bun-based CLI, and the Rust binary. The macOS build embeds a local DeepSeek V4 Flash Metal inference engine with an OpenAI/Anthropic-compatible gateway, which lets the agent run fully on-device. It is aimed at DeepSeek-centric developers who want an agent, REPL, and inference runtime from one project rather than assembling them separately.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deeptide.md)
