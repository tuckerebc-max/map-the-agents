# husnainpk/symdex -- full detail

[Back to orientation](symdex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/husnainpk/symdex/257bb3c215b347f623b2d1c7ab453bb621623baf/a1afcb7025639afb.json](../../../wiki/dossiers/husnainpk/symdex/257bb3c215b347f623b2d1c7ab453bb621623baf/a1afcb7025639afb.json)

## specifications (1 claim(s))

- [observation/documented] SymDex is described as a repo-local symbolic indexing engine that maps a project into symbols, files, routes, relations, docs, tests, and retrieval context for AI coding agents. -- evidence: [README.md#L64-L64](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L64-L64), [README.md#L491-L491](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L491-L491) (`clm_78bb77fd5b09de3131c54752ad039f32c8f1a50cd38fb6fcc977cab595d474e4`)

## components (1 claim(s))

- [observation/documented] Indexes are stored as per-repo SQLite databases under ~/.symdex by default, plus a central registry; SYMDEX_STATE_DIR or --state-dir enables workspace-local ./.symdex state with registry.db and registry.json. -- evidence: [README.md#L215-L217](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L215-L217), [README.md#L547-L547](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L547-L547), [README.md#L205-L205](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L205-L205) (`clm_20f65a420c29769def7379bdd8e3b25f498335a236be553cc3ed1ef443bdbc50`)

## design-choices (2 claim(s))

- [observation/documented] Semantic search is optional: the base install stays lean, and embedding backends include local sentence-transformers, Voyage (text and multimodal), OpenAI-compatible /embeddings endpoints, and Gemini, configured via environment variables. -- evidence: [README.md#L84-L84](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L84-L84), [README.md#L399-L401](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L399-L401), [README.md#L420-L423](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L420-L423), [README.md#L410-L413](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L410-L413), [README.md#L397-L397](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L397-L397), [README.md#L434-L441](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L434-L441), [README.md#L449-L455](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L449-L455), [README.md#L403-L403](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L403-L403) (`clm_31faf4136eaaeffb63cf739be2e98de7178f64c581e32b23f38d218e7a035c78`)
- [observation/documented] Watch mode is documented as low-memory by default, refreshing structure without loading embedding models unless --embed is passed, with duplicate-watcher protection and idle auto-exit. -- evidence: [README.md#L88-L103](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L88-L103), [README.md#L543-L543](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L543-L543) (`clm_b3cf5014f1fe583f35ea7d9c472468ab2c050f85142b4784e62aa2fd568a5409`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's contributing section only says issues and PRs are welcome at the GitHub repository; no detailed contributor workflow, CI, or test-running instructions appear in the evidence. -- evidence: [README.md#L585-L585](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L585-L585) (`clm_ab16bcb6907b944c6e8adccbf1b0c45ff0e3f12a5f6f0c859be03499c5d08637`)

## skills-patterns (1 claim(s))

- [observation/documented] A symdex-code-search agent skill ships at skills/symdex-code-search/SKILL.md, installable via the skills CLI, instructing agents to check index readiness, prefer symbol/outline retrieval, and use context packs before broad file reads. -- evidence: [README.md#L111-L113](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L111-L113), [README.md#L126-L126](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L126-L126), [README.md#L117-L124](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L117-L124) (`clm_88b9268644ea19ab43acedea4ad73eefabcea4d249ae6f1c7c56a1f7eb8098f6`)

## interfaces (3 claim(s))

- [observation/documented] The product exposes both CLI commands and an MCP server; the MCP server reportedly exposes 21 tools covering indexing, search, context packs, outlines, routes, stats, graphs, cache invalidation, and stale-index cleanup. -- evidence: [README.md#L503-L503](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L503-L503), [README.md#L316-L316](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L316-L316), [README.md#L64-L64](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L64-L64), [README.md#L318-L340](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L318-L340) (`clm_ac5aba8aa994bd01719dae06cc7914b0b467aabf92d8e536a2ed49bc97d5a47a`)
- [observation/documented] Documented CLI surface includes index, watch, invalidate, gc, repos, search, find, text, semantic, pack, outline, callers, callees, routes, and serve commands, with serve supporting a --port option. -- evidence: [README.md#L306-L308](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L306-L308), [README.md#L298-L303](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L298-L303), [README.md#L277-L286](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L277-L286), [README.md#L289-L295](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L289-L295) (`clm_5da68bca9f3e804331ec55217c294224ff27516da133f4af8629a743020e040b`)
- [observation/documented] MCP exposes repo-tree and stats views (get_file_tree, get_repo_outline, get_index_status, get_repo_stats) that are not surfaced as dedicated CLI commands. -- evidence: [README.md#L310-L310](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L310-L310) (`clm_3051516f88262d0d7f879528da908933e732241770cace07ad17b2977dea63f2`)

## memory-state (1 claim(s))

- [observation/documented] A cross-repo registry supports multiple repos and worktrees, auto-generating stable repo ids from git branch and path hash when --repo is omitted, with gc for stale entries. -- evidence: [README.md#L165-L174](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L165-L174), [README.md#L551-L551](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L551-L551), [README.md#L72-L80](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L72-L80) (`clm_ef59f68962155ebe581b42e3f80ddeff8ecadcaa87bfe883ed8feb3816ccbf37`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Parsing is documented as powered by tree-sitter with language-pack grammar fallbacks and a native Markdown scanner; remote OpenAI-compatible and Gemini backends use the Python standard library HTTP client so they add no required dependency. -- evidence: [README.md#L370-L370](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L370-L370), [README.md#L403-L403](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L403-L403) (`clm_d083de3891ee07a196a2c2a77ce81de01fb78199aac20030d94dba54d4c87f49`)

## limitations (1 claim(s))

- [observation/documented] The README states SymDex is not a full static analyzer, type checker, or refactoring engine, and semantic search requires stored embeddings, so repos indexed without a backend must be re-indexed. -- evidence: [README.md#L539-L539](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L539-L539), [README.md#L515-L515](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L515-L515), [README.md#L499-L499](https://github.com/husnainpk/SymDex/blob/257bb3c215b347f623b2d1c7ab453bb621623baf/README.md#L499-L499) (`clm_d79428f6222ace19b9ec747c5e837929dabe1d814f52d2ce2cb4b3aae36b996a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

