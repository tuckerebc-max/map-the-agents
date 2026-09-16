# aider-desk (`aider-desk`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
AiderDesk began as an Electron front-end for the Aider CLI and evolved into a full coding platform: tasks with forkable context, git worktrees for isolated experiments, and a diff viewer that shows ev
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
