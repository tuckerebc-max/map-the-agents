# VSCode Agent (`vscode-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Microsoft
- License: Proprietary (VS Code is MIT-licensed but Copilot/agent features require subscription)
- Language: TypeScript
- Interface: platforms=IDE; install=Built into VS Code / VS Code Insiders; requires GitHub Copilot subscription
- Model providers: GitHub Copilot models (Claude, GPT-4, Gemini, and others)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Built-in agent-first experience in VS Code with dedicated Agents window, multiple chat surfaces (Agents window, Chat view, inline chat, Quick Chat). Full MCP support, plugin system, subagents, hooks, and plan mode. Agents can autonomously analyze code, make changes, run terminal commands, and use tools. Backed by GitHub Copilot's multi-model provider system.

(captured site page body (agents/vscode-agent.md), not a verified repo-code finding)
VS Code evolved from an editor with AI completions into an agent-first harness: a dedicated Agents window hosts autonomous sessions where agents analyze code, edit files, run terminal commands, and use tools, while chat also remains available inline and through Quick Chat. The harness supports MCP servers for external tools, a plugin system for packaging agents, subagents, lifecycle hooks, and plan mode for reviewing multi-step work before execution. Because agents run inside the editor with workspace context, they can analyze code, apply edits, and run terminal commands without leaving the surface. It targets VS Code's large installed base, from individual developers to enterprise teams already using GitHub Copilot or BYO MCP endpoints.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/vscode-agent.md)
