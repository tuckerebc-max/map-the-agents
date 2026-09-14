# ACP Client (`acp-client`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Jun Han
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=Install from the VS Code Marketplace
- Model providers: agent CLIs: Copilot, Claude Code, Gemini CLI, Qwen Code, Auggie, Qoder, Codex CLI, OpenCode, OpenClaw, Kiro CLI, custom ACP agents
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Agent Client Protocol client connecting Copilot, Claude Code, Gemini CLI, Qwen Code, Codex CLI, OpenCode

(captured site page body (agents/acp-client.md), not a verified repo-code finding)
The Agent Client Protocol standardizes how editors talk to coding agents, but each editor needs a client implementation, and VS Code's built-in options leave gaps. ACP Client plugs the protocol into VS Code with 11 agents pre-configured — GitHub Copilot, Claude Code, Gemini CLI, Qwen Code, Codex CLI, OpenCode, Auggie, and more — plus support for custom agents over the same protocol. The chat panel renders markdown and reasoning, exposes mode and model pickers, handles file and terminal access with per-action permission management, and logs raw protocol traffic for debugging. With 27,000+ installs, it is one of the most-used ACP frontends, serving developers who switch among multiple agent CLIs.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/acp-client.md)
