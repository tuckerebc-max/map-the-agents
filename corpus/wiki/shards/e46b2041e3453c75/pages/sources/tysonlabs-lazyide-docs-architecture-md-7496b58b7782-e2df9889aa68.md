---
access: public
aliases: []
claim_ids:
- clm_05fb9e66743f1c5906fefab6582e25832e4ffdffc4ce4e6aaf9ef9ab2b5a2091
- clm_2d39f520e0eba27be3e961603fd9120c421afe83b3a104584ccd1b59f4d64203
- clm_2eb9ddae7c129961a65df2c7a09a36fab51bea743278b4abe55bf9a353f3b43d
- clm_5db2b1aa864e46049c5cd5cc81ec371f4c8d4ef36c5df686481a792b8d28b4a2
- clm_93cb96735cba6cc5868e325c1714aa64e9a1e3fc50d962eb9535c1154a4bdb3e
- clm_d7ef6ef6e84a4172b22e75b24420486d37da5349677f73d5f43fb7dc89796ef8
- clm_db15d92c7985ee8ad9593d82e6b532eda70e1a24110b9012d272b23353c825f4
- clm_f4e57c4cacd889b20b2c6058efadbf6b1bd6d6746988a679ad742e6c6299bf56
maturity: draft
page_id: pg_27364faf58175dada829e2df9889aa68
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9d6b58263dc85c3d8d28ea01e3d379a9
title: TysonLabs/lazyide/docs/ARCHITECTURE.md @ 7496b58b7782
updated_at: '2026-09-14T04:28:48Z'
---

# TysonLabs/lazyide/docs/ARCHITECTURE.md @ 7496b58b7782

<!-- rcw:begin owner=source:src_9d6b58263dc85c3d8d28ea01e3d379a9 block=evidence -->
- Two editor panes are implemented via a state-swap: the focused pane's fields live on `App` and the other pane in `App::other_pane`, so existing active-tab code paths need no pane awareness. [@claim:clm_05fb9e66743f1c5906fefab6582e25832e4ffdffc4ce4e6aaf9ef9ab2b5a2091]
- Git integration shells out to the `git` binary rather than using libgit2, using commands like `git rev-parse`, `git status --porcelain -z`, and `git diff HEAD` for branch, status, and line-level diff data. [@claim:clm_2d39f520e0eba27be3e961603fd9120c421afe83b3a104584ccd1b59f4d64203]
- All application state lives in a single `App` struct with methods split across `app/*.rs` impl blocks; UI rendering functions take `&App` and never mutate state, which happens only in `app/` methods. [@claim:clm_2eb9ddae7c129961a65df2c7a09a36fab51bea743278b4abe55bf9a353f3b43d]
- Syntax highlighting is line-at-a-time keyword/string/comment matching with bracket depth tracking, not AST-based, covering 11 language families detected by file extension. [@claim:clm_5db2b1aa864e46049c5cd5cc81ec371f4c8d4ef36c5df686481a792b8d28b4a2]
- Repository development practice: contributors build with cargo (build/run/test), tests are inline `#[cfg(test)]` modules (about 300 tests), and CONTRIBUTING.md asks for an issue before large changes, minimal diffs, and a PR workflow. [@claim:clm_93cb96735cba6cc5868e325c1714aa64e9a1e3fc50d962eb9535c1154a4bdb3e]
- Keybindings are data-driven: ~40 actions in a `KeyAction` enum with defaults in `KeyBindings::defaults()`, user overrides loaded from `~/.config/lazyide/keybinds.json`, and a two-pass lookup that first requires exact modifier match then falls back to a Shift-lenient match. [@claim:clm_d7ef6ef6e84a4172b22e75b24420486d37da5349677f73d5f43fb7dc89796ef8]
- LSP support is implemented by spawning a rust-analyzer child process over JSON-RPC, with a background stdout reader thread and per-frame polling that matches responses to pending completion/definition requests. [@claim:clm_db15d92c7985ee8ad9593d82e6b532eda70e1a24110b9012d272b23353c825f4]
- The main event loop polls LSP responses, a debounced (120ms) file watcher, and autosave (every 2s) each iteration, draws a frame, then waits up to 100ms for terminal key/mouse events. [@claim:clm_f4e57c4cacd889b20b2c6058efadbf6b1bd6d6746988a679ad742e6c6299bf56]
<!-- rcw:end owner=source:src_9d6b58263dc85c3d8d28ea01e3d379a9 block=evidence -->

## Researcher notes

