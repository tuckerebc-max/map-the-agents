# agentnotch (`agentnotch`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: AppGram
- License: MIT
- Language: Swift
- Interface: platforms=Desktop, IDE; install=brew tap AppGram/tap && brew install --cask agentnotch (or manual download from GitHub Releases)
- Model providers: Claude Code, OpenAI Codex (observes via OTLP telemetry)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [appgram/agentnotch](../../repos/appgram/agentnotch.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): macOS menu-bar app living in the Mac notch that shows real-time AI coding assistant telemetry (tool calls, token usage, cost estimates); uses source-aware color indicators (orange for Claude, blue for Codex), runs 100% locally for privacy, expands on hover to show activity.

(captured site page body (agents/agentnotch.md), not a verified repo-code finding)
Coding agents run long tool sequences in a terminal, and developers currently have no ambient way to see what the agent is doing without switching windows. AgentNotch receives OpenTelemetry OTLP logs and metrics that Claude Code and Codex CLI emit after a one-line configuration change (OTEL_EXPORTER_OTLP_ENDPOINT for Claude Code, an \[otel\] block in ~/.codex/config.toml), and renders tool calls, token usage, and cost estimates in the notch, expanding on hover. Completion notifications fire when a run finishes, and source-based coloring distinguishes which assistant produced each event. Everything is processed locally on port 4318; the app sends nothing anywhere. It targets macOS 14+ on notch-equipped MacBook Pros, falling back to the menu bar elsewhere.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentnotch.md)
