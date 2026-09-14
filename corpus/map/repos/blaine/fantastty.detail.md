# blaine/fantastty -- full detail

[Back to orientation](fantastty.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/blaine/fantastty/60d248d0d20af6bacc249df056a0f76b95c1e8b1/4d4c6f8db32e1e6b.json](../../../wiki/dossiers/blaine/fantastty/60d248d0d20af6bacc249df056a0f76b95c1e8b1/4d4c6f8db32e1e6b.json)

## specifications (3 claim(s))

- [observation/documented] Fantastty is a macOS terminal app built on Ghostty's libghostty, offering workspace-based session management and persistent tmux-backed sessions. -- evidence: [README.md#L3-L3](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L3-L3) (`clm_bd3c0752e888d4545abd9e1f10a309f4a42e6d1c7dc342e03a333dd794c42295`)
- [inference/documented] A dated design document proposes tmux control-mode (-CC) attach so tmux windows render as native tabs and panes as Ghostty splits; it appears to be a plan, not necessarily shipped behavior. -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L7-L10](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L7-L10), [docs/plans/2026-03-07-tmux-attach-design.md#L3-L3](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L3-L3), [docs/plans/2026-03-07-tmux-attach-design.md#L14-L20](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L14-L20) (`clm_91adb5957045edfa9c0a803ea604a92b2781e5daa6253043c28bbd8308a069cf`)
- [inference/documented] A second design document defines a restore contract for attached tmux: one workspace maps to one tmux session and one tab to one tmux window, with terminal tabs derived only from live tmux state. -- evidence: [docs/plans/2026-03-10-attached-tmux-restore-contract-design.md#L5-L5](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-10-attached-tmux-restore-contract-design.md#L5-L5), [docs/plans/2026-03-10-attached-tmux-restore-contract-design.md#L32-L32](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-10-attached-tmux-restore-contract-design.md#L32-L32), [docs/plans/2026-03-10-attached-tmux-restore-contract-design.md#L7-L9](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-10-attached-tmux-restore-contract-design.md#L7-L9) (`clm_7a1469e736d4fdc086db61bc56c995f0dc7098fca71cd26f2f01ed7de53d87d2`)

## components (2 claim(s))

- [observation/documented] Documented features include workspaces with tabs, splits, notes with revision history, workspace URLs, archiving, SSH sessions, attention indicators, and shell integration. -- evidence: [README.md#L13-L21](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L13-L21) (`clm_4537119e0fd3e20e7089e426cd008b37dc50dea3a7497de2f7ccefb35ee102cb`)
- [observation/documented] The architecture is a SwiftUI app using libghostty as a static library for terminal rendering, with SessionManager, Session, TerminalTab, and TmuxManager components. -- evidence: [README.md#L89-L92](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L89-L92), [README.md#L87-L87](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L87-L87) (`clm_e422927d1dc3b0eb7251ba77b81cc26b32cdebfd6278787d6f86393cd8dd6bc5`)

## design-choices (3 claim(s))

- [observation/documented] Zsh integration for pwd tracking and escape-sequence passthrough is set up automatically when persistent sessions are enabled. -- evidence: [README.md#L35-L35](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L35-L35) (`clm_920076d4e89e564531bc3cfe896a7b44cf09377fb033d9899e5bcc4dcc344bf5`)
- [observation/documented] The attach design specifies a TmuxControlClient Swift actor per attached session, with all I/O and event handling actor-isolated, plus pure parser structs for protocol and layout. -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L77-L78](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L77-L78), [docs/plans/2026-03-07-tmux-attach-design.md#L33-L44](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L33-L44), [docs/plans/2026-03-07-tmux-attach-design.md#L46-L47](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L46-L47), [docs/plans/2026-03-07-tmux-attach-design.md#L110-L110](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L110-L110) (`clm_d08bdecd2526bf4bc9cbb1979230fbfe17fe4acc12d084749e0ab4a720805cbe`)
- [observation/documented] The attach design uses inert do-nothing PTYs per pane (discarding input) so real I/O flows through the tmux control connection, with input intercepted at SurfaceView level. -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L206-L207](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L206-L207), [docs/plans/2026-03-07-tmux-attach-design.md#L201-L202](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L201-L202), [docs/plans/2026-03-07-tmux-attach-design.md#L195-L195](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L195-L195), [docs/plans/2026-03-07-tmux-attach-design.md#L197-L199](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L197-L199) (`clm_77577541eb5f0a9cf8f26cd1045adc0f58820ca1e859602ff4fd80aa62e3e850`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: building requires Xcode 16+, the Metal toolchain, a pinned Zig version, cloning with submodules, and 'make xcframework' before an xcodebuild build. -- evidence: [README.md#L60-L60](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L60-L60), [README.md#L41-L44](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L41-L44), [README.md#L56-L57](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L56-L57), [README.md#L63-L64](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L63-L64) (`clm_96109b758a141f26aaabdd47613e71b08317d0bb2d76fadb992ca001fd08fac4`)
- [observation/documented] Repository development practice: the release gate before merging to main runs xcodebuild tests, go test ./..., a Python unittest module, and git diff --check, with fast-forward merges preferred. -- evidence: [docs/release-engineering.md#L46-L46](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L46-L46), [docs/release-engineering.md#L33-L38](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L33-L38), [docs/release-engineering.md#L48-L52](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L48-L52) (`clm_5cadf8a669d9d042218472e985822f843be6decf505fc803ca33df70faa51cd4`)
- [observation/documented] Repository development practice: the Build and Release workflow creates a GitHub Release only for pushed v* tags, builds, signs, notarizes, and publishes the DMG and Sparkle appcast, and tags must never be force-pushed. -- evidence: [docs/release-engineering.md#L81-L81](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L81-L81), [docs/release-engineering.md#L7-L11](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/release-engineering.md#L7-L11), [doc/GITHUB_ACTIONS_SETUP.md#L111-L115](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/doc/GITHUB_ACTIONS_SETUP.md#L111-L115) (`clm_0bbb77d9d7e0ffb4fe9b82c8b6ca2db0c7917474edaf49515512fc9f30136d0e`)
- [observation/documented] Repository development practice: CI requires seven GitHub secrets, including a Sparkle EdDSA private key whose matching public key is committed in Info.plist as SUPublicEDKey. -- evidence: [doc/GITHUB_ACTIONS_SETUP.md#L15-L16](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/doc/GITHUB_ACTIONS_SETUP.md#L15-L16), [doc/GITHUB_ACTIONS_SETUP.md#L89-L91](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/doc/GITHUB_ACTIONS_SETUP.md#L89-L91) (`clm_6e3a2f73c2820e75141dfc39fda3392c9751034145bfdc213f750c8029c80070`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The app ships as a signed, notarized DMG from GitHub Releases and requires macOS 15.0 (Sequoia) or later on Apple Silicon. -- evidence: [README.md#L7-L7](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L7-L7), [README.md#L9-L9](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L9-L9) (`clm_c8aa640e7a9efbfb3411da5408b9edb0faa941f4509ca4fdf478dd832d513108`)
- [observation/documented] A shell integration script sourced from ~/.fantastty provides the fantastty-note command (alias fn) for adding notes from the terminal. -- evidence: [README.md#L27-L28](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L27-L28), [README.md#L25-L25](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L25-L25), [README.md#L31-L33](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L31-L33) (`clm_a87230fb4d1009b547ec76ef585e5acb09d910051b2b5a90fee47e6e7f9d6f72`)
- [observation/documented] Installed builds check a GitHub-hosted appcast.xml via the Check for Updates menu item, indicating Sparkle-based auto-update. -- evidence: [README.md#L80-L83](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L80-L83) (`clm_7a002533d71817b89a80ae03753f66b603986734afbbfe6eb3ca0bad3dbfa333`)

## memory-state (1 claim(s))

- [observation/documented] Workspace metadata (names, notes, URLs, tags) persists in ~/.fantastty/workspaces.json; layout state saves to ~/.fantastty/layout.json on quit and restores on launch. -- evidence: [README.md#L94-L94](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L94-L94) (`clm_d679f9077dabee53a0e0096e9707788d6e687db7aa70a8bb02f4b2e8da2c3cd0`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The attach design requires tmux control mode from tmux 1.8+ and tmux 3.3+ for shell-integration passthrough, with a version check and warning on connect. -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L358-L360](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L358-L360) (`clm_f3e99aceead92ea62c85b9b92b107f1687276f0df0cfc613194cf8d828d758dc`)
- [observation/documented] The project is MIT licensed and vendors Ghostty as a submodule whose build.zig.zon pins the required Zig version. -- evidence: [README.md#L98-L98](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L98-L98), [README.md#L41-L44](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L41-L44), [README.md#L56-L57](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/README.md#L56-L57) (`clm_707cb6b3be427b82c4fb214631591fede09603e87e12a60744bfb2da1d1d9cb1`)

## limitations (1 claim(s))

- [observation/documented] The attach design lists non-goals: no tmux status-bar or border rendering, no Mosh support (standard SSH only), and no auto-reconnect on SSH drop (manual reconnect). -- evidence: [docs/plans/2026-03-07-tmux-attach-design.md#L24-L27](https://github.com/blaine/fantastty/blob/60d248d0d20af6bacc249df056a0f76b95c1e8b1/docs/plans/2026-03-07-tmux-attach-design.md#L24-L27) (`clm_f7fa31157bbb834300751eae16d569f871be4a41a8c9efdaab2544df9d084e21`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

