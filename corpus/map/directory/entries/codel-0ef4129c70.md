# Codel (`codel`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: semanser
- License: AGPL-3.0
- Language: Go
- Interface: platforms=Autonomous, CLI, Web; install=Docker (pre-built image from GitHub Container Registry)
- Model providers: OpenAI,Ollama
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [semanser/codel](../../repos/semanser/codel.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fully autonomous AI agent running in a sandboxed Docker environment with a built-in browser, text editor, automatic Docker-image picker, and PostgreSQL-backed command history.

(captured site page body (agents/codel.md), not a verified repo-code finding)
Codel is a self-hosted autonomous agent that carries a task from description to completion using a terminal, a browser, and a text editor, all inside sandboxed Docker containers. The agent decides its next step autonomously, consulting the web through a built-in browser when it needs information and editing files through an editor viewable in the web UI; command and output history persists in PostgreSQL for later review. It selects an appropriate Docker image for each task automatically and works with OpenAI models or self-hosted Ollama endpoints configured through environment variables. The project drew attention as an early open-source answer to Cognition's Devin, accumulating roughly 2.5k stars, but development stalled in 2024 and the repository has been dormant since.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codel.md)
