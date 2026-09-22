# agents-cli (`agents-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: phnx-labs
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @phnx-labs/agents-cli (or curl -fsSL agi-cli.sh | sh)
- Model providers: Claude Code, Codex CLI, Antigravity, Grok Build, OpenClaw, Cursor, OpenCode, Copilot, Amp, Kiro, Kimi, MiniMax, GLM, Qwen, DeepSeek (via OpenRouter), Factory AI Droid, Meta Muse Code, Warp Agent CLI, Hermes Agent, Ollama, vLLM
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry (renamed): original lead [phnx-labs/agents-cli](https://github.com/phnx-labs/agents-cli) (source: backing, field: `source_code_url`) now resolves to [phnx-labs/agi-cli](../../repos/phnx-labs/agi-cli.md) (github id 1215855441, verified [https://github.com/phnx-labs/agi-cli](https://github.com/phnx-labs/agi-cli)).

## Description

Highlight (site page `what_makes_it_special`): Distributed agent factory — dispatches multiple AI coding agents (Claude, Codex, Antigravity, Grok, etc.) across your own machines in parallel on existing subscriptions. Fleet management, cross-agent session search, performance insights, routines/monitors scheduling, browser automation via your real Chrome, menu-bar fleet control, and one-config-syncs-to-all-agents resource management. Note: repo redirects to phnx-labs/agi-cli.

(captured site page body (agents/agents-cli.md), not a verified repo-code finding)
Individual developers accumulate subscriptions to several coding agents but can only run one or two at a time on a laptop. agents-cli turns the collection of machines a user already has into a dispatchable fleet: agents.yaml profiles are reconciled onto each device over SSH, OAuth logins stay native per machine rather than being copied, and runs fan out to one device or all of them through the same CLI. Routines (cron-style schedules) and event-driven monitors turn recurring work into scheduled jobs, while the feed, insights, and a macOS menu bar surface every open question across the fleet. Teams run parallel agents in dependency order, each in an isolated worktree, and cloud dispatch can hand tasks to managed providers that open PRs. It is free with no account requirement, licensed under FSL-1.1-Apache-2.0.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agents-cli.md)
