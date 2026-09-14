# supabitapp/supacode -- full detail

[Back to orientation](supacode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/supabitapp/supacode/81cba5538f1e9618308dfea89dbd424b908ed0d7/66b194affe240b6a.json](../../../wiki/dossiers/supabitapp/supacode/81cba5538f1e9618308dfea89dbd424b908ed0d7/66b194affe240b6a.json)

## specifications (1 claim(s))

- [observation/documented] Supacode is a native macOS application (macOS 26.0+ required) that acts as a command center for running coding agents in parallel. -- evidence: [README.md#L3-L3](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L3-L3), [README.md#L73-L76](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L73-L76) (`clm_48b385d754319bff29becc4179c6723523812ddeb10ed4b5e8e1cff98cdc9a75`)

## components (5 claim(s))

- [observation/documented] Remote SSH repositories are supported in beta: git probes and terminals share one multiplexed SSH connection, and with zmx on the host, remote sessions survive dropped connections and sleep. -- evidence: [README.md#L31-L35](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L31-L35) (`clm_efcc6ae171408e9bb261b1a8236a8fc211f10be1aa829a8eff985b5f2f538449`)
- [observation/documented] The app detects the coding agent per pane (busy, awaiting input, idle) via installed hooks, supporting Claude, Codex, and Copilot locally and over SSH, and drives notifications. -- evidence: [README.md#L45-L47](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L45-L47) (`clm_d5a7b591406a7b56b73604c4bc37ab25a0676b514e26b453f693b7a76dc094aa`)
- [observation/documented] Plain folders are first-class alongside git repos, getting a persistent terminal with tabs, scripts, and pinning but without git-only tools; remote URLs can be cloned into a folder. -- evidence: [README.md#L39-L41](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L39-L41) (`clm_3e6ade29cc1fa6f941efcaaa365948cd4e3ecf6f380355301efb2c4541a9d5a4`)
- [observation/documented] Terminal rendering uses libghostty with tabs, splits, per-surface backgrounds, and theme sync; auto-updates come through Sparkle with a selectable channel. -- evidence: [README.md#L58-L69](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L58-L69), [README.md#L128-L130](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L128-L130) (`clm_fbd2c36d4c3662bb20f026d01467ae112b5cb0ef9fae0dfe63eb0e6a792f7104`)
- [observation/documented] With GitHub integration enabled, each worktree's PR state, checks, and merge readiness display in the sidebar and refresh live with a configurable merge strategy. -- evidence: [README.md#L58-L69](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L58-L69) (`clm_e9f9f2cc74f20d628e884dc302b8f6db8d319e9f5ce0e1d0789172f7f56c5286`)

## design-choices (1 claim(s))

- [observation/documented] Each task gets its own git worktree and real terminal so agents run in parallel without colliding; worktrees can be created from the sidebar, hotkey, command palette, CLI, or deeplink. -- evidence: [README.md#L5-L7](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L5-L7), [README.md#L17-L21](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L17-L21) (`clm_efd1bb32ede8674e3d21bf6832a8092f258a99af4fdaab2dd71da7d9c011ad88`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use mise for a pinned toolchain, git submodules, and make targets (doctor, build-ghostty-xcframework, build-app, run-app); on macOS 26.4+ Xcode 26.3 is needed because the pinned Zig 0.15.2 linker cannot link that SDK. -- evidence: [README.md#L94-L98](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L94-L98), [README.md#L80-L86](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L80-L86), [README.md#L102-L108](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L102-L108), [README.md#L73-L76](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L73-L76) (`clm_758b40717cbc9dcbcf1720de55c49469e07c1d43675592a097640d4ebaa68915`)
- [observation/documented] Repository development practice: contributions require opening an issue first, waiting for a `ready` label, then a focused linked PR; a human, never an AI agent, must be the accountable author, and code follows Swift 6/TCA style rules checked by `make check`. -- evidence: [README.md#L120-L124](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L120-L124), [AGENTS.md#L24-L39](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/AGENTS.md#L24-L39), [AGENTS.md#L51-L55](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/AGENTS.md#L51-L55), [README.md#L134-L137](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L134-L137) (`clm_f6e32765a27d77f4a7b859e4b7fa018a79ab2107199e41f1cbff84b6f7a47b33`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A `supacode` CLI manages worktrees, tabs, splits, and repos; sessions export repo, worktree, tab, and surface IDs, and `supacode://` deeplinks mirror CLI actions. -- evidence: [README.md#L51-L54](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L51-L54) (`clm_1ca17220c02cf118c478f77e87464e44a03671b15f270792a0d3810537f52b85`)

## memory-state (1 claim(s))

- [observation/documented] Sessions run inside zmx, a session daemon, rather than as app children, so quitting and relaunching reattaches sessions with scrollback; this is on by default with an optional teardown quit. -- evidence: [README.md#L25-L27](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L25-L27) (`clm_6e34f8bfa3b5989771a5febc10c07025fa8b4c72ae26bc09f9adc23b33bd62fc`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Key dependencies include The Composable Architecture for app state, GhosttyKit as the terminal emulator, Sparkle for updates, PostHog for analytics, and Sentry for error tracking. -- evidence: [README.md#L128-L130](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/README.md#L128-L130), [AGENTS.md#L15-L20](https://github.com/supabitapp/supacode/blob/81cba5538f1e9618308dfea89dbd424b908ed0d7/AGENTS.md#L15-L20) (`clm_7c2c27d715b8bd31b8112f00542baa3a50f5307df3d4aab7ed85cd430168ac74`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

