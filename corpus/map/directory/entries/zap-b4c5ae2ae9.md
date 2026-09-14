# Zap (`zap`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: zap-coding-agent
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=macOS/Linux: curl -fsSL https://raw.githubusercontent.com/zap-coding-agent/zap-coding-agent/main/install.sh | bash; Windows: download zip from releases; Build: cargo build --release; also on crates.io
- Model providers: Anthropic, OpenAI, Google Gemini (incl. keyless gcloud ADC), LM Studio, Ollama, Groq, OpenRouter, DeepSeek, xAI, Together AI, Mistral, Perplexity, Cohere, any OpenAI-compatible endpoint
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [zap-coding-agent/zap-coding-agent](../../repos/zap-coding-agent/zap-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Zap is a Rust, terminal-first coding agent distributed as a single statically-linked binary with a millisecond cold start and roughly 20 MB idle memory, designed around eliminating prompt bloat. Start
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
