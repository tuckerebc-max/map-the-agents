# husnainpk/symdex

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 257bb3c215b3 @ a1afcb7025639afb

## Summary (orientation draft, not independently verified)

Evidence consists solely of README slices for SymDex, a repo-local symbolic indexing engine for AI coding agents exposing CLI commands and 21 MCP tools backed by SQLite indexes. All product claims are documentation-based; no code inspection is available.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] SymDex is described as a repo-local symbolic indexing engine that maps a project into symbols, files, routes, relations, docs, tests, and retrieval context for AI coding agents. -- evidence: [README.md#L64-L64](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L64-L64), [README.md#L491-L491](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L491-L491)
- components (1 claim(s)):
  - [observation/documented] Indexes are stored as per-repo SQLite databases under ~/.symdex by default, plus a central registry; SYMDEX_STATE_DIR or --state-dir enables workspace-local ./.symdex state with registry.db and registry.json. -- evidence: [README.md#L215-L217](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L215-L217), [README.md#L547-L547](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L547-L547), [README.md#L205-L205](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L205-L205)
- design-choices (2 claim(s)):
  - [observation/documented] Semantic search is optional: the base install stays lean, and embedding backends include local sentence-transformers, Voyage (text and multimodal), OpenAI-compatible /embeddings endpoints, and Gemini, configured via environment variables. -- evidence: [README.md#L84-L84](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L84-L84), [README.md#L399-L401](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L399-L401), [README.md#L420-L423](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L420-L423), [README.md#L410-L413](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L410-L413), [README.md#L397-L397](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L397-L397), [README.md#L434-L441](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L434-L441), [README.md#L449-L455](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L449-L455), [README.md#L403-L403](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L403-L403)
  - [observation/documented] Watch mode is documented as low-memory by default, refreshing structure without loading embedding models unless --embed is passed, with duplicate-watcher protection and idle auto-exit. -- evidence: [README.md#L88-L103](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L88-L103), [README.md#L543-L543](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L543-L543)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's contributing section only says issues and PRs are welcome at the GitHub repository; no detailed contributor workflow, CI, or test-running instructions appear in the evidence. -- evidence: [README.md#L585-L585](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L585-L585)
- skills-patterns (1 claim(s)):
  - [observation/documented] A symdex-code-search agent skill ships at skills/symdex-code-search/SKILL.md, installable via the skills CLI, instructing agents to check index readiness, prefer symbol/outline retrieval, and use context packs before broad file reads. -- evidence: [README.md#L111-L113](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L111-L113), [README.md#L126-L126](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L126-L126), [README.md#L117-L124](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L117-L124)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes both CLI commands and an MCP server; the MCP server reportedly exposes 21 tools covering indexing, search, context packs, outlines, routes, stats, graphs, cache invalidation, and stale-index cleanup. -- evidence: [README.md#L503-L503](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L503-L503), [README.md#L316-L316](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L316-L316), [README.md#L64-L64](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L64-L64), [README.md#L318-L340](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L318-L340)
  - [observation/documented] Documented CLI surface includes index, watch, invalidate, gc, repos, search, find, text, semantic, pack, outline, callers, callees, routes, and serve commands, with serve supporting a --port option. -- evidence: [README.md#L306-L308](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L306-L308), [README.md#L298-L303](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L298-L303), [README.md#L277-L286](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L277-L286), [README.md#L289-L295](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L289-L295)
- memory-state (1 claim(s)):
  - [observation/documented] A cross-repo registry supports multiple repos and worktrees, auto-generating stable repo ids from git branch and path hash when --repo is omitted, with gc for stale entries. -- evidence: [README.md#L165-L174](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L165-L174), [README.md#L551-L551](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L551-L551), [README.md#L72-L80](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L72-L80)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](symdex.detail.md)

Metadata and full claim list: [full detail](symdex.detail.md)
Human notes ([notes](symdex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
