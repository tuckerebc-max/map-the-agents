---
access: public
aliases: []
claim_ids:
- clm_11c8f0bf4cd9c5ed0c5b817f74ca77c6f4b0e3e065756f756420f7b88468675b
- clm_44e437980b43550add7d25f9c2b5f81bd5668e9b6f4d0f381b46f8ec3ab74f6d
- clm_71e59a435c3f9c1e1adbb44c94e3aa932622c1fd0b8e50b8e76ca57f290e5b0c
- clm_884b8370b306205f7a65ff15e4d6907816b87a3bd3a42c74d15748474e147382
- clm_94a5e729008de8450df67e98a4127ed817354a8284e431506314a3fc00ff3ded
- clm_a08034b0c94e5bdfa336b43231f768fd2bf16d3e40ae7cb3279f97816e295817
- clm_d44257328f992eaf2466c90d6ea982d1d2f1d151f820b74948c6c23f3ed4d06c
- clm_dadecfda4d2a15e1bc428c991384154601d37ce0758c59e36bf5d56eaaef43a8
maturity: draft
page_id: pg_fa37429daf9b5502a23d1b1639b7f384
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_224550d58ffb5ceda3bd9e91548547b5
title: GCWing/OpenBitFun/AGENTS-CN.md @ 32b20c5b291d
updated_at: '2026-09-14T03:52:38Z'
---

# GCWing/OpenBitFun/AGENTS-CN.md @ 32b20c5b291d

<!-- rcw:begin owner=source:src_224550d58ffb5ceda3bd9e91548547b5 block=evidence -->
- The architecture keeps product logic platform-independent and exposes capabilities through platform adapter layers; shared core must avoid host APIs like Tauri's AppHandle in favor of shared abstractions. [@claim:clm_11c8f0bf4cd9c5ed0c5b817f74ca77c6f4b0e3e065756f756420f7b88468675b]
- Remote scenarios (remote workspaces, remote control, peer-device mode, and detached task dispatch) are treated as first-class design targets, with rules requiring explicit unsupported states and reconnect-tolerant, resumable behavior. [@claim:clm_44e437980b43550add7d25f9c2b5f81bd5668e9b6f4d0f381b46f8ec3ab74f6d]
- Repository development practice: verification scope is owner-determined; contributors pick the narrowest focused command near the change and leave broad builds and platform matrices to CI. [@claim:clm_71e59a435c3f9c1e1adbb44c94e3aa932622c1fd0b8e50b8e76ca57f290e5b0c]
- Repository development practice: contributors run `pnpm install` and `pnpm run desktop:dev` for full hot reload (Vite HMR plus automatic Rust rebuild), with a lighter `desktop:preview:debug` mode that reuses a prebuilt binary. [@claim:clm_884b8370b306205f7a65ff15e4d6907816b87a3bd3a42c74d15748474e147382]
- Repository development practice: Rust files should be formatted with `pnpm run fmt:rs` targeting only changed or staged files, and repo-level checks include hygiene, GitHub config, and core-boundaries scripts. [@claim:clm_94a5e729008de8450df67e98a4127ed817354a8284e431506314a3fc00ff3ded]
- Repository development practice: logs must be English-only without emoji, and Tauri commands use snake_case names with structured request parameters passed from TypeScript. [@claim:clm_a08034b0c94e5bdfa336b43231f768fd2bf16d3e40ae7cb3279f97816e295817]
- Running from source requires Node.js 22.12+, pnpm 10.15.0, the Rust toolchain, and Tauri prerequisites; the project is a Rust workspace with a React/TypeScript frontend. [@claim:clm_d44257328f992eaf2466c90d6ea982d1d2f1d151f820b74948c6c23f3ed4d06c]
- Native user Hooks implement the Codex Hook contract, with the portable hook engine in `openbitfun-agent-runtime::native_hooks` and hooks from user config, plugins, or built-ins registered in a shared HookRegistry. [@claim:clm_dadecfda4d2a15e1bc428c991384154601d37ce0758c59e36bf5d56eaaef43a8]
<!-- rcw:end owner=source:src_224550d58ffb5ceda3bd9e91548547b5 block=evidence -->

## Researcher notes

