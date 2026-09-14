# Grok CLI (`grok-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: superagent-ai
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/superagent-ai/grok-cli/main/install.sh | bash
- Model providers: xAI Grok API exclusively
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [superagent-ai/grok-cli](../../repos/superagent-ai/grok-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Deeply integrated with Grok API including X (Twitter) live search and web search, built-in computer sub-agent for host desktop automation (macOS), Telegram remote control with voice transcription, media generation (image/video), microVM sandboxing via Shuru, scheduling support, and OpenTUI React-based terminal UI.

(captured site page body (agents/grok-cli.md), not a verified repo-code finding)
grok-cli is a community terminal coding agent built by Superagent on xAI's Grok API, using TypeScript, Bun, and OpenTUI for its interface. Beyond standard file and shell tools, it integrates Grok-specific capabilities: live search over X posts and the web, media generation, and a computer sub-agent that drives macOS applications through accessibility snapshots and scripted actions. Sessions persist and can be driven remotely through a paired Telegram bot, including voice notes transcribed via Grok's speech-to-text API, and a daemon supports scheduled tasks. MCP servers, hooks, AGENTS.md instructions, and an optional microVM sandbox round out the toolset, and a /verify command runs apps in isolation for verification. It targets developers already using Grok models who want those unique data sources and remote-control paths inside their agent loop.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/grok-cli.md)
