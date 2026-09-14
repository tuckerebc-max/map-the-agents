# tig (`tig`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: rsrohan99
- License: unknown
- Language: Python
- Interface: platforms=CLI; install=pip install tig-code
- Model providers: OpenAI, Anthropic, Google, DeepSeek, Groq, Ollama, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [rsrohan99/tig](../../repos/rsrohan99/tig.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-based autonomous AI coding agent similar to Claude Code/OpenAI Codex but works with many more LLMs; uses LlamaIndex Workflow, Tree-sitter, Ripgrep, and Google's diff-match-patch. Has an Architect mode (designs system) and Code mode (implements plan).

(captured site page body (agents/tig.md), not a verified repo-code finding)
Tig is a terminal coding agent built in the vein of Claude Code but with provider breadth as its main feature: it runs against Gemini, OpenAI, Claude, DeepSeek, Groq, OpenRouter, or local Ollama models, selected through environment variables. Work is split into two modes — Architect, which discusses a design with the user and saves it to a markdown file, and Code, which implements the plan step by step with approval gates (or --auto-approve for unattended runs). Under the hood it composes LlamaIndex Workflows for orchestration, tree-sitter for symbol search and syntax validation, ripgrep for fast text search, and diff-match-patch for reviewable diffs. The project is a compact Python package (pip install tig-code) with a YouTube build-along series, which doubles as its documentation. It suits developers who want a Claude Code-style loop untethered from any single vendor.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tig.md)
