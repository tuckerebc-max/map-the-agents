# Zap (`zap`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): Terminal-first, local AI coding agent built in Rust (single statically-linked binary, ~20 MB idle memory, millisecond cold start). AST-powered code indexing (tree-sitter + SQLite) — deliberately opposite to Claude Code's no-index approach; knows what exists before writing. Skill-first prompt architecture (~1.8k token baseline vs ~8-10k in competitors). Lazy-loaded MCP with zero token cost until a server is needed. SLM support ...

(captured site page body (agents/zap.md), not a verified repo-code finding)
Zap is a Rust, terminal-first coding agent distributed as a single statically-linked binary with a millisecond cold start and roughly 20 MB idle memory, designed around eliminating prompt bloat. Startup builds a tree-sitter-plus-SQLite symbol index that powers code_map, find_definition, find_references, ripple_analysis, and LSP-backed diagnostics across Rust, Python, TypeScript, JavaScript, Go, and Java, with ripgrep as fallback. Its prompt architecture is skill-first: 23 built-in markdown skills inject only on keyword triggers, compatible with the SKILL.md standard and importable from Claude Code, Cursor, and Kiro. MCP servers load lazily via mcp_connect() so unused tool schemas cost zero tokens, and per-task model routing can split coding and review across different models. Security features include permission modes, Docker/Podman shell sandboxing, a 25-pattern secret scanner, full audit logging, and per-edit undo.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/zap.md)
