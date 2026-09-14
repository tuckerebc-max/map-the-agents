# tysonlabs/lazyide

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7496b58b7782 @ f12e7adbb1301325

## Summary (orientation draft, not independently verified)

lazyide is a Rust/ratatui terminal IDE with LSP, syntax highlighting, git integration, themes, and split panes; evidence is mostly README/docs describing product features plus contributor guidance.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] lazyide is a lightweight terminal IDE written in Rust with ratatui, shipped as a single binary with file tree, tabbed editing, LSP, syntax highlighting, folding, git integration, project search, 32 themes, and customizable keybindings. -- evidence: [README.md#L8-L8](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L8-L8)
- components (2 claim(s)):
  - [observation/documented] LSP support is implemented by spawning a rust-analyzer child process over JSON-RPC, with a background stdout reader thread and per-frame polling that matches responses to pending completion/definition requests. -- evidence: [docs/ARCHITECTURE.md#L122-L122](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L122-L122), [docs/ARCHITECTURE.md#L124-L127](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L124-L127)
  - [observation/documented] Git integration shells out to the `git` binary rather than using libgit2, using commands like `git rev-parse`, `git status --porcelain -z`, and `git diff HEAD` for branch, status, and line-level diff data. -- evidence: [docs/ARCHITECTURE.md#L152-L152](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L152-L152), [docs/ARCHITECTURE.md#L154-L159](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L154-L159)
- design-choices (3 claim(s)):
  - [observation/documented] All application state lives in a single `App` struct with methods split across `app/*.rs` impl blocks; UI rendering functions take `&App` and never mutate state, which happens only in `app/` methods. -- evidence: [docs/ARCHITECTURE.md#L42-L42](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L42-L42), [docs/ARCHITECTURE.md#L46-L46](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L46-L46)
  - [observation/documented] Two editor panes are implemented via a state-swap: the focused pane's fields live on `App` and the other pane in `App::other_pane`, so existing active-tab code paths need no pane awareness. -- evidence: [docs/ARCHITECTURE.md#L44-L44](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L44-L44)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors build with cargo (build/run/test), tests are inline `#[cfg(test)]` modules (about 300 tests), and CONTRIBUTING.md asks for an issue before large changes, minimal diffs, and a PR workflow. -- evidence: [docs/ARCHITECTURE.md#L163-L163](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L163-L163), [docs/ARCHITECTURE.md#L171-L171](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L171-L171), [README.md#L191-L195](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L191-L195), [CONTRIBUTING.md#L115-L119](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CONTRIBUTING.md#L115-L119)
  - [observation/documented] Repository development practice: CLAUDE.md guides Claude Code when working in the repo, stating the project should stay minimal, avoid heavy abstractions, and noting Rust 2024 edition with no custom build scripts or CI/CD. -- evidence: [CLAUDE.md#L7-L7](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L7-L7), [CLAUDE.md#L18-L18](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L18-L18), [CLAUDE.md#L3-L3](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/CLAUDE.md#L3-L3)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a `--setup` CLI flag that detects and installs optional tools (rust-analyzer, ripgrep), and is run as `lazyide` (or `cargo run -- /path/to/project`) inside a terminal. -- evidence: [README.md#L63-L63](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L63-L63), [README.md#L191-L195](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L191-L195)
  - [observation/documented] Keybindings are data-driven: ~40 actions in a `KeyAction` enum with defaults in `KeyBindings::defaults()`, user overrides loaded from `~/.config/lazyide/keybinds.json`, and a two-pass lookup that first requires exact modifier match then falls back to a Shift-lenient match. -- evidence: [README.md#L175-L175](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/README.md#L175-L175), [docs/ARCHITECTURE.md#L48-L48](https://github.com/TysonLabs/lazyide/blob/7496b58b7782dd7d0534c0db29bc61b3171f0df2/docs/ARCHITECTURE.md#L48-L48)
- memory-state: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](lazyide.detail.md)

Metadata and full claim list: [full detail](lazyide.detail.md)
Human notes ([notes](lazyide.notes.md), never overwritten by build)

[Back to map index](../../index.md)
