# JACoB (`jacob`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Renaissance-Innovation-Labs
- License: Apache-2.0
- Language: TypeScript/JavaScript (Next.js, tRPC, Tailwind, Orchid ORM)
- Interface: install=Hosted: sign up at jacb.ai/signup. Self-hosted: clone repo, create GitHub App, configure .env, docker compose up -d, npm install, npm run db create & npm run db migrate, npm run dev. Also requires Figma plugin install and npx jacob-setup create in target projects.
- Model providers: OpenAI, Ollama, PortKey
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [renaissance-innovation-labs/jacob-ai](../../repos/renaissance-innovation-labs/jacob-ai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI coding bot that automates development tasks, transforms Figma designs into deployable code, and integrates into GitHub workflows via webhooks (Issues, PRs, reviews). Learns your coding style to generate project-aligned code. Figma-to-code via dedicated plugin. Customizable via JSON config (jacob.config). Privacy-focused (no codebase storage, no data training). Outperformed 7 top design-to-code tools in their JACoB Arena benchmark. Forked from ...

(captured site page body (agents/jacob.md), not a verified repo-code finding)
JACoB positions itself beyond autocomplete: assign it a GitHub issue or a Figma design and it produces a complete pull request, having mapped the repository to match existing patterns. A Figma plugin hands it design context, and webhooks let it respond to issues, PRs, and reviews without leaving GitHub. Behavior is tuned through a jacob.config JSON file in the repo, and the project emphasized privacy — no codebase storage, no training on user code — alongside a JACoB Arena benchmark where it compared itself against seven design-to-code tools. The site went dark around December 2025 (jacb.ai no longer resolves), so the entry now stands on the archived Apache-2.0 codebase.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/jacob.md)
