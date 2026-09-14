# butttons/dora -- full detail

[Back to orientation](dora.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/butttons/dora/f4edb8fd349e142e78dea3258c3cd754a27d37bb/f6d9ac8d861f83d6.json](../../../wiki/dossiers/butttons/dora/f4edb8fd349e142e78dea3258c3cd754a27d37bb/f6d9ac8d861f83d6.json)

## specifications (1 claim(s))

- [observation/documented] dora is a CLI that turns a SCIP index into a queryable SQLite database, giving AI agents structured answers about a codebase instead of grepping files and reading imports. -- evidence: [README.md#L3-L3](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L3-L3) (`clm_8e919bf4b9d9b9ea868e5d50e32d0d09af50c686a99106ea5dde81f9ab303a42`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The tool has two layers: a SCIP layer that runs a configured indexer, parses the resulting protobuf, and loads symbols, references, and file dependencies into SQLite; and a tree-sitter layer that parses source on demand via WebAssembly grammars for things SCIP doesn't cover. -- evidence: [README.md#L158-L158](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L158-L158), [README.md#L160-L160](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L160-L160) (`clm_9d28b22943393267a15dc812adabd93cf55e44a24e944f47405e9a0b0ffca1b9`)
- [observation/documented] The SQLite schema stores denormalized counts (symbol_count, dependency_count, dependent_count, reference_count) so most queries are index lookups rather than aggregations. -- evidence: [README.md#L162-L162](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L162-L162) (`clm_fdae466263ac23313f2e20b0c854cacdb6f206eff1a5bab5d3c94bd4c3887ef0`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the docs/ directory is an Astro starter template; its README instructs contributors to scaffold with 'pnpm create astro' and run pnpm install/dev/build/preview from the project root to develop and build the docs site. -- evidence: [docs/README.md#L32-L39](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/docs/README.md#L32-L39), [docs/README.md#L30-L30](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/docs/README.md#L30-L30), [docs/README.md#L3-L5](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/docs/README.md#L3-L5) (`clm_4f5634f937a51529796a4915551cd5cff065b87a01049173f29270017b85b815`)
- [observation/documented] Repository development practice: the root README points contributors to CONTRIBUTING.md for contribution guidance. -- evidence: [README.md#L173-L173](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L173-L173) (`clm_513c84712bc0f64731b3d55104fc2792c1b66a2c56beb489c67af108bd8167c7`)

## skills-patterns (1 claim(s))

- [observation/documented] dora generates integration assets under .dora/docs (SKILL.md, SNIPPET.md) that can be symlinked into .claude/skills/dora or .windsurf/skills/dora and appended to CLAUDE.md or AGENTS.md, enabling a /dora skill reference. -- evidence: [AGENTS.README.md#L88-L90](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L88-L90), [AGENTS.README.md#L110-L110](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L110-L110), [AGENTS.README.md#L458-L461](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L458-L461), [AGENTS.README.md#L476-L478](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L476-L478), [AGENTS.README.md#L79-L82](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L79-L82), [AGENTS.README.md#L75-L75](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L75-L75) (`clm_a513641a3709b6126506161f775b82272758c1c6004d881bdd7d2a6d4d946cb0`)

## interfaces (2 claim(s))

- [observation/documented] All commands output TOON, a compact JSON encoding optimized for LLM token usage, by default; passing --json yields standard JSON. -- evidence: [README.md#L138-L138](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L138-L138) (`clm_37104d1129062a232a57c7f1f11cebc15b81f698e1cc3b9190afb4f21fdce60b`)
- [observation/documented] dora mcp starts an MCP server over stdio, and the README shows registering it with Claude Code via 'claude mcp add --transport stdio dora -- dora mcp'. -- evidence: [README.md#L133-L134](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L133-L134), [README.md#L129-L130](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L129-L130) (`clm_760156e21eee44caf72ee36d291528f44b65817e153f285d4355db1979ee54bb`)

## memory-state (1 claim(s))

- [observation/documented] dora init creates a .dora directory containing config.json (indexer command, ignore patterns, grammar paths), index.scip (raw SCIP protobuf), and dora.db, the SQLite database dora queries. -- evidence: [README.md#L56-L56](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L56-L56), [README.md#L164-L169](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L164-L169) (`clm_885f600a74850f1b837bec893cf6d63953483884f6b797d056f681636bb0ceac`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The documented agent integrations pre-approve dora commands: Claude Code settings allow Bash(dora:*) and Skill(dora), and OpenCode configs set bash permission 'dora *' to allow so commands run without permission prompts. -- evidence: [AGENTS.README.md#L182-L182](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L182-L182), [AGENTS.README.md#L39-L67](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L39-L67), [AGENTS.README.md#L171-L180](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L171-L180), [AGENTS.README.md#L71-L73](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L71-L73) (`clm_ac732d9bb10f785bbae8c01fc456c00e2a0b5a099ffa19fd408e395737257c46`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] dora requires a SCIP indexer for its language; scip-typescript is shown for TypeScript/JavaScript, with pointers to scip-java, rust-analyzer, scip-python, scip-ruby, scip-clang, scip-dotnet, and scip-dart for other languages. -- evidence: [README.md#L39-L39](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L39-L39), [README.md#L43-L44](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L43-L44), [README.md#L46-L46](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L46-L46) (`clm_45d5e65643661d3da840a80567cccfb9c8273c0f6c35adcfb3ea2564d1e12d45`)
- [observation/documented] Tree-sitter analysis commands need a grammar installed, e.g. 'bun add -g tree-sitter-typescript' for TypeScript/JavaScript. -- evidence: [README.md#L96-L98](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L96-L98), [README.md#L94-L94](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L94-L94) (`clm_d5f4a228921bdc03131df538603c408e5c964166680773112d9fe9fefa45e76c`)
- [observation/documented] Besides prebuilt binaries for macOS ARM, macOS Intel, and Linux x64, dora can be installed via npm using Bun ('bun install -g @butttons/dora'). -- evidence: [README.md#L19-L20](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L19-L20), [README.md#L33-L35](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L33-L35), [README.md#L31-L31](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L31-L31), [README.md#L27-L29](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L27-L29), [README.md#L23-L24](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L23-L24) (`clm_8d557d7446b3445b1ad5bb33ee5eb7c151a6c45743052d9ed9b3abbb94b72335`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

