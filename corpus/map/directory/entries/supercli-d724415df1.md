# supercli (`supercli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: yashdev9274
- License: MIT
- Language: TypeScript
- Interface: install=npm install -g supercode (CLI); monorepo: clone + bun install
- Model providers: OpenRouter, Anthropic Claude, Google Gemini, Vercel Minimax AI Provider
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [yashdev9274/supercli](../../repos/yashdev9274/supercli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Full-stack AI-powered SWE agent platform: Next.js dashboard, MDX docs site, terminal web client, and installable CLI coding agent ('supercode' on npm), plus a parallel project fine-tuning its own coding-focused LLMs (Qwen3-8B, GLM-4-9B) via dual-track training (Tinker + Modal/Axolotl). Includes a 'skills' system shared across apps.

(captured site page body (agents/supercli.md), not a verified repo-code finding)
Supercode is developed as a Bun/Turborepo monorepo spanning the agent CLI published on npm as supercode, a Next.js dashboard for repo management and analytics, an MDX docs site, and a browser terminal client that mirrors the CLI. The agent runs on AI SDK v6 against Anthropic (default), OpenRouter, Gemini, and Minimax providers with file, execution, and search tools, and a shared @super/skills package provides reusable capabilities across apps. A parallel track, supercode-openmodel, fine-tunes Qwen3-8B through Tinker and GLM-4-9B through Modal/Axolotl to produce open coding-tuned weights for the platform. The project is MIT-licensed, Vercel-sponsored, and actively developed with no GitHub releases — distribution is the npm package. It fits developers who want an open, self-hostable agent plus the surrounding product surface.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/supercli.md)
