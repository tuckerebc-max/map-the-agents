---
access: public
aliases: []
claim_ids:
- clm_06b571ebb4f377585c41fbff0f36d8ac2cc9790eb6549833364b5ba631d35f64
- clm_5424e1bab7ced145dec46f54f6182fc4592ff3bcf1992329e130e2ff66b23409
- clm_5480a7cfb79f0be9eca4f737d770f3f02b949d0938504601eca8059b1034edeb
- clm_eb8b142d8da726cb48de1fafc9894d79902ea0afa680698d00408866a3f0640b
maturity: draft
page_id: pg_33ef54c2fc265d158b0c9e54c3521e56
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6c5e3f350b7b5002b9df1a9587aa53cb
title: with-geun/alive-analysis/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md
  @ e9f8d8209ff2
updated_at: '2026-09-14T04:32:58Z'
---

# with-geun/alive-analysis/docs/archive/2026-03/alive-dashboard/alive-dashboard.report.md @ e9f8d8209ff2

<!-- rcw:begin owner=source:src_6c5e3f350b7b5002b9df1a9587aa53cb block=evidence -->
- The dashboard was deliberately built as vanilla single-file HTML/CSS/JS with no build step, using a seeded PRNG (seed 42) for deterministic demo layouts and a three-level opacity scheme (1.0/0.22/0.05) for highlighting. [@claim:clm_06b571ebb4f377585c41fbff0f36d8ac2cc9790eb6549833364b5ba631d35f64]
- The dashboard's only external JS dependency is D3.js v7 loaded from a CDN, and the export path requires no server or database (pure file-based JSON export). [@claim:clm_5424e1bab7ced145dec46f54f6182fc4592ff3bcf1992329e130e2ff66b23409]
- The team dashboard is a single-file HTML5 force-directed node graph (D3.js v7) where node size encodes stage progress, color encodes analysis type, and edges show follow-up or shared-tag connections; data comes from a bash export script emitting JSON. [@claim:clm_5480a7cfb79f0be9eca4f737d770f3f02b949d0938504601eca8059b1034edeb]
- The MCP server (alive-analysis-mcp) exposes four tools — alive_list, alive_get, alive_search, alive_dashboard_export — configured for Claude Desktop via an --analyses-dir argument or for Claude Code via an ALIVE_ANALYSES_DIR environment variable. [@claim:clm_eb8b142d8da726cb48de1fafc9894d79902ea0afa680698d00408866a3f0640b]
<!-- rcw:end owner=source:src_6c5e3f350b7b5002b9df1a9587aa53cb block=evidence -->

## Researcher notes

