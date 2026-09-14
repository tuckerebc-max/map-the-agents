# interface (`interface`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: arctic-cli
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=curl -fsSL https://usearctic.sh/install | bash
- Model providers: OpenAI, Anthropic, Google, Perplexity, OpenRouter, Ollama
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [arctic-cli/interface](../../repos/arctic-cli/interface.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-provider AI coding interface with real-time usage tracking, multiple accounts per provider (personal + work), switch models mid-conversation, imports existing Claude Code and OpenCode config (custom commands, agents, MCP servers).

(captured site page body (agents/interface.md), not a verified repo-code finding)
Arctic's premise is that heavy agent users juggle subscriptions: Claude here, Codex there, a work Copilot account, and no single view of what is left. The interface aggregates coding plans from ten providers (Claude Code, Codex, Gemini CLI, Antigravity, Copilot, Z.AI, Kimi, Amp, Qwen, MiniMax) alongside BYOK APIs (OpenAI, Anthropic, Google, Perplexity, OpenRouter, Ollama), tracking usage in real time and letting you switch models mid-conversation. Existing Claude Code and OpenCode setups import directly, so agents, slash commands, and MCP servers carry over without reconfiguration. Local-first storage keeps conversations on-device; an anonymous telemetry phase is opt-out. It targets developers juggling personal and work AI accounts across several agent subscriptions.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/interface.md)
