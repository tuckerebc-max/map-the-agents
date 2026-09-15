# agentbridge (`agentbridge`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: catatafishen
- License: Apache-2.0
- Language: Java
- Interface: platforms=IDE; install=JetBrains Marketplace (recommended, auto-updates), or build from source and install via Settings \> Plugins \> Install Plugin from Disk
- Model providers: GitHub Copilot, Claude Code, Codex, Kiro, Junie, OpenCode, Hermes Agent, Mistral Vibe
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [catatafishen/agentbridge](../../repos/catatafishen/agentbridge.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): JetBrains IDE plugin bridging AI coding agents to IntelliJ platform APIs through 120+ native MCP tools, letting agents call deterministic IntelliJ tools (PSI, VFS, refactoring engine, test runner, debugger) directly instead of relying on LLMs to approximate code intelligence from text. Supports 8 agents with one-click switching and cross-client session resume.

(captured site page body (agents/agentbridge.md), not a verified repo-code finding)
When a coding agent edits through a terminal, it sees IntelliJ projects as text and misses what the compiler, index, and refactoring engine already know. agentbridge closes that gap by exposing the IntelliJ platform — PSI syntax trees, VFS, refactoring actions, test runner, build system — as 120-plus MCP tools over an HTTP bridge, so agents like Claude Code, Codex, Copilot, Kiro, Junie, or OpenCode call deterministic IDE operations instead of guessing. Per-agent tool permissions gate what each client may touch, sessions resume across clients, and a PWA exposes the chat over HTTPS from any device. Developers working in JetBrains IDEs who want agents to use the IDE's own code intelligence are the audience.
Sources: [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/agentbridge.md)
