# glincker/stacklit -- full detail

[Back to orientation](stacklit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/glincker/stacklit/6aa017643d19ab2718d42f098ee2a65717c2e3b6/b685fa5ba411ed97.json](../../../wiki/dossiers/glincker/stacklit/6aa017643d19ab2718d42f098ee2a65717c2e3b6/b685fa5ba411ed97.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Running stacklit init produces three artifacts: stacklit.json (committable index), DEPENDENCIES.md (Mermaid diagram, committable), and stacklit.html (interactive map, gitignored and regenerable). -- evidence: [README.md#L56-L60](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L56-L60) (`clm_ec385cc9147552863657ffb7a9e6331122dcc455e280cfa17674ddc74db1c51f`)
- [observation/documented] The visual map opened by 'stacklit view' offers four views: a force-directed dependency graph, a collapsible tree, a sortable searchable table, and a top-down dependency flow. -- evidence: [README.md#L227-L227](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L227-L227), [README.md#L229-L232](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L229-L232) (`clm_c49f76ddf667ab2908195206cdaaf5748a146ccd92b56575a9728b1a25574c8e`)

## design-choices (1 claim(s))

- [observation/documented] The tool is designed so AI agents read a small (~250-token) navigation map or stacklit.json instead of scanning many files, which the README claims cuts exploration from hundreds of thousands of tokens to a few thousand. -- evidence: [README.md#L75-L75](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L75-L75), [README.md#L3-L3](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L3-L3), [README.md#L71-L71](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L71-L71), [README.md#L73-L73](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L73-L73), [README.md#L137-L137](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L137-L137) (`clm_cd86994fb8551dfd7f34e13b3699f06b3196b97b41bcf6c995982489aea6ec8f`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors build with 'make build' and run all tests with 'make test', per the README contributing section. -- evidence: [README.md#L331-L334](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L331-L334) (`clm_ffebf1331684b7e0c157c670eab019069e7f1926dc095ac6c05c1a31a5bd1130`)
- [observation/documented] Repository development practice: an internal plan document instructs agentic workers to use superpowers subagent-driven-development or executing-plans skills to implement tasks step-by-step with checkbox tracking. -- evidence: [docs/superpowers/plans/2026-04-12-growth-package.md#L3-L3](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L3-L3) (`clm_88cc76840f0c9325a2bc7d552de4de3cb59ce2bceaacce3141c3cd85dee42197`)
- [observation/documented] Repository development practice: the plan's Task 5 prescribes a test-first workflow — write framework-pattern detection tests, run them to confirm failure, then implement in internal/detect and internal/engine. -- evidence: [docs/superpowers/plans/2026-04-12-growth-package.md#L491-L491](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L491-L491), [docs/superpowers/plans/2026-04-12-growth-package.md#L487-L489](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L487-L489), [docs/superpowers/plans/2026-04-12-growth-package.md#L401-L406](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L401-L406), [docs/superpowers/plans/2026-04-12-growth-package.md#L410-L410](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L410-L410), [docs/superpowers/plans/2026-04-12-growth-package.md#L485-L485](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L485-L485) (`clm_ee068570e7d3bfc6e0ef8e94988e300442dbfed145e501d260ca6c4906f63329`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands including init (with --hook and --multi flags), generate, view, diff, serve, derive, export, and setup with per-tool variants for claude and cursor. -- evidence: [README.md#L254-L269](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L254-L269) (`clm_ec454bb52b833e58bc0d038310e51ebb79eceadce05fa7062144428a1a769764`)
- [observation/documented] The MCP server started via 'stacklit serve' exposes seven tools: get_overview, get_module, find_module, list_modules, get_dependencies, get_hot_files, and get_hints. -- evidence: [README.md#L173-L173](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L173-L173) (`clm_409d9a1db29f383cf0fcb69f7efdb157981e3a945b2e87694d4d6bc21dc30101`)
- [observation/documented] stacklit.json contains per-module entries with purpose, file/line counts, exports, depends_on, and activity, plus hints such as where to add features and the test command. -- evidence: [README.md#L108-L108](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L108-L108), [README.md#L90-L106](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L90-L106) (`clm_92ba88bd8b7a702ef4b698c97eb2ecb65d8cdc8307f22e3d1131aa6bd495651c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] 'stacklit setup' auto-detects Claude Code, Cursor, and Aider, injecting a ~250-token codebase map into each tool's config, configuring MCP integration, and installing a git hook to refresh the map on commits. -- evidence: [README.md#L118-L121](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L118-L121), [README.md#L125-L129](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L125-L129) (`clm_73e0df5396557e48ea46a583128de4956420536473b664819cae637c4b2cf009`)

## tools-permissions (1 claim(s))

- [observation/documented] Parsing runs locally and no code is sent anywhere unless the optional --summary flag is used, which calls the Claude API. -- evidence: [README.md#L309-L310](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L309-L310) (`clm_570df8c567277466bfacf94281856fc758f41add916cc9bc9751e9106b47c222`)

## evaluation (1 claim(s))

- [inference/documented] The README's token-efficiency table reports index sizes for real projects, but the planned agent benchmark (tool calls, tokens, correctness) contains only placeholder XX values, so no completed agent-performance evaluation appears in this snapshot. -- evidence: [docs/superpowers/plans/2026-04-12-growth-package.md#L246-L251](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L246-L251), [README.md#L79-L84](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L79-L84), [docs/superpowers/plans/2026-04-12-growth-package.md#L277-L277](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L277-L277), [docs/superpowers/plans/2026-04-12-growth-package.md#L255-L260](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L255-L260) (`clm_8a0c0265295844950403b6c8ef0dcb495e96d5939b66fa5e5bb25232329ffa84`)

## dependencies (2 claim(s))

- [observation/documented] Parsing uses tree-sitter to extract structure for 11 languages (Go, TypeScript/JS, Python, Rust, Java, C#, Ruby, PHP, Kotlin, Swift, C/C++); other languages fall back to line count and language detection. -- evidence: [README.md#L250-L250](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L250-L250), [README.md#L236-L248](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L236-L248), [README.md#L309-L310](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L309-L310) (`clm_2626bc2418e005db4e9f95bd5787b4b043181c82e8a7b395362841e15306df8b`)
- [observation/documented] The project is written in Go and is installable via npx, npm global install, 'go install github.com/glincker/stacklit/cmd/stacklit@latest', or prebuilt binaries for macOS, Linux, and Windows. -- evidence: [docs/superpowers/plans/2026-04-12-growth-package.md#L9-L9](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L9-L9), [README.md#L22-L25](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L22-L25), [README.md#L27-L27](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L27-L27) (`clm_8aa16b80fbc4bfdedbc23ba19a6292625e59df6aee01b044aec180897b3c53f7`)

## limitations (1 claim(s))

- [observation/documented] Languages outside the tree-sitter list get only basic support (line count plus language detection), though the module map, dependency graph, and git activity still work for them. -- evidence: [README.md#L312-L313](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L312-L313) (`clm_deaf18f278013b9a325da39d101cc09bb3f2258e68f76c4b254e37b1c9f40034`)

## relevance (1 claim(s))

- [observation/documented] Stacklit targets teams using AI coding agents on larger codebases, providing a committable structured index so agents avoid rebuilding a mental model of the repo each session. -- evidence: [README.md#L71-L71](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L71-L71), [README.md#L305-L305](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L305-L305), [README.md#L67-L67](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L67-L67) (`clm_0e2a1964afcb4b5aa046953c2967232f0803be39876027c2439185f7ca4602fb`)

