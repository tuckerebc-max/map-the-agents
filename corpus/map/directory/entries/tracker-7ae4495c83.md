# Tracker (`tracker`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: 2389-research
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=brew install 2389-research/tap/tracker or go install
- Model providers: Anthropic, OpenAI, Gemini, OpenAI-compatible APIs
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (parallel agent fan-out/fan-in, subgraphs) (yes)
  - hooks: yes (human-in-the-loop gates) (yes)
  - plan_mode: yes (pipeline definitions in .dip files) (yes)

Repository map entry: [2389-research/tracker](../../repos/2389-research/tracker.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Pipeline orchestration engine for multi-agent LLM workflows that executes pipelines defined in the Dippin DSL (.dip files) with parallel LLM agents, human-in-the-loop gates, Slack bot and terminal REPL front-ends, cost governance/budget limits, decision audit trails, and git checkpointing. Embedded workflows include ask_and_execute (competitive implementation across Claude/Codex/Gemini) and build_product (milestone-based spec-driven building).

(captured site page body (agents/tracker.md), not a verified repo-code finding)
Tracker is a pipeline orchestration engine for multi-agent LLM workflows rather than a coding agent itself. Pipelines are authored in the Dippin DSL as .dip files — node graphs of agent, tool, human, parallel, and subgraph steps — and Tracker executes them with parallel LLM agent fan-out and fan-in, human-in-the-loop gates that pause for approval, and budget limits that enforce cost governance. A human-facing TUI dashboard surfaces live status, and Slack bot and terminal REPL front-ends let operators drive runs from where they already work. Every decision is recorded to an audit trail and each step is git-checkpointed, so a failed run can be inspected and resumed. Embedded workflows ship out of the box: ask_and_execute runs competitive implementations across Claude, Codex, and Gemini, and build_product drives milestone-based spec-driven building. The audience is teams orchestrating coding agents through defined, reviewable pipelines.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tracker.md)
