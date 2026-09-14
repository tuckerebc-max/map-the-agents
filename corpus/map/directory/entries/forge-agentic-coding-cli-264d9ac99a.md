# Forge-Agentic-Coding-CLI (`forge-agentic-coding-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: hoangsonww
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE, Web; install=npm install -g @hoangsonw/forge, Docker, docker compose, or VS Code extension
- Model providers: Ollama, LM Studio, vLLM, llama.cpp, OpenAI-compatible (OpenAI/Azure/LocalAI/Together/Groq/Fireworks), Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [hoangsonww/forge-agentic-coding-cli](../../repos/hoangsonww/forge-agentic-coding-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first, plan-first, multi-agent, programmable software-engineering runtime with its own scheduler, sandbox, default-deny permission system, state machine, agentic loop, and 4-tier memory (hot/warm/cold/learning). Fully inspectable and replayable sessions (JSONL/SQLite), 6 built-in role-typed agents (planner, architect, executor, reviewer, debugger, memory), no telemetry.

(captured site page body (agents/forge-agentic-coding-cli.md), not a verified repo-code finding)
Forge was built as an alternative to trusting a hosted agent with your repository: everything runs locally with no telemetry, actions pass through a default-deny permission system with a realpath-confined filesystem and destructive-command blocking, and secrets live in the OS keychain. Requests flow through a plan-first loop — classify, plan into a DAG, user approval, bounded execution, validation gate, reviewer — with retry capped at three before a debugger diagnosis phase. Local model runtimes (Ollama, LM Studio, vLLM, llama.cpp) are auto-detected and prompts are adapted across 41 classified model families per agent role, with hosted Anthropic/OpenAI-compatible access optional. Nine enforceable modes with per-mode budgets, a local web dashboard, a GitHub Action, and 24 subcommands round out a runtime aimed at developers who want Claude Code-style capability without cloud dependency.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/forge-agentic-coding-cli.md)
