---
access: public
aliases: []
claim_ids:
- clm_0110bf258516e4d42e4af88354022f4d07f5a2ef858b8a0bc70135370788740b
- clm_3707a80a926d79d111432cea4a0d548748f1f2479d2259cd61fe8eb2c37c1857
- clm_3906595df4649609478cdaea6a2e18c09a5e745a0193766b0b5a87a248e4ac89
- clm_3ac6a5dfd3e6bad357a2ddc1415902add787b8fadb954c56eac1cbdc96ff8ae5
- clm_515bd0b95a78a485af9831c2786c43ec469ce0d2fe948138d2e20b4ea4be9ca4
- clm_64a38775f0715bcaf3d5eb04efb7b66ea0474a330a057e2c962b174bffdd3a45
- clm_815345e43a540db8fac1b5438599769c0530bbc3084ac1b746c99d9930dcbfd6
- clm_8375d983b76f6c5fa66d12525c2bda557e96bf1f37d1fd5d673c5bed26f0b949
- clm_87f3d6bbdd32bfd42319db95dbd2c5a5051ed6a753d86fa84c4ad664cd103c37
- clm_97fdb7978ff94349707562434b5b3406db85e507a49709c3e308fa05c16094e8
- clm_a6adac92bb100e80c0cecd74afdb9c4815726681bc2c0ffe49ed96aba91dceca
- clm_bb467ffddfbafe29774fbd87ccb2c473f2145693f01bdc30fd6d5295159d5f89
- clm_c3cb31e0e293324857fa7297c12039d754bd3e17199ff051e3e05d71b7fdaf67
- clm_dd19ee519dca136680f34a22e6e25f2c8d49aae1a051ed1ffcae7e3afdf09775
- clm_e969e6673a9218637c2eeec15c521fcb1bc36ad1811c20c2ce86aa5452fcf244
maturity: draft
page_id: pg_2140bcb83f245427a649ea8379f4ffcb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1a5e028046345d249ae06958f7b1686b
title: yuuichieguchi/Calyx/README.md @ 8415801ce661
updated_at: '2026-09-14T03:26:10Z'
---

# yuuichieguchi/Calyx/README.md @ 8415801ce661

<!-- rcw:begin owner=source:src_1a5e028046345d249ae06958f7b1686b block=evidence -->
- The AI Agent IPC MCP server offers tools register_peer, list_peers, send_message, broadcast, receive_messages, and get_peer_status; receive_messages deletes messages on delivery so each is delivered once. [@claim:clm_0110bf258516e4d42e4af88354022f4d07f5a2ef858b8a0bc70135370788740b]
- A Git sidebar shows working changes, staging state, commit graph, branch visualization, and inline diffs per repository, including linked worktrees and submodules, with per-line diff comments submittable to agent panes. [@claim:clm_3707a80a926d79d111432cea4a0d548748f1f2479d2259cd61fe8eb2c37c1857]
- Repository development practice: external pull requests are not accepted and are closed automatically without review; bug reports and feature ideas go through GitHub Issues. [@claim:clm_3906595df4649609478cdaea6a2e18c09a5e745a0193766b0b5a87a248e4ac89]
- The terminal engine is libghostty (Ghostty v1.3.1) providing Metal GPU-accelerated rendering; the tech stack is Swift 6.2, AppKit, SwiftUI, and XcodeGen. [@claim:clm_3ac6a5dfd3e6bad357a2ddc1415902add787b8fadb954c56eac1cbdc96ff8ae5]
- Calyx is a native macOS terminal for running and supervising coding agents (Claude Code, Codex, OpenCode, Hermes, Grok, pi) in parallel, with an approval inbox, live status, persistent sessions, and inline diff review. [@claim:clm_515bd0b95a78a485af9831c2786c43ec469ce0d2fe948138d2e20b4ea4be9ca4]
- Calyx exposes panes, commands, captured output, browser tabs, language servers, and peer agents to agents through MCP and a bundled CLI. [@claim:clm_64a38775f0715bcaf3d5eb04efb7b66ea0474a330a057e2c962b174bffdd3a45]
- An LSP proxy MCP exposes lsp_hover, lsp_definition, lsp_references, lsp_rename, and lsp_diagnostics to agents, keeping servers running in the background and starting the right one per workspace. [@claim:clm_815345e43a540db8fac1b5438599769c0530bbc3084ac1b746c99d9930dcbfd6]
- Persistent sessions are opt-in daemon-backed terminals that survive app quit and crashes, with a Session Browser, recovery flow, optional on-disk history, and remote sessions via calyx-session on SSH hosts. [@claim:clm_8375d983b76f6c5fa66d12525c2bda557e96bf1f37d1fd5d673c5bed26f0b949]
- Architecture: AppKit handles window/tab/focus management with SwiftUI rendering bridged via NSHostingView; all ghostty C API calls go through a GhosttyFFI enum and @MainActor is enforced on UI and model code. [@claim:clm_87f3d6bbdd32bfd42319db95dbd2c5a5051ed6a753d86fa84c4ad664cd103c37]
- Cursor click-to-move may be offset on Japanese/full-width text because Ghostty translates clicks into arrow-key steps over terminal cells; Calyx also overrides certain Ghostty config keys for Glass UI. [@claim:clm_97fdb7978ff94349707562434b5b3406db85e507a49709c3e308fa05c16094e8]
- An Agents Sidebar shows each connected agent as working, blocked, idle, or done, with unread badges, click-to-focus navigation, and expandable subagent rows for CLIs that report them. [@claim:clm_a6adac92bb100e80c0cecd74afdb9c4815726681bc2c0ffe49ed96aba91dceca]
- Repository development practice: building requires macOS 26+, Xcode 26+, Zig matching ghostty's build.zig.zon, and XcodeGen; clone with submodules, build the GhosttyKit xcframework with zig, then generate the Xcode project and build with xcodebuild. [@claim:clm_bb467ffddfbafe29774fbd87ccb2c473f2145693f01bdc30fd6d5295159d5f89]
- Command text and output are redacted for known secret patterns (tokens, passwords, API keys, JWTs) before agents can read them, with pending redaction reported via output_pending. [@claim:clm_c3cb31e0e293324857fa7297c12039d754bd3e17199ff051e3e05d71b7fdaf67]
- The approval inbox is opt-in via Settings; nothing is automatically approved unless the user separately opts in, and cockpit tools like pane_run and pane_send_keys are approval-gated. [@claim:clm_dd19ee519dca136680f34a22e6e25f2c8d49aae1a051ed1ffcae7e3afdf09775]
- Browser tabs are non-persistent WKWebViews limited to http/https with popups blocked, scriptable via 25 bundled 'calyx browser' commands; the browser server listens on localhost:41840. [@claim:clm_e969e6673a9218637c2eeec15c521fcb1bc36ad1811c20c2ce86aa5452fcf244]
<!-- rcw:end owner=source:src_1a5e028046345d249ae06958f7b1686b block=evidence -->

## Researcher notes

