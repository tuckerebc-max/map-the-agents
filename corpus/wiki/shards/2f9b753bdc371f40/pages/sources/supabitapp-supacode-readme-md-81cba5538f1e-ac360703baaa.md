---
access: public
aliases: []
claim_ids:
- clm_1ca17220c02cf118c478f77e87464e44a03671b15f270792a0d3810537f52b85
- clm_3e6ade29cc1fa6f941efcaaa365948cd4e3ecf6f380355301efb2c4541a9d5a4
- clm_48b385d754319bff29becc4179c6723523812ddeb10ed4b5e8e1cff98cdc9a75
- clm_6e34f8bfa3b5989771a5febc10c07025fa8b4c72ae26bc09f9adc23b33bd62fc
- clm_758b40717cbc9dcbcf1720de55c49469e07c1d43675592a097640d4ebaa68915
- clm_7c2c27d715b8bd31b8112f00542baa3a50f5307df3d4aab7ed85cd430168ac74
- clm_d5a7b591406a7b56b73604c4bc37ab25a0676b514e26b453f693b7a76dc094aa
- clm_e9f9f2cc74f20d628e884dc302b8f6db8d319e9f5ce0e1d0789172f7f56c5286
- clm_efcc6ae171408e9bb261b1a8236a8fc211f10be1aa829a8eff985b5f2f538449
- clm_efd1bb32ede8674e3d21bf6832a8092f258a99af4fdaab2dd71da7d9c011ad88
- clm_f6e32765a27d77f4a7b859e4b7fa018a79ab2107199e41f1cbff84b6f7a47b33
- clm_fbd2c36d4c3662bb20f026d01467ae112b5cb0ef9fae0dfe63eb0e6a792f7104
maturity: draft
page_id: pg_3feb306bb7e952e9be92ac360703baaa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_464ab6303eae54498ea24394368c4b63
title: supabitapp/supacode/README.md @ 81cba5538f1e
updated_at: '2026-09-14T03:15:34Z'
---

# supabitapp/supacode/README.md @ 81cba5538f1e

<!-- rcw:begin owner=source:src_464ab6303eae54498ea24394368c4b63 block=evidence -->
- A `supacode` CLI manages worktrees, tabs, splits, and repos; sessions export repo, worktree, tab, and surface IDs, and `supacode://` deeplinks mirror CLI actions. [@claim:clm_1ca17220c02cf118c478f77e87464e44a03671b15f270792a0d3810537f52b85]
- Plain folders are first-class alongside git repos, getting a persistent terminal with tabs, scripts, and pinning but without git-only tools; remote URLs can be cloned into a folder. [@claim:clm_3e6ade29cc1fa6f941efcaaa365948cd4e3ecf6f380355301efb2c4541a9d5a4]
- Supacode is a native macOS application (macOS 26.0+ required) that acts as a command center for running coding agents in parallel. [@claim:clm_48b385d754319bff29becc4179c6723523812ddeb10ed4b5e8e1cff98cdc9a75]
- Sessions run inside zmx, a session daemon, rather than as app children, so quitting and relaunching reattaches sessions with scrollback; this is on by default with an optional teardown quit. [@claim:clm_6e34f8bfa3b5989771a5febc10c07025fa8b4c72ae26bc09f9adc23b33bd62fc]
- Repository development practice: contributors use mise for a pinned toolchain, git submodules, and make targets (doctor, build-ghostty-xcframework, build-app, run-app); on macOS 26.4+ Xcode 26.3 is needed because the pinned Zig 0.15.2 linker cannot link that SDK. [@claim:clm_758b40717cbc9dcbcf1720de55c49469e07c1d43675592a097640d4ebaa68915]
- Key dependencies include The Composable Architecture for app state, GhosttyKit as the terminal emulator, Sparkle for updates, PostHog for analytics, and Sentry for error tracking. [@claim:clm_7c2c27d715b8bd31b8112f00542baa3a50f5307df3d4aab7ed85cd430168ac74]
- The app detects the coding agent per pane (busy, awaiting input, idle) via installed hooks, supporting Claude, Codex, and Copilot locally and over SSH, and drives notifications. [@claim:clm_d5a7b591406a7b56b73604c4bc37ab25a0676b514e26b453f693b7a76dc094aa]
- With GitHub integration enabled, each worktree's PR state, checks, and merge readiness display in the sidebar and refresh live with a configurable merge strategy. [@claim:clm_e9f9f2cc74f20d628e884dc302b8f6db8d319e9f5ce0e1d0789172f7f56c5286]
- Remote SSH repositories are supported in beta: git probes and terminals share one multiplexed SSH connection, and with zmx on the host, remote sessions survive dropped connections and sleep. [@claim:clm_efcc6ae171408e9bb261b1a8236a8fc211f10be1aa829a8eff985b5f2f538449]
- Each task gets its own git worktree and real terminal so agents run in parallel without colliding; worktrees can be created from the sidebar, hotkey, command palette, CLI, or deeplink. [@claim:clm_efd1bb32ede8674e3d21bf6832a8092f258a99af4fdaab2dd71da7d9c011ad88]
- Repository development practice: contributions require opening an issue first, waiting for a `ready` label, then a focused linked PR; a human, never an AI agent, must be the accountable author, and code follows Swift 6/TCA style rules checked by `make check`. [@claim:clm_f6e32765a27d77f4a7b859e4b7fa018a79ab2107199e41f1cbff84b6f7a47b33]
- Terminal rendering uses libghostty with tabs, splits, per-surface backgrounds, and theme sync; auto-updates come through Sparkle with a selectable channel. [@claim:clm_fbd2c36d4c3662bb20f026d01467ae112b5cb0ef9fae0dfe63eb0e6a792f7104]
<!-- rcw:end owner=source:src_464ab6303eae54498ea24394368c4b63 block=evidence -->

## Researcher notes

