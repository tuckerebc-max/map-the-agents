---
access: public
aliases: []
claim_ids:
- clm_17b4253abbac653d1a99289c146b6c999295746a473a54357a5558d34c19ccce
- clm_261b505e60e72cdcb80af4a8a4432ea2b131fec3045972a42d1df6a9cc51779d
- clm_27188dabee1e60b6f804f6a09a8e4c807274279b8f9d53fa413d2a63e6fb5a12
- clm_37247f9beba8fcb9b424bd24135fc61bd237cfa87911425f4deff8ca3872c797
- clm_554ab49f5056dba5cfe068fe0b3f70a93c6d2c6b583f41c20a818cbd17676707
- clm_6287023967a7768b3a4b4772c5c6f75eccb93667b2eaf2d0a0687c471bc8f245
- clm_90d3b8925815020f79f9825b279882d53aaec44863bdc1c977f7334035f8c52c
- clm_b017e9da4456ae0d374087939540d099f3cf663c1985cb3c681de87682ed5dee
- clm_d1d1e347261ce7ec9a3abcc7810dd35b25399a372e5f523df18909ef27338ce9
maturity: draft
page_id: pg_f46469a1f30c56ce9559450b7e77c3a4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_df83fd5d596a59f288f6190f4b7438f7
title: robzilla1738/harness-terminal/README.md @ 923f44e64473
updated_at: '2026-09-14T02:36:11Z'
---

# robzilla1738/harness-terminal/README.md @ 923f44e64473

<!-- rcw:begin owner=source:src_df83fd5d596a59f288f6190f4b7438f7 block=evidence -->
- The product consists of a GPU terminal engine, a background daemon that owns sessions/splits/scrollback, and a harness-cli, all written in first-party Swift as one self-contained app. [@claim:clm_17b4253abbac653d1a99289c146b6c999295746a473a54357a5558d34c19ccce]
- harness-cli exposes commands such as list-surfaces, new-session, new-tab, send-keys, notify, capture-pane, color-check, and theme-preview, and can be installed onto PATH from the app bundle or a source build. [@claim:clm_261b505e60e72cdcb80af4a8a4432ea2b131fec3045972a42d1df6a9cc51779d]
- The only external dependency is Sparkle, the macOS auto-update framework, which is GUI-only per the README. [@claim:clm_27188dabee1e60b6f804f6a09a8e4c807274279b8f9d53fa413d2a63e6fb5a12]
- HARNESS_SURFACE is set in every Harness pane so agents can notify the exact tab they run in, and 'harness-cli install-hooks claude-code' installs per-agent hooks; agents without hook support fall back to built-in activity detection. [@claim:clm_37247f9beba8fcb9b424bd24135fc61bd237cfa87911425f4deff8ca3872c797]
- Four experience modes are offered: Plain Terminal (sessions close on quit), Persistent Terminal, Full Terminal (prefix, status line, copy mode, paste buffers, full CLI), and Agent Workspace with detection and notifications enabled up front; new installs start in Plain. [@claim:clm_554ab49f5056dba5cfe068fe0b3f70a93c6d2c6b583f41c20a818cbd17676707]
- Repository development practice: Harness.xcodeproj is generated from project.yml via XcodeGen, and the app target bundles HarnessDaemon and harness-cli into the app's MacOS directory so Xcode runs match the release layout. [@claim:clm_6287023967a7768b3a4b4772c5c6f75eccb93667b2eaf2d0a0687c471bc8f245]
- Repository development practice: contributors build with 'make release' or swift build, run 'swift test' plus HARNESS_LIVE_DAEMON_TESTS=1 for real socket/PTY tests, and CI runs the deterministic suite, live daemon tests, and a release build on every push. [@claim:clm_90d3b8925815020f79f9825b279882d53aaec44863bdc1c977f7334035f8c52c]
- Any harness-cli command accepts a global --host flag to target a headless or remote daemon over an SSH tunnel that forwards the remote control socket, reusing existing SSH trust; remotes are registered with 'remote add' and extra SSH options pass via --ssh-arg. [@claim:clm_b017e9da4456ae0d374087939540d099f3cf663c1985cb3c681de87682ed5dee]
- Harness detects agents like Claude Code, Codex, and Cursor by their process tree, shows which session runs what, and notifies when an agent stops or requests approval; Cmd+Shift+U jumps to the waiting agent. [@claim:clm_d1d1e347261ce7ec9a3abcc7810dd35b25399a372e5f523df18909ef27338ce9]
<!-- rcw:end owner=source:src_df83fd5d596a59f288f6190f4b7438f7 block=evidence -->

## Researcher notes

