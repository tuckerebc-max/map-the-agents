# trailhq/graft -- full detail

[Back to orientation](graft.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/trailhq/graft/f9e65396e638e517aecae0d731017f53084d70ed/0609a629c52368da.json](../../../wiki/dossiers/trailhq/graft/f9e65396e638e517aecae0d731017f53084d70ed/0609a629c52368da.json)

## specifications (1 claim(s))

- [observation/documented] Graft builds a codebase understanding graph once and writes it into the repo as a folder of linked markdown files, one node per system, API, or concept. -- evidence: [README.md#L114-L114](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L114-L114) (`clm_5055a3ff44842ff8b4cdca6365e2a1386288a7dc999221a1e9a94571d8be39cf`)

## components (1 claim(s))

- [observation/documented] Parsing uses tree-sitter at two fidelity tiers plus optional compiler-grade lsp_resolved edges via rust-analyzer, clangd, gopls, pyright, or typescript-language-server when on PATH; 23 languages total, unlisted languages are skipped. -- evidence: [README.md#L216-L220](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L216-L220), [README.md#L200-L201](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L200-L201), [README.md#L222-L224](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L222-L224), [README.md#L211-L214](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L211-L214), [README.md#L203-L209](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L203-L209) (`clm_b5dfa06f740d39d5b292d39badd8dd4657a9cdadd2fe774a4dbe35261097c83c`)

## design-choices (2 claim(s))

- [observation/documented] The graph is a regenerable local cache: graft build adds graft/ to .gitignore, and only the wiring in .claude/ and instruction files is committed; teammates each run graft build themselves. -- evidence: [README.md#L82-L82](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L82-L82), [README.md#L116-L120](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L116-L120) (`clm_449f17ab94dbc2aa46e25d9c733423db671dfab81ecc22f0b62fff5647e86935`)
- [observation/documented] Every query refreshes the graph against the working tree first via a ~3ms structural fingerprint check, never calling the LLM; disable per-command with --no-refresh or globally with GRAFT_NO_REFRESH=1. -- evidence: [README.md#L192-L192](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L192-L192) (`clm_abbccba2ef0f4ea123b0c1edee0e842fe50a8187c9af6dba3c283c011b015cce`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] graft init registers an MCP server exposing six tools: graft_find_code, graft_file_api, graft_trace_calls, graft_find_all, graft_repo_map, and graft_check_freshness. -- evidence: [README.md#L303-L310](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L303-L310), [README.md#L301-L301](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L301-L301) (`clm_42a0ca9b10196b75606c789da48071ebf832b18faa59639ce3e239c65473ef8b`)
- [observation/documented] Claude Code deep integration adds a live statusline (graph size, % enriched, stale warning), automatic structural graph refresh per query, per-prompt node injection, and post-edit blast-radius hooks; init is idempotent and merges rather than clobbers .claude/settings.json. -- evidence: [README.md#L324-L326](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L324-L326), [README.md#L338-L338](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L338-L338), [README.md#L322-L322](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L322-L322) (`clm_2305f4ab852b1a20e81a7f1bec04b9bdd1ac5846fa2a8218af3a4878ee5f511a`)

## memory-state (1 claim(s))

- [observation/documented] Each markdown node holds a model-written summary, inline crux code, content-hash-tracked sources, typed [[wikilinks]] (depends_on, part_of, uses, implements, produces), and user notes preserved across regeneration. -- evidence: [README.md#L244-L244](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L244-L244), [README.md#L234-L240](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L234-L240) (`clm_3b4e8d1fce188a04cd9c003f6be59946d4736c5fc0bf88897cf0945deee59f4d`)

## orchestration (1 claim(s))

- [observation/documented] graft init wires multiple agents (Claude, Cursor, Gemini, Codex, Copilot, Kiro, Windsurf, Grok, AdaL) via marker-fenced instruction-file sections or owned skill/rule files, with flags like --agents, --dry-run, --no-mcp, --no-hooks, --no-statusline, --no-global. -- evidence: [README.md#L272-L272](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L272-L272), [README.md#L270-L270](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L270-L270), [README.md#L274-L285](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L274-L285) (`clm_77cc71b8b6ae25a1630054a349dc8f1a8f6ea99fe2a73ec101834404fad2db75`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports a 162-run harness (cold vs Graft push vs pull variants, Opus judge with keyword floor) and SWE-bench Verified 50-instance runs where graft resolved 33/50 vs 27/50 with fewer tokens, calls, and wall-clock time. -- evidence: [README.md#L135-L135](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L135-L135), [README.md#L139-L145](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L139-L145), [README.md#L147-L147](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L147-L147), [README.md#L166-L166](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L166-L166), [README.md#L155-L155](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L155-L155), [README.md#L157-L164](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L157-L164), [README.md#L153-L153](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L153-L153), [README.md#L137-L137](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L137-L137) (`clm_d8b984d6f9667c3ccce9936d216a6a5232c36202a01d997d042ab5191b17f2a8`)

## dependencies (1 claim(s))

- [observation/documented] LLM summaries use the user's own provider key; GRAFT_PROVIDER/GRAFT_API_KEY/GRAFT_MODEL/GRAFT_BASE_URL (or CLI flags) support OpenAI-compatible endpoints, native Anthropic, LiteLLM, OpenRouter, Fireworks, Groq, or local models. -- evidence: [README.md#L252-L254](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L252-L254), [README.md#L116-L120](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L116-L120) (`clm_2c2ce4c8ad109f9476f473c7d4fac68fe01d56a87d8a4e13c4ebacef5007cef2`)

## limitations (1 claim(s))

- [observation/documented] Per the README, the crux currently ships per-symbol in the code graph via graft build --deep; inlining crux into markdown nodes is described as future work. -- evidence: [README.md#L246-L246](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L246-L246) (`clm_8b203dfbbf64a3021b5a0b1496ae3857f43d8fa6aeb561ae1ba54423f6fe4333`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

