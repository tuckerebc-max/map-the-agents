# memorax-code (`memorax-code`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: memorax-ai
- License: MIT
- Language: TypeScript
- Interface: install=npm install -g @memorax/memorax-code --foreground-scripts
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [memorax-ai/memorax-code](../../repos/memorax-ai/memorax-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Memory plugin giving Codex, Claude Code, DeepSeek Harness, and OpenCode a shared memory layer; four memory boundaries (Coding, Repo, Personal, Procedure); background memory writeback; preference continuity; procedure reuse; local Memory Viewer; semantic deduplication.

(captured site page body (agents/memorax-code.md), not a verified repo-code finding)
Coding agents restart every session with no memory of the fixes, conventions, and preferences learned in earlier runs, and each tool stores what it does remember in its own silo. MemoraX Code addresses this by persisting knowledge into typed boundaries: verified fixes and failed approaches under Coding, architecture maps with commit and PR evidence under Repo, style and format preferences under Personal, and reusable checklists under Procedure. Integration is agent-native rather than API-based, using each host's skill mechanism plus a CLI, and writeback runs in the background so the primary coding session is uninterrupted. A cloud backend carries memory across machines, with a free 90-day guest mode before an account is required, and a local Memory Viewer lets users inspect what the agent remembers. Developers running several different agent CLIs over the same codebase use it to stop re-explaining the same context to each one.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/memorax-code.md)
