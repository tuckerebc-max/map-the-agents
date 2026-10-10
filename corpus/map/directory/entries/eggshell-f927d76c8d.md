# EggShell (`eggshell`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Best Practice
- License: unknown
- Language: unknown
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Embeds terminal sessions dedicated to AI CLI coding agents

(captured site page body (agents/eggshell.md), not a verified repo-code finding)
EggShell exists because JetBrains users wanted to talk to CLI coding agents without leaving the IDE or juggling a separate terminal app. It opens a native IDE terminal bound to a chosen agent CLI, tracks chat sessions and their owning agent in .idea/eggshell.xml so tabs persist across restarts, and wires IDE state into the conversation: files dragged from the project tree become agent-specific @path references, editor selections become line-range code citations, and clipboard images are saved and passed as paths. Agent launch commands are editable templates in Settings with dry-run test buttons to validate argv before spawning, and API keys live in the IDE Password Safe while the plugin itself collects no data. The split-plugin structure lets it run identically in local IDEs and JetBrains Gateway remote environments.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/eggshell.md)
