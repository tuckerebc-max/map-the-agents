# agent-of-empires (`agent-of-empires`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: agent-of-empires
- License: MIT
- Language: Rust
- Interface: platforms=CLI, Web; install=brew
- Model providers: Anthropic, OpenAI, Google, Mistral, BYOK
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [njbrake/agent-of-empires](https://github.com/njbrake/agent-of-empires) (source: backing, field: `source_code_url`) now resolves to [agent-of-empires/agent-of-empires](../../repos/agent-of-empires/agent-of-empires.md) (github id 1131238324, verified [https://github.com/agent-of-empires/agent-of-empires](https://github.com/agent-of-empires/agent-of-empires)).

## Description

Highlight (site page `what_makes_it_special`): Session manager for AI coding agents (TUI + web dashboard) that runs multiple agents in parallel across git branches in isolated tmux sessions with optional Docker sandboxing, accessible from any browser or phone.

(captured site page body (agents/agent-of-empires.md), not a verified repo-code finding)
Running several coding agents against one repository creates branch collisions and terminal sprawl, so agent-of-empires assigns each agent its own git branch inside an isolated tmux session, with Docker sandboxing optional for riskier work. It speaks the Agent Client Protocol, which is why the web dashboard can show structured views — plan panels, tool-call cards, swipe-to-approve permission requests — instead of raw terminal output, all reachable from a laptop browser or a phone. A TUI covers terminal-native workflows, and agents (Claude Code, Codex CLI, Gemini CLI, OpenCode) run in parallel across branches. It is MIT-licensed Rust, installed via brew or an install script, aimed at developers running several agents concurrently.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/agent-of-empires.md)
