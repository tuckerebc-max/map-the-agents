# sourcebot (`sourcebot`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: sourcebot-dev
- License: Fair-source (see LICENSE.md)
- Language: TypeScript
- Interface: install=docker
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [sourcebot-dev/sourcebot](../../repos/sourcebot-dev/sourcebot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted code intelligence platform that helps humans and agents understand codebases. Combines AI-powered Q&A with inline citations, code search (regex/filters/boolean across all repos/branches on any code host), IDE-level cross-repo goto definition and find references, and a built-in file explorer. Enables both humans and AI agents to navigate large multi-repo codebases. Public demo at app.sourcebot.dev.

(captured site page body (agents/sourcebot.md), not a verified repo-code finding)
Sourcebot addresses the cost of understanding large multi-repo codebases, for engineers and increasingly for the agents working alongside them. A Docker Compose deployment indexes all repos and branches on any code host, then serves fast regex and boolean search, IDE-grade cross-repo go-to-definition and find-references, a file explorer, and a natural-language Q&A mode whose answers cite specific code with navigable snippets. Configuration is a JSON file describing code hosts, LLM providers, and auth; the enterprise directory carries additional paid capabilities under a Fair Source license. A public demo runs at app.sourcebot.dev, and the project releases frequently (v5.1.x as of August 2026). Teams with sprawling monorepo estates use it as shared infrastructure for humans and AI tools alike.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sourcebot.md)
