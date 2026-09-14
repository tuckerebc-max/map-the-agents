# tysonlabs/lazyide -- full detail

[Back to orientation](lazyide.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tysonlabs/lazyide/7496b58b7782dd7d0534c0db29bc61b3171f0df2/f12e7adbb1301325.json](../../../wiki/dossiers/tysonlabs/lazyide/7496b58b7782dd7d0534c0db29bc61b3171f0df2/f12e7adbb1301325.json)

## specifications (1 claim(s))

- [observation/documented] lazyide is a lightweight terminal IDE written in Rust with ratatui, shipped as a single binary with file tree, tabbed editing, LSP, syntax highlighting, folding, git integration, project search, 32 themes, and customizable keybindings. -- evidence: [README.md#L8-L8](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L8-L8) (`clm_4a1f7bdc44b030bb0cd5e85635d43795e9c9ed65c1f2c68c1aae310c0d21ad06`)

## components (2 claim(s))

- [observation/documented] LSP support is implemented by spawning a rust-analyzer child process over JSON-RPC, with a background stdout reader thread and per-frame polling that matches responses to pending completion/definition requests. -- evidence: [docs/ARCHITECTURE.md#L122-L122](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L122-L122), [docs/ARCHITECTURE.md#L124-L127](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L124-L127) (`clm_db15d92c7985ee8ad9593d82e6b532eda70e1a24110b9012d272b23353c825f4`)
- [observation/documented] Git integration shells out to the `git` binary rather than using libgit2, using commands like `git rev-parse`, `git status --porcelain -z`, and `git diff HEAD` for branch, status, and line-level diff data. -- evidence: [docs/ARCHITECTURE.md#L152-L152](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L152-L152), [docs/ARCHITECTURE.md#L154-L159](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L154-L159) (`clm_2d39f520e0eba27be3e961603fd9120c421afe83b3a104584ccd1b59f4d64203`)

## design-choices (3 claim(s))

- [observation/documented] All application state lives in a single `App` struct with methods split across `app/*.rs` impl blocks; UI rendering functions take `&App` and never mutate state, which happens only in `app/` methods. -- evidence: [docs/ARCHITECTURE.md#L42-L42](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L42-L42), [docs/ARCHITECTURE.md#L46-L46](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L46-L46) (`clm_2eb9ddae7c129961a65df2c7a09a36fab51bea743278b4abe55bf9a353f3b43d`)
- [observation/documented] Two editor panes are implemented via a state-swap: the focused pane's fields live on `App` and the other pane in `App::other_pane`, so existing active-tab code paths need no pane awareness. -- evidence: [docs/ARCHITECTURE.md#L44-L44](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L44-L44) (`clm_05fb9e66743f1c5906fefab6582e25832e4ffdffc4ce4e6aaf9ef9ab2b5a2091`)
- [observation/documented] Syntax highlighting is line-at-a-time keyword/string/comment matching with bracket depth tracking, not AST-based, covering 11 language families detected by file extension. -- evidence: [docs/ARCHITECTURE.md#L142-L142](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L142-L142) (`clm_5db2b1aa864e46049c5cd5cc81ec371f4c8d4ef36c5df686481a792b8d28b4a2`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors build with cargo (build/run/test), tests are inline `#[cfg(test)]` modules (about 300 tests), and CONTRIBUTING.md asks for an issue before large changes, minimal diffs, and a PR workflow. -- evidence: [docs/ARCHITECTURE.md#L163-L163](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L163-L163), [docs/ARCHITECTURE.md#L171-L171](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L171-L171), [README.md#L191-L195](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L191-L195), [CONTRIBUTING.md#L115-L119](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CONTRIBUTING.md#L115-L119) (`clm_93cb96735cba6cc5868e325c1714aa64e9a1e3fc50d962eb9535c1154a4bdb3e`)
- [observation/documented] Repository development practice: CLAUDE.md guides Claude Code when working in the repo, stating the project should stay minimal, avoid heavy abstractions, and noting Rust 2024 edition with no custom build scripts or CI/CD. -- evidence: [CLAUDE.md#L7-L7](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L7-L7), [CLAUDE.md#L18-L18](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L18-L18), [CLAUDE.md#L3-L3](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L3-L3) (`clm_4823c52e39b36ec80fd8477b1a443289e01f19422c9c8282f95d48a919245bad`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a `--setup` CLI flag that detects and installs optional tools (rust-analyzer, ripgrep), and is run as `lazyide` (or `cargo run -- /path/to/project`) inside a terminal. -- evidence: [README.md#L63-L63](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L63-L63), [README.md#L191-L195](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L191-L195) (`clm_c1dd30162aac2892624a2be780d1a6c703c94ff38c3ddbf1730af1a7a94ba2a5`)
- [observation/documented] Keybindings are data-driven: ~40 actions in a `KeyAction` enum with defaults in `KeyBindings::defaults()`, user overrides loaded from `~/.config/lazyide/keybinds.json`, and a two-pass lookup that first requires exact modifier match then falls back to a Shift-lenient match. -- evidence: [README.md#L175-L175](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L175-L175), [docs/ARCHITECTURE.md#L48-L48](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L48-L48) (`clm_d7ef6ef6e84a4172b22e75b24420486d37da5349677f73d5f43fb7dc89796ef8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The main event loop polls LSP responses, a debounced (120ms) file watcher, and autosave (every 2s) each iteration, draws a frame, then waits up to 100ms for terminal key/mouse events. -- evidence: [docs/ARCHITECTURE.md#L52-L64](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L52-L64) (`clm_f4e57c4cacd889b20b2c6058efadbf6b1bd6d6746988a679ad742e6c6299bf56`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Optional external tools are rust-analyzer (LSP completions/diagnostics/go-to-definition), ripgrep (project-wide search), and git (branch display, gutter markers); the system clipboard is accessed via the arboard crate. -- evidence: [CLAUDE.md#L50-L52](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L50-L52), [README.md#L201-L205](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L201-L205) (`clm_76ce59ad7c6c56f99dc1ece0cff836f147134b3309c8c8d2e450d2703c3aaf59`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

