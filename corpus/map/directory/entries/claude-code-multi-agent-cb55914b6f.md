# Claude-Code-Multi-Agent (`claude-code-multi-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Prorise-cool
- License: MIT
- Language: Python
- Interface: install=Install Ollama + uv, git clone, configure .env, place project in directory and open with Claude Code
- Model providers: Ollama (gemma3:1b, llama3.2:3b, qwen2.5:7b), Anthropic (Claude Code)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [prorise-cool/claude-code-multi-agent](../../repos/prorise-cool/claude-code-multi-agent.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Intelligent development framework for Claude Code that adds project awareness via a Hooks system. Uses Ollama (local LLM) to auto-detect project type/framework, recommend 300+ expert Skills, perform intent analysis, and maintain docs automatically. Replaces Memory MCP with document-driven context injection to avoid context explosion.

(captured site page body (agents/claude-code-multi-agent.md), not a verified repo-code finding)
The framework addresses context amnesia in Claude Code: sessions start cold, conventions drift, and documentation rots. It works by cloning a dedicated workspace, placing the project inside, and wiring hooks so that every session start injects detected project context, relevant skills, and intent analysis from a locally running Ollama model, so no extra cloud calls are needed for the meta-layer. Recommended MCP tools and execution plans are surfaced per prompt, and predefined command workflows cover spec-driven development and git workflows. Solo developers, primarily in the Chinese-language community, use it; the repo has few commits and no releases beyond v1.0.0.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-code-multi-agent.md)
