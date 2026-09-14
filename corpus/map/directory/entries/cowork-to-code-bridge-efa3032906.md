# cowork-to-code-bridge (`cowork-to-code-bridge`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: abhinaykrupa
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, Desktop, IDE, Web; install=curl -fsSL https://raw.githubusercontent.com/abhinaykrupa/cowork-to-code-bridge/main/install.sh | bash; brew install abhinaykrupa/tap/cowork-to-code-bridge; pip install cowork-to-code-bridge
- Model providers: Claude (haiku, sonnet, opus, fable)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [abhinaykrupa/cowork-to-code-bridge](../../repos/abhinaykrupa/cowork-to-code-bridge.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Bridges Claude Cowork (cloud sandbox) to Claude Code on your local machine via a shared file-based queue — no open ports, no network listener. Outbound-only, idempotent task execution (safe retries after dropped connections/crashes), token-gated, only runs user-whitelisted scripts, daemon auto-restarts and survives reboots. Designed as a universal MCP-based local code execution backend.

(captured site page body (agents/cowork-to-code-bridge.md), not a verified repo-code finding)
Claude Cowork runs in a cloud sandbox that cannot reach the local machine, so any task needing the real filesystem - builds, tests, commits - stops at the sandbox wall. This bridge connects the two environments without opening a network port: a Claude skill converts a Cowork request into a JSON task written to a shared bridge folder, a launchd/systemd daemon on the local machine polls that folder roughly once per second, and an approved script hands the task to Claude Code on the host. Execution is whitelisted to user-approved scripts, idempotency keys make retries safe (a repeated git push returns the cached result), and spend caps plus permission scopes bound each task. Progress and results stream back into the Cowork chat. Developers who work in Cowork but need local execution use it; it is a third-party fill for a gap Anthropic's --remote-control only partly covers.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cowork-to-code-bridge.md)
