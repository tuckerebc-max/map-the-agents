# timvw/tmux-assistant-resurrect -- full detail

[Back to orientation](tmux-assistant-resurrect.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/timvw/tmux-assistant-resurrect/4d740923614a522e984885a75041baf1bf1c6b5c/819817bffcc019b3.json](../../../wiki/dossiers/timvw/tmux-assistant-resurrect/4d740923614a522e984885a75041baf1bf1c6b5c/819817bffcc019b3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository contains a TPM plugin entry point, hook scripts for Claude/Cursor session tracking and cleanup, an OpenCode session-tracker plugin, and save/restore hook scripts under scripts/. -- evidence: [README.md#L158-L182](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L158-L182) (`clm_eddbfac44151134d0154d3e70ac8751f06ebb85505daf44d9c7af8c0c3bf7d6e`)

## design-choices (2 claim(s))

- [observation/documented] Assistant detection is done by taking a single ps snapshot, finding children of each tmux pane shell, and matching known assistant binary names such as claude, copilot, opencode, codex, pi, omp, and grok. -- evidence: [README.md#L57-L60](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L57-L60) (`clm_d5ca70b369b3dac6ea6e45ae0a645a5cb66535c66005fd29bd3bf306d631cef4`)
- [observation/documented] Each supported tool has a primary session-ID extraction method plus fallbacks (e.g. hook state files, process args, transcript or SQLite lookups) to handle cases where hooks have not yet fired after a restore. -- evidence: [README.md#L75-L78](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L75-L78), [README.md#L64-L73](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L64-L73) (`clm_c47a528f4cade39b27cd923adade4faf36585946df8d1c5759439f36797f2aa7`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the full test suite runs in Docker with real CLI binaries via 'just test', covering install, save, restore, uninstall, hooks, session ID extraction, and regression scenarios; fast hermetic suites exist for save hardening, restore, cursor, and plugin hardening. -- evidence: [README.md#L188-L188](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L188-L188), [README.md#L190-L192](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L190-L192), [README.md#L203-L211](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L203-L211), [README.md#L196-L201](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L196-L201) (`clm_6bab8e8645d9b365e849c0122f0feaae5159d6a340cc9e5a2a793fe8a7b8631a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The plugin exposes tmux options including @assistant-resurrect-capture-env for extra environment variables, per-tool and global drop-flags/drop-env exclusions, @assistant-resurrect-relaunch, and a save-timeout watchdog option. -- evidence: [README.md#L687-L689](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L687-L689), [README.md#L476-L478](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L476-L478), [README.md#L551-L554](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L551-L554), [README.md#L564-L567](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L564-L567), [README.md#L640-L640](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L640-L640) (`clm_7c28ede6b860bccaeb08fa5c8cedaa55f1ed530ffa995fee51ddf17f4188ef66`)
- [observation/documented] Session-less commands such as 'claude agents' are only relaunched if the user explicitly vouches the exact canonical command in a plain-text voucher file; restore reads the current voucher, never the sidecar value, and missing vouchers leave panes as bare shells. -- evidence: [README.md#L629-L634](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L629-L634), [README.md#L621-L627](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L621-L627), [README.md#L607-L610](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L607-L610) (`clm_11b73566a7f2715ef5d53706c983c00895b8f8c168dec5279eefc64dc41827fd`)

## memory-state (2 claim(s))

- [observation/documented] Session tracking files are written to $HOME/.local/state/tmux-assistant-resurrect on every platform; the path deliberately uses a plain $HOME literal so the assistant-side hook and tmux-server-side save hook agree even when their environments differ. -- evidence: [README.md#L421-L422](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L421-L422), [README.md#L424-L432](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L424-L432) (`clm_eb7f6b92f53837337a58f43e13abfc95062996f10da5313fade246aff13ab9e2`)
- [observation/documented] The save hook sweeps state files whose process has exited on every run, so the state directory does not grow without bound; the persistent sidecar assistant-sessions.json is what restore reads. -- evidence: [README.md#L448-L452](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L448-L452) (`clm_71395645f768abdd863a4e73ce3d0e39ecd736fa1d759025027c0aa4b3667977`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A Docker benchmark matrix measures save-hook performance, producing CSV and Markdown summaries in test-results/ and running on every push/PR in GitHub Actions with published step summaries and artifacts. -- evidence: [README.md#L217-L219](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L217-L219), [README.md#L215-L215](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L215-L215), [README.md#L230-L231](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L230-L231), [README.md#L233-L235](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L233-L235) (`clm_0fee14fdb77b10f2cae1af975bfbc5526b6f69cab61b4f81827abbc807df066c`)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are tmux (tested 3.4-3.7), TPM, jq, and at least one supported assistant CLI; the plugin also integrates with tmux-resurrect and tmux-continuum. -- evidence: [README.md#L98-L102](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L98-L102), [README.md#L82-L86](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L82-L86) (`clm_79199f603a043259d0c68cb23f64d22c70a30a9f777242e3fe58a18d2661e44f`)

## limitations (2 claim(s))

- [observation/documented] Credential-flag stripping matches flag names only, so a secret embedded inside an opaque value (e.g. inside a --settings JSON document) is persisted as written; protection relies on file permissions instead. -- evidence: [README.md#L535-L539](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L535-L539) (`clm_c87dc7d4735372f543545e2827b0e8d13a4352432c630ff5744436ea00cc8133`)
- [observation/documented] On macOS, reading another process's environment is not possible unprivileged, so hookless tools (Copilot, Codex, Pi, Oh My Pi, Grok) capture no extra environment variables at save time there; /proc-based capture works on Linux/WSL. -- evidence: [README.md#L492-L498](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L492-L498), [README.md#L500-L504](https://github.com/timvw/tmux-assistant-resurrect/blob/4d740923614a522e984885a75041baf1bf1c6b5c/README.md#L500-L504) (`clm_01606217d66b74f7db75c72ad19c6ff690d73ffd661fcb960a4f186ee94f1cb9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

