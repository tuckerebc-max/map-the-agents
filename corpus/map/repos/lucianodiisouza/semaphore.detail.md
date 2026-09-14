# lucianodiisouza/semaphore -- full detail

[Back to orientation](semaphore.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lucianodiisouza/semaphore/0632b3147987e9d41cce3aa8145a7a79bddc7b41/2d0f49ea8635d35c.json](../../../wiki/dossiers/lucianodiisouza/semaphore/0632b3147987e9d41cce3aa8145a7a79bddc7b41/2d0f49ea8635d35c.json)

## specifications (2 claim(s))

- [observation/documented] Semaphore is an always-on-top floating traffic-light widget that signals when an AI coding agent is idle, thinking, or writing files, without switching windows. -- evidence: [README.md#L11-L11](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L11-L11), [README.md#L3-L3](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L3-L3) (`clm_a0d4ee56ae5ade944f5a4ce3c54b4690b9d444c633d46ff6c38abedd2d404609`)
- [observation/documented] Light states are defined as green for idle/ready, yellow for thinking or running tools, and red for writing or editing files. -- evidence: [README.md#L5-L9](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L5-L9) (`clm_b48f467d22daf0778348a21f0667d9d22f4ff8b878bc6cd6908c86685b69e324`)

## components (3 claim(s))

- [observation/documented] The project comprises a sem-core library (state machine, session aggregation, IPC, config), a semctl CLI, a Tauri-based widget app, and a TypeScript/Vite frontend. -- evidence: [README.md#L325-L336](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L325-L336), [README.md#L291-L296](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L291-L296) (`clm_34c7a35859333be503af9fe809104237b728f45fd038b8d842ab9a712e8c9c0d`)
- [observation/documented] sem-hook is a thin wrapper invoked by AI tool hooks that parses optional JSON from stdin for session identifiers and then calls semctl set. -- evidence: [README.md#L205-L205](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L205-L205) (`clm_ae2430f76c7a82829e81ebe9494520e8c4761915bf97d2fe244154d230ee1e17`)
- [observation/documented] A Stream Deck plugin runs as a Node.js process, polls the Semaphore IPC socket every 500 ms with a status command, and updates key images, showing grey when the app is not running. -- evidence: [README.md#L435-L435](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L435-L435), [README.md#L477-L477](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L477-L477), [README.md#L437-L442](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L437-L442) (`clm_cc97f4500562f20ac515eee218795a7c2f0c0d4631d4eef6a5a5153f38e4629e`)

## design-choices (2 claim(s))

- [observation/documented] The state machine tracks one entry per session ID and picks the highest-priority color with red over yellow over green; setting green removes the session. -- evidence: [README.md#L277-L281](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L277-L281), [README.md#L283-L283](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L283-L283) (`clm_0da62a4f6e2dff83e439a228a1741f0e4fc345f1b746614338c03e8de243595c`)
- [observation/documented] Hooks always exit 0 so they never block the agent, and the installer merges hook entries using a _semaphore marker without overwriting unrelated hooks. -- evidence: [README.md#L156-L156](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L156-L156), [README.md#L205-L205](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L205-L205) (`clm_d17afce1cc2b920561cf16e5d7d8124e52e4f6b27a2cea1101820cfbbfac1ca0`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: building requires Rust stable, Node.js 20+, and npm (plus WebKit/GTK dev packages on Linux); tests run via cargo test and npm test (Vitest). -- evidence: [README.md#L378-L381](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L378-L381), [README.md#L348-L348](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L348-L348), [README.md#L344-L346](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L344-L346) (`clm_87a0866a6d2233955e009eb6d36e691a96d1000464f2e8a7d4a1e76976791d43`)
- [observation/documented] Repository development practice: tagging a version (e.g. git tag v0.2.0 and pushing) triggers a GitHub Actions release workflow that builds macOS arm64/x64, Linux x64, and Windows x64 artifacts. -- evidence: [README.md#L387-L390](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L387-L390), [README.md#L385-L385](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L385-L385), [README.md#L392-L392](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L392-L392) (`clm_9374b6f07783a4c253098df8da667a86a437bb12c1e635d311578e1a5e4e29c4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The semctl CLI supports set/status light control, install/uninstall of hooks, doctor diagnostics, and launch, and lives at ~/.semaphore/bin after install. -- evidence: [README.md#L162-L162](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L162-L162), [README.md#L190-L193](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L190-L193), [README.md#L181-L186](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L181-L186), [README.md#L175-L177](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L175-L177), [README.md#L166-L171](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L166-L171) (`clm_a2e809a2caddde58a68aa181dbbb9ae7d226a698ee4794f103e4ae068017f6b7`)
- [observation/documented] IPC is newline-delimited JSON over a Unix socket ($XDG_RUNTIME_DIR/semaphore.sock or /tmp/semaphore-<uid>.sock) or the Windows named pipe \\.\pipe\semaphore, with set and status commands. -- evidence: [README.md#L313-L315](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L313-L315), [README.md#L300-L300](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L300-L300), [README.md#L302-L303](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L302-L303), [README.md#L307-L309](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L307-L309), [README.md#L319-L321](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L319-L321) (`clm_040105d27c0e438e5c00bdaf5283ac978a64d1bdf7fce0fcd64ea65ccc515f6f`)
- [observation/documented] Environment variables SEMAPHORE_SOCKET, SEMAPHORE_BIN, and SEMAPHORE_SEMCTL override the IPC socket path and semctl binary locations. -- evidence: [README.md#L197-L201](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L197-L201) (`clm_c7651fe042752145b9309d66bc086638ff04bc6ef8050fb2b8d1366e36f3a5d2`)
- [observation/documented] The tray menu offers show/hide, settings, stealth toggle, always-on-top, horizontal layout, a light test melody, a Genius memory game, and quit; left-click shows or focuses the widget. -- evidence: [README.md#L113-L113](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L113-L113), [README.md#L101-L111](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L101-L111) (`clm_98ebb78cc71ab1b6da0eace379f004e047fa628670ba6d5c145fcc687dc5d66e`)

## memory-state (1 claim(s))

- [observation/documented] Stale sessions are pruned every 30 seconds after idle_timeout_secs (default 300 seconds) without updates; config is stored at ~/.semaphore/config.json. -- evidence: [README.md#L283-L283](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L283-L283), [README.md#L211-L211](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L211-L211), [README.md#L239-L250](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L239-L250) (`clm_326962af14fa99d3dd660304d5bfdeaca50e64b9f2e6a312edfd80da598f280b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The Stream Deck integration requires the Elgato Stream Deck app v6.0 or later on Windows or macOS, with Semaphore running in the background for the IPC socket. -- evidence: [README.md#L446-L447](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L446-L447) (`clm_29b62f0919d4228c5400cc339e0cf41f75e7dd1ad684d546af0170ae4d9c1038`)
- [observation/documented] The app supports hook-based integration with Cursor, Claude Code, Codex CLI, Gemini CLI, and Copilot CLI, each with documented config paths and semctl install commands. -- evidence: [README.md#L127-L133](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L127-L133) (`clm_8d985e97fd9c1cd575bdf7cd774a22f7e7f3d4255eea5e27e08af0a8645a507f`)

## limitations (3 claim(s))

- [observation/documented] Codex CLI support is limited: PreToolUse/PostToolUse hooks mainly fire for Bash, so the red light for file edits is limited; Copilot CLI support is partial and varies by version. -- evidence: [README.md#L127-L133](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L127-L133), [README.md#L150-L154](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L150-L154) (`clm_69b6b02c449c02f9d49fdaab308499481ade585786ce606ac536217b2827dc20`)
- [observation/documented] Stealth mode hides the widget from many capture tools but may still appear in some macOS 15+ apps (OS limitation) and depends on the compositor on Linux. -- evidence: [README.md#L504-L504](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L504-L504), [README.md#L506-L510](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L506-L510) (`clm_1513470eb2fcb5372a3e7ca36a2d56b3e73b3b1a9776a5fe54a47999fdd63da4`)
- [observation/documented] macOS releases are not yet Apple-notarized, so Gatekeeper may report the downloaded app as damaged until quarantine is removed. -- evidence: [README.md#L520-L520](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L520-L520) (`clm_5a6e9fcd0714fb131ed272fa867baf23a9d351d4b7b7b9ea4af0855d7a1701de`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

