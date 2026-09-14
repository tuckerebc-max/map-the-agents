# MiMo Code (`mimo-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: XiaomiMiMo
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=curl -fsSL https://mimo.xiaomi.com/install | bash
- Model providers: OpenAI-compatible, Xiaomi MiMo Platform, OpenAI/Codex, Claude Code, xAI/Grok, OpenRouter, custom providers
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: yes (yes)

Repository map entry: [xiaomimimo/mimo-code](../../repos/xiaomimimo/mimo-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Persistent cross-session memory via SQLite FTS5, subagent orchestration with parallel execution, goal-driven autonomous loops with independent judge models, compose workflows (specs-driven development), self-improvement via /dream and /distill, voice input via MiMo ASR, Max Mode (parallel best-of-N reasoning). Forked from OpenCode.

(captured site page body (agents/mimo-code.md), not a verified repo-code finding)
MiMo Code extends OpenCode's terminal harness with the persistence and autonomy layer Xiaomi wanted for long-running work. Memory lives in SQLite with FTS5: project knowledge in MEMORY.md, session checkpoints written by a dedicated checkpoint-writer subagent, scratch notes, and per-task progress logs, all re-injected automatically when a session resumes. The agent operates in build mode (full write permissions), plan mode (read-only exploration and design), or compose mode — a specs-driven workflow isolated from interactive editing — and a /goal condition is judged by an independent model so the loop does not stop prematurely. Deterministic JavaScript workflows orchestrate multi-agent pipelines (deep-research, fact-check, research-experiment built-ins) with bounded retries and parallelization, while subagents spawn on demand and run in parallel with lifecycle tracking. Voice input routes through MiMo ASR, and Max Mode runs best-of-N reasoning in parallel. The project is very active with roughly 12.9k stars, works with any OpenAI-compatible provider plus OAuth against Xiaomi MiMo, OpenAI, and xAI, and explicitly does not run in macOS Terminal.app.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mimo-code.md)
