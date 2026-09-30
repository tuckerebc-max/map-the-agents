# Claude Code Tools (`claude-code-tools`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: pchalasani
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=pip
- Model providers: BYOK (alt-llm-providers integration)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [pchalasani/claude-code-tools](../../repos/pchalasani/claude-code-tools.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Practical productivity toolkit spanning multiple CLI coding agents (Claude Code, Codex-CLI, and similar), offering tools like aichat-search, voxtype voice input, tmux-cli, amux, agent-tunnel, session porting between Claude and Codex, inter-agent messaging, Google Docs/Sheets integrations, and safety hooks.

(captured site page body (agents/claude-code-tools.md), not a verified repo-code finding)
The toolkit solves context loss and operational friction across CLI agents: histories and sessions are trapped inside each tool, so aichat-search indexes them for retrieval, and the session-porting tool converts a Claude Code conversation into a Codex session and vice versa, letting work migrate between agents mid-task. Around that core, voxtype adds voice input, amux runs multiple agents concurrently, agent-tunnel exposes remote access, and github-watch wakes agents when PR comments arrive. Components are pip/crates-installable and integrate through Claude Code's plugin, hook, and skill mechanisms rather than replacing the agents. Developers running multi-agent workflows use it; it is MIT-licensed and actively maintained with roughly two thousand stars.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/claude-code-tools.md)
