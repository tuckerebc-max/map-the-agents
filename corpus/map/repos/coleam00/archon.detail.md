# coleam00/archon -- full detail

[Back to orientation](archon.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coleam00/archon/a7e300b2a74051711b7de2262c267cb96d3002d2/dfc91846333717e8.json](../../../wiki/dossiers/coleam00/archon/a7e300b2a74051711b7de2262c267cb96d3002d2/dfc91846333717e8.json)

## specifications (2 claim(s))

- [observation/documented] Archon is described as a workflow engine for AI coding agents in which development processes (planning, implementation, validation, review, PR creation) are defined as YAML workflows. -- evidence: [README.md#L23-L23](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L23-L23) (`clm_c124c3c6d625bde3c36424315838955023e0f13d0a3d53e915a0db28f88fb24a`)
- [observation/documented] The project ships 19 default workflows, and a router can select an appropriate workflow when the user describes what they want. -- evidence: [README.md#L258-L258](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L258-L258) (`clm_33347610d71307300dfcdd0e38fb21a5edc926addf3197ccc6e72331ba408f81`)

## components (1 claim(s))

- [observation/documented] The documented architecture layers platform adapters above an orchestrator, with a slash command handler, YAML workflow executor, AI assistant clients (Claude/Codex/Pi), and a SQLite/PostgreSQL store of 14 core tables covering codebases, conversations, sessions, and workflow runs. -- evidence: [README.md#L277-L310](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L277-L310) (`clm_9170c4e779383ced6acb1e5ad012ce04b66118dddc3405073fc8dea422edb2fe`)

## design-choices (2 claim(s))

- [observation/documented] Workflows compose deterministic nodes (bash scripts, tests, git operations) with AI nodes, so AI runs only where it adds value; the example includes a test loop iterating until tests pass and an interactive human approval gate. -- evidence: [README.md#L64-L69](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L64-L69), [README.md#L49-L54](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L49-L54), [README.md#L33-L37](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L33-L37), [README.md#L56-L58](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L56-L58) (`clm_1df2c71a0b50eb66b1333572da6f56bc45b481c77553e5a94b1d3f152b1299f7`)
- [observation/documented] Telemetry sends anonymous categorical events (bundled workflow names only, run outcomes, token/cost totals, machine context) with no PII; it can be disabled via environment variables and is auto-disabled when CI=true. -- evidence: [README.md#L344-L344](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L344-L344), [README.md#L333-L333](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L333-L333), [README.md#L335-L342](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L335-L342), [README.md#L354-L354](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L354-L354), [README.md#L348-L352](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L348-L352) (`clm_e532d56a1b7977a4e3a5db667fff6411eada76c91d0590b4522d3d9c4ee298af`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The setup wizard copies the Archon skill into target projects, and users are told to run Claude Code from the target repo rather than the Archon repo. -- evidence: [README.md#L153-L153](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L153-L153), [README.md#L214-L214](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L214-L214), [README.md#L104-L104](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L104-L104) (`clm_c3cce7a9eabe16f04cae46ac22d9aedde8118a1edff17df88af2688066e0c259`)

## interfaces (2 claim(s))

- [observation/documented] The CLI includes commands such as `archon serve` (start the web dashboard), `archon workflow list`, `archon telemetry status/reset`, and `archon doctor`. -- evidence: [README.md#L356-L356](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L356-L356), [README.md#L258-L258](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L258-L258), [README.md#L218-L218](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L218-L218) (`clm_88a3f2a04300e73d06e95ad91b35f97de0fc4081a45c7d035da680c2701978d3`)
- [observation/documented] The web dashboard offers a chat page with streaming and tool-call visualization, a workflow monitoring dashboard, a drag-and-drop workflow builder for DAG workflows, and per-run execution views. -- evidence: [README.md#L222-L226](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L222-L226) (`clm_aa8471b8fe6df8093717d207f7218a81b4d3030fa6c22d04d22cb4eed87e3048`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Each workflow run gets its own git worktree, allowing multiple fixes to run in parallel without conflicts. -- evidence: [README.md#L33-L37](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L33-L37) (`clm_bc2a879d8142ada95be7a78c10d7d55e7a0ca2927574dd892d0f80e3da889f58`)
- [observation/documented] Beyond the Web UI and CLI, optional chat-platform adapters for Telegram, Slack, GitHub webhooks, and Discord provide remote access, and the sidebar aggregates activity from all platforms. -- evidence: [README.md#L268-L273](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L268-L273), [README.md#L228-L228](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L228-L228) (`clm_cee59ae989649fb8bb47173db4189f85648a49b07ee5adbe5701c17d3cd61ff3`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Full setup lists Bun, Claude Code, and the GitHub CLI as prerequisites, with platform-specific install commands provided. -- evidence: [README.md#L132-L132](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L132-L132), [README.md#L109-L109](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L109-L109), [README.md#L106-L107](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L106-L107), [README.md#L119-L119](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L119-L119) (`clm_afaa62988b79901ba25cc46aea06f689fd12876bc255de89b6c3ec8851cd2ebc`)

## limitations (1 claim(s))

- [observation/documented] The macOS/Linux quick install requires AVX2 on x64 CPUs, and compiled binaries do not bundle Claude Code, so users must set CLAUDE_BIN_PATH or a config path; the Docker image ships Claude Code pre-installed. -- evidence: [README.md#L164-L167](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L164-L167), [README.md#L179-L193](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L179-L193) (`clm_61ede137ce230e0ebf2f3f5775283ba15954a580226287791be20742bb6fcdf5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

