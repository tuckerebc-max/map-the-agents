# vibesdk (`vibesdk`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: cloudflare
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=binary
- Model providers: Cloudflare AI Gateway (routes to multiple providers)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [cloudflare/vibesdk](../../repos/cloudflare/vibesdk.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source agentic platform by Cloudflare for building full-stack apps entirely on the Cloudflare stack (Durable Objects, Dynamic Workers, Artifacts, AI Gateway). No long-running dev server — previews load as Dynamic Workers on demand. Human-in-the-loop clarification, reversible Artifacts-backed history, signed branch-scoped preview URLs, bash disabled for safety.

(captured site page body (agents/vibesdk.md), not a verified repo-code finding)
VibeSDK packages the stack behind Cloudflare's own app-building experience as a deployable product: organizations that want a Lovable-style builder under their own brand, models, and data boundaries can run one entirely on Cloudflare's platform rather than assembling a code-generation API, a code-execution sandbox, and hosting separately. A user describes an application; the agent plans, edits files through explicit tools, and deploys each iteration as a Dynamic Worker serving a live preview with no long-running dev server. It reads the preview's console output to detect runtime errors, repairs them, and redeploys, and it asks structured clarifying questions when the request is underspecified. Every generated app gets isolated SQLite storage in a Durable Object facet and reversible version history in Cloudflare Artifacts, with model calls routed through AI Gateway for observability and caching. Teams building internal builders or AI product prototypes self-host it; production previews require Workers Paid and Workers for Platforms.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/vibesdk.md)
