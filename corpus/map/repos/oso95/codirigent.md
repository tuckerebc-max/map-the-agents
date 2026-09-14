# oso95/codirigent

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 03d9f6b7302e @ c4a8c82490e66983

## Summary (orientation draft, not independently verified)

Evidence consists solely of README files (English, Simplified Chinese, Traditional Chinese) describing Codirigent, a Rust-based tmux-style terminal workspace for running Claude Code, Codex, and Gemini CLI sessions in parallel, at version 0.1.0 alpha under GPL-3.0. No source code is present in the snapshot, so all claims are documentation-based.

## Source coverage

Source coverage (partial): 3 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Codirigent is described as a terminal workspace for running multiple AI coding CLIs in parallel, styled after tmux, with sessions restored to their prior directory, layout, and agent on launch. -- evidence: [README.md#L35-L35](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L35-L35), [README.md#L7-L9](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L7-L9)
- components (3 claim(s)):
  - [observation/documented] The project ships two binaries: the main `codirigent` app and a `codirigent-hook` binary that gets registered into supported CLIs' configuration files for real-time agent status tracking. -- evidence: [README.md#L107-L107](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L107-L107), [README.md#L86-L86](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L86-L86)
  - [observation/documented] Documented features include custom saveable grid layouts with drag-and-drop session headers, a file tree synced to the focused session, and Git worktree support for running agents on isolated branches concurrently. -- evidence: [README.md#L54-L54](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L54-L54), [README.md#L50-L50](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L50-L50), [README.md#L58-L58](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L58-L58)
- design-choices (2 claim(s)):
  - [observation/documented] Status tracking uses lightweight hooks registered into each CLI's config (Claude Code at ~/.claude/settings.json, Codex at ~/.codex/config.toml, Gemini at ~/.gemini/settings.json); when hooks are unavailable it falls back to a less precise reader/detector path. -- evidence: [README.md#L84-L84](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L84-L84), [README.md#L88-L92](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L88-L92)
  - [observation/documented] Hooks are installed automatically on first launch for supported CLIs, and relaunching after moving or reinstalling the app re-registers the hook binary path. -- evidence: [README.md#L94-L94](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L94-L94), [README.md#L86-L86](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L86-L86)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run tests with `cargo test --all --all-targets`, format with `cargo fmt --all`, and lint with `cargo clippy --all -- -D warnings`; major changes require opening an issue first, and PRs are welcome. -- evidence: [README.md#L127-L127](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L127-L127), [README.md#L119-L123](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L119-L123)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Each session displays a real-time status indicator with four states: Idle (gray), Working (amber, agent generating a response), Attention (rose, awaiting user input or permission), and Ready (green, finished response in an unfocused session). -- evidence: [README.md#L41-L46](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L41-L46), [README.md#L39-L39](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L39-L39)
  - [observation/documented] Distribution is via a code-signed .msi installer for Windows (with a SmartScreen reputation warning on first install) and a .dmg for macOS, both from GitHub releases. -- evidence: [README.md#L74-L74](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L74-L74), [README.md#L76-L76](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L76-L76), [README.md#L80-L80](https://github.com/oso95/Codirigent/blob/03d9f6b7302e4bb13629578d13561e10c5bb1b0f/README.md#L80-L80)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](codirigent.detail.md)

Metadata and full claim list: [full detail](codirigent.detail.md)
Human notes ([notes](codirigent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
