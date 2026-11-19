# Agav (`agav`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: prapaa-ai
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=curl -fsSL https://agav.dev/install.sh | bash (self-contained binary, no Node.js); Windows: irm https://www.agav.dev/install.ps1 | iex; binaries from GitHub releases
- Model providers: Anthropic, OpenAI, OpenRouter, NVIDIA NIM, Google Gemini, Vertex AI, Ollama (switch mid-session with /model)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [prapaa-ai/agav](../../repos/prapaa-ai/agav.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A terminal coding agent built around harness efficiency — cached context, bounded retries and budgets, interrupted repair loops, and isolated subagent exploration — publishing its cost methodology alongside its benchmarks, with per-action tool permissions, sandboxed commands on macOS and Linux, and skills, plugins and an agent marketplace on top.

(captured site page body (agents/agav.md), not a verified repo-code finding)
Agav is an open-source terminal agent for work in real repositories, and its distinguishing bet is that coding cost is a harness problem: it reuses cached context, limits repeated work, interrupts unproductive repair loops, bounds retries and token budgets, and keeps subagent exploration in fresh contexts so the same repository context is not resent over and over. The authors publish the evidence with the engineering — a Terminal-Bench 2.1 cost study reporting 15.2¢ median trial cost and 49.1% lower total spend than Codex at matched rates, alongside the accuracy numbers and their limitations, and a #1-verified spot on the SWE-bench-Live Lite leaderboard at the time of the README — which sets it apart from harnesses that quote only accuracy. Day to day it behaves like a modern coding CLI: inspect code, make focused edits, run tests, verify changes, with LSP queries, notebook support, /undo, and a planning UI whose plans survive restarts; sessions resume, branch, and compact without losing the plan; /permission switches ask/auto-accept/deny-writes mid-session; and non-interactive agav run takes a one-shot prompt for scripts and CI with per-tool permissions and optional JSON Schema output. Local plugins are plain JavaScript tools in ~/.agav/plugins, subagents take scoped work on the same or a different model, skills bundle instructions, a marketplace offers installable service agents, and background jobs with cron schedules outlive a single turn. API keys are encrypted at rest, local-first ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/agav.md)
