# clawcodex (`clawcodex`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
ClawCodex keeps Claude Code's architecture - the same query loop, tool set, two-tier state, and hooks - while removing its single-vendor constraint: thirty providers from Anthropic and OpenAI to DeepS
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
