---
access: public
aliases: []
claim_ids:
- clm_20f65a420c29769def7379bdd8e3b25f498335a236be553cc3ed1ef443bdbc50
- clm_3051516f88262d0d7f879528da908933e732241770cace07ad17b2977dea63f2
- clm_31faf4136eaaeffb63cf739be2e98de7178f64c581e32b23f38d218e7a035c78
- clm_5da68bca9f3e804331ec55217c294224ff27516da133f4af8629a743020e040b
- clm_78bb77fd5b09de3131c54752ad039f32c8f1a50cd38fb6fcc977cab595d474e4
- clm_88b9268644ea19ab43acedea4ad73eefabcea4d249ae6f1c7c56a1f7eb8098f6
- clm_ab16bcb6907b944c6e8adccbf1b0c45ff0e3f12a5f6f0c859be03499c5d08637
- clm_ac5aba8aa994bd01719dae06cc7914b0b467aabf92d8e536a2ed49bc97d5a47a
- clm_b3cf5014f1fe583f35ea7d9c472468ab2c050f85142b4784e62aa2fd568a5409
- clm_d083de3891ee07a196a2c2a77ce81de01fb78199aac20030d94dba54d4c87f49
- clm_d79428f6222ace19b9ec747c5e837929dabe1d814f52d2ce2cb4b3aae36b996a
- clm_ef59f68962155ebe581b42e3f80ddeff8ecadcaa87bfe883ed8feb3816ccbf37
maturity: draft
page_id: pg_24915be937d35663a88123d85e2eceee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cf470e97e5b558b38a75f7e0c676b687
title: husnainpk/SymDex/README.md @ 257bb3c215b3
updated_at: '2026-09-14T03:58:07Z'
---

# husnainpk/SymDex/README.md @ 257bb3c215b3

<!-- rcw:begin owner=source:src_cf470e97e5b558b38a75f7e0c676b687 block=evidence -->
- Indexes are stored as per-repo SQLite databases under ~/.symdex by default, plus a central registry; SYMDEX_STATE_DIR or --state-dir enables workspace-local ./.symdex state with registry.db and registry.json. [@claim:clm_20f65a420c29769def7379bdd8e3b25f498335a236be553cc3ed1ef443bdbc50]
- MCP exposes repo-tree and stats views (get_file_tree, get_repo_outline, get_index_status, get_repo_stats) that are not surfaced as dedicated CLI commands. [@claim:clm_3051516f88262d0d7f879528da908933e732241770cace07ad17b2977dea63f2]
- Semantic search is optional: the base install stays lean, and embedding backends include local sentence-transformers, Voyage (text and multimodal), OpenAI-compatible /embeddings endpoints, and Gemini, configured via environment variables. [@claim:clm_31faf4136eaaeffb63cf739be2e98de7178f64c581e32b23f38d218e7a035c78]
- Documented CLI surface includes index, watch, invalidate, gc, repos, search, find, text, semantic, pack, outline, callers, callees, routes, and serve commands, with serve supporting a --port option. [@claim:clm_5da68bca9f3e804331ec55217c294224ff27516da133f4af8629a743020e040b]
- SymDex is described as a repo-local symbolic indexing engine that maps a project into symbols, files, routes, relations, docs, tests, and retrieval context for AI coding agents. [@claim:clm_78bb77fd5b09de3131c54752ad039f32c8f1a50cd38fb6fcc977cab595d474e4]
- A symdex-code-search agent skill ships at skills/symdex-code-search/SKILL.md, installable via the skills CLI, instructing agents to check index readiness, prefer symbol/outline retrieval, and use context packs before broad file reads. [@claim:clm_88b9268644ea19ab43acedea4ad73eefabcea4d249ae6f1c7c56a1f7eb8098f6]
- Repository development practice: the README's contributing section only says issues and PRs are welcome at the GitHub repository; no detailed contributor workflow, CI, or test-running instructions appear in the evidence. [@claim:clm_ab16bcb6907b944c6e8adccbf1b0c45ff0e3f12a5f6f0c859be03499c5d08637]
- The product exposes both CLI commands and an MCP server; the MCP server reportedly exposes 21 tools covering indexing, search, context packs, outlines, routes, stats, graphs, cache invalidation, and stale-index cleanup. [@claim:clm_ac5aba8aa994bd01719dae06cc7914b0b467aabf92d8e536a2ed49bc97d5a47a]
- Watch mode is documented as low-memory by default, refreshing structure without loading embedding models unless --embed is passed, with duplicate-watcher protection and idle auto-exit. [@claim:clm_b3cf5014f1fe583f35ea7d9c472468ab2c050f85142b4784e62aa2fd568a5409]
- Parsing is documented as powered by tree-sitter with language-pack grammar fallbacks and a native Markdown scanner; remote OpenAI-compatible and Gemini backends use the Python standard library HTTP client so they add no required dependency. [@claim:clm_d083de3891ee07a196a2c2a77ce81de01fb78199aac20030d94dba54d4c87f49]
- The README states SymDex is not a full static analyzer, type checker, or refactoring engine, and semantic search requires stored embeddings, so repos indexed without a backend must be re-indexed. [@claim:clm_d79428f6222ace19b9ec747c5e837929dabe1d814f52d2ce2cb4b3aae36b996a]
- A cross-repo registry supports multiple repos and worktrees, auto-generating stable repo ids from git branch and path hash when --repo is omitted, with gc for stale entries. [@claim:clm_ef59f68962155ebe581b42e3f80ddeff8ecadcaa87bfe883ed8feb3816ccbf37]
<!-- rcw:end owner=source:src_cf470e97e5b558b38a75f7e0c676b687 block=evidence -->

## Researcher notes

