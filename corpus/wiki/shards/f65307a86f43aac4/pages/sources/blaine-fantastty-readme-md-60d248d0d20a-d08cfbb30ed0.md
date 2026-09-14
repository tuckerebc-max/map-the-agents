---
access: public
aliases: []
claim_ids:
- clm_4537119e0fd3e20e7089e426cd008b37dc50dea3a7497de2f7ccefb35ee102cb
- clm_707cb6b3be427b82c4fb214631591fede09603e87e12a60744bfb2da1d1d9cb1
- clm_7a002533d71817b89a80ae03753f66b603986734afbbfe6eb3ca0bad3dbfa333
- clm_920076d4e89e564531bc3cfe896a7b44cf09377fb033d9899e5bcc4dcc344bf5
- clm_96109b758a141f26aaabdd47613e71b08317d0bb2d76fadb992ca001fd08fac4
- clm_a87230fb4d1009b547ec76ef585e5acb09d910051b2b5a90fee47e6e7f9d6f72
- clm_bd3c0752e888d4545abd9e1f10a309f4a42e6d1c7dc342e03a333dd794c42295
- clm_c8aa640e7a9efbfb3411da5408b9edb0faa941f4509ca4fdf478dd832d513108
- clm_d679f9077dabee53a0e0096e9707788d6e687db7aa70a8bb02f4b2e8da2c3cd0
- clm_e422927d1dc3b0eb7251ba77b81cc26b32cdebfd6278787d6f86393cd8dd6bc5
maturity: draft
page_id: pg_f0bdf54158645b4dbe65d08cfbb30ed0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a228f79fca215118a5063d3649bb3303
title: blaine/fantastty/README.md @ 60d248d0d20a
updated_at: '2026-09-14T03:38:52Z'
---

# blaine/fantastty/README.md @ 60d248d0d20a

<!-- rcw:begin owner=source:src_a228f79fca215118a5063d3649bb3303 block=evidence -->
- Documented features include workspaces with tabs, splits, notes with revision history, workspace URLs, archiving, SSH sessions, attention indicators, and shell integration. [@claim:clm_4537119e0fd3e20e7089e426cd008b37dc50dea3a7497de2f7ccefb35ee102cb]
- The project is MIT licensed and vendors Ghostty as a submodule whose build.zig.zon pins the required Zig version. [@claim:clm_707cb6b3be427b82c4fb214631591fede09603e87e12a60744bfb2da1d1d9cb1]
- Installed builds check a GitHub-hosted appcast.xml via the Check for Updates menu item, indicating Sparkle-based auto-update. [@claim:clm_7a002533d71817b89a80ae03753f66b603986734afbbfe6eb3ca0bad3dbfa333]
- Zsh integration for pwd tracking and escape-sequence passthrough is set up automatically when persistent sessions are enabled. [@claim:clm_920076d4e89e564531bc3cfe896a7b44cf09377fb033d9899e5bcc4dcc344bf5]
- Repository development practice: building requires Xcode 16+, the Metal toolchain, a pinned Zig version, cloning with submodules, and 'make xcframework' before an xcodebuild build. [@claim:clm_96109b758a141f26aaabdd47613e71b08317d0bb2d76fadb992ca001fd08fac4]
- A shell integration script sourced from ~/.fantastty provides the fantastty-note command (alias fn) for adding notes from the terminal. [@claim:clm_a87230fb4d1009b547ec76ef585e5acb09d910051b2b5a90fee47e6e7f9d6f72]
- Fantastty is a macOS terminal app built on Ghostty's libghostty, offering workspace-based session management and persistent tmux-backed sessions. [@claim:clm_bd3c0752e888d4545abd9e1f10a309f4a42e6d1c7dc342e03a333dd794c42295]
- The app ships as a signed, notarized DMG from GitHub Releases and requires macOS 15.0 (Sequoia) or later on Apple Silicon. [@claim:clm_c8aa640e7a9efbfb3411da5408b9edb0faa941f4509ca4fdf478dd832d513108]
- Workspace metadata (names, notes, URLs, tags) persists in ~/.fantastty/workspaces.json; layout state saves to ~/.fantastty/layout.json on quit and restores on launch. [@claim:clm_d679f9077dabee53a0e0096e9707788d6e687db7aa70a8bb02f4b2e8da2c3cd0]
- The architecture is a SwiftUI app using libghostty as a static library for terminal rendering, with SessionManager, Session, TerminalTab, and TmuxManager components. [@claim:clm_e422927d1dc3b0eb7251ba77b81cc26b32cdebfd6278787d6f86393cd8dd6bc5]
<!-- rcw:end owner=source:src_a228f79fca215118a5063d3649bb3303 block=evidence -->

## Researcher notes

