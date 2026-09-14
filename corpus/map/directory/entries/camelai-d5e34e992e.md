# camelAI (`camelai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: qaml-ai
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=git clone; bun install --frozen-lockfile; cp .dev.vars.example .dev.vars; bun run dev (requires Node.js 22+, Bun, Cloudflare account, Docker)
- Model providers: Anthropic, OpenAI, OpenRouter, AWS Bedrock, custom endpoints
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [qaml-ai/camelai](../../repos/qaml-ai/camelai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Each chat thread runs its own coding agent in a Cloudflare Durable Object (not a VM) for persistent state without container overhead. Custom agent harness (not Claude Code or Codex) that writes JavaScript instead of bash, runs it in fresh V8 isolates, and keeps credentials outside the execution sandbox. Publishes user apps directly to live URLs via Workers for Platforms.

(captured site page body (agents/camelai.md), not a verified repo-code finding)
camelAI is an open-source, full-stack AI app-building platform built entirely on Cloudflare's serverless primitives. Each conversation thread instantiates a Durable Object holding the agent loop and its state, while project files live across Durable Object SQLite and R2 storage with git history via Cloudflare Artifacts — no VMs or containers for the interactive loop. The custom agent harness, built on pi's agent libraries rather than Claude Code or Codex, generates JavaScript instead of shell commands; that code runs in fresh V8 isolates with credentials kept outside the execution sandbox, and applications publish to live URLs through Workers for Platforms. The platform also ships with organizational features (SSO, billing, usage metering), Slack and Discord bridges, and an eval harness, and it self-hosts via Docker Compose for teams that want the whole stack on their own infrastructure. It is MIT-licensed and under active development, targeting teams that want a self-hostable alternative to proprietary app builders.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/camelai.md)
