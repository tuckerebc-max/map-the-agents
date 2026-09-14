---
access: public
aliases: []
claim_ids:
- clm_040105d27c0e438e5c00bdaf5283ac978a64d1bdf7fce0fcd64ea65ccc515f6f
- clm_0da62a4f6e2dff83e439a228a1741f0e4fc345f1b746614338c03e8de243595c
- clm_1513470eb2fcb5372a3e7ca36a2d56b3e73b3b1a9776a5fe54a47999fdd63da4
- clm_29b62f0919d4228c5400cc339e0cf41f75e7dd1ad684d546af0170ae4d9c1038
- clm_326962af14fa99d3dd660304d5bfdeaca50e64b9f2e6a312edfd80da598f280b
- clm_34c7a35859333be503af9fe809104237b728f45fd038b8d842ab9a712e8c9c0d
- clm_5a6e9fcd0714fb131ed272fa867baf23a9d351d4b7b7b9ea4af0855d7a1701de
- clm_69b6b02c449c02f9d49fdaab308499481ade585786ce606ac536217b2827dc20
- clm_87a0866a6d2233955e009eb6d36e691a96d1000464f2e8a7d4a1e76976791d43
- clm_8d985e97fd9c1cd575bdf7cd774a22f7e7f3d4255eea5e27e08af0a8645a507f
- clm_9374b6f07783a4c253098df8da667a86a437bb12c1e635d311578e1a5e4e29c4
- clm_98ebb78cc71ab1b6da0eace379f004e047fa628670ba6d5c145fcc687dc5d66e
- clm_a0d4ee56ae5ade944f5a4ce3c54b4690b9d444c633d46ff6c38abedd2d404609
- clm_a2e809a2caddde58a68aa181dbbb9ae7d226a698ee4794f103e4ae068017f6b7
- clm_ae2430f76c7a82829e81ebe9494520e8c4761915bf97d2fe244154d230ee1e17
- clm_b48f467d22daf0778348a21f0667d9d22f4ff8b878bc6cd6908c86685b69e324
- clm_c7651fe042752145b9309d66bc086638ff04bc6ef8050fb2b8d1366e36f3a5d2
- clm_cc97f4500562f20ac515eee218795a7c2f0c0d4631d4eef6a5a5153f38e4629e
- clm_d17afce1cc2b920561cf16e5d7d8124e52e4f6b27a2cea1101820cfbbfac1ca0
maturity: draft
page_id: pg_1965c519229c5f0fa6fe59d69f9fae2d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c4a71a5301015d7da018cce86241f850
title: lucianodiisouza/semaphore/README.md @ 0632b3147987
updated_at: '2026-09-14T04:08:05Z'
---

# lucianodiisouza/semaphore/README.md @ 0632b3147987

