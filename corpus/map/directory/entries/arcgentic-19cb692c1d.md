# Arcgentic (`arcgentic`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Arch1eSUN
- License: MIT
- Language: Python, JavaScript
- Interface: install=npm install -g arcgentic; pipx install arcgentic; /plugin marketplace add Arch1eSUN/Arcgentic; git clone + scripts/install-codex-local.sh
- Model providers: OpenAI (Codex), Anthropic (Claude Code)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [arch1esun/arcgentic](../../repos/arch1esun/arcgentic.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Harness engineering layer for AI coding agents (Codex & Claude Code). Turns ad-hoc prompting into a gated engineering workflow with fixed roles (Orchestrator, Planner, Developer, Test, Auditor), stop states, audit gates, and evidence-based pass/fix decisions. Features a configurable role-routing topology engine.

(captured site page body (agents/arcgentic.md), not a verified repo-code finding)
Ad-hoc prompting of coding agents produces drift: silent scope changes, skipped tests, and unverified done claims. Arcgentic is a layer installed into Codex or Claude Code that structures each session into an Orchestrator dispatching fixed Planner, Developer, Test, and Auditor roles through plan, build, self-audit, and independent-audit gates, with NEEDS_FIX loops and stop states enforced at each handoff. Role routing runs through a topology engine overridable via state.yaml, with an optional MCP server exposing a live status panel of round progress and verdicts. It ships as a Claude Code plugin, Codex plugin, and pipx/npm CLI, requiring no model keys of its own. It targets developers running Claude Code or Codex who want audit-grade discipline on personal or small-team projects.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/arcgentic.md)
