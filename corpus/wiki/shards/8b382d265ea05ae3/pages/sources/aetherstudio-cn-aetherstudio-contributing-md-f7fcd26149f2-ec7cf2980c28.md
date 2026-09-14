---
access: public
aliases: []
claim_ids:
- clm_a6d18f4ce77c2fa6edf69eb5426a5fe440bf8fc20586030948f1c4233057af85
- clm_efc3db0ad90748a6fc14286ab0201f689380daf83b294216402cae9af2185a3c
maturity: draft
page_id: pg_18b6b3641c6e5f9da986ec7cf2980c28
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4d237f01b686541eb87386cb5f8a0e86
title: aetherstudio-cn/AetherStudio/CONTRIBUTING.md @ f7fcd26149f2
updated_at: '2026-09-14T01:29:58Z'
---

# aetherstudio-cn/AetherStudio/CONTRIBUTING.md @ f7fcd26149f2

<!-- rcw:begin owner=source:src_4d237f01b686541eb87386cb5f8a0e86 block=evidence -->
- Repository development practice: a pre-push checklist mandates cargo fmt --check, cargo check -p aether-win32, and cargo test --workspace --lib --no-fail-fast; the README also documents workspace tests run with CARGO_INCREMENTAL=0 to avoid an ICE, clippy with -D warnings, a GUI smoke test script, and a coverage script. [@claim:clm_a6d18f4ce77c2fa6edf69eb5426a5fe440bf8fc20586030948f1c4233057af85]
- Repository development practice: CONTRIBUTING.md requires external contributors to use a fork workflow, branch from dev (temp/ or fix/ prefixes), target PRs at dev rather than main, and follow a <type>(<scope>): <description> commit format with types like feat, fix, perf, and refactor. [@claim:clm_efc3db0ad90748a6fc14286ab0201f689380daf83b294216402cae9af2185a3c]
<!-- rcw:end owner=source:src_4d237f01b686541eb87386cb5f8a0e86 block=evidence -->

## Researcher notes

