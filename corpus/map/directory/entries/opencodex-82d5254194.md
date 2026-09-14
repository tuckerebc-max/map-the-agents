# OpenCodex (`opencodex`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: lidge-jun
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm
- Model providers: OpenAI, Anthropic, Google Gemini, xAI, Kimi, Azure OpenAI, Ollama, DeepSeek, Groq, OpenRouter, Together, Fireworks, Cerebras, Mistral, HuggingFace, NVIDIA NIM, MiniMax, Qwen Cloud, SiliconFlow, 40+ providers
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [lidge-jun/opencodex](../../repos/lidge-jun/opencodex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Universal local proxy that translates OpenAI Codex's Responses API into any LLM provider's format (streaming, tool calls, reasoning tokens, images). Unifies four AI coding tools (Codex CLI/App/SDK, Claude Code, Claude Desktop, Grok Build) with any model while preserving native UIs. Combos feature for virtual model IDs with failover or weighted round-robin. ChatGPT account pooling with quota-aware routing and thread affinity. ...

(captured site page body (agents/opencodex.md), not a verified repo-code finding)
Codex speaks OpenAI's Responses API, Claude Code speaks Anthropic's, and Grok Build has its own protocol, so mixing providers across those tools means juggling keys, endpoints, and incompatible streaming formats. OpenCodex runs a local proxy on localhost:10100 that speaks the Responses API on one side and translates to Claude, Gemini, Grok, GLM, DeepSeek, Kimi, Qwen, Ollama, and other OpenAI-compatible endpoints on the other, handling streaming, tool calls, reasoning tokens, and images in both directions. ChatGPT account pooling adds quota-aware routing across accounts, and model combos provide failover or round-robin across providers; a web dashboard exposes traffic and configuration. Install is npm -g with an ocx CLI that can register itself as a background service on launchd, systemd, or Task Scheduler. The maintainers explicitly warn it is unaffiliated with OpenAI and Anthropic and that some providers may suspend accounts routed through third-party proxies, so it targets users who accept that risk.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencodex.md)
