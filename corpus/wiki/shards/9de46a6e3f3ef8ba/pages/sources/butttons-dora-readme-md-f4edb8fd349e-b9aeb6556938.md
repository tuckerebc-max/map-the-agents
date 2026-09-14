---
access: public
aliases: []
claim_ids:
- clm_37104d1129062a232a57c7f1f11cebc15b81f698e1cc3b9190afb4f21fdce60b
- clm_45d5e65643661d3da840a80567cccfb9c8273c0f6c35adcfb3ea2564d1e12d45
- clm_513c84712bc0f64731b3d55104fc2792c1b66a2c56beb489c67af108bd8167c7
- clm_760156e21eee44caf72ee36d291528f44b65817e153f285d4355db1979ee54bb
- clm_885f600a74850f1b837bec893cf6d63953483884f6b797d056f681636bb0ceac
- clm_8d557d7446b3445b1ad5bb33ee5eb7c151a6c45743052d9ed9b3abbb94b72335
- clm_8e919bf4b9d9b9ea868e5d50e32d0d09af50c686a99106ea5dde81f9ab303a42
- clm_9d28b22943393267a15dc812adabd93cf55e44a24e944f47405e9a0b0ffca1b9
- clm_d5f4a228921bdc03131df538603c408e5c964166680773112d9fe9fefa45e76c
- clm_fdae466263ac23313f2e20b0c854cacdb6f206eff1a5bab5d3c94bd4c3887ef0
maturity: draft
page_id: pg_10d769f14dca59c79fe6b9aeb6556938
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_10833c0aa20554bd99c20c03e8eb03ea
title: butttons/dora/README.md @ f4edb8fd349e
updated_at: '2026-09-14T03:39:38Z'
---

# butttons/dora/README.md @ f4edb8fd349e

<!-- rcw:begin owner=source:src_10833c0aa20554bd99c20c03e8eb03ea block=evidence -->
- All commands output TOON, a compact JSON encoding optimized for LLM token usage, by default; passing --json yields standard JSON. [@claim:clm_37104d1129062a232a57c7f1f11cebc15b81f698e1cc3b9190afb4f21fdce60b]
- dora requires a SCIP indexer for its language; scip-typescript is shown for TypeScript/JavaScript, with pointers to scip-java, rust-analyzer, scip-python, scip-ruby, scip-clang, scip-dotnet, and scip-dart for other languages. [@claim:clm_45d5e65643661d3da840a80567cccfb9c8273c0f6c35adcfb3ea2564d1e12d45]
- Repository development practice: the root README points contributors to CONTRIBUTING.md for contribution guidance. [@claim:clm_513c84712bc0f64731b3d55104fc2792c1b66a2c56beb489c67af108bd8167c7]
- dora mcp starts an MCP server over stdio, and the README shows registering it with Claude Code via 'claude mcp add --transport stdio dora -- dora mcp'. [@claim:clm_760156e21eee44caf72ee36d291528f44b65817e153f285d4355db1979ee54bb]
- dora init creates a .dora directory containing config.json (indexer command, ignore patterns, grammar paths), index.scip (raw SCIP protobuf), and dora.db, the SQLite database dora queries. [@claim:clm_885f600a74850f1b837bec893cf6d63953483884f6b797d056f681636bb0ceac]
- Besides prebuilt binaries for macOS ARM, macOS Intel, and Linux x64, dora can be installed via npm using Bun ('bun install -g @butttons/dora'). [@claim:clm_8d557d7446b3445b1ad5bb33ee5eb7c151a6c45743052d9ed9b3abbb94b72335]
- dora is a CLI that turns a SCIP index into a queryable SQLite database, giving AI agents structured answers about a codebase instead of grepping files and reading imports. [@claim:clm_8e919bf4b9d9b9ea868e5d50e32d0d09af50c686a99106ea5dde81f9ab303a42]
- The tool has two layers: a SCIP layer that runs a configured indexer, parses the resulting protobuf, and loads symbols, references, and file dependencies into SQLite; and a tree-sitter layer that parses source on demand via WebAssembly grammars for things SCIP doesn't cover. [@claim:clm_9d28b22943393267a15dc812adabd93cf55e44a24e944f47405e9a0b0ffca1b9]
- Tree-sitter analysis commands need a grammar installed, e.g. 'bun add -g tree-sitter-typescript' for TypeScript/JavaScript. [@claim:clm_d5f4a228921bdc03131df538603c408e5c964166680773112d9fe9fefa45e76c]
- The SQLite schema stores denormalized counts (symbol_count, dependency_count, dependent_count, reference_count) so most queries are index lookups rather than aggregations. [@claim:clm_fdae466263ac23313f2e20b0c854cacdb6f206eff1a5bab5d3c94bd4c3887ef0]
<!-- rcw:end owner=source:src_10833c0aa20554bd99c20c03e8eb03ea block=evidence -->

## Researcher notes

