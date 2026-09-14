# project-os-for-codex (`project-os-for-codex`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: herry2059
- License: Apache-2.0
- Language: TypeScript, React, Node.js
- Interface: install=docker compose up --build (recommended) or manual pnpm install + pnpm dev; requires Node.js 22+, pnpm 9+, Git
- Model providers: AI provider adapter (replaceable boundary); OpenAI Codex CLI / ChatGPT
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [herry2059/project-os-for-codex](../../repos/herry2059/project-os-for-codex.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Git-as-durable-project-record design; fail-closed MCP preflight with strict two-tool surface; short-lived (24h/7d) project-bound credentials instead of password sharing; handoff packages readable by humans and AI; built from real delivery experience (14,570 Codex tasks, 8.8B tokens); not affiliated with OpenAI

(captured site page body (agents/project-os-for-codex.md), not a verified repo-code finding)
Project OS for Codex exists because handing a coding agent a long-running project usually means sharing passwords, losing context between sessions, and having no auditable record of what the agent actually did. It provides a web dashboard plus a strict two-tool MCP server: one tool returns the current kickoff card, acceptance criteria, and handoff package, and the other appends one validated, idempotent progress event with an agent-reported verification note and a matching commit in a separate record repository. A fail-closed preflight verifies the credential, project binding, and exact tool surface before Codex starts, and high-risk operations like key management or deployment are deliberately kept outside the MCP surface for humans. Handoffs use short-lived, scope-limited credentials — 24-hour or 7-day expiry — instead of shared passwords, with everything hashed and independently revocable. Solo developers running Codex on multi-session projects use it to keep work auditable and handoff-safe.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/project-os-for-codex.md)
