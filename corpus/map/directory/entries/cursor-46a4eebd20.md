# Cursor (`cursor`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: cursor
- License: Closed Source
- Language: TypeScript (VS Code fork)
- Interface: platforms=Desktop, IDE; install=Download from https://cursor.com
- Model providers: OpenAI, Anthropic, Google Gemini, SpaceXAI (Grok), Cursor's own models, bring-your-own-model
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [cursor/cursor](../../repos/cursor/cursor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-powered IDE with multi-agent collaboration, fleets of parallel agents working for hours or days, built-in marketplace with plugins, Plan Mission Control, and support for multiple model providers including bring-your-own-model. Closed source; GitHub repo contains only issue templates.

(captured site page body (agents/cursor.md), not a verified repo-code finding)
Cursor began as a VS Code fork with AI-assisted editing and has grown into a full agentic development platform used by individual developers and large engineering organizations. Its agents operate in several modes — inline edits, an interactive agent chat, and background cloud agents — and can run in parallel for hours or days, with Plan Mission Control giving oversight of long-running fleets. The platform supports multiple model providers configured per user, an in-IDE plugin marketplace, MCP integrations, and event-triggered Automations that execute in cloud sandboxes. The IDE itself is proprietary and distributed from cursor.com, with the public GitHub repository serving only as an issue tracker; revenue comes from subscription tiers for individuals and enterprises.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cursor.md)
