# pagecast (`pagecast`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Amal-David
- License: MIT
- Language: JavaScript (Node.js)
- Interface: platforms=CLI, Web; install=npx pagecast (no global install); or docker ghcr.io/amal-david/pagecast:latest; or from source npm start
- Model providers: none (tool is model-agnostic; invoked by coding agents via an MCP server mode and a publish-report skill)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [amal-david/pagecast](../../repos/amal-david/pagecast.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first publishing tool that previews HTML reports, Markdown docs, and static mini apps, then publishes them to shareable Cloudflare Pages URLs from the terminal or coding agents. Context-aware publishing (upserts update same URL in same agent session), edge-level password protection, immutable deploy history, activity analytics, and integrations via MCP, Claude Code plugin, and Codex skill.

(captured site page body (agents/pagecast.md), not a verified repo-code finding)
Coding agents generate HTML reports, dashboards, and static demos that are awkward to share: screenshots lose fidelity, and full hosting setups are disproportionate for a disposable artifact. Pagecast runs locally (npx pagecast, or Docker), previews the artifact in an admin UI, and publishes it to a shareable Cloudflare Pages URL after a one-time scoped OAuth connection or API-token setup. Edge Functions enforce optional password protection, links expire after a default 30 days, and deploy history supports pruning and revocation; self-hosted analytics via a Worker plus D1 are optional. Coding agents integrate directly through an MCP server mode and a publish-report skill listed on Skills.sh, so a Claude Code or Codex session can publish mid-task. Static assets only — server-rendered apps need a backend and are out of scope. Developers and agents that need fast, access-controlled, disposable sharing of generated pages are the audience, under an MIT license.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pagecast.md)
