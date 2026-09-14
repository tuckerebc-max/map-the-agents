# project-codeguard (`project-codeguard`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: cosai-oasis
- License: CC BY 4.0
- Language: Python, Markdown
- Interface: platforms=IDE; install=Download skills/rules from GitHub Releases; copy AI agent/IDE-specific skills and rules into your repository; start coding
- Model providers: Model-agnostic: Cursor, GitHub Copilot, Codex, Windsurf, Claude Code
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [cosai-oasis/project-codeguard](../../repos/cosai-oasis/project-codeguard.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Vendor-neutral, model-agnostic security coding agent skills framework from the Coalition for Secure AI (CoSAI, an OASIS Open Project). Ships unified security rules in markdown covering cryptography, input validation, authentication, authorization, supply chain, cloud security, and post-quantum cryptography; includes translators for popular coding agents, an MCP server for centralized organizational deployment, and validators to test compliance.

(captured site page body (agents/project-codeguard.md), not a verified repo-code finding)
Project CodeGuard exists because security guidance for AI coding agents was fragmented across vendor-specific formats with no neutral governance. The Coalition for Secure AI, an OASIS-hosted industry consortium, publishes a single set of security rules in markdown spanning cryptography, injection, authentication and authorization, supply chain, cloud infrastructure, and data protection. A translation pipeline converts those unified sources into skills and rules for Cursor, Copilot, Codex, Windsurf, and Claude Code, so an organization writes its security posture once and every agent consumes the same content. Distribution works two ways: teams can copy released rules into their repositories as static context, or run the included MCP server so every developer's assistant pulls centrally managed rules over HTTP. Validators test rule compliance, and releases package everything as downloadable archives. Enterprises and open-source projects adopt it to get consistent, auditable security behavior from whatever agents their developers use.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/project-codeguard.md)
