# bbarit-agent-oss (`bbarit-agent-oss`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: bbarit
- License: MIT
- Language: Rust
- Interface: platforms=CLI, IDE; install=curl -fsSL https://bbarit.com/agent/install.sh | sh (macOS/Linux); irm https://bbarit.com/agent/install.ps1 | iex (Windows); or cargo build --release; self-update via bbarit-oss --upgrade
- Model providers: Anthropic, OpenAI, Google Gemini/Vertex, OpenRouter, Groq, Mistral, Together, Fireworks, DeepSeek, Cerebras, Amazon Bedrock, GitHub Copilot, Ollama (15+ providers, 1000+ models)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [bbarit/bbarit-agent-oss](../../repos/bbarit/bbarit-agent-oss.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Single self-contained Rust binary AI coding agent (no Node/Python runtime); 295 curated agent personas across 30 domains; built-in project wiki for cross-session knowledge persistence, cross-session auto-memory, bundled semantic code search (semble engine), multi-process parallel sub-agents via --orchestrate; can reuse existing Claude Code & Codex MCP servers/skills via /interop.

(captured site page body (agents/bbarit-agent-oss.md), not a verified repo-code finding)
bbarit-agent-oss is a terminal-native AI coding agent distributed as a single static Rust binary with no Node or Python runtime dependency, originating from the agent inside the BBARIT desktop IDE and rewritten from Pi with documented provenance. It supports 15+ LLM providers and over a thousand models (Anthropic, OpenAI, Gemini, OpenRouter, Groq, Bedrock, Copilot, Ollama), switchable mid-session, and works fully offline with Ollama. Sessions support branching, forking, and export; a built-in project wiki persists cross-session knowledge; and an --orchestrate mode runs parallel sub-agents. 295 personas across 30 domains ship by default with a read-only persona mode, and a bundled semantic code search tool (semble) indexes repos. It is MIT-licensed, installed via curl script or cargo, and aimed at developers wanting a private, single-binary agent that owns its keys and data.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bbarit-agent-oss.md)
