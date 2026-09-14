# edge-pi (`edge-pi`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: marcusschiesser
- License: MIT
- Language: TypeScript
- Interface: install=npm install -g edge-pi-cli
- Model providers: Multi-provider via Vercel AI SDK
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [marcusschiesser/edge-pi](../../repos/marcusschiesser/edge-pi.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight Vercel AI SDK-based coding agent library providing core primitives for building AI-powered coding assistants with tool support, session management, and context compaction; includes epi CLI as a full-featured coding agent with multi-provider support and skills

(captured site page body (agents/edge-pi.md), not a verified repo-code finding)
Building a coding assistant on the Claude Agent SDK locks the loop to Anthropic's runtime, and the Vercel AI SDK alone leaves you to write session handling, tool plumbing, and context compaction yourself. edge-pi supplies exactly those missing primitives on top of the Vercel AI SDK: tool execution, session management, and compaction, usable with any LLM provider. Its epi CLI is a compact, working agent — multi-provider, skills-aware — included to show the library end to end; the code descends from Mario Zechner's pi coding agent. It is aimed at developers who want an embeddable, provider-neutral agent kernel rather than a finished product.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/edge-pi.md)
