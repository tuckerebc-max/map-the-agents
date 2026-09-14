---
access: public
aliases: []
claim_ids:
- clm_0b034bd9d02bff3f122cbfb9838ef0984e4b7233068285ba6bef7a7b6477b90a
- clm_3de5165edc34a1d2c3e2be931f8d4f381259aa90ee4e803122cf8c38eff31341
- clm_573c7d00bef214c2b4cf52725ed558f05446cf06a064c4be042d4b8f841e25c9
- clm_589c19a93afb31a38750191703fba035cffdb226153d2aa24f2d0be3e648b04a
- clm_8de61ea72895fd3de4ab4639107c4cf034d5a89e91c78f78340b3691d392c0f7
- clm_980886ecbf94247bfa09218a3a4eb22589304e938ea385f834204a5071e39ed9
- clm_a9ece0720fa6a7ebc58bea40c95738efd583efbc22d74516d99168ab3543ffe5
- clm_afd50d603ff7a6ef2880cf59d40c019f48780770f3cef122d06bdb5a61e0b472
- clm_b9580984505b4a10a070c74e1125a56ffecf70c28319574bf5a7fa998c81bd67
- clm_c791d2a25b0af66afaafee7a973d132a49a64b83653f73f7bf48717cca24f242
- clm_dd7a977fd81359edc34f5ebe7d7211907b730b0af8d403589ac6a3c692bcb41d
- clm_e1b5f6142c611e201527b74b1653970bf728583ea60909a3963c03f92ab0bc2c
- clm_e3ff139b3fe5ca32040bd3f1bdc95fa9bc0442e2f7e78b9a364ec3b9e9b69c7c
- clm_efae817ed2e158423f84d5d89a19bdd6538e1458df8f53f97bc3e5c12c128c23
- clm_f6d4934b8263a9e7d74b73de83aae7b0f3e11d793d859ad6f4f942f49239902a
- clm_f7c3ad77a082cae5bd0b0d582fa020dc3db99d23d34bddb824eb0a832f9a8333
maturity: draft
page_id: pg_3c8b6e14b22e5ad8af3e534fd15113f6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_336a734894ee55b9b915d34d0bc18f66
title: manaflow-ai/cmux/README.md @ 419cf0a00cc3
updated_at: '2026-09-14T02:14:59Z'
---

# manaflow-ai/cmux/README.md @ 419cf0a00cc3

<!-- rcw:begin owner=source:src_336a734894ee55b9b915d34d0bc18f66 block=evidence -->
- cmux is a native macOS app built with Swift and AppKit (not Electron), using libghostty for GPU-accelerated terminal rendering. [@claim:clm_0b034bd9d02bff3f122cbfb9838ef0984e4b7233068285ba6bef7a7b6477b90a]
- cmux positions itself as a non-prescriptive primitive: a terminal, browser, notifications, workspaces, splits, tabs, and CLI, without forcing an opinionated agent workflow. [@claim:clm_3de5165edc34a1d2c3e2be931f8d4f381259aa90ee4e803122cf8c38eff31341]
- cmux does not checkpoint arbitrary live process state; for live detach/reattach users must opt into `cmux local-tmux`, and a local tmux server cannot survive logout, restart, or power loss. [@claim:clm_573c7d00bef214c2b4cf52725ed558f05446cf06a064c4be042d4b8f841e25c9]
- Agent hooks (`cmux hooks setup`) save native session IDs under ~/.cmuxterm/ so supported agents like Claude Code, Codex, and OpenCode can resume sessions on reopen. [@claim:clm_589c19a93afb31a38750191703fba035cffdb226153d2aa24f2d0be3e648b04a]
- When an agent spawns subagents or teammates, cmux turns them into native panes and splits, and supports Claude Code teams and oh-my-opencode multi-model orchestration. [@claim:clm_8de61ea72895fd3de4ab4639107c4cf034d5a89e91c78f78340b3691d392c0f7]
- cmux supports macOS only, for now; an iOS companion app exists in beta on TestFlight. [@claim:clm_980886ecbf94247bfa09218a3a4eb22589304e938ea385f834204a5071e39ed9]
- cmux supports reusable skills for agents running in it (CLI control, workspace automation, settings, browser surfaces), with an open collection in the manaflow-ai/cmux-skills repository. [@claim:clm_a9ece0720fa6a7ebc58bea40c95738efd583efbc22d74516d99168ab3543ffe5]
- cmux targets developers running multiple AI coding agents (Claude Code, Codex, OpenCode, Gemini CLI, etc.) in parallel, surfacing which agent needs attention via rings, badges, and a notification panel. [@claim:clm_afd50d603ff7a6ef2880cf59d40c019f48780770f3cef122d06bdb5a61e0b472]
- cmux provides a `cmux notify` CLI and picks up OSC 9/99/777 terminal escape sequences to trigger notifications, usable from agent hooks. [@claim:clm_b9580984505b4a10a070c74e1125a56ffecf70c28319574bf5a7fa998c81bd67]
- cmux reads the existing ~/.config/ghostty/config for themes, fonts, colors, and terminal keybindings, while its own settings live in ~/.config/cmux/cmux.json with editable shortcuts. [@claim:clm_c791d2a25b0af66afaafee7a973d132a49a64b83653f73f7bf48717cca24f242]
- An in-app browser can be split beside the terminal, with a scriptable API ported from vercel-labs/agent-browser for snapshotting, clicking, filling forms, and evaluating JavaScript. [@claim:clm_dd7a977fd81359edc34f5ebe7d7211907b730b0af8d403589ac6a3c692bcb41d]
- The product exposes a CLI and Unix socket API to create workspaces, split panes, send keystrokes, read screen contents, take screenshots, and drive the in-app browser. [@claim:clm_e1b5f6142c611e201527b74b1653970bf728583ea60909a3963c03f92ab0bc2c]
- On quit, cmux saves a versioned snapshot under ~/Library/Application Support/cmux/ and restores window/workspace/pane layout, working directories, best-effort scrollback, and browser history on relaunch. [@claim:clm_e3ff139b3fe5ca32040bd3f1bdc95fa9bc0442e2f7e78b9a364ec3b9e9b69c7c]
- Stable releases auto-update via Sparkle, and the nightly build is a separate app with its own bundle ID and Sparkle feed built from the latest main commit. [@claim:clm_efae817ed2e158423f84d5d89a19bdd6538e1458df8f53f97bc3e5c12c128c23]
- The CLI supports SSH workspaces (`cmux ssh user@remote` with an optional initial --command), remote tmux attachment, and custom surface resume commands such as `cmux surface resume set`. [@claim:clm_f6d4934b8263a9e7d74b73de83aae7b0f3e11d793d859ad6f4f942f49239902a]
- Resume bindings are security-gated: only trusted bindings auto-run, approved command prefixes are bound to working directory and environment values, and sensitive environment keys are dropped before storage. [@claim:clm_f7c3ad77a082cae5bd0b0d582fa020dc3db99d23d34bddb824eb0a832f9a8333]
<!-- rcw:end owner=source:src_336a734894ee55b9b915d34d0bc18f66 block=evidence -->

## Researcher notes

