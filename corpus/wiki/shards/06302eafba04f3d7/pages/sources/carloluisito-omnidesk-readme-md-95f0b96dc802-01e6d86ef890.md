---
access: public
aliases: []
claim_ids:
- clm_36f87aa766b03a2dd8e163633d39c1c766ad46882a36a0c4a77469899aa99780
- clm_4129a57d88a35ec32cfd20b627ea4fab40f8bbf850943a8e8e1d6b34e18930e5
- clm_5607cd0526382b6778a7e55d041d78788cb3e7cfb029d51c350c63eeb72269c0
- clm_60203a0fedd7c475279849434b9a9433a0c0dc0c1285a3d2bf440b8777c302ce
- clm_812bbb8f74009f764a06bb85719779428acffe523c053e15afc58321e9aed6a7
- clm_8d527ad052bb3e8923dbc3c625b5c9d7795ee4eaf86d81ef2642b46ed882965a
- clm_910b9529803912bbea8772b761ab85c2394c7108e82dd87c3f0405e677a6d994
- clm_9ea9712bd92b1b04dfc818781258946f202613d980a78774c1f4cc9861934cd0
- clm_a8d75c833707851e7c262afbcc8c99eb7021e9c21ca4d13fc5dbd87cc36886d1
- clm_ae2e2aeb7a172232e09ecac579e49a8b01144040de3c388785b2076d89d803c7
- clm_ba2b2eced0792e57cdf6217158c7fbadc2532f24f80129fb0834d784db55c8ce
- clm_dc2846740053baf383e808b6c2fb7d22851b58d72fad40839f075d617ca0ada7
- clm_de25b3c7ca452a91f22b6e293776f2caf1d3b0300f3178128bf60bfaed9f898b
- clm_e104d304af0b1f30eca8c736b86e863c5138c48fbd5927014346ca5952e7fffe
- clm_e768f9ec548bf1d2bfe367603ce055fe8a7fa47538a26dd8b27cdc4f9352115e
maturity: draft
page_id: pg_40a9f2ad4b125f5584ea01e6d86ef890
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f8adcb7025ae5ac1a0061f4cc0212916
title: carloluisito/omnidesk/README.md @ 95f0b96dc802
updated_at: '2026-09-14T01:39:39Z'
---

# carloluisito/omnidesk/README.md @ 95f0b96dc802

<!-- rcw:begin owner=source:src_f8adcb7025ae5ac1a0061f4cc0212916 block=evidence -->
- Remote access serves the same UI from a browser over a one-click managed Cloudflare tunnel, bound to 127.0.0.1 only with its own access token (cookie plus WebSocket check), off by default, with a QR sign-in and installable PWA. [@claim:clm_36f87aa766b03a2dd8e163633d39c1c766ad46882a36a0c4a77469899aa99780]
- The project is local-first and telemetry-free: session data stays on the machine, and network calls are limited to Anthropic's quota API, GitHub update checks, configured git remotes, and a one-time consented Hugging Face voice-model download. [@claim:clm_4129a57d88a35ec32cfd20b627ea4fab40f8bbf850943a8e8e1d6b34e18930e5]
- OmniDesk is an Electron 28 desktop app using React 18 + TypeScript, xterm.js with node-pty for terminals, Tailwind CSS styling, and Vite with electron-builder for building. [@claim:clm_5607cd0526382b6778a7e55d041d78788cb3e7cfb029d51c350c63eeb72269c0]
- Repository development practice: development uses npm run electron:dev for hot-reload dev mode, npm test for the 1418-test Vitest suite, npm run test:e2e for Playwright E2E tests requiring a built app, and npm run test:coverage for coverage. [@claim:clm_60203a0fedd7c475279849434b9a9433a0c0dc0c1285a3d2bf440b8777c302ce]
- No agent/task performance evaluation (benchmarks or success-rate metrics) appears in the evidence; the 1418 Vitest tests and Playwright suite are the repository's own test suite, not an eval harness. [@claim:clm_812bbb8f74009f764a06bb85719779428acffe523c053e15afc58321e9aed6a7]
- Documented platform caveats: Windows uses cmd.exe as the default shell so claude must be on PATH, macOS 10.13+ is required, and Linux may need libxtst6 and libnss3 packages. [@claim:clm_8d527ad052bb3e8923dbc3c625b5c9d7795ee4eaf86d81ef2642b46ed882965a]
- For Claude sessions, a per-session launch mode picker offers claude, claude --dangerously-skip-permissions, or claude agents, gated by an automatic CLI availability probe at creation time. [@claim:clm_910b9529803912bbea8772b761ab85c2394c7108e82dd87c3f0405e677a6d994]
- Sessions can run on a new git worktree/branch, an existing branch, or the current checkout, with git status, branch, and worktree operations handled in the main process and optional worktree cleanup on session close. [@claim:clm_9ea9712bd92b1b04dfc818781258946f202613d980a78774c1f4cc9861934cd0]
- Prerequisites are Node.js 20+ and the Claude Code CLI (installed globally via npm), with Claude API credentials read from ~/.claude/.credentials.json; the Codex CLI is optional and auto-detected. [@claim:clm_a8d75c833707851e7c262afbcc8c99eb7021e9c21ca4d13fc5dbd87cc36886d1]
- Repository development practice: contributors are directed to CONTRIBUTING.md for guidelines and a Code of Conduct, with bug reports and feature requests via GitHub issue templates; the repo workflow requires worktree-per-task branching from an up-to-date main. [@claim:clm_ae2e2aeb7a172232e09ecac579e49a8b01144040de3c388785b2076d89d803c7]
- Multiple concurrent sessions per repository are supported, with a pre-warmed session pool for fast creation, session persistence across app restarts, and auto-renaming of unnamed sessions to the agent's live task summary from the CLI terminal title. [@claim:clm_ba2b2eced0792e57cdf6217158c7fbadc2532f24f80129fb0834d784db55c8ce]
- The app exposes keyboard-driven interfaces: Ctrl/Cmd+K command palette, Ctrl/Cmd+J attention cockpit, Ctrl/Cmd+Shift+K repo switcher, Ctrl/Cmd+1/2 for Focus/Grid views, and Ctrl+Shift+Space for voice dictation. [@claim:clm_dc2846740053baf383e808b6c2fb7d22851b58d72fad40839f075d617ca0ada7]
- A Session History Explorer stores past-session transcripts with cross-session content search, Markdown/JSON export, deletion, storage stats, retention policy, plus a Checkpoints panel for named session checkpoints. [@claim:clm_de25b3c7ca452a91f22b6e293776f2caf1d3b0300f3178128bf60bfaed9f898b]
- The IPC contract file is treated as the single source of truth, auto-deriving channels, preload bridge methods, and TypeScript types; a provider abstraction (IProvider) decouples CLI specifics from session management. [@claim:clm_e104d304af0b1f30eca8c736b86e863c5138c48fbd5927014346ca5952e7fffe]
- The architecture is a three-layer pattern per domain: managers in the Electron main process, hooks in the renderer, and shell components, connected via roughly 115 IPC methods through an auto-derived preload bridge. [@claim:clm_e768f9ec548bf1d2bfe367603ce055fe8a7fa47538a26dd8b27cdc4f9352115e]
<!-- rcw:end owner=source:src_f8adcb7025ae5ac1a0061f4cc0212916 block=evidence -->

## Researcher notes

