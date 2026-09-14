# with-geun/alive-analysis -- full detail

[Back to orientation](alive-analysis.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/with-geun/alive-analysis/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/6b4d0200ca737e10.json](../../../wiki/dossiers/with-geun/alive-analysis/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/6b4d0200ca737e10.json)

## specifications (1 claim(s))

- [observation/documented] The product is a structured analysis workflow for AI coding agents, versioned 1.4.0 and MIT-licensed, with its MCP server distributed on npm as alive-analysis-mcp. -- evidence: [README.md#L3-L3](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L3-L3), [README.md#L5-L9](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L5-L9) (`clm_8eca49103057ef62c2b73cadf2d63d29a3a6e5e650e4cfb8bb845a331e910a2b`)

## components (3 claim(s))

- [observation/documented] Three analysis modes exist: Full (five per-stage files, ~40-item checklists), Quick (single file, compressed checklist, promotable to Full via /analysis-promote), and Learn (guided scenarios with rubric-based scoring). -- evidence: [README.md#L104-L104](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L104-L104), [README.md#L85-L85](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L85-L85), [README.md#L97-L97](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L97-L97) (`clm_68a747fa5b84177e8c72b23a834b71d99e8911595d41008d634785c50377b4e3`)
- [observation/documented] The team dashboard is a single-file HTML5 force-directed node graph (D3.js v7) where node size encodes stage progress, color encodes analysis type, and edges show follow-up or shared-tag connections; data comes from a bash export script emitting JSON. -- evidence: [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L132-L132](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L132-L132), [README.md#L333-L340](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L333-L340), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L25-L46](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L25-L46), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L13-L13](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L13-L13), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L124-L124](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L124-L124) (`clm_5480a7cfb79f0be9eca4f737d770f3f02b949d0938504601eca8059b1034edeb`)
- [observation/documented] Platform support is documented for Claude Code and Cursor 2.4+, with Cursor using a batch interaction model that presents all required inputs at once. -- evidence: [README.md#L515-L524](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L515-L524), [README.md#L526-L526](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L526-L526) (`clm_ef3c31899f024447ae41c0d8abe2737080c85cd26bcdee574b7d18a6f50075f5`)

## design-choices (3 claim(s))

- [observation/documented] Analyses follow a five-stage ALIVE loop (ASK, LOOK, INVESTIGATE, VOICE, EVOLVE); each stage produces a markdown file and has a checklist plus a quality gate before advancing. -- evidence: [README.md#L70-L76](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L70-L76), [README.md#L68-L68](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L68-L68), [README.md#L21-L21](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L21-L21) (`clm_8c713e5de00cf36e36dd5dfd45cb26a4f8f315e617623a16d7f0b359c62d2ce5`)
- [observation/documented] Experiment-type analyses adapt the loop to DESIGN, VALIDATE, ANALYZE, DECIDE, LEARN with enforcements including a pre-registration lock, automatic SRM detection, guardrail metrics, and multiple-comparison correction. -- evidence: [README.md#L204-L209](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L204-L209), [README.md#L200-L202](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L200-L202), [README.md#L198-L198](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L198-L198) (`clm_0a0059637d9c2dec44469c8016c9b5119cd0c3a6ab73b65419c60346199c2b79`)
- [observation/documented] The dashboard was deliberately built as vanilla single-file HTML/CSS/JS with no build step, using a seeded PRNG (seed 42) for deterministic demo layouts and a three-level opacity scheme (1.0/0.22/0.05) for highlighting. -- evidence: [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L77-L82](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L77-L82), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L56-L56](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L56-L56), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L86-L89](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L86-L89), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L58-L62](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L58-L62) (`clm_06b571ebb4f377585c41fbff0f36d8ac2cc9790eb6549833364b5ba631d35f64`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's Contributing section says issues and PRs are welcome and points contributors to CONTRIBUTING.md. -- evidence: [README.md#L557-L557](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L557-L557) (`clm_e34bea2087838fa9d13c24274906cc14a3bd5e1ad2244be65a23e893b7116c5a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product exposes slash commands including /analysis-init, /analysis-new, /analysis-next, /analysis-status, /analysis-archive, /analysis-list, /analysis-promote, /analysis-search, /analysis-retro, /analysis-dashboard, /analysis-dr, and /analysis-wiki. -- evidence: [README.md#L116-L124](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L116-L124), [README.md#L128-L134](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L128-L134) (`clm_d549687835c904fd64a719ee9a77bac891c203766fbffd0bcf89da3dc365c8d4`)
- [observation/documented] The MCP server (alive-analysis-mcp) exposes four tools — alive_list, alive_get, alive_search, alive_dashboard_export — configured for Claude Desktop via an --analyses-dir argument or for Claude Code via an ALIVE_ANALYSES_DIR environment variable. -- evidence: [README.md#L397-L402](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L397-L402), [README.md#L373-L383](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L373-L383), [README.md#L385-L393](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L385-L393), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L138-L141](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L138-L141) (`clm_eb8b142d8da726cb48de1fafc9894d79902ea0afa680698d00408866a3f0640b`)
- [observation/documented] The analyses/ folder doubles as an Obsidian vault; wiki-links like [[F-2026-0305-001]] are picked up by Obsidian's graph view. -- evidence: [README.md#L464-L464](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L464-L464), [README.md#L462-L462](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L462-L462) (`clm_ca335db59b0fc1a02d2aa7e0aab28c0b93ebbacc0497fa0ec913c85923b58b23`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A routing engine reads analysis context and recommends specialists from a pool of 31 agents, presenting the top 3 with explanations; four gate agents (scope-guard, data-quality-sentinel, ethics-guard, reproducibility-keeper) auto-run when their trigger conditions are met. -- evidence: [README.md#L165-L165](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L165-L165), [README.md#L169-L169](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L169-L169), [README.md#L190-L190](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L190-L190), [README.md#L171-L176](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L171-L176) (`clm_d0c198c3e506aef2728817f79cdfde75acb6d1e4a78863dc95863926a278aae1`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents can be disabled per-project via a .analysis/agents.yml configuration file. -- evidence: [README.md#L192-L192](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L192-L192) (`clm_4eb19095b825e1dce149eb592b543a2c3cba59be0d3a5c9fb358d80f6e477c5b`)

## evaluation (1 claim(s))

- [observation/documented] Education mode scores learner work against rubrics with three progressive hint levels and a graduation path (70%+ on two Beginner scenarios unlocks Intermediate; 75%+ there is deemed production-ready). -- evidence: [README.md#L436-L436](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L436-L436), [README.md#L434-L434](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L434-L434) (`clm_0475b89f5bfe31899de4be72b7abcd8e06ae41d2b69a02a99397caa4c687dd30`)

## dependencies (1 claim(s))

- [observation/documented] The dashboard's only external JS dependency is D3.js v7 loaded from a CDN, and the export path requires no server or database (pure file-based JSON export). -- evidence: [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L126-L130](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L126-L130), [docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L58-L62](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md#L58-L62) (`clm_5424e1bab7ced145dec46f54f6182fc4592ff3bcf1992329e130e2ff66b23409`)

## limitations (1 claim(s))

- [observation/documented] The README states the product is not a BI tool, does not connect to databases or run queries automatically, and is tool-agnostic about the user's data stack (SQL, Python, R, notebooks, spreadsheets). -- evidence: [README.md#L532-L532](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L532-L532), [README.md#L534-L534](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L534-L534), [README.md#L536-L536](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L536-L536) (`clm_4f40ab06dac6a094c5ae2d85ccbce7383fd4bf12378cf8e15c31da7f1b715339`)

## relevance (1 claim(s))

- [observation/documented] The tool targets teams doing product/metric analysis with AI agents, aiming to preserve reasoning, data checks, and audit trails across sessions instead of losing them in chat history. -- evidence: [README.md#L17-L17](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L17-L17), [README.md#L15-L15](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L15-L15), [README.md#L21-L21](https://github.com/with-geun/alive-analysis/blob/e9f8d8209ff2fcdbd5389470cc2d8588889b7575/README.md#L21-L21) (`clm_bc85f846cbe4371da7a7bd63cc0021c9ad8192e27c22f0bda0ef2d785f126c18`)

