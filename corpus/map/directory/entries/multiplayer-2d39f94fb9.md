# multiplayer (`multiplayer`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
Multiplayer attacks the weakest input to AI debugging: coding agents fix production bugs poorly because they see stack traces, not the unsampled full-stack session data — request and response bodies,
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
