# multiplayer (`multiplayer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: multiplayer-app
- License: MIT
- Language: JavaScript, TypeScript (Node.js, pnpm/Turborepo monorepo)
- Interface: install=Docker Compose (recommended): cp .env.example docker/.env, edit credentials, docker compose -f docker/docker-compose.prod.yml up -d. Requires Node v22+, pnpm v10+, Docker. Local dev: pnpm install; cp .env.example .env; docker compose -f docker/docker-compose.dev.yml up -d; pnpm start:pm2
- Model providers: Claude Code (GA), Codex (private beta), Copilot (private beta)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [multiplayer-app/multiplayer](../../repos/multiplayer-app/multiplayer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source debugging agent that runs locally alongside coding agents and bridges them directly to production runtime data; captures deep, unsampled full-stack session data (including request/response bodies and headers that APMs miss); intelligently deduplicates identical errors to produce one merge-ready fix instead of duplicate PRs; provides session recorder SDKs for JavaScript, React Native, Go, .NET, Python, Ruby, and Java.

(captured site page body (agents/multiplayer.md), not a verified repo-code finding)
Multiplayer attacks the weakest input to AI debugging: coding agents fix production bugs poorly because they see stack traces, not the unsampled full-stack session data — request and response bodies, headers, cross-service correlation — that APM tools sample away. The platform runs locally alongside a coding agent, captures complete session data through recorder SDKs spanning JavaScript, React Native, Go, .NET, Python, Ruby, and Java, and auto-correlates the traces across components. Its triage layer filters for high-priority bugs and deduplicates identical errors, so a recurring exception produces one merge-ready pull request rather than a flood of duplicates; the loop runs from error capture through agent prompting to PR creation and notification. The self-hostable stack (MongoDB, Kafka, ClickHouse, Redis, MinIO) deploys via Docker Compose, and a companion CLI provides a terminal surface for reviewing sessions and turning fixes into branches. Teams running Claude Code against production incidents are the target users; the project is young, with a small commit history and adoption still forming.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/multiplayer.md)
