# AI Free Chat & Agent (`ai-free-chat-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Staks-sor
- License: Custom (personal-use-only, non-standard)
- Language: JavaScript
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [staks-sor/ai-free](../../repos/staks-sor/ai-free.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): DeepSeek, Qwen, ChatGPT chats and coding agents in PyCharm

(captured site page body (agents/ai-free-chat-agent.md), not a verified repo-code finding)
The project exists because commercial API access is the main cost barrier for AI-assisted coding; it converts free web chat sessions into a programmatic backend by automating a Chromium session per provider. On top of that transport it runs a /code agent bound to a project folder: it reloads hierarchical AGENTS.md instructions before each task, executes commands through risk-tiered whitelists (rm -rf blocked, curl and bash denied by default), and keeps memory in SQLite FTS5 plus a Markdown vault linking tasks to files and fixes. The JetBrains plugin is the IDE-facing entry point, while the local API also lets tools like Kilo Code or Continue consume the same sessions. It is solo-maintained, releases frequently (v0.4.25), and is free under a personal-use-only custom license.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/ai-free-chat-agent.md)
