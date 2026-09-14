---
access: public
aliases: []
claim_ids:
- clm_11c8f0bf4cd9c5ed0c5b817f74ca77c6f4b0e3e065756f756420f7b88468675b
- clm_71e59a435c3f9c1e1adbb44c94e3aa932622c1fd0b8e50b8e76ca57f290e5b0c
- clm_884b8370b306205f7a65ff15e4d6907816b87a3bd3a42c74d15748474e147382
- clm_8a2051265d85dda7cc4eadb003032ee852168005a1996830163403673858ecd9
- clm_a08034b0c94e5bdfa336b43231f768fd2bf16d3e40ae7cb3279f97816e295817
- clm_aac7a47abf47c581964215b7ac990254f9a0379e4631e7b5c4114971886a05ef
- clm_c2cc43472c3d2aeb849b67cd1af27408b04cb7b7f998a23c228a9bbaef480b44
- clm_d44257328f992eaf2466c90d6ea982d1d2f1d151f820b74948c6c23f3ed4d06c
- clm_d7be599558f7b69a28305799d16a29e259bb599963ba48fe601918e12f896695
maturity: draft
page_id: pg_a247e54ced3454caadfe71ac71b40a07
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0e2033bc46fd59d9bb4b1b888ce6b92c
title: GCWing/OpenBitFun/CONTRIBUTING_CN.md @ 32b20c5b291d
updated_at: '2026-09-14T03:52:38Z'
---

# GCWing/OpenBitFun/CONTRIBUTING_CN.md @ 32b20c5b291d

<!-- rcw:begin owner=source:src_0e2033bc46fd59d9bb4b1b888ce6b92c block=evidence -->
- The architecture keeps product logic platform-independent and exposes capabilities through platform adapter layers; shared core must avoid host APIs like Tauri's AppHandle in favor of shared abstractions. [@claim:clm_11c8f0bf4cd9c5ed0c5b817f74ca77c6f4b0e3e065756f756420f7b88468675b]
- Repository development practice: verification scope is owner-determined; contributors pick the narrowest focused command near the change and leave broad builds and platform matrices to CI. [@claim:clm_71e59a435c3f9c1e1adbb44c94e3aa932622c1fd0b8e50b8e76ca57f290e5b0c]
- Repository development practice: contributors run `pnpm install` and `pnpm run desktop:dev` for full hot reload (Vite HMR plus automatic Rust rebuild), with a lighter `desktop:preview:debug` mode that reuses a prebuilt binary. [@claim:clm_884b8370b306205f7a65ff15e4d6907816b87a3bd3a42c74d15748474e147382]
- Repository development practice: a repository object-size check rejects Git objects over 5 MiB, including files added and later deleted in intermediate commits, with a script available to check before pushing. [@claim:clm_8a2051265d85dda7cc4eadb003032ee852168005a1996830163403673858ecd9]
- Repository development practice: logs must be English-only without emoji, and Tauri commands use snake_case names with structured request parameters passed from TypeScript. [@claim:clm_a08034b0c94e5bdfa336b43231f768fd2bf16d3e40ae7cb3279f97816e295817]
- Repository development practice: a build prerequisites checker (`pnpm run check:build-prereqs`) diagnoses missing node_modules, mobile-web dist output, or sherpa-onnx libraries, with an optional --fix mode. [@claim:clm_aac7a47abf47c581964215b7ac990254f9a0379e4631e7b5c4114971886a05ef]
- The sherpa-onnx prebuilt library is downloaded from GitHub at build time by sherpa-onnx-sys, with a `SHERPA_ONNX_LIB_DIR` fallback to a local prebuilt copy when downloads fail. [@claim:clm_c2cc43472c3d2aeb849b67cd1af27408b04cb7b7f998a23c228a9bbaef480b44]
- Running from source requires Node.js 22.12+, pnpm 10.15.0, the Rust toolchain, and Tauri prerequisites; the project is a Rust workspace with a React/TypeScript frontend. [@claim:clm_d44257328f992eaf2466c90d6ea982d1d2f1d151f820b74948c6c23f3ed4d06c]
- Repository development practice: PRs go directly to the `main` branch, should use Conventional Commits-style titles, stay small and focused, and AI-assisted output must be declared with its testing level. [@claim:clm_d7be599558f7b69a28305799d16a29e259bb599963ba48fe601918e12f896695]
<!-- rcw:end owner=source:src_0e2033bc46fd59d9bb4b1b888ce6b92c block=evidence -->

## Researcher notes

