# OpenCursor (`opencursor`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: PawanOsman
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=VS Code Marketplace
- Model providers: OpenAI, Anthropic, Gemini, OpenRouter, Ollama, llama.cpp, custom OpenAI-compatible/Anthropic-style endpoints
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [pawanosman/opencursor](../../repos/pawanosman/opencursor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first / offline capable (built-in llama.cpp, Ollama, on-device ONNX MiniLM embeddings for semantic search), no cloud required; per-hunk inline review CodeLenses without git; OAuth subscription reuse for Claude Code, OpenAI Codex, Google Antigravity; 25 tools; 11 lifecycle hooks (Cursor/Claude-Code compatible); risk-heuristic approval policies.

(captured site page body (agents/opencursor.md), not a verified repo-code finding)
Cursor-class assistants assume cloud APIs and per-token billing, which excludes air-gapped machines, sensitive codebases, and users avoiding subscription lock-in. OpenCursor takes the Cursor experience into a VS Code extension with a 25-tool agentic loop — workspace reading, file editing, command execution, semantic search — and makes the offline path first-class: it spawns and manages a llama.cpp server for GGUF models pulled from Hugging Face, supports Ollama, and computes semantic-search embeddings on-device with ONNX MiniLM, so it works in airplane mode. When cloud models are wanted, OAuth sign-in reuses Claude Code, OpenAI Codex, or Google Antigravity subscriptions instead of API keys, alongside standard OpenAI/Anthropic/Gemini/OpenRouter keys and MCP, hooks, and subagents across Agent/Ask/Plan/Debug/Multitask modes. It installs from the VS Code Marketplace under MIT. Developers who want a Cursor-style agent under their own hardware and terms are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencursor.md)
