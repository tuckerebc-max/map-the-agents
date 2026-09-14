# VibeRaven (`viberaven`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: ohad6k
- License: MIT
- Language: TypeScript/JavaScript
- Interface: install=npx -y viberaven
- Model providers: AI agents: Claude Code, Codex, Gemini CLI. Service providers: Supabase, Vercel, GitHub, Stripe, Sentry, Resend, Clerk, Upstash, Auth.js, PostHog
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [ohad6k/viberaven](../../repos/ohad6k/viberaven.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source local cockpit for AI-built apps. Local-first philosophy: runs entirely on your machine — no login, no API key, no telemetry. 'Can I ship?' verdict: offline checks produce a gated score with blockers/warnings before deploy. Multi-agent cockpit drives Codex, Claude Code, and Gemini CLI from one local UI. Markdown on disk: all context lives in .viberaven/ as plain files readable ...

(captured site page body (agents/viberaven.md), not a verified repo-code finding)
VibeRaven exists for the gap between 'the agent says it's done' and 'this is safe to deploy': AI-built apps routinely miss production essentials like auth wiring, service-role key exposure, webhook configuration, and monitoring. Running entirely locally with no login or telemetry, it connects the coding agent to the app's real context — stack and provider detection, release timeline, architecture map — and produces a gated ship-readiness verdict from offline checks covering auth/RLS, secret exposure, webhooks, and deploy readiness; a CI mode exits nonzero on blockers. Its agent cockpit drives Codex, Claude Code, or Gemini CLI from one UI with ask/approve/full access modes, and every artifact lives as plain markdown under .viberaven/, versioned by git and readable by any agent. Indie developers and small teams shipping AI-built apps use it as a pre-deploy gate; note the core product code is developed in a private repository, with the public repo carrying the CLI and agent integration surface.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/viberaven.md)
