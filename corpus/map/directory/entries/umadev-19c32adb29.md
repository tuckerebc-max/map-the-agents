# umadev (`umadev`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: umacloud
- License: MIT
- Language: Rust
- Interface: install=npm install -g umadev; or native installer (curl -fsSL https://umadev.goder.ai/install.sh | bash / irm https://umadev.goder.ai/install.ps1 | iex); or build from source with Cargo
- Model providers: Claude Code, Codex, OpenCode, Grok Build, Kimi Code (drives 5 base CLIs which bring their own models)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [umacloud/umadev](../../repos/umacloud/umadev.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Orchestrates a 9-seat dev team (8 specialist roles + coordinator) over borrowed AI brains — driving one of 5 existing AI coding CLIs rather than owning any model endpoint. Deterministic acceptance floor (build/test/contract verification runs regardless of model self-assessment). 113 governance checks with fail-open design. Delivery evidence with proof packs, scorecards, compliance mappings (SOC 2 / ISO 27001 / EU ...

(captured site page body (agents/umadev.md), not a verified repo-code finding)
UmaDev exists because a raw coding CLI has no delivery discipline: it declares completion without evidence, and teams adopting it for real work need governance, plans, and proof. The tool drives one of five installed coding CLIs as its brain — the CLI keeps its own login and model config — while umadev supplies the process: clarify, research, PRD/architecture/UI-UX documents, staged gates, and delivery artifacts including a proof pack and compliance mapping. Roles coordinate through shared blackboard artifact files rather than chat; reviewer roles run as fresh read-only child sessions whose verdicts feed a coordinator; and quality gates run builds, tests, and OpenAPI contract checks regardless of what the model claims. Trust tiers (plan/guarded/auto) set autonomy per task, irreversible actions always confirm, and hooks wire governance into Claude Code and git pre-commit; an MCP server exposes the governor to other clients. Teams needing auditable, compliance-mapped AI development use it; it is a single MIT-licensed Rust binary distributed via npm or native installer.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/umadev.md)
