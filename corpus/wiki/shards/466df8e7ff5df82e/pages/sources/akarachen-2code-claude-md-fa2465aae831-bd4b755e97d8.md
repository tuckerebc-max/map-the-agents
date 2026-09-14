---
access: public
aliases: []
claim_ids:
- clm_487ea6b661c068529ffed753d17ab4d6fe244fb26379b816f662de479a6821cc
- clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e
- clm_e0b5edb52d7116d28f2531f6c25b47bffc428b7179bd1739c482e43f3986fa93
- clm_e75d81ee3930dbc7e1718383f453c75b8d8892881b94f43ce4102ec24365bc24
maturity: draft
page_id: pg_a40c591dd2105d00a521bd4b755e97d8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_882fb090ad7f51bcb79b7a703f562644
title: AkaraChen/2code/CLAUDE.md @ fa2465aae831
updated_at: '2026-09-14T03:32:48Z'
---

# AkaraChen/2code/CLAUDE.md @ fa2465aae831

<!-- rcw:begin owner=source:src_882fb090ad7f51bcb79b7a703f562644 block=evidence -->
- The Rust backend is layered into handler (Tauri command entry points), service (business logic), repo (Diesel CRUD), infra (DB, PTY, git, watcher), and model crates. [@claim:clm_487ea6b661c068529ffed753d17ab4d6fe244fb26379b816f662de479a6821cc]
- Repository development practice: contributors add Tauri commands in handler/*.rs, register them in lib.rs, then run cargo tauri-typegen generate; Rust tests run via cargo test with in-memory SQLite, and CI includes a Tauri smoke test on ubuntu-24.04 with xvfb-run. [@claim:clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e]
- The frontend detects coding-agent state (running/waiting/idle) from xterm screen text, OSC titles, and OSC progress, with per-agent rule manifests; waiting status can trigger a system sound. [@claim:clm_e0b5edb52d7116d28f2531f6c25b47bffc428b7179bd1739c482e43f3986fa93]
- Profiles create isolated branch workspaces via git worktree add under ~/.2code/workspace/{profile_id}, running a setup_script from 2code.json on creation and teardown_script plus worktree/branch removal on deletion. [@claim:clm_e75d81ee3930dbc7e1718383f453c75b8d8892881b94f43ce4102ec24365bc24]
<!-- rcw:end owner=source:src_882fb090ad7f51bcb79b7a703f562644 block=evidence -->

## Researcher notes

