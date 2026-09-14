# Zot (`zot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: patriceckhart
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl -fsSL https://www.zot.sh/install.sh | bash (single static Go binary; also manual download from GitHub releases)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: unknown (unknown)
  - subagents: yes (yes)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [patriceckhart/zot](../../repos/patriceckhart/zot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A deliberately minimal terminal coding agent shipped as one static Go binary with a four-tool toolbox (read, write, edit, bash), no mandatory MCP, extensions in any language over subprocess JSON-RPC, and a Telegram bridge for driving the agent by direct message.

(captured site page body (agents/zot.md), not a verified repo-code finding)
Zot is built as a counter-position to harness bloat: a terminal coding agent shipped as a single static Go binary with no runtime, no Docker, and no package manager — put it on the PATH and it works. Its tool set is deliberately the minimum viable set for a coding loop (read, write, edit, bash), a design stance the project maintains rather than grows past. Model access is nonetheless broad, with a unified catalog spanning Anthropic, OpenAI, Gemini, Bedrock, Azure, Ollama, llama.cpp, and roughly twenty other providers, plus custom entries through models.json. When four tools are not enough, extensions connect over JSON-RPC from any language, registering slash commands, tools, permission gates, and interactive panels — installed opt-in rather than bundled. Sessions can be resumed, forked, branched, compacted, and exported, background subagent loops run within the same repository, and an unusual Telegram bridge lets the agent be steered by direct message from a phone. The project is MIT-licensed, hosted on GitHub, and self-described as in beta indefinitely; the harness itself is free with users paying provider API costs shown per model in the UI. Its audience is developers who want a small, inspectable harness they can carry as one binary rather than a platform.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zot.md)
