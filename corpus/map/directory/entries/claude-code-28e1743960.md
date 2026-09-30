# Claude Code (`claude-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: anthropics
- License: Closed Source
- Language: TypeScript, JavaScript (Node.js)
- Interface: platforms=CLI; install=curl -fsSL https://claude.ai/install.sh | bash (macOS/Linux); brew install --cask claude-code; irm https://claude.ai/install.ps1 | iex (Windows); winget install Anthropic.ClaudeCode; or npm install -g @anthropic-ai/claude-code (deprecated)
- Model providers: Anthropic (Claude models)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [anthropics/claude-code](../../repos/anthropics/claude-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Anthropic's official terminal-native agentic coding assistant that understands your codebase and operates through natural language; works across terminal, IDE (VS Code with @-mentions and plan review), and GitHub (via @claude mentions). Extensible plugin system for custom commands and agents; MCP server support for external data sources (Google Drive, Jira, Slack); hooks to run shell commands before/after actions (auto-format, lint); subagents ...

(captured site page body (agents/claude-code.md), not a verified repo-code finding)
Claude Code established the pattern most entries in this census copy: an agent that receives an instruction, plans, and executes a tool loop against the real filesystem with permission prompts, rather than a chat window. It is distributed as a closed-source product governed by Anthropic's Commercial Terms, with the GitHub repo hosting issues, the plugin marketplace, and examples rather than the product source. The same agent core is reachable from interactive terminals, IDEs with @-mentions and diff review, desktop and web clients, and GitHub through @claude automation, sharing configuration like CLAUDE.md memory, hooks, and MCP servers. Teams use it for refactoring, test writing, git workflows, and CI automation; headless mode supports scripting.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/claude-code.md)
