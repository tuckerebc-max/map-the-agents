# Orca (`orca-orchestrator`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: junkyard22
- License: PolyForm Noncommercial 1.0.0
- Language: TypeScript
- Interface: platforms=Desktop; install=git clone, pnpm install, run apps/desktop (Electron) or apps/runner (CLI)
- Model providers: OpenRouter, Ollama
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [junkyard22/orca](../../repos/junkyard22/orca.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-Role AI Agent Runtime orchestrating multiple AI roles through a quality-gated pipeline (Brain -\> Miranda -\> Pappy -\> Benson). Maestro manages a subagent pool (brain, strong_model, cheap_model, reviewer, narrator, planner_deep, debugger, reader, vision). MCP support, SQLite persistence, role routing between cheap and strong models, self-improving distillation loop, and training-data export for fine-tuning — all running locally.

(captured site page body (agents/orca-orchestrator.md), not a verified repo-code finding)
Single-model coding pipelines blur responsibility: the same context plans, codes, reviews, and talks to the user, so quality control becomes an afterthought. Orca assigns each function a named role in a fixed pipeline — Brain decomposes the request, Miranda runs a PLAN-ANSWER-CRITIQUE-REWRITE compliance loop, Pappy issues PASS/WARN/FAIL quality verdicts, and Benson handles intent parsing — with a Maestro router managing a nine-role subagent pool that includes strong and cheap model tiers, debugger, reviewer, and vision roles. Runs persist in SQLite, MCP connects external tools, and a distillation loop exports interactions as training data for fine-tuning. The runtime is a TypeScript pnpm monorepo with an Electron desktop app and a CLI runner keyed to OpenRouter or local Ollama, under a PolyForm Noncommercial license and aimed primarily at Windows. It is an early personal project (39 stars, 442 commits) exploring role-decomposed agent architectures.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/orca-orchestrator.md)
