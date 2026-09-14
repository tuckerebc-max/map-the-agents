# sahithvibudhi/vibe-tree -- full detail

[Back to orientation](vibe-tree.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sahithvibudhi/vibe-tree/f88907703af1d9b287c5dd1ae93c01645c7dab78/b3c79a6d3c9ac605.json](../../../wiki/dossiers/sahithvibudhi/vibe-tree/f88907703af1d9b287c5dd1ae93c01645c7dab78/b3c79a6d3c9ac605.json)

## specifications (1 claim(s))

- [observation/documented] VibeTree runs each AI coding agent in its own git worktree in parallel, giving every task an isolated checkout with its own branch and terminal. -- evidence: [README.md#L6-L6](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L6-L6), [README.md#L20-L20](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L20-L20) (`clm_205f718d29f83017b4dd1053175d525326c958d35a7637161c44bdc52bd82bda`)

## components (2 claim(s))

- [observation/documented] The repo is a pnpm + Turborepo monorepo with apps (desktop, web, server) and packages (core, server-core, ui, auth), where desktop and web share one backend. -- evidence: [ARCHITECTURE.md#L9-L25](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L9-L25), [ARCHITECTURE.md#L5-L5](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L5-L5) (`clm_a44f0c79ca66c5d069a7fed306baef60599721a5dd1dee1868cc18e6aa689789`)
- [observation/documented] ShellSessionManager in packages/core owns all PTYs, one per worktree+terminal, buffering bounded (~100KB) output for replay on reconnect. -- evidence: [ARCHITECTURE.md#L29-L41](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L29-L41), [ARCHITECTURE.md#L51-L55](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L51-L55), [ARCHITECTURE.md#L49-L49](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L49-L49) (`clm_b865c942a485e261dccbb5de74fbaebe92e34c7b134ffbcac9a65e3497e748e4`)

## design-choices (2 claim(s))

- [observation/documented] Worktree lifecycle hooks (.vibetree/hooks/post-create and pre-remove) run around git worktree add/remove; failures warn but never block, and pre-remove cannot block deletion. -- evidence: [ARCHITECTURE.md#L59-L59](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L59-L59), [README.md#L75-L75](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L75-L75) (`clm_db6fedb16fd6d15dffc4b1d1aa9c491ac9f2c450f8e6a2406264bd173e66ceb5`)
- [observation/documented] Electron IPC is reserved for native OS concerns (dialogs, notifications, theme, IDE launching, settings, menus), while app logic goes through the embedded server over WebSocket. -- evidence: [ARCHITECTURE.md#L43-L45](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L43-L45) (`clm_aaa5312f9f39baa65d5b282b8f736630451866492506c76c26ee1375ac01d675`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run pnpm install, pnpm dev:desktop/dev:all, unit tests via pnpm test:run, Playwright e2e suites, and pnpm typecheck && pnpm lint; CI runs lint, typecheck, unit tests, builds, and e2e. -- evidence: [README.md#L84-L92](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L84-L92), [ARCHITECTURE.md#L72-L74](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L72-L74) (`clm_038be0631a5b316ce43a12c48361046d211de994430d6a8a7bf263b734a821e9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product works with terminal-based agent CLIs including Claude Code, OpenAI Codex CLI, Gemini CLI, Aider, and opencode, since agents run in a real terminal. -- evidence: [README.md#L54-L63](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L54-L63), [README.md#L12-L12](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L12-L12) (`clm_78a0f40fdd92ef82d64cf8bb0182e42bd399a308354d37e7387ed4cfd7536611`)
- [observation/documented] It ships as an Electron desktop app and as a standalone server drivable from any browser or phone, including QR pairing for mobile access. -- evidence: [ARCHITECTURE.md#L9-L25](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L9-L25), [README.md#L54-L63](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L54-L63), [README.md#L20-L20](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L20-L20) (`clm_e665bba61dedeba4332280ee61f483389303b23b9c92b03eeba5dd0307ce192e`)
- [observation/documented] All shell and git traffic uses a single WebSocket protocol (shell:* and git:* messages) via a shared WebSocketAdapter used by both desktop renderer and web app. -- evidence: [ARCHITECTURE.md#L43-L45](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L43-L45) (`clm_ce7a94b59158215c517165eb840a3daefebfdd24819507bcbff0e75e30d942f5`)

## memory-state (2 claim(s))

- [observation/documented] Terminal sessions survive disconnects: session IDs are deterministic per worktree path and terminal ID, output is buffered from PTY start, and reattach returns the scrollback. -- evidence: [ARCHITECTURE.md#L51-L55](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L51-L55) (`clm_8fb9f574f371febe578a617ec7c39e2a18a695554bbaf486f6238a6a4c045ada`)
- [observation/documented] The standalone server reaps sessions idle beyond SESSION_IDLE_TIMEOUT_MS (default 24h), while the desktop keeps sessions until quit. -- evidence: [ARCHITECTURE.md#L51-L55](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L51-L55) (`clm_120f33a32db1906d70eb6c1aca5d13617c1a12398a21dae3bedbbfb481bfd98b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The desktop app embeds its server on 127.0.0.1 with a per-launch token so nothing is exposed to the network; the standalone server can require login via AUTH_REQUIRED, VIBETREE_USERNAME, and VIBETREE_PASSWORD. -- evidence: [ARCHITECTURE.md#L65-L68](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L65-L68), [README.md#L79-L80](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L79-L80) (`clm_6bbfe589dc93ac98ce2be6097884687e70eaa6e5474380c79c60a604e33c1847`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Build tooling documented includes esbuild bundles for core/ui/auth, tsc for server-core and apps/server, Vite for desktop renderer and web, electron-builder packaging, and vite-plugin-pwa. -- evidence: [ARCHITECTURE.md#L78-L81](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L78-L81) (`clm_74a17aba42834e1f0e713c9438b121100c15d01e0ba6464f2cc54d8e68a9ae54`)

## limitations (2 claim(s))

- [observation/documented] macOS builds are not yet notarized; users must approve the app once under System Settings, Privacy and Security, or install via the provided Homebrew cask. -- evidence: [README.md#L38-L38](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L38-L38) (`clm_570f150a49075883bf351b0166be5dd84cc2af6c1288cccc544c302a1751003d`)
- [observation/documented] Authentication is off by default; the standalone server runs unauthenticated in its default mode and only warns when bound to 0.0.0.0 without auth. -- evidence: [ARCHITECTURE.md#L63-L63](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L63-L63), [ARCHITECTURE.md#L65-L68](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L65-L68) (`clm_d97f765257bbed3b802b64d586ca3a8f2a6139b8d4888e3b87cc5e68fd6466db`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

