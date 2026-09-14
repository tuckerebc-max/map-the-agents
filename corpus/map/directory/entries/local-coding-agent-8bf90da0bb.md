# local-coding-agent (`local-coding-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: LongNgn204
- License: AGPL-3.0-or-later
- Language: JavaScript
- Interface: platforms=Desktop, Web; install=git clone then scripts/lca install (macOS/Linux) or scripts/lca.cmd install (Windows); optional tray app .exe from Releases
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [longngn204/local-coding-agent](../../repos/longngn204/local-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first MCP server with a live dashboard showing health metrics. Compact & Resume feature for context handoff across ChatGPT sessions. Named multi-root permission profiles with per-path rights. Optional Chrome Companion and Windows tray app with DPAPI-encrypted key storage. Works with any MCP client.

(captured site page body (agents/local-coding-agent.md), not a verified repo-code finding)
The project addresses the trust gap that opens when cloud agents are allowed to operate on a real workstation. Every capability - file reads and patches, command execution, git inspection, bounded browser preview - is exposed as an MCP tool bounded by permission profiles, with a balanced policy that routes risky actions through a local approval request. A dashboard at localhost shows health scores, latency, tool calls, and git diffs in real time, and compact/resume prompts let ChatGPT sessions hand context across conversation boundaries. An Electron tray app supervises the server with secrets held in Windows DPAPI or macOS Keychain. Developers who want Claude Code, Codex, Cursor, or ChatGPT to work on their machine under explicit, revocable permissions are the target users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/local-coding-agent.md)
