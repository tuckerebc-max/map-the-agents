# blaine/fantastty

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 60d248d0d20a @ 4d4c6f8db32e1e6b

## Summary (orientation draft, not independently verified)

Selected evidence records: Fantastty is a macOS terminal app built on Ghostty's libghostty, offering workspace-based session management and persistent tmux-backed sessions. The app ships as a signed, notarized DMG from GitHub Releases and requires macOS 15.0 (Sequoia) or later on Apple Silicon.

## Source coverage

Source coverage (partial): 6 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] Fantastty is a macOS terminal app built on Ghostty's libghostty, offering workspace-based session management and persistent tmux-backed sessions. -- evidence: [README.md#L3-L3](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L3-L3)
  - [inference/documented] A dated design document proposes tmux control-mode (-CC) attach so tmux windows render as native tabs and panes as Ghostty splits; it appears to be a plan, not necessarily shipped behavior. -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L7-L10](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L7-L10), [docs/plans/2026-03-07-tmux-attach-design.md#L3-L3](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L3-L3), [docs/plans/2026-03-07-tmux-attach-design.md#L14-L20](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L14-L20)
- components (2 claim(s)):
  - [observation/documented] Documented features include workspaces with tabs, splits, notes with revision history, workspace URLs, archiving, SSH sessions, attention indicators, and shell integration. -- evidence: [README.md#L13-L21](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L13-L21)
  - [observation/documented] The architecture is a SwiftUI app using libghostty as a static library for terminal rendering, with SessionManager, Session, TerminalTab, and TmuxManager components. -- evidence: [README.md#L89-L92](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L89-L92), [README.md#L87-L87](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L87-L87)
- design-choices (3 claim(s)):
  - [observation/documented] Zsh integration for pwd tracking and escape-sequence passthrough is set up automatically when persistent sessions are enabled. -- evidence: [README.md#L35-L35](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L35-L35)
  - [observation/documented] The attach design specifies a TmuxControlClient Swift actor per attached session, with all I/O and event handling actor-isolated, plus pure parser structs for protocol and layout. -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L77-L78](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L77-L78), [docs/plans/2026-03-07-tmux-attach-design.md#L33-L44](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L33-L44), [docs/plans/2026-03-07-tmux-attach-design.md#L46-L47](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L46-L47), [docs/plans/2026-03-07-tmux-attach-design.md#L110-L110](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L110-L110)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: building requires Xcode 16+, the Metal toolchain, a pinned Zig version, cloning with submodules, and 'make xcframework' before an xcodebuild build. -- evidence: [README.md#L60-L60](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L60-L60), [README.md#L41-L44](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L41-L44), [README.md#L56-L57](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L56-L57), [README.md#L63-L64](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L63-L64)
  - [observation/documented] Repository development practice: the release gate before merging to main runs xcodebuild tests, go test ./..., a Python unittest module, and git diff --check, with fast-forward merges preferred. -- evidence: [docs/release-engineering.md#L46-L46](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L46-L46), [docs/release-engineering.md#L33-L38](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L33-L38), [docs/release-engineering.md#L48-L52](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L48-L52)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The app ships as a signed, notarized DMG from GitHub Releases and requires macOS 15.0 (Sequoia) or later on Apple Silicon. -- evidence: [README.md#L7-L7](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L7-L7), [README.md#L9-L9](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L9-L9)
  - [observation/documented] A shell integration script sourced from ~/.fantastty provides the fantastty-note command (alias fn) for adding notes from the terminal. -- evidence: [README.md#L27-L28](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L27-L28), [README.md#L25-L25](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L25-L25), [README.md#L31-L33](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L31-L33)
- memory-state (1 claim(s)):
  - [observation/documented] Workspace metadata (names, notes, URLs, tags) persists in ~/.fantastty/workspaces.json; layout state saves to ~/.fantastty/layout.json on quit and restores on launch. -- evidence: [README.md#L94-L94](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L94-L94)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](fantastty.detail.md)

Metadata and full claim list: [full detail](fantastty.detail.md)
Human notes ([notes](fantastty.notes.md), never overwritten by build)

[Back to map index](../../index.md)
