# with-geun/alive-analysis

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e9f8d8209ff2 @ 6b4d0200ca737e10

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is a structured analysis workflow for AI coding agents, versioned 1.4.0 and MIT-licensed, with its MCP server distributed on npm as alive-analysis-mcp. Analyses follow a five-stage ALIVE loop (ASK, LOOK, INVESTIGATE, VOICE, EVOLVE); each stage produces a markdown file and has a checklist plus a quality gate before advancing.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is a structured analysis workflow for AI coding agents, versioned 1.4.0 and MIT-licensed, with its MCP server distributed on npm as alive-analysis-mcp. -- evidence: [README.md#L3-L3](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L3-L3), [README.md#L5-L9](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L5-L9)
- components (3 claim(s)):
  - [observation/documented] Three analysis modes exist: Full (five per-stage files, ~40-item checklists), Quick (single file, compressed checklist, promotable to Full via /analysis-promote), and Learn (guided scenarios with rubric-based scoring). -- evidence: [README.md#L104-L104](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L104-L104), [README.md#L85-L85](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L85-L85), [README.md#L97-L97](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L97-L97)
  - [observation/documented] The team dashboard is a single-file HTML5 force-directed node graph (D3.js v7) where node size encodes stage progress, color encodes analysis type, and edges show follow-up or shared-tag connections; data comes from a bash export script emitting JSON. -- evidence: [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L132-L132](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L132-L132), [README.md#L333-L340](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L333-L340), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L25-L46](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L25-L46), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L13-L13](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L13-L13), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L124-L124](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L124-L124)
- design-choices (3 claim(s)):
  - [observation/documented] Analyses follow a five-stage ALIVE loop (ASK, LOOK, INVESTIGATE, VOICE, EVOLVE); each stage produces a markdown file and has a checklist plus a quality gate before advancing. -- evidence: [README.md#L70-L76](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L70-L76), [README.md#L68-L68](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L68-L68), [README.md#L21-L21](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L21-L21)
  - [observation/documented] Experiment-type analyses adapt the loop to DESIGN, VALIDATE, ANALYZE, DECIDE, LEARN with enforcements including a pre-registration lock, automatic SRM detection, guardrail metrics, and multiple-comparison correction. -- evidence: [README.md#L204-L209](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L204-L209), [README.md#L200-L202](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L200-L202), [README.md#L198-L198](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L198-L198)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's Contributing section says issues and PRs are welcome and points contributors to CONTRIBUTING.md. -- evidence: [README.md#L557-L557](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L557-L557)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes slash commands including /analysis-init, /analysis-new, /analysis-next, /analysis-status, /analysis-archive, /analysis-list, /analysis-promote, /analysis-search, /analysis-retro, /analysis-dashboard, /analysis-dr, and /analysis-wiki. -- evidence: [README.md#L116-L124](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L116-L124), [README.md#L128-L134](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L128-L134)
  - [observation/documented] The MCP server (alive-analysis-mcp) exposes four tools — alive_list, alive_get, alive_search, alive_dashboard_export — configured for Claude Desktop via an --analyses-dir argument or for Claude Code via an ALIVE_ANALYSES_DIR environment variable. -- evidence: [README.md#L397-L402](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L397-L402), [README.md#L373-L383](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L373-L383), [README.md#L385-L393](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L385-L393), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L138-L141](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L138-L141)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A routing engine reads analysis context and recommends specialists from a pool of 31 agents, presenting the top 3 with explanations; four gate agents (scope-guard, data-quality-sentinel, ethics-guard, reproducibility-keeper) auto-run when their trigger conditions are met. -- evidence: [README.md#L165-L165](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L165-L165), [README.md#L169-L169](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L169-L169), [README.md#L190-L190](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L190-L190), [README.md#L171-L176](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L171-L176)
More evidence: [full detail](alive-analysis.detail.md)

Metadata and full claim list: [full detail](alive-analysis.detail.md)
Human notes ([notes](alive-analysis.notes.md), never overwritten by build)

[Back to map index](../../index.md)
