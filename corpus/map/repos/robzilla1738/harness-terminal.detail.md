# robzilla1738/harness-terminal -- full detail

[Back to orientation](harness-terminal.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/robzilla1738/harness-terminal/923f44e6447359c752b15b60f0e90eb7382e0001/b4ca97a39b361395.json](../../../wiki/dossiers/robzilla1738/harness-terminal/923f44e6447359c752b15b60f0e90eb7382e0001/b4ca97a39b361395.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The product consists of a GPU terminal engine, a background daemon that owns sessions/splits/scrollback, and a harness-cli, all written in first-party Swift as one self-contained app. -- evidence: [README.md#L7-L7](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L7-L7), [README.md#L9-L9](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L9-L9) (`clm_17b4253abbac653d1a99289c146b6c999295746a473a54357a5558d34c19ccce`)
- [observation/documented] Harness detects agents like Claude Code, Codex, and Cursor by their process tree, shows which session runs what, and notifies when an agent stops or requests approval; Cmd+Shift+U jumps to the waiting agent. -- evidence: [README.md#L7-L7](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L7-L7), [README.md#L23-L26](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L23-L26) (`clm_d1d1e347261ce7ec9a3abcc7810dd35b25399a372e5f523df18909ef27338ce9`)

## design-choices (2 claim(s))

- [observation/documented] Four experience modes are offered: Plain Terminal (sessions close on quit), Persistent Terminal, Full Terminal (prefix, status line, copy mode, paste buffers, full CLI), and Agent Workspace with detection and notifications enabled up front; new installs start in Plain. -- evidence: [README.md#L37-L37](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L37-L37), [README.md#L32-L35](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L32-L35) (`clm_554ab49f5056dba5cfe068fe0b3f70a93c6d2c6b583f41c20a818cbd17676707`)
- [observation/documented] The audit roadmap states the daemon uses single-lock serialization as a documented correctness invariant, and the daemon control socket is secured with 0o600 permissions plus a peer-UID check; OSC 52 clipboard reads are silently refused. -- evidence: [docs/AUDIT_ROADMAP.md#L37-L37](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L37-L37) (`clm_27eaee531bfc71a17a05c10cf1ee4d54881000b8961357400e35f8b4b2bc3552`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors build with 'make release' or swift build, run 'swift test' plus HARNESS_LIVE_DAEMON_TESTS=1 for real socket/PTY tests, and CI runs the deterministic suite, live daemon tests, and a release build on every push. -- evidence: [README.md#L160-L165](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L160-L165), [README.md#L151-L156](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L151-L156), [README.md#L167-L167](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L167-L167) (`clm_90d3b8925815020f79f9825b279882d53aaec44863bdc1c977f7334035f8c52c`)
- [observation/documented] Repository development practice: Harness.xcodeproj is generated from project.yml via XcodeGen, and the app target bundles HarnessDaemon and harness-cli into the app's MacOS directory so Xcode runs match the release layout. -- evidence: [README.md#L175-L175](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L175-L175) (`clm_6287023967a7768b3a4b4772c5c6f75eccb93667b2eaf2d0a0687c471bc8f245`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] harness-cli exposes commands such as list-surfaces, new-session, new-tab, send-keys, notify, capture-pane, color-check, and theme-preview, and can be installed onto PATH from the app bundle or a source build. -- evidence: [README.md#L83-L83](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L83-L83), [README.md#L86-L86](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L86-L86), [README.md#L69-L77](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L69-L77) (`clm_261b505e60e72cdcb80af4a8a4432ea2b131fec3045972a42d1df6a9cc51779d`)
- [observation/documented] Any harness-cli command accepts a global --host flag to target a headless or remote daemon over an SSH tunnel that forwards the remote control socket, reusing existing SSH trust; remotes are registered with 'remote add' and extra SSH options pass via --ssh-arg. -- evidence: [README.md#L100-L104](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L100-L104), [README.md#L118-L119](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L118-L119), [README.md#L109-L116](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L109-L116) (`clm_b017e9da4456ae0d374087939540d099f3cf663c1985cb3c681de87682ed5dee`)
- [observation/documented] HARNESS_SURFACE is set in every Harness pane so agents can notify the exact tab they run in, and 'harness-cli install-hooks claude-code' installs per-agent hooks; agents without hook support fall back to built-in activity detection. -- evidence: [README.md#L130-L130](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L130-L130), [README.md#L125-L128](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L125-L128), [README.md#L123-L123](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L123-L123) (`clm_37247f9beba8fcb9b424bd24135fc61bd237cfa87911425f4deff8ca3872c797`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A 42-agent audit workflow (parallel finders, adversarial verification, synthesis, completeness critic) produced 101 findings with 28 adversarially verified, and reported parity scores such as VT core 90%, input protocols 92%, and tmux commands 85% versus ghostty/tmux. -- evidence: [docs/AUDIT_ROADMAP.md#L12-L12](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L12-L12), [docs/AUDIT_ROADMAP.md#L20-L35](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L20-L35), [docs/AUDIT_ROADMAP.md#L10-L10](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L10-L10), [docs/AUDIT_ROADMAP.md#L8-L8](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L8-L8) (`clm_1634d253f6758eb84a9ec13893d3bc44540d0943bade947bf17ef5b7f8255ec0`)

## dependencies (1 claim(s))

- [observation/documented] The only external dependency is Sparkle, the macOS auto-update framework, which is GUI-only per the README. -- evidence: [README.md#L9-L9](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/README.md#L9-L9) (`clm_27188dabee1e60b6f804f6a09a8e4c807274279b8f9d53fa413d2a63e6fb5a12`)

## limitations (1 claim(s))

- [observation/documented] The audit identified gaps later fixed via shipped PRs, including a paste escape-injection bug, missing DECSTR/REP/IRM/DECOM handlers, DCS misrouting into the Sixel decoder, and Kitty graphics being display-only; animation (a=a) and iTerm2 multipart upload remain deliberately deferred. -- evidence: [docs/AUDIT_ROADMAP.md#L205-L214](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L205-L214), [docs/AUDIT_ROADMAP.md#L47-L50](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L47-L50), [docs/AUDIT_ROADMAP.md#L74-L77](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L74-L77), [docs/AUDIT_ROADMAP.md#L69-L72](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L69-L72), [docs/AUDIT_ROADMAP.md#L118-L121](https://github.com/robzilla1738/harness-terminal/blob/923f44e6447359c752b15b60f0e90eb7382e0001/docs/AUDIT_ROADMAP.md#L118-L121) (`clm_81d61ef732659003886a59996f86a6b7832915a08f68cf51a0e5a23cb08c3302`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

