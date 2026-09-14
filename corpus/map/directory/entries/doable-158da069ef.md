# Doable (`doable`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: doable-me
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=git clone + ./deployment/docker/setup.sh (Docker); local dev via pnpm install; one-click deploy to DigitalOcean/Render/Railway/Heroku/Codespaces; doable Rust CLI for provisioning
- Model providers: Anthropic, OpenAI, Google Gemini, Groq, Mistral, DeepSeek, xAI, Ollama, LM Studio, vLLM, OpenRouter, Moonshot, Alibaba, Baidu, any OpenAI-compatible endpoint
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [doable-me/doable](../../repos/doable-me/doable.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fully self-hostable and air-gappable multi-tenant AI app builder with row-level security isolation, sandboxed code execution (per-project Linux UIDs, seccomp, egress firewall), audit logs, MFA, RBAC, real-time collaboration, BYOK for 53+ AI providers, and 630+ integrations — all MIT-licensed and owned by you.

(captured site page body (agents/doable.md), not a verified repo-code finding)
Doable rebuilds the AI app-builder stack — the Lovable/Bolt category — for operators who cannot send code or data to a hosted service. A describe-and-preview loop generates frontend, in-process backend, and database per tenant, with each project sandboxed under its own Linux UID, seccomp profile, and egress firewall, and audit logs covering the run. Administration is product surface, not ops: a five-step setup wizard covers AI provider (BYOK from 53+ providers), Cloudflare DNS, and plan quotas, and row-level security isolates tenants on shared hardware. It is aimed at teams and regulated organizations that want a self-hostable builder on their own VPS or PaaS.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/doable.md)
