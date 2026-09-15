# Agent GUI (`agent-gui`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: matsumo0922
- License: MIT
- Language: Kotlin
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: Anthropic (via Claude Code CLI)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Native chat GUI for AI coding agents inside JetBrains

(captured site page body (agents/agent-gui.md), not a verified repo-code finding)
Running Claude Code next to IntelliJ means context lives in two places: the IDE knows the project, the terminal knows the agent. Agent GUI embeds the agent as a native JetBrains tool window built with Compose for IDE, streaming responses with markdown rendering, visualizing tool calls and sub-agent tasks inline, and routing file-edit permissions through approve/deny prompts inside the IDE. Sessions persist across IDE restarts, files attach to prompts, and the UI follows the editor's light/dark theme. It currently drives Claude Code (CLI on PATH with an Anthropic API key or Claude Max plan), with Codex support planned. JetBrains-centric developers who want their agent conversation co-located with their code are the audience.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/agent-gui.md)
