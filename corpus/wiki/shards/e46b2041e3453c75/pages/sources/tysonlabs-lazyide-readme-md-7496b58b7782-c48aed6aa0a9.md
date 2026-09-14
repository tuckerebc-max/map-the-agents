---
access: public
aliases: []
claim_ids:
- clm_4a1f7bdc44b030bb0cd5e85635d43795e9c9ed65c1f2c68c1aae310c0d21ad06
- clm_76ce59ad7c6c56f99dc1ece0cff836f147134b3309c8c8d2e450d2703c3aaf59
- clm_93cb96735cba6cc5868e325c1714aa64e9a1e3fc50d962eb9535c1154a4bdb3e
- clm_c1dd30162aac2892624a2be780d1a6c703c94ff38c3ddbf1730af1a7a94ba2a5
- clm_d7ef6ef6e84a4172b22e75b24420486d37da5349677f73d5f43fb7dc89796ef8
maturity: draft
page_id: pg_6c1b0b75e74a54309571c48aed6aa0a9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bd8d8c1fd54e52c18c60ffe852826b08
title: TysonLabs/lazyide/README.md @ 7496b58b7782
updated_at: '2026-09-14T04:28:48Z'
---

# TysonLabs/lazyide/README.md @ 7496b58b7782

<!-- rcw:begin owner=source:src_bd8d8c1fd54e52c18c60ffe852826b08 block=evidence -->
- lazyide is a lightweight terminal IDE written in Rust with ratatui, shipped as a single binary with file tree, tabbed editing, LSP, syntax highlighting, folding, git integration, project search, 32 themes, and customizable keybindings. [@claim:clm_4a1f7bdc44b030bb0cd5e85635d43795e9c9ed65c1f2c68c1aae310c0d21ad06]
- Optional external tools are rust-analyzer (LSP completions/diagnostics/go-to-definition), ripgrep (project-wide search), and git (branch display, gutter markers); the system clipboard is accessed via the arboard crate. [@claim:clm_76ce59ad7c6c56f99dc1ece0cff836f147134b3309c8c8d2e450d2703c3aaf59]
- Repository development practice: contributors build with cargo (build/run/test), tests are inline `#[cfg(test)]` modules (about 300 tests), and CONTRIBUTING.md asks for an issue before large changes, minimal diffs, and a PR workflow. [@claim:clm_93cb96735cba6cc5868e325c1714aa64e9a1e3fc50d962eb9535c1154a4bdb3e]
- The product exposes a `--setup` CLI flag that detects and installs optional tools (rust-analyzer, ripgrep), and is run as `lazyide` (or `cargo run -- /path/to/project`) inside a terminal. [@claim:clm_c1dd30162aac2892624a2be780d1a6c703c94ff38c3ddbf1730af1a7a94ba2a5]
- Keybindings are data-driven: ~40 actions in a `KeyAction` enum with defaults in `KeyBindings::defaults()`, user overrides loaded from `~/.config/lazyide/keybinds.json`, and a two-pass lookup that first requires exact modifier match then falls back to a Shift-lenient match. [@claim:clm_d7ef6ef6e84a4172b22e75b24420486d37da5349677f73d5f43fb7dc89796ef8]
<!-- rcw:end owner=source:src_bd8d8c1fd54e52c18c60ffe852826b08 block=evidence -->

## Researcher notes

