---
access: public
aliases: []
claim_ids:
- clm_01606217d66b74f7db75c72ad19c6ff690d73ffd661fcb960a4f186ee94f1cb9
- clm_0fee14fdb77b10f2cae1af975bfbc5526b6f69cab61b4f81827abbc807df066c
- clm_11b73566a7f2715ef5d53706c983c00895b8f8c168dec5279eefc64dc41827fd
- clm_6bab8e8645d9b365e849c0122f0feaae5159d6a340cc9e5a2a793fe8a7b8631a
- clm_71395645f768abdd863a4e73ce3d0e39ecd736fa1d759025027c0aa4b3667977
- clm_79199f603a043259d0c68cb23f64d22c70a30a9f777242e3fe58a18d2661e44f
- clm_7c28ede6b860bccaeb08fa5c8cedaa55f1ed530ffa995fee51ddf17f4188ef66
- clm_c47a528f4cade39b27cd923adade4faf36585946df8d1c5759439f36797f2aa7
- clm_c87dc7d4735372f543545e2827b0e8d13a4352432c630ff5744436ea00cc8133
- clm_d5ca70b369b3dac6ea6e45ae0a645a5cb66535c66005fd29bd3bf306d631cef4
- clm_eb7f6b92f53837337a58f43e13abfc95062996f10da5313fade246aff13ab9e2
- clm_eddbfac44151134d0154d3e70ac8751f06ebb85505daf44d9c7af8c0c3bf7d6e
maturity: draft
page_id: pg_77bd0a7ad5245586b98d05cc5fcd1414
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_83420083763d561d8bfa6086401cb304
title: timvw/tmux-assistant-resurrect/README.md @ 4d740923614a
updated_at: '2026-09-14T03:19:45Z'
---

# timvw/tmux-assistant-resurrect/README.md @ 4d740923614a

<!-- rcw:begin owner=source:src_83420083763d561d8bfa6086401cb304 block=evidence -->
- On macOS, reading another process's environment is not possible unprivileged, so hookless tools (Copilot, Codex, Pi, Oh My Pi, Grok) capture no extra environment variables at save time there; /proc-based capture works on Linux/WSL. [@claim:clm_01606217d66b74f7db75c72ad19c6ff690d73ffd661fcb960a4f186ee94f1cb9]
- A Docker benchmark matrix measures save-hook performance, producing CSV and Markdown summaries in test-results/ and running on every push/PR in GitHub Actions with published step summaries and artifacts. [@claim:clm_0fee14fdb77b10f2cae1af975bfbc5526b6f69cab61b4f81827abbc807df066c]
- Session-less commands such as 'claude agents' are only relaunched if the user explicitly vouches the exact canonical command in a plain-text voucher file; restore reads the current voucher, never the sidecar value, and missing vouchers leave panes as bare shells. [@claim:clm_11b73566a7f2715ef5d53706c983c00895b8f8c168dec5279eefc64dc41827fd]
- Repository development practice: the full test suite runs in Docker with real CLI binaries via 'just test', covering install, save, restore, uninstall, hooks, session ID extraction, and regression scenarios; fast hermetic suites exist for save hardening, restore, cursor, and plugin hardening. [@claim:clm_6bab8e8645d9b365e849c0122f0feaae5159d6a340cc9e5a2a793fe8a7b8631a]
- The save hook sweeps state files whose process has exited on every run, so the state directory does not grow without bound; the persistent sidecar assistant-sessions.json is what restore reads. [@claim:clm_71395645f768abdd863a4e73ce3d0e39ecd736fa1d759025027c0aa4b3667977]
- Prerequisites are tmux (tested 3.4-3.7), TPM, jq, and at least one supported assistant CLI; the plugin also integrates with tmux-resurrect and tmux-continuum. [@claim:clm_79199f603a043259d0c68cb23f64d22c70a30a9f777242e3fe58a18d2661e44f]
- The plugin exposes tmux options including @assistant-resurrect-capture-env for extra environment variables, per-tool and global drop-flags/drop-env exclusions, @assistant-resurrect-relaunch, and a save-timeout watchdog option. [@claim:clm_7c28ede6b860bccaeb08fa5c8cedaa55f1ed530ffa995fee51ddf17f4188ef66]
- Each supported tool has a primary session-ID extraction method plus fallbacks (e.g. hook state files, process args, transcript or SQLite lookups) to handle cases where hooks have not yet fired after a restore. [@claim:clm_c47a528f4cade39b27cd923adade4faf36585946df8d1c5759439f36797f2aa7]
- Credential-flag stripping matches flag names only, so a secret embedded inside an opaque value (e.g. inside a --settings JSON document) is persisted as written; protection relies on file permissions instead. [@claim:clm_c87dc7d4735372f543545e2827b0e8d13a4352432c630ff5744436ea00cc8133]
- Assistant detection is done by taking a single ps snapshot, finding children of each tmux pane shell, and matching known assistant binary names such as claude, copilot, opencode, codex, pi, omp, and grok. [@claim:clm_d5ca70b369b3dac6ea6e45ae0a645a5cb66535c66005fd29bd3bf306d631cef4]
- Session tracking files are written to $HOME/.local/state/tmux-assistant-resurrect on every platform; the path deliberately uses a plain $HOME literal so the assistant-side hook and tmux-server-side save hook agree even when their environments differ. [@claim:clm_eb7f6b92f53837337a58f43e13abfc95062996f10da5313fade246aff13ab9e2]
- The repository contains a TPM plugin entry point, hook scripts for Claude/Cursor session tracking and cleanup, an OpenCode session-tracker plugin, and save/restore hook scripts under scripts/. [@claim:clm_eddbfac44151134d0154d3e70ac8751f06ebb85505daf44d9c7af8c0c3bf7d6e]
<!-- rcw:end owner=source:src_83420083763d561d8bfa6086401cb304 block=evidence -->

## Researcher notes

