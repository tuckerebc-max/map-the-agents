# OpenHands (`openhands`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: OpenHands
- License: MIT
- Language: TypeScript, Python
- Interface: platforms=Autonomous, CLI, Web; install=npm install -g @openhands/agent-canvas, Docker image, or build from source
- Model providers: Any LLM (bring your own model)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [openhands/openhands](../../repos/openhands/openhands.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted developer control center for coding agents and automations. Runs OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. Supports webhook-triggered automations integrating with Slack, GitHub, Linear, Notion.

(captured site page body (agents/openhands.md), not a verified repo-code finding)
The OpenHands project repositioned from a single coding agent to Agent Canvas, a self-hosted control center for running whichever agents an organization already uses. It connects to Agent Server backends — a laptop, Docker host, VM, or cloud instance — and runs OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent against them from one web UI, so teams mix agent engines without changing tooling. Automations extend the pool beyond interactive sessions: scheduled Slack reports, GitHub issues that auto-decompose into agent tasks, and webhook-triggered runs, all self-hosted under MIT with the commercial offering being OpenHands Cloud. The stack pairs a TypeScript/React frontend with Python Agent Servers over the software-agent-sdk, installable via npm, Docker (ghcr.io/openhands/agent-canvas), or source, with the UI on localhost:8000. Teams building an internal agent platform on open infrastructure are the audience, and the project remains in beta with very high activity (8,115 commits, 85k stars).
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openhands.md)
