# Crush (`crush`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: charmbracelet
- License: FSL-1.1-MIT
- Language: Go
- Interface: platforms=CLI; install=Homebrew, NPM, Winget, Scoop, apt (Debian/Ubuntu), yum (Fedora/RHEL), Nix, FreeBSD pkg, Arch (yay), go install, or direct binary download
- Model providers: Charm Hyper, Anthropic, OpenAI, Google Gemini, OpenRouter, Amazon Bedrock, Azure OpenAI, Vertex AI, Ollama, llama.cpp, LM Studio, LiteLLM, Groq, Cerebras, Hugging Face, Moonshot, MiniMax, Z.ai, Vercel AI Gateway, any OpenAI/Anthropic-compatible API
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [charmbracelet/crush](../../repos/charmbracelet/crush.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Glamourous terminal-based coding agent by Charmbracelet. Supports multi-model LLMs, session-based contexts, LSP integration, MCP servers (stdio/http/sse with OAuth), agent skills (agentskills.io standard), and preliminary hooks support.

(captured site page body (agents/crush.md), not a verified repo-code finding)
Crush is Charmbracelet's entry into terminal coding agents, built to run anywhere a terminal exists: macOS, Linux, Windows, BSDs, and even Android. It maintains multiple named sessions per project, enriches model context through language servers, and connects to tools via MCP servers (with OAuth) and the agentskills.io Agent Skills standard, with hooks and configurable permissions including a --yolo bypass. Any OpenAI- or Anthropic-compatible provider works, alongside auto-discovered local models through Ollama or LM Studio, and models can be switched mid-session without losing context. Charm offers its own Hyper subscription as the hosted option, while the agent itself installs through Homebrew, npm, winget, and most system package managers; with about 28,000 GitHub stars it is one of the most widely used open terminal agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/crush.md)
