# sandboxd (`sandboxd`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: tastyeffectco
- License: MIT
- Language: Go
- Interface: install=docker
- Model providers: OpenCode, Claude Code
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [tastyeffectco/sandboxd](../../repos/tastyeffectco/sandboxd.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted AI app builder with deliberately minimal architecture (one Go binary + Docker + Traefik + SQLite); sleep/wake sandboxes so idle apps cost nothing; credential isolation via proxy injection (API keys never enter sandboxes); 80+ curated one-click open-source apps.

(captured site page body (agents/sandboxd.md), not a verified repo-code finding)
sandboxd is the self-hosted answer to Lovable-style app builders: an operator runs one binary on a VPS, and users prompt a coding agent that works inside an isolated container per app, exposed at a preview URL. Each app sleeps when idle and wakes on request, keeping idle cost at zero, while tasks are checkpointed so any agent mistake can be reverted. Beyond generated apps it curates more than eighty one-click apps (n8n, Ghost, Grafana, Gitea, Jupyter, Keycloak) and runtime presets for React, Next.js, Express, FastAPI, and Workers. Everything is a versioned /v1 REST call, so the browser console is just one client. It is MIT-licensed and beta (0.x) with container-level isolation and API auth off by default, aimed at developers who want an app-builder platform under their own domain rather than a SaaS.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/sandboxd.md)
