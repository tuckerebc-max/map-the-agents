---
access: public
aliases: []
claim_ids:
- clm_3a4502f9d5bb5014aa1a41046bcf33e64185419b3ca075cdbfad23d58d5e87f4
- clm_5cde1f24e4b81236bf9bb3d9e5e815fd601cbcb5e325cc05dcd459832bc8c489
- clm_5e9a4abb38fbb022c3f0df4f8ac59f39754a0c63292f71b953c29492e9db0671
- clm_b8ae567a59542113674b21e6503fa4e46a708c65bb185c3d19d64cdb2a1d4fbc
- clm_b8b92e706647bc2da089c036db9800cd51594a2cea2e1193fd673d4bb526f71b
- clm_c14e7f109651ea3e49cff611ddc04cb7cde8f774ee49df32be11ebec6d009c7c
- clm_c7582ede32b4a53f771a0d589cdfafe6f08f504879d23c78bba42508b7bc2710
- clm_faca359b6c675c559e5b0a3f9006150f49ad43feb988e541c7580caf4f9c42c3
maturity: draft
page_id: pg_f39055f421635bd6a29f3d2ff541e283
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d14d305b5eb35f26b7be40edd32c652d
title: 233i/ore-code/README.md @ b36da0c05720
updated_at: '2026-09-14T01:58:37Z'
---

# 233i/ore-code/README.md @ b36da0c05720

<!-- rcw:begin owner=source:src_d14d305b5eb35f26b7be40edd32c652d block=evidence -->
- Configuration supports DeepSeek, Mimo, Ark Coding, or custom endpoints via ~/.ore-code/config.toml, with API keys kept in the OS keychain and user-level MCP servers in ~/.ore-code/mcp.json. [@claim:clm_3a4502f9d5bb5014aa1a41046bcf33e64185419b3ca075cdbfad23d58d5e87f4]
- The current release does not read project-level .ore-code/config.toml files; only user-level configuration is supported. [@claim:clm_5cde1f24e4b81236bf9bb3d9e5e815fd601cbcb5e325cc05dcd459832bc8c489]
- The product combines a TypeScript agent runtime, a React/Tauri desktop app, and a Rust OS boundary handling local file, shell, process, Git, keychain, artifact, and MCP operations. [@claim:clm_5e9a4abb38fbb022c3f0df4f8ac59f39754a0c63292f71b953c29492e9db0671]
- The shipped release provides a macOS Apple Silicon installer; the Windows x64 build is listed as pending and must be built separately in a Windows environment. [@claim:clm_b8ae567a59542113674b21e6503fa4e46a708c65bb185c3d19d64cdb2a1d4fbc]
- The workspace includes packages for protocol event schemas, tool specs with approval policy, agent engine with model adapters, JSONL session/artifact state storage, and a scenario-replay harness. [@claim:clm_b8b92e706647bc2da089c036db9800cd51594a2cea2e1193fd673d4bb526f71b]
- Repository development practice: contributors use Node 22 (pinned in .node-version), pnpm 11.x, Rust stable, and Tauri 2 prerequisites; local checks run via pnpm ci:local plus per-package test/typecheck/lint filters. [@claim:clm_c14e7f109651ea3e49cff611ddc04cb7cde8f774ee49df32be11ebec6d009c7c]
- The macOS build is ad-hoc signed and not notarized because the project does not yet use an Apple Developer ID certificate, so macOS may block the app on first launch. [@claim:clm_c7582ede32b4a53f771a0d589cdfafe6f08f504879d23c78bba42508b7bc2710]
- The agent offers context-control features including history compression, context briefing, checkpoint summaries, usage visibility, and provider-aware request shaping for long conversations. [@claim:clm_faca359b6c675c559e5b0a3f9006150f49ad43feb988e541c7580caf4f9c42c3]
<!-- rcw:end owner=source:src_d14d305b5eb35f26b7be40edd32c652d block=evidence -->

## Researcher notes

