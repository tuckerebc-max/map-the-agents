---
access: public
aliases: []
claim_ids:
- clm_2305f4ab852b1a20e81a7f1bec04b9bdd1ac5846fa2a8218af3a4878ee5f511a
- clm_2c2ce4c8ad109f9476f473c7d4fac68fe01d56a87d8a4e13c4ebacef5007cef2
- clm_3b4e8d1fce188a04cd9c003f6be59946d4736c5fc0bf88897cf0945deee59f4d
- clm_42a0ca9b10196b75606c789da48071ebf832b18faa59639ce3e239c65473ef8b
- clm_449f17ab94dbc2aa46e25d9c733423db671dfab81ecc22f0b62fff5647e86935
- clm_5055a3ff44842ff8b4cdca6365e2a1386288a7dc999221a1e9a94571d8be39cf
- clm_77cc71b8b6ae25a1630054a349dc8f1a8f6ea99fe2a73ec101834404fad2db75
- clm_8b203dfbbf64a3021b5a0b1496ae3857f43d8fa6aeb561ae1ba54423f6fe4333
- clm_abbccba2ef0f4ea123b0c1edee0e842fe50a8187c9af6dba3c283c011b015cce
- clm_b5dfa06f740d39d5b292d39badd8dd4657a9cdadd2fe774a4dbe35261097c83c
- clm_d8b984d6f9667c3ccce9936d216a6a5232c36202a01d997d042ab5191b17f2a8
maturity: draft
page_id: pg_ed28de7d84ba5cb2ae49b7ffb4155e02
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_691424a8f159591c9a5330f1cfad6df8
title: trailhq/Graft/README.md @ f9e65396e638
updated_at: '2026-09-14T04:27:38Z'
---

# trailhq/Graft/README.md @ f9e65396e638

<!-- rcw:begin owner=source:src_691424a8f159591c9a5330f1cfad6df8 block=evidence -->
- Claude Code deep integration adds a live statusline (graph size, % enriched, stale warning), automatic structural graph refresh per query, per-prompt node injection, and post-edit blast-radius hooks; init is idempotent and merges rather than clobbers .claude/settings.json. [@claim:clm_2305f4ab852b1a20e81a7f1bec04b9bdd1ac5846fa2a8218af3a4878ee5f511a]
- LLM summaries use the user's own provider key; GRAFT_PROVIDER/GRAFT_API_KEY/GRAFT_MODEL/GRAFT_BASE_URL (or CLI flags) support OpenAI-compatible endpoints, native Anthropic, LiteLLM, OpenRouter, Fireworks, Groq, or local models. [@claim:clm_2c2ce4c8ad109f9476f473c7d4fac68fe01d56a87d8a4e13c4ebacef5007cef2]
- Each markdown node holds a model-written summary, inline crux code, content-hash-tracked sources, typed [[wikilinks]] (depends_on, part_of, uses, implements, produces), and user notes preserved across regeneration. [@claim:clm_3b4e8d1fce188a04cd9c003f6be59946d4736c5fc0bf88897cf0945deee59f4d]
- graft init registers an MCP server exposing six tools: graft_find_code, graft_file_api, graft_trace_calls, graft_find_all, graft_repo_map, and graft_check_freshness. [@claim:clm_42a0ca9b10196b75606c789da48071ebf832b18faa59639ce3e239c65473ef8b]
- The graph is a regenerable local cache: graft build adds graft/ to .gitignore, and only the wiring in .claude/ and instruction files is committed; teammates each run graft build themselves. [@claim:clm_449f17ab94dbc2aa46e25d9c733423db671dfab81ecc22f0b62fff5647e86935]
- Graft builds a codebase understanding graph once and writes it into the repo as a folder of linked markdown files, one node per system, API, or concept. [@claim:clm_5055a3ff44842ff8b4cdca6365e2a1386288a7dc999221a1e9a94571d8be39cf]
- graft init wires multiple agents (Claude, Cursor, Gemini, Codex, Copilot, Kiro, Windsurf, Grok, AdaL) via marker-fenced instruction-file sections or owned skill/rule files, with flags like --agents, --dry-run, --no-mcp, --no-hooks, --no-statusline, --no-global. [@claim:clm_77cc71b8b6ae25a1630054a349dc8f1a8f6ea99fe2a73ec101834404fad2db75]
- Per the README, the crux currently ships per-symbol in the code graph via graft build --deep; inlining crux into markdown nodes is described as future work. [@claim:clm_8b203dfbbf64a3021b5a0b1496ae3857f43d8fa6aeb561ae1ba54423f6fe4333]
- Every query refreshes the graph against the working tree first via a ~3ms structural fingerprint check, never calling the LLM; disable per-command with --no-refresh or globally with GRAFT_NO_REFRESH=1. [@claim:clm_abbccba2ef0f4ea123b0c1edee0e842fe50a8187c9af6dba3c283c011b015cce]
- Parsing uses tree-sitter at two fidelity tiers plus optional compiler-grade lsp_resolved edges via rust-analyzer, clangd, gopls, pyright, or typescript-language-server when on PATH; 23 languages total, unlisted languages are skipped. [@claim:clm_b5dfa06f740d39d5b292d39badd8dd4657a9cdadd2fe774a4dbe35261097c83c]
- The README reports a 162-run harness (cold vs Graft push vs pull variants, Opus judge with keyword floor) and SWE-bench Verified 50-instance runs where graft resolved 33/50 vs 27/50 with fewer tokens, calls, and wall-clock time. [@claim:clm_d8b984d6f9667c3ccce9936d216a6a5232c36202a01d997d042ab5191b17f2a8]
<!-- rcw:end owner=source:src_691424a8f159591c9a5330f1cfad6df8 block=evidence -->

## Researcher notes

