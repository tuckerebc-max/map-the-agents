# Claude Autopilot (`claude-autopilot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: benbasha
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=Install from Open VSX
- Model providers: Anthropic (via Claude Code CLI)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [benbasha/claude-autopilot](../../repos/benbasha/claude-autopilot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Automated Claude Code task management with queue processing and auto-resume

(captured site page body (agents/claude-autopilot.md), not a verified repo-code finding)
Claude Autopilot addresses the operational problem of running long batches of Claude Code tasks unattended: queued work stalls when usage limits reset, the machine sleeps, or the CLI process dies. The extension launches each queued prompt as a sequential Claude Code run, monitors process health, retries failures, detects rate-limit messages, and resumes automatically when the limit window resets, while keeping the machine awake. A local web server with password and QR-code login provides mobile monitoring. Developers use it for overnight batches such as refactoring, migrations, and documentation generation; it requires an existing Claude Code installation and subscription.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-autopilot.md)
