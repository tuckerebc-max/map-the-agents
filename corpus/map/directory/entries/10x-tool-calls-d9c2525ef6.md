# 10x-Tool-Calls (`10x-tool-calls`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: perrypixel
- License: unknown
- Language: Python
- Interface: install=copy files (Python script + rules)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [perrypixel/10x-tool-calls](../../repos/perrypixel/10x-tool-calls.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Exploits tool-call quotas (e.g., 25 tool calls per request) of agent-based IDEs (Cursor, Windsurf) by running interactive task loops, keeping a session alive within a single request's tool-call limit to yield 10x or more work for the same quota cost.

(captured site page body (agents/10x-tool-calls.md), not a verified repo-code finding)
Cursor and Windsurf meter usage by requests and tool calls rather than tokens, which means a finished or stalled agent session burns quota when the chat restarts. 10x-Tool-Calls ships a rules file plus a userinput.py script: after each completed task the script prompts for the next instruction inside the same request, keeping the session alive within one request's tool-call limit. It installs by copying the script into the project and pasting the rules into .cursorrules or the IDE's project rules set to always-on, and it requires Agent Mode. It only helps on tool-call-metered plans, not token-based ones, and its audience is quota-conscious Cursor and Windsurf users.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/10x-tool-calls.md)
