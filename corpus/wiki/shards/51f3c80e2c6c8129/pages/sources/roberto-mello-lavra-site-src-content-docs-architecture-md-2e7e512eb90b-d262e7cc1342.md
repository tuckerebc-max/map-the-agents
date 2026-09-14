---
access: public
aliases: []
claim_ids:
- clm_3a585a3901557192b9c72fece8243a642d4be055681b4bf0dcd8021c2b202cc0
- clm_51e4c4920a85e9d9d7259859ffb1bb9376dfe12e617d5468497e0504234c7a24
- clm_53fb2d98d15ce3f271d638fdbc0247d92e588684a9c6dc2d36530b39cfe3a834
- clm_5c1e51242568c4b9eb38a9fafccb8c353e3638f05a4d765141aef5b768ab1a54
- clm_95fba6fe4638d0c11be02732049650374d8487396ca5d876c807f912a5aaf4b7
- clm_e98223c3058e6b9c6255214e875511577ad93b2df1fc9a84850e38ebca0a7d24
maturity: draft
page_id: pg_b978f88baba454bdb441d262e7cc1342
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cd9b9ee0e3a0502880efbc7045a89629
title: roberto-mello/lavra/site/src/content/docs/ARCHITECTURE.md @ 2e7e512eb90b
updated_at: '2026-09-14T04:18:53Z'
---

# roberto-mello/lavra/site/src/content/docs/ARCHITECTURE.md @ 2e7e512eb90b

<!-- rcw:begin owner=source:src_cd9b9ee0e3a0502880efbc7045a89629 block=evidence -->
- The architecture doc reports FTS5 search with BM25 ranking improved precision by 18%, recall by 17%, and MRR by 24% over grep-based search across 25 benchmark queries. [@claim:clm_3a585a3901557192b9c72fece8243a642d4be055681b4bf0dcd8021c2b202cc0]
- Knowledge is stored in a shared append-only JSONL log (.lavra/memory/knowledge.jsonl) committed to git, with a local SQLite FTS5 search index, a curated active cache, and an audit log of sanitizer filtering actions. [@claim:clm_51e4c4920a85e9d9d7259859ffb1bb9376dfe12e617d5468497e0504234c7a24]
- Lavra requires the beads CLI, jq, and sqlite3; the memory sanitizer compiles a Go helper when Go is available and falls back to a jq-based path otherwise, and grep-based search remains if sqlite3 is missing. [@claim:clm_53fb2d98d15ce3f271d638fdbc0247d92e588684a9c6dc2d36530b39cfe3a834]
- Lavra is a fork of Every's compound-engineering-plugin (MIT), replacing markdown knowledge storage with beads-based JSONL memory, FTS5 search, and workflows that create and update beads instead of markdown files. [@claim:clm_5c1e51242568c4b9eb38a9fafccb8c353e3638f05a4d765141aef5b768ab1a54]
- Agents run at assigned model tiers (Haiku/Sonnet/Opus) by reasoning complexity; the 'quality' model_profile routes critical agents like security-sentinel and goal-verifier to Opus, with a documented claim of 60-70% cost reduction versus running everything on the top model. [@claim:clm_95fba6fe4638d0c11be02732049650374d8487396ca5d876c807f912a5aaf4b7]
- The plugin ships 30 specialized agents (16 review, 5 research, 3 design, 5 workflow, 1 docs per the architecture tree), 16 core skills, 4 hooks, and a Context7 MCP server for framework documentation lookup. [@claim:clm_e98223c3058e6b9c6255214e875511577ad93b2df1fc9a84850e38ebca0a7d24]
<!-- rcw:end owner=source:src_cd9b9ee0e3a0502880efbc7045a89629 block=evidence -->

## Researcher notes

