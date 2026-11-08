# tokentelemetry (`tokentelemetry`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: VasiHemanth
- License: MIT
- Language: Python, TypeScript
- Interface: platforms=Autonomous, CLI; install=macOS/Linux: curl -fsSL https://tokentelemetry.com/install.sh | bash; Windows: irm https://tokentelemetry.com/install.ps1 | iex; or clone and run ./start.sh / start.bat / node bin/cli.js
- Model providers: Anthropic, Google, OpenAI, xAI, Meta (Muse), Qwen (provider-aware pricing across direct/OpenRouter/Together/Fireworks)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: n/a (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [vasihemanth/tokentelemetry](../../repos/vasihemanth/tokentelemetry.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 100% local observability dashboard for AI coding agents and autonomous agents: tracks token usage, LLM costs, tool calls, session traces, and reasoning steps. Zero-config (auto-detects agent logs), no signup, no SDK, no cloud - unlike Langfuse/LangSmith/Helicone. Includes a dedicated Hermes Agent autonomous-agent dashboard across 38 source platforms.

(captured site page body (agents/tokentelemetry.md), not a verified repo-code finding)
tokentelemetry is a local-first observability dashboard for AI coding and autonomous agents, built on the observation that most agents already write detailed JSONL logs that nobody aggregates. It watches those files directly — Claude Code's session logs, Gemini CLI, Codex, Cursor, Copilot, OpenCode, and more — parsing token counts, tool calls, session traces, and reasoning steps without any SDK, instrumentation, or account, then renders dashboards for usage, per-project costs with provider-aware pricing, budgets, and traces; a dedicated Hermes Agent view covers that autonomous agent's 38 source platforms, skills, memory, and subagents. The stack is FastAPI plus Next.js, state lives in plain JSON under ~/.tokentelemetry, and everything binds to localhost with optional token-authed remote access; the only outbound calls are an update check and opt-in, content-free telemetry. It is MIT-licensed, installable via a curl script, and positioned against cloud APM tools like Langfuse and LangSmith for developers who want cost and behavior visibility without sending data anywhere.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/tokentelemetry.md)
