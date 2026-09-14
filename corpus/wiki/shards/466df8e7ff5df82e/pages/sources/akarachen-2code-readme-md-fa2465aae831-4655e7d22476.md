---
access: public
aliases: []
claim_ids:
- clm_1773df8e4126991bc781f36452a315c1ba3434ef7c5e3b7b4f7032cd16ecc3fc
- clm_487ea6b661c068529ffed753d17ab4d6fe244fb26379b816f662de479a6821cc
- clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e
- clm_af0975d7da28362cf9f2612c0688712568e3b721a18908586dc37dab3d5bd3de
- clm_e0b5edb52d7116d28f2531f6c25b47bffc428b7179bd1739c482e43f3986fa93
- clm_e75d81ee3930dbc7e1718383f453c75b8d8892881b94f43ce4102ec24365bc24
- clm_f5cf8800e6b7e498dc4d3a3efecfdb95d5898bbc7b3248f52ee84080ead95e0d
maturity: draft
page_id: pg_c1df077bfd0059a492bc4655e7d22476
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a0a3572ceb8c5bf9ad50a7faadfb9e64
title: AkaraChen/2code/README.md @ fa2465aae831
updated_at: '2026-09-14T03:32:48Z'
---

# AkaraChen/2code/README.md @ fa2465aae831

<!-- rcw:begin owner=source:src_a0a3572ceb8c5bf9ad50a7faadfb9e64 block=evidence -->
- Building and developing the app requires Bun, a stable Rust toolchain, Tauri 2 prerequisites, just, and fama on PATH for TypeScript formatting. [@claim:clm_1773df8e4126991bc781f36452a315c1ba3434ef7c5e3b7b4f7032cd16ecc3fc]
- The Rust backend is layered into handler (Tauri command entry points), service (business logic), repo (Diesel CRUD), infra (DB, PTY, git, watcher), and model crates. [@claim:clm_487ea6b661c068529ffed753d17ab4d6fe244fb26379b816f662de479a6821cc]
- Repository development practice: contributors add Tauri commands in handler/*.rs, register them in lib.rs, then run cargo tauri-typegen generate; Rust tests run via cargo test with in-memory SQLite, and CI includes a Tauri smoke test on ubuntu-24.04 with xvfb-run. [@claim:clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e]
- The project is early and under active construction; macOS is the primary supported platform while Windows and Linux builds are experimental. [@claim:clm_af0975d7da28362cf9f2612c0688712568e3b721a18908586dc37dab3d5bd3de]
- The frontend detects coding-agent state (running/waiting/idle) from xterm screen text, OSC titles, and OSC progress, with per-agent rule manifests; waiting status can trigger a system sound. [@claim:clm_e0b5edb52d7116d28f2531f6c25b47bffc428b7179bd1739c482e43f3986fa93]
- Profiles create isolated branch workspaces via git worktree add under ~/.2code/workspace/{profile_id}, running a setup_script from 2code.json on creation and teardown_script plus worktree/branch removal on deletion. [@claim:clm_e75d81ee3930dbc7e1718383f453c75b8d8892881b94f43ce4102ec24365bc24]
- The app is a Tauri 2 desktop shell with a React 19 + TypeScript + Vite frontend, Zustand/Immer client state, TanStack Query server state, and a Rust workspace backend with SQLite via Diesel. [@claim:clm_f5cf8800e6b7e498dc4d3a3efecfdb95d5898bbc7b3248f52ee84080ead95e0d]
<!-- rcw:end owner=source:src_a0a3572ceb8c5bf9ad50a7faadfb9e64 block=evidence -->

## Researcher notes

