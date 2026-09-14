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
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibesdk.md)
