# codehamr (`codehamr`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: codehamr
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl -fsSL https://codehamr.com/install.sh | bash (Linux/macOS); Windows: install.cmd
- Model providers: Ollama, vLLM, LM-Studio (local); any OpenAI-compatible endpoint (OpenAI, OpenRouter)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [codehamr/codehamr](../../repos/codehamr/codehamr.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Minimalist terminal coding agent for local LLMs: three slash commands, one embedded system prompt, no router/sub-agents/skills/MCP. Designed for local LLMs where the context window is precious; verifies its own work by running tests/compiling as a habit, not a gate.

(captured site page body (agents/codehamr.md), not a verified repo-code finding)
Codehamr is written for developers who run coding agents against local models, where the context window is the scarce resource. The design keeps everything out of the prompt that is not the user's work: three slash commands, a single embedded system prompt, and a plain tool loop over bash, file reading, writing, and editing, with verification by running tests or compiling treated as habit rather than enforcement. It targets roughly 30B-class models on hardware with 32GB or more of unified memory, seeded with qwen3 27B over Ollama, vLLM, or LM Studio, while also accepting any OpenAI-compatible cloud endpoint. There is no router, subagent system, skill loader, or MCP layer, and HamrPass — an optional waitlisted hosted endpoint — exists as an optional convenience rather than a requirement. The agent is written in Go and installs via curl scripts on Linux, macOS, and Windows (WSL2).
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codehamr.md)
