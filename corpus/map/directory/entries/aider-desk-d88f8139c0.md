# aider-desk (`aider-desk`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: hotovo
- License: Apache-2.0
- Language: TypeScript/JavaScript (Electron + React 19 + Tailwind)
- Interface: install=binary
- Model providers: 30+ providers: OpenAI, Anthropic, Gemini, DeepSeek, Ollama, others
- Feature flags (directory-reported):
  - mcp_support: yes - both MCP client (connect to any MCP server) and MCP server (expose itself to Claude Desktop, Cursor) (yes)
  - plugin_support: yes - modular Extensions system (lifecycle hooks, custom tools, React UI injection) + IDE Connector Plugins for IntelliJ & VS Code (yes)
  - claude_code_plugin: no - Claude Desktop referenced as an MCP client target, not Claude Code (no)
  - subagents: yes - delegate to specialized subagents with custom Agent Profiles (system prompts, boundaries) (yes)
  - hooks: yes - 30+ lifecycle hooks (onTaskCreated, onPromptFinished, onToolCalled, onFileAdded, etc.) (yes)
  - plan_mode: unknown (unknown)

Repository map entry: [hotovo/aider-desk](../../repos/hotovo/aider-desk.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source agentic orchestration layer emphasizing Transparency (see every token, context file, proposed change), Control (tool approval gates, fork/duplicate tasks, edit chat history), and Flexibility (works alongside IDE/terminal/Git with no lock-in). Originally a GUI for the Aider CLI, now a full orchestration platform. Git worktrees give each task an isolated directory; built-in merge workflow. Fork tasks to explore alternatives; delete specific ...

(captured site page body (agents/aider-desk.md), not a verified repo-code finding)
AiderDesk began as an Electron front-end for the Aider CLI and evolved into a full coding platform: tasks with forkable context, git worktrees for isolated experiments, and a diff viewer that shows every proposed change before it lands. Tool approval gates require human authorization for risky operations, and token, cost, and usage dashboards make spending visible per task. An extension system exposes 30+ lifecycle events, custom tools, and React UI injection, with a gallery installable via npx @aiderdesk/extensions; IDE connectors exist for IntelliJ and VS Code. Teams that want agent automation with human checkpoints use it, with local-first storage (LanceDB) and 30+ model providers behind Apache-2.0 licensing.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/aider-desk.md)
