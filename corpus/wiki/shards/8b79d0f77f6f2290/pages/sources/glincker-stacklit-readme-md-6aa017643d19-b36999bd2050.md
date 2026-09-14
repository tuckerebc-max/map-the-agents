---
access: public
aliases: []
claim_ids:
- clm_0e2a1964afcb4b5aa046953c2967232f0803be39876027c2439185f7ca4602fb
- clm_2626bc2418e005db4e9f95bd5787b4b043181c82e8a7b395362841e15306df8b
- clm_409d9a1db29f383cf0fcb69f7efdb157981e3a945b2e87694d4d6bc21dc30101
- clm_570df8c567277466bfacf94281856fc758f41add916cc9bc9751e9106b47c222
- clm_73e0df5396557e48ea46a583128de4956420536473b664819cae637c4b2cf009
- clm_8a0c0265295844950403b6c8ef0dcb495e96d5939b66fa5e5bb25232329ffa84
- clm_8aa16b80fbc4bfdedbc23ba19a6292625e59df6aee01b044aec180897b3c53f7
- clm_92ba88bd8b7a702ef4b698c97eb2ecb65d8cdc8307f22e3d1131aa6bd495651c
- clm_c49f76ddf667ab2908195206cdaaf5748a146ccd92b56575a9728b1a25574c8e
- clm_cd86994fb8551dfd7f34e13b3699f06b3196b97b41bcf6c995982489aea6ec8f
- clm_deaf18f278013b9a325da39d101cc09bb3f2258e68f76c4b254e37b1c9f40034
- clm_ec385cc9147552863657ffb7a9e6331122dcc455e280cfa17674ddc74db1c51f
- clm_ec454bb52b833e58bc0d038310e51ebb79eceadce05fa7062144428a1a769764
- clm_ffebf1331684b7e0c157c670eab019069e7f1926dc095ac6c05c1a31a5bd1130
maturity: draft
page_id: pg_2f433441b28650ec97dab36999bd2050
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fd8ace5df19e5c4688f8b186f29b8c9e
title: glincker/stacklit/README.md @ 6aa017643d19
updated_at: '2026-09-14T03:53:45Z'
---

# glincker/stacklit/README.md @ 6aa017643d19

<!-- rcw:begin owner=source:src_fd8ace5df19e5c4688f8b186f29b8c9e block=evidence -->
- Stacklit targets teams using AI coding agents on larger codebases, providing a committable structured index so agents avoid rebuilding a mental model of the repo each session. [@claim:clm_0e2a1964afcb4b5aa046953c2967232f0803be39876027c2439185f7ca4602fb]
- Parsing uses tree-sitter to extract structure for 11 languages (Go, TypeScript/JS, Python, Rust, Java, C#, Ruby, PHP, Kotlin, Swift, C/C++); other languages fall back to line count and language detection. [@claim:clm_2626bc2418e005db4e9f95bd5787b4b043181c82e8a7b395362841e15306df8b]
- The MCP server started via 'stacklit serve' exposes seven tools: get_overview, get_module, find_module, list_modules, get_dependencies, get_hot_files, and get_hints. [@claim:clm_409d9a1db29f383cf0fcb69f7efdb157981e3a945b2e87694d4d6bc21dc30101]
- Parsing runs locally and no code is sent anywhere unless the optional --summary flag is used, which calls the Claude API. [@claim:clm_570df8c567277466bfacf94281856fc758f41add916cc9bc9751e9106b47c222]
- 'stacklit setup' auto-detects Claude Code, Cursor, and Aider, injecting a ~250-token codebase map into each tool's config, configuring MCP integration, and installing a git hook to refresh the map on commits. [@claim:clm_73e0df5396557e48ea46a583128de4956420536473b664819cae637c4b2cf009]
- The README's token-efficiency table reports index sizes for real projects, but the planned agent benchmark (tool calls, tokens, correctness) contains only placeholder XX values, so no completed agent-performance evaluation appears in this snapshot. [@claim:clm_8a0c0265295844950403b6c8ef0dcb495e96d5939b66fa5e5bb25232329ffa84]
- The project is written in Go and is installable via npx, npm global install, 'go install github.com/glincker/stacklit/cmd/stacklit@latest', or prebuilt binaries for macOS, Linux, and Windows. [@claim:clm_8aa16b80fbc4bfdedbc23ba19a6292625e59df6aee01b044aec180897b3c53f7]
- stacklit.json contains per-module entries with purpose, file/line counts, exports, depends_on, and activity, plus hints such as where to add features and the test command. [@claim:clm_92ba88bd8b7a702ef4b698c97eb2ecb65d8cdc8307f22e3d1131aa6bd495651c]
- The visual map opened by 'stacklit view' offers four views: a force-directed dependency graph, a collapsible tree, a sortable searchable table, and a top-down dependency flow. [@claim:clm_c49f76ddf667ab2908195206cdaaf5748a146ccd92b56575a9728b1a25574c8e]
- The tool is designed so AI agents read a small (~250-token) navigation map or stacklit.json instead of scanning many files, which the README claims cuts exploration from hundreds of thousands of tokens to a few thousand. [@claim:clm_cd86994fb8551dfd7f34e13b3699f06b3196b97b41bcf6c995982489aea6ec8f]
- Languages outside the tree-sitter list get only basic support (line count plus language detection), though the module map, dependency graph, and git activity still work for them. [@claim:clm_deaf18f278013b9a325da39d101cc09bb3f2258e68f76c4b254e37b1c9f40034]
- Running stacklit init produces three artifacts: stacklit.json (committable index), DEPENDENCIES.md (Mermaid diagram, committable), and stacklit.html (interactive map, gitignored and regenerable). [@claim:clm_ec385cc9147552863657ffb7a9e6331122dcc455e280cfa17674ddc74db1c51f]
- The CLI exposes commands including init (with --hook and --multi flags), generate, view, diff, serve, derive, export, and setup with per-tool variants for claude and cursor. [@claim:clm_ec454bb52b833e58bc0d038310e51ebb79eceadce05fa7062144428a1a769764]
- Repository development practice: contributors build with 'make build' and run all tests with 'make test', per the README contributing section. [@claim:clm_ffebf1331684b7e0c157c670eab019069e7f1926dc095ac6c05c1a31a5bd1130]
<!-- rcw:end owner=source:src_fd8ace5df19e5c4688f8b186f29b8c9e block=evidence -->

## Researcher notes

