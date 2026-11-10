# vibe-coding-template (`vibe-coding-template`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: humanstack
- License: MIT
- Language: Python
- Interface: install=git clone + ./first-time.sh + make dev
- Model providers: OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [humanstack/vibe-coding-template](../../repos/humanstack/vibe-coding-template.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Full-stack starter template optimized specifically for AI coding agents (Cursor & AGENTS.md) with context-aware Cursor Rules, code templates, and built-in best practices — designed to save tokens and boilerplate effort when vibe coding. FastAPI backend + Next.js frontend with Supabase integration.

(captured site page body (agents/vibe-coding-template.md), not a verified repo-code finding)
The template addresses the cost and inconsistency of pointing a coding agent at an empty repository: the agent invents project structure, rewrites boilerplate, and drifts from the intended stack with every session. Vibe-coding-template ships the structure instead — a FastAPI backend with Supabase integration (Google/LinkedIn/email auth, realtime, storage, migrations) and Qdrant vector search with a local fallback, a Next.js/Tailwind frontend with complete auth flows, and Docker Compose for development and production — paired with Cursor rules and an AGENTS.md that encode the architecture, conventions, and reusable code templates so Cursor or any AGENTS.md-aware agent generates code that already fits. Founders and small teams starting AI-built full-stack apps clone it as their base; it is MIT-licensed starter code with a small number of commits rather than an actively developed tool.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/vibe-coding-template.md)