<!-- rcw:begin owner=source:src_c4a71a5301015d7da018cce86241f850 block=evidence -->
- IPC is newline-delimited JSON over a Unix socket ($XDG_RUNTIME_DIR/semaphore.sock or /tmp/semaphore-<uid>.sock) or the Windows named pipe \\.\pipe\semaphore, with set and status commands. [@claim:clm_040105d27c0e438e5c00bdaf5283ac978a64d1bdf7fce0fcd64ea65ccc515f6f]
- The state machine tracks one entry per session ID and picks the highest-priority color with red over yellow over green; setting green removes the session. [@claim:clm_0da62a4f6e2dff83e439a228a1741f0e4fc345f1b746614338c03e8de243595c]
- Stealth mode hides the widget from many capture tools but may still appear in some macOS 15+ apps (OS limitation) and depends on the compositor on Linux. [@claim:clm_1513470eb2fcb5372a3e7ca36a2d56b3e73b3b1a9776a5fe54a47999fdd63da4]
- The Stream Deck integration requires the Elgato Stream Deck app v6.0 or later on Windows or macOS, with Semaphore running in the background for the IPC socket. [@claim:clm_29b62f0919d4228c5400cc339e0cf41f75e7dd1ad684d546af0170ae4d9c1038]
- Stale sessions are pruned every 30 seconds after idle_timeout_secs (default 300 seconds) without updates; config is stored at ~/.semaphore/config.json. [@claim:clm_326962af14fa99d3dd660304d5bfdeaca50e64b9f2e6a312edfd80da598f280b]
- The project comprises a sem-core library (state machine, session aggregation, IPC, config), a semctl CLI, a Tauri-based widget app, and a TypeScript/Vite frontend. [@claim:clm_34c7a35859333be503af9fe809104237b728f45fd038b8d842ab9a712e8c9c0d]
- macOS releases are not yet Apple-notarized, so Gatekeeper may report the downloaded app as damaged until quarantine is removed. [@claim:clm_5a6e9fcd0714fb131ed272fa867baf23a9d351d4b7b7b9ea4af0855d7a1701de]
- Codex CLI support is limited: PreToolUse/PostToolUse hooks mainly fire for Bash, so the red light for file edits is limited; Copilot CLI support is partial and varies by version. [@claim:clm_69b6b02c449c02f9d49fdaab308499481ade585786ce606ac536217b2827dc20]
- Repository development practice: building requires Rust stable, Node.js 20+, and npm (plus WebKit/GTK dev packages on Linux); tests run via cargo test and npm test (Vitest). [@claim:clm_87a0866a6d2233955e009eb6d36e691a96d1000464f2e8a7d4a1e76976791d43]
- The app supports hook-based integration with Cursor, Claude Code, Codex CLI, Gemini CLI, and Copilot CLI, each with documented config paths and semctl install commands. [@claim:clm_8d985e97fd9c1cd575bdf7cd774a22f7e7f3d4255eea5e27e08af0a8645a507f]
- Repository development practice: tagging a version (e.g. git tag v0.2.0 and pushing) triggers a GitHub Actions release workflow that builds macOS arm64/x64, Linux x64, and Windows x64 artifacts. [@claim:clm_9374b6f07783a4c253098df8da667a86a437bb12c1e635d311578e1a5e4e29c4]
- The tray menu offers show/hide, settings, stealth toggle, always-on-top, horizontal layout, a light test melody, a Genius memory game, and quit; left-click shows or focuses the widget. [@claim:clm_98ebb78cc71ab1b6da0eace379f004e047fa628670ba6d5c145fcc687dc5d66e]
- Semaphore is an always-on-top floating traffic-light widget that signals when an AI coding agent is idle, thinking, or writing files, without switching windows. [@claim:clm_a0d4ee56ae5ade944f5a4ce3c54b4690b9d444c633d46ff6c38abedd2d404609]
- The semctl CLI supports set/status light control, install/uninstall of hooks, doctor diagnostics, and launch, and lives at ~/.semaphore/bin after install. [@claim:clm_a2e809a2caddde58a68aa181dbbb9ae7d226a698ee4794f103e4ae068017f6b7]
- sem-hook is a thin wrapper invoked by AI tool hooks that parses optional JSON from stdin for session identifiers and then calls semctl set. [@claim:clm_ae2430f76c7a82829e81ebe9494520e8c4761915bf97d2fe244154d230ee1e17]
- Light states are defined as green for idle/ready, yellow for thinking or running tools, and red for writing or editing files. [@claim:clm_b48f467d22daf0778348a21f0667d9d22f4ff8b878bc6cd6908c86685b69e324]
- Environment variables SEMAPHORE_SOCKET, SEMAPHORE_BIN, and SEMAPHORE_SEMCTL override the IPC socket path and semctl binary locations. [@claim:clm_c7651fe042752145b9309d66bc086638ff04bc6ef8050fb2b8d1366e36f3a5d2]
- A Stream Deck plugin runs as a Node.js process, polls the Semaphore IPC socket every 500 ms with a status command, and updates key images, showing grey when the app is not running. [@claim:clm_cc97f4500562f20ac515eee218795a7c2f0c0d4631d4eef6a5a5153f38e4629e]
- Hooks always exit 0 so they never block the agent, and the installer merges hook entries using a _semaphore marker without overwriting unrelated hooks. [@claim:clm_d17afce1cc2b920561cf16e5d7d8124e52e4f6b27a2cea1101820cfbbfac1ca0]
<!-- rcw:end owner=source:src_c4a71a5301015d7da018cce86241f850 block=evidence -->

## Researcher notes

