---
access: public
aliases: []
claim_ids:
- clm_038be0631a5b316ce43a12c48361046d211de994430d6a8a7bf263b734a821e9
- clm_120f33a32db1906d70eb6c1aca5d13617c1a12398a21dae3bedbbfb481bfd98b
- clm_6bbfe589dc93ac98ce2be6097884687e70eaa6e5474380c79c60a604e33c1847
- clm_74a17aba42834e1f0e713c9438b121100c15d01e0ba6464f2cc54d8e68a9ae54
- clm_8fb9f574f371febe578a617ec7c39e2a18a695554bbaf486f6238a6a4c045ada
- clm_a44f0c79ca66c5d069a7fed306baef60599721a5dd1dee1868cc18e6aa689789
- clm_aaa5312f9f39baa65d5b282b8f736630451866492506c76c26ee1375ac01d675
- clm_b865c942a485e261dccbb5de74fbaebe92e34c7b134ffbcac9a65e3497e748e4
- clm_ce7a94b59158215c517165eb840a3daefebfdd24819507bcbff0e75e30d942f5
- clm_d97f765257bbed3b802b64d586ca3a8f2a6139b8d4888e3b87cc5e68fd6466db
- clm_db6fedb16fd6d15dffc4b1d1aa9c491ac9f2c450f8e6a2406264bd173e66ceb5
- clm_e665bba61dedeba4332280ee61f483389303b23b9c92b03eeba5dd0307ce192e
maturity: draft
page_id: pg_2758018b680b597aa36a0911fc30d9db
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fd2505662b675f9397e819aa770d9968
title: sahithvibudhi/vibe-tree/ARCHITECTURE.md @ f88907703af1
updated_at: '2026-09-14T02:38:42Z'
---

# sahithvibudhi/vibe-tree/ARCHITECTURE.md @ f88907703af1

<!-- rcw:begin owner=source:src_fd2505662b675f9397e819aa770d9968 block=evidence -->
- Repository development practice: contributors run pnpm install, pnpm dev:desktop/dev:all, unit tests via pnpm test:run, Playwright e2e suites, and pnpm typecheck && pnpm lint; CI runs lint, typecheck, unit tests, builds, and e2e. [@claim:clm_038be0631a5b316ce43a12c48361046d211de994430d6a8a7bf263b734a821e9]
- The standalone server reaps sessions idle beyond SESSION_IDLE_TIMEOUT_MS (default 24h), while the desktop keeps sessions until quit. [@claim:clm_120f33a32db1906d70eb6c1aca5d13617c1a12398a21dae3bedbbfb481bfd98b]
- The desktop app embeds its server on 127.0.0.1 with a per-launch token so nothing is exposed to the network; the standalone server can require login via AUTH_REQUIRED, VIBETREE_USERNAME, and VIBETREE_PASSWORD. [@claim:clm_6bbfe589dc93ac98ce2be6097884687e70eaa6e5474380c79c60a604e33c1847]
- Build tooling documented includes esbuild bundles for core/ui/auth, tsc for server-core and apps/server, Vite for desktop renderer and web, electron-builder packaging, and vite-plugin-pwa. [@claim:clm_74a17aba42834e1f0e713c9438b121100c15d01e0ba6464f2cc54d8e68a9ae54]
- Terminal sessions survive disconnects: session IDs are deterministic per worktree path and terminal ID, output is buffered from PTY start, and reattach returns the scrollback. [@claim:clm_8fb9f574f371febe578a617ec7c39e2a18a695554bbaf486f6238a6a4c045ada]
- The repo is a pnpm + Turborepo monorepo with apps (desktop, web, server) and packages (core, server-core, ui, auth), where desktop and web share one backend. [@claim:clm_a44f0c79ca66c5d069a7fed306baef60599721a5dd1dee1868cc18e6aa689789]
- Electron IPC is reserved for native OS concerns (dialogs, notifications, theme, IDE launching, settings, menus), while app logic goes through the embedded server over WebSocket. [@claim:clm_aaa5312f9f39baa65d5b282b8f736630451866492506c76c26ee1375ac01d675]
- ShellSessionManager in packages/core owns all PTYs, one per worktree+terminal, buffering bounded (~100KB) output for replay on reconnect. [@claim:clm_b865c942a485e261dccbb5de74fbaebe92e34c7b134ffbcac9a65e3497e748e4]
- All shell and git traffic uses a single WebSocket protocol (shell:* and git:* messages) via a shared WebSocketAdapter used by both desktop renderer and web app. [@claim:clm_ce7a94b59158215c517165eb840a3daefebfdd24819507bcbff0e75e30d942f5]
- Authentication is off by default; the standalone server runs unauthenticated in its default mode and only warns when bound to 0.0.0.0 without auth. [@claim:clm_d97f765257bbed3b802b64d586ca3a8f2a6139b8d4888e3b87cc5e68fd6466db]
- Worktree lifecycle hooks (.vibetree/hooks/post-create and pre-remove) run around git worktree add/remove; failures warn but never block, and pre-remove cannot block deletion. [@claim:clm_db6fedb16fd6d15dffc4b1d1aa9c491ac9f2c450f8e6a2406264bd173e66ceb5]
- It ships as an Electron desktop app and as a standalone server drivable from any browser or phone, including QR pairing for mobile access. [@claim:clm_e665bba61dedeba4332280ee61f483389303b23b9c92b03eeba5dd0307ce192e]
<!-- rcw:end owner=source:src_fd2505662b675f9397e819aa770d9968 block=evidence -->

## Researcher notes

