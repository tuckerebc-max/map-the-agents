---
access: public
aliases: []
claim_ids:
- clm_1df2c71a0b50eb66b1333572da6f56bc45b481c77553e5a94b1d3f152b1299f7
- clm_33347610d71307300dfcdd0e38fb21a5edc926addf3197ccc6e72331ba408f81
- clm_61ede137ce230e0ebf2f3f5775283ba15954a580226287791be20742bb6fcdf5
- clm_88a3f2a04300e73d06e95ad91b35f97de0fc4081a45c7d035da680c2701978d3
- clm_9170c4e779383ced6acb1e5ad012ce04b66118dddc3405073fc8dea422edb2fe
- clm_aa8471b8fe6df8093717d207f7218a81b4d3030fa6c22d04d22cb4eed87e3048
- clm_afaa62988b79901ba25cc46aea06f689fd12876bc255de89b6c3ec8851cd2ebc
- clm_bc2a879d8142ada95be7a78c10d7d55e7a0ca2927574dd892d0f80e3da889f58
- clm_c124c3c6d625bde3c36424315838955023e0f13d0a3d53e915a0db28f88fb24a
- clm_c3cce7a9eabe16f04cae46ac22d9aedde8118a1edff17df88af2688066e0c259
- clm_cee59ae989649fb8bb47173db4189f85648a49b07ee5adbe5701c17d3cd61ff3
- clm_e532d56a1b7977a4e3a5db667fff6411eada76c91d0590b4522d3d9c4ee298af
maturity: draft
page_id: pg_f728b8a962ee5088b0eec1d7ab9fd074
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_643e1a72450654a2940c2b7bb406e24f
title: coleam00/Archon/README.md @ a7e300b2a740
updated_at: '2026-09-14T01:43:05Z'
---

# coleam00/Archon/README.md @ a7e300b2a740

<!-- rcw:begin owner=source:src_643e1a72450654a2940c2b7bb406e24f block=evidence -->
- Workflows compose deterministic nodes (bash scripts, tests, git operations) with AI nodes, so AI runs only where it adds value; the example includes a test loop iterating until tests pass and an interactive human approval gate. [@claim:clm_1df2c71a0b50eb66b1333572da6f56bc45b481c77553e5a94b1d3f152b1299f7]
- The project ships 19 default workflows, and a router can select an appropriate workflow when the user describes what they want. [@claim:clm_33347610d71307300dfcdd0e38fb21a5edc926addf3197ccc6e72331ba408f81]
- The macOS/Linux quick install requires AVX2 on x64 CPUs, and compiled binaries do not bundle Claude Code, so users must set CLAUDE_BIN_PATH or a config path; the Docker image ships Claude Code pre-installed. [@claim:clm_61ede137ce230e0ebf2f3f5775283ba15954a580226287791be20742bb6fcdf5]
- The CLI includes commands such as `archon serve` (start the web dashboard), `archon workflow list`, `archon telemetry status/reset`, and `archon doctor`. [@claim:clm_88a3f2a04300e73d06e95ad91b35f97de0fc4081a45c7d035da680c2701978d3]
- The documented architecture layers platform adapters above an orchestrator, with a slash command handler, YAML workflow executor, AI assistant clients (Claude/Codex/Pi), and a SQLite/PostgreSQL store of 14 core tables covering codebases, conversations, sessions, and workflow runs. [@claim:clm_9170c4e779383ced6acb1e5ad012ce04b66118dddc3405073fc8dea422edb2fe]
- The web dashboard offers a chat page with streaming and tool-call visualization, a workflow monitoring dashboard, a drag-and-drop workflow builder for DAG workflows, and per-run execution views. [@claim:clm_aa8471b8fe6df8093717d207f7218a81b4d3030fa6c22d04d22cb4eed87e3048]
- Full setup lists Bun, Claude Code, and the GitHub CLI as prerequisites, with platform-specific install commands provided. [@claim:clm_afaa62988b79901ba25cc46aea06f689fd12876bc255de89b6c3ec8851cd2ebc]
- Each workflow run gets its own git worktree, allowing multiple fixes to run in parallel without conflicts. [@claim:clm_bc2a879d8142ada95be7a78c10d7d55e7a0ca2927574dd892d0f80e3da889f58]
- Archon is described as a workflow engine for AI coding agents in which development processes (planning, implementation, validation, review, PR creation) are defined as YAML workflows. [@claim:clm_c124c3c6d625bde3c36424315838955023e0f13d0a3d53e915a0db28f88fb24a]
- The setup wizard copies the Archon skill into target projects, and users are told to run Claude Code from the target repo rather than the Archon repo. [@claim:clm_c3cce7a9eabe16f04cae46ac22d9aedde8118a1edff17df88af2688066e0c259]
- Beyond the Web UI and CLI, optional chat-platform adapters for Telegram, Slack, GitHub webhooks, and Discord provide remote access, and the sidebar aggregates activity from all platforms. [@claim:clm_cee59ae989649fb8bb47173db4189f85648a49b07ee5adbe5701c17d3cd61ff3]
- Telemetry sends anonymous categorical events (bundled workflow names only, run outcomes, token/cost totals, machine context) with no PII; it can be disabled via environment variables and is auto-disabled when CI=true. [@claim:clm_e532d56a1b7977a4e3a5db667fff6411eada76c91d0590b4522d3d9c4ee298af]
<!-- rcw:end owner=source:src_643e1a72450654a2940c2b7bb406e24f block=evidence -->

## Researcher notes

