# singulary (`singulary`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: sammwyy
- License: MIT
- Language: TypeScript
- Interface: install=git clone + cp .env.example .env + docker compose up --build; or pnpm install + pnpm dev for local dev (Node \>=22, pnpm 9)
- Model providers: OpenAI, Anthropic, OpenRouter, Groq, Google, xAI, DeepSeek, OpenAI-compatible (Ollama, LM Studio)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [sammwyy/singulary](../../repos/sammwyy/singulary.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source self-hosted FOSS alternative to v0/Lovable/Bolt/Replit Agent; agent reads/writes/patches files, runs shell commands, and provisions services inside isolated Docker workspaces with built-in Monaco editor, interactive terminals, live preview, multi-user support, and encrypted secrets at rest.

(captured site page body (agents/singulary.md), not a verified repo-code finding)
Singulary replicates the v0/Lovable/Bolt workflow — prompt, get a running web app, iterate — but on the operator's own hardware with their own API keys and no SaaS backend or telemetry. Each project runs in an isolated Docker container and network where the agent edits files, installs dependencies, restarts dev servers, and asks approval before dangerous calls, with a Monaco editor, interactive terminals, and live preview with automatic port detection in the browser. The whole stack is a single Node process with SQLite, deployable with one docker compose up, and secrets are AES-GCM encrypted at rest. Being very early (a handful of commits), it lacks snapshots and quota enforcement at call time, both on the roadmap. It targets teams and self-hosters who want an app-builder platform they control, and the Docker socket mount warrants rootless-Docker hardening before exposure.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/singulary.md)
