# Paseo (`paseo`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: getpaseo
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Claude Code, Codex, GitHub Copilot, OpenCode, Pi
- Feature flags (directory-reported):
  - mcp_support: yes (packages/server includes an MCP server; transport not specified) (yes)
  - plugin_support: partial (plugin-examples/ directory; skills system for extensibility) (reported)
  - claude_code_plugin: yes (.claude/skills/ directory; Claude Code is a supported agent) (yes)
  - subagents: yes (/paseo-advisor and /paseo-committee skills spin up additional agents) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [getpaseo/paseo](../../repos/getpaseo/paseo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted, privacy-first orchestration platform providing a single interface across multiple AI coding agents (Claude Code, Codex, Copilot, OpenCode, Pi), enabling parallel agent execution on your own machine with cross-device control via desktop, mobile, web, and CLI.

(captured site page body (agents/paseo.md), not a verified repo-code finding)
Paseo exists because coding agents strand work in a single terminal on a single machine: sessions die when the laptop closes and there is no way to supervise several agents at once. Its self-hosted daemon runs Claude Code, Codex, GitHub Copilot, OpenCode, and Pi locally with the user's own credentials, exposing them through desktop, web, mobile, and CLI clients, with agents running in parallel and handoff skills that pass work between them or convene advisor and committee agents for review. The design is deliberately privacy-first: no telemetry, no forced accounts, and an E2E-encrypted relay only for pairing remote devices. The server package includes an MCP server and a TypeScript SDK for integrations, and a skills system extends orchestration. With 15k+ GitHub stars and multilingual documentation, it draws individual developers and small teams who want local control over multi-agent workflows.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/paseo.md)
