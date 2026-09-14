# clawcodex (`clawcodex`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: agentforce314
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: Anthropic, OpenAI, DeepSeek, MiniMax, Gemini, OpenRouter, Ollama, vLLM, sglang, Groq, Cerebras, xAI, and more (30 total); subscription auth: Claude Pro/Max, ChatGPT Plus/Pro
- Feature flags (directory-reported):
  - mcp_support: partial — MCP-oriented tools and wiring implemented; clawcodex mcp serve re-exposes tools as MCP stdio server; OAuth server auth; full protocol polish ongoing (reported)
  - plugin_support: partial — plugins listed under Phase 4 roadmap (in progress); markdown-based SKILL.md slash commands as plugin-like system (reported)
  - claude_code_plugin: no (no)
  - subagents: yes — Agent fan-out with parallel execution, isolated AbortControllers, concurrency-cap; /advisor worker/reviewer pairing; coordinator mode; Team/Brief tools (yes)
  - hooks: yes — production as of v1.0.0; types: UserPromptSubmit, PreToolUse (permissionDecision), PermissionRequest, MCP elicitation, teammate TaskCompleted/TeammateIdle stop hooks (yes)
  - plan_mode: yes — /plan mode with implicit entry/exit; keeps restraining edits even in Full Access sessions; --permission-mode plan flag (yes)

Repository map entry: [agentforce314/clawcodex](../../repos/agentforce314/clawcodex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Production-oriented Python rebuild of Claude Code (~310K lines); Terminal-Bench 2.1 score 80.9%; 30 model providers vs Claude Code's Claude-only limitation; /eco token compression (80% fewer Bash-output tokens); DeepSeek prefix cache (~230x cheaper); three UIs (TUI, Web, Desktop).

(captured site page body (agents/clawcodex.md), not a verified repo-code finding)
ClawCodex keeps Claude Code's architecture - the same query loop, tool set, two-tier state, and hooks - while removing its single-vendor constraint: thirty providers from Anthropic and OpenAI to DeepSeek, MiniMax, Ollama, and vLLM are supported, plus subscription OAuth for Claude Pro/Max and ChatGPT. Its /eco toggle applies deterministic output filters (failure-focused test summaries, git and package-manager ceremony stripping, log dedup) to cut Bash output tokens by roughly 80 percent, with full output teed to disk so nothing is lost. The agent core is shared by CLI, TUI, Desktop, and Web surfaces, and releases ship weekly with published benchmark claims. Engineers who want the Claude Code workflow on cheaper or local models are the target users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/clawcodex.md)
