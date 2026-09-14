# robzilla1738/harness-terminal

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 923f44e64473 @ b4ca97a39b361395

## Summary (orientation draft, not independently verified)

Harness is a native macOS GPU terminal with a daemon-owned session model, a first-party Swift CLI, agent detection/notifications, and tmux-style multiplexing; the README documents product behavior and build/test workflows, and docs/AUDIT_ROADMAP.md records a 42-agent audit with parity scores and shipped fixes. Evidence coverage: 81 of 111 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 26 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The product consists of a GPU terminal engine, a background daemon that owns sessions/splits/scrollback, and a harness-cli, all written in first-party Swift as one self-contained app. -- evidence: [README.md#L7-L7](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L7-L7), [README.md#L9-L9](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L9-L9)
  - [observation/documented] Harness detects agents like Claude Code, Codex, and Cursor by their process tree, shows which session runs what, and notifies when an agent stops or requests approval; Cmd+Shift+U jumps to the waiting agent. -- evidence: [README.md#L7-L7](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L7-L7), [README.md#L23-L26](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L23-L26)
- design-choices (2 claim(s)):
  - [observation/documented] Four experience modes are offered: Plain Terminal (sessions close on quit), Persistent Terminal, Full Terminal (prefix, status line, copy mode, paste buffers, full CLI), and Agent Workspace with detection and notifications enabled up front; new installs start in Plain. -- evidence: [README.md#L37-L37](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L37-L37), [README.md#L32-L35](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L32-L35)
  - [observation/documented] The audit roadmap states the daemon uses single-lock serialization as a documented correctness invariant, and the daemon control socket is secured with 0o600 permissions plus a peer-UID check; OSC 52 clipboard reads are silently refused. -- evidence: [docs/AUDIT_ROADMAP.md#L37-L37](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L37-L37)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors build with 'make release' or swift build, run 'swift test' plus HARNESS_LIVE_DAEMON_TESTS=1 for real socket/PTY tests, and CI runs the deterministic suite, live daemon tests, and a release build on every push. -- evidence: [README.md#L160-L165](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L160-L165), [README.md#L151-L156](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L151-L156), [README.md#L167-L167](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L167-L167)
  - [observation/documented] Repository development practice: Harness.xcodeproj is generated from project.yml via XcodeGen, and the app target bundles HarnessDaemon and harness-cli into the app's MacOS directory so Xcode runs match the release layout. -- evidence: [README.md#L175-L175](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L175-L175)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] harness-cli exposes commands such as list-surfaces, new-session, new-tab, send-keys, notify, capture-pane, color-check, and theme-preview, and can be installed onto PATH from the app bundle or a source build. -- evidence: [README.md#L83-L83](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L83-L83), [README.md#L86-L86](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L86-L86), [README.md#L69-L77](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L69-L77)
More evidence: [full detail](harness-terminal.detail.md)

Metadata and full claim list: [full detail](harness-terminal.detail.md)
Human notes ([notes](harness-terminal.notes.md), never overwritten by build)

[Back to map index](../../index.md)
