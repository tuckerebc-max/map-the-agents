---
access: public
aliases: []
claim_ids:
- clm_06e0dbd46664ed1d9c79c3e8fc24b8ddf772541e7de6da62154429f95110b5fc
- clm_3a6ffe09b53ab3335f02eb53ea0fca967a1b611290503c2cfa3f9e796656c7ce
- clm_3fc46f19495864502d04abb40d85a862cf3726ee243aff195f62973f5954d721
- clm_44331079c376013a27d99f61294eb18f19d9e5fe267ae56a734c9953a481a540
- clm_4f71d3eaf14a8b67b90842ea2abbd1536f6dd003919b1adeb9ba65afd87b733e
- clm_5c4cc40242278bcef3764eedbe513954a656a1b914a99a5120a08df94e31649a
- clm_6032897e5cc7d98bab7e9b8e9a6b4363cb29ea9c47b00757f704d0d1f4f58389
- clm_718f2d0f03822247d92fce2429792f8fda244d9219df1824c11684a8e8719e00
- clm_74c52ebfcfd9961d38e015505f601039c0bfb086441c160503a39b0025e2a896
- clm_7e006a36f54d73716fb27c29ffb551414f644b139bc7568daa3f4cd500536dc4
- clm_832d90395d1481406e81d3762fe90137ef7f65d0b498c11b5daae173fc003fad
- clm_e6e3569065d57049a44c6ea05da0a4d19a33844dc507a599ba5687207a2c6d0b
- clm_f55da37270386608e70c36267407f18c52354ebe18533e886ad85a2ec067a2cd
maturity: draft
page_id: pg_4a5da9c50232511d8f2c97943649321a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8d371595d4755a8ba2f8172c7dfb834b
title: minghinmatthewlam/pi-gui/README.md @ eb9a7380705d
updated_at: '2026-09-14T02:18:50Z'
---

# minghinmatthewlam/pi-gui/README.md @ eb9a7380705d

<!-- rcw:begin owner=source:src_8d371595d4755a8ba2f8172c7dfb834b block=evidence -->
- The app depends on @earendil-works/pi-coding-agent as its upstream runtime and uses node-pty for the integrated terminal. [@claim:clm_06e0dbd46664ed1d9c79c3e8fc24b8ddf772541e7de6da62154429f95110b5fc]
- Features include a threaded timeline with collapsible tool calls, an integrated node-pty terminal, an inline diff viewer toggled with Cmd/Ctrl+D, @-file mentions, image attachments, themes, and OS notifications when runs finish. [@claim:clm_3a6ffe09b53ab3335f02eb53ea0fca967a1b611290503c2cfa3f9e796656c7ce]
- Native computer use is not built into pi-gui; desktop/browser control is offered separately via the author's standalone computer-use-mcp server. [@claim:clm_3fc46f19495864502d04abb40d85a862cf3726ee243aff195f62973f5954d721]
- An orchestrator thread can spin up and supervise child worker threads, and each thread can run locally or in an isolated git worktree so parallel work does not collide. [@claim:clm_44331079c376013a27d99f61294eb18f19d9e5fe267ae56a734c9953a481a540]
- The renderer communicates with the main process only through a typed IPC surface exposed by the preload bridge, with no broad Node access granted to the renderer. [@claim:clm_4f71d3eaf14a8b67b90842ea2abbd1536f6dd003919b1adeb9ba65afd87b733e]
- Repository development practice: desktop changes are expected to be verified on the real Electron surface, not only by unit tests, and contributors must not delete session history or artifacts without approval. [@claim:clm_5c4cc40242278bcef3764eedbe513954a656a1b914a99a5120a08df94e31649a]
- pi persists each session as a JSONL transcript on disk, and pi-gui reads those files as the authoritative record for closed sessions instead of keeping a divergent copy. [@claim:clm_6032897e5cc7d98bab7e9b8e9a6b4363cb29ea9c47b00757f704d0d1f4f58389]
- pi-gui reuses pi's auth and session state, so provider credentials configured with the pi CLI carry over; providers connect via OAuth or API key in Settings. [@claim:clm_718f2d0f03822247d92fce2429792f8fda244d9219df1824c11684a8e8719e00]
- pi-gui is a Codex-style desktop app for the pi coding agent, in public beta for macOS (Apple Silicon) and Linux (AppImage). [@claim:clm_74c52ebfcfd9961d38e015505f601039c0bfb086441c160503a39b0025e2a896]
- The app is a UI shell around @earendil-works/pi-coding-agent rather than a separate agent runtime; session management, auth setup, and agent execution run through upstream pi. [@claim:clm_7e006a36f54d73716fb27c29ffb551414f644b139bc7568daa3f4cd500536dc4]
- Repository development practice: contributors use Node 20+ with pnpm via corepack, and run pnpm dev/build/typecheck/lint/test from the repo root; desktop E2E tests use a Playwright+Electron harness split into lanes, with the core lane run by default. [@claim:clm_832d90395d1481406e81d3762fe90137ef7f65d0b498c11b5daae173fc003fad]
- Supporting packages include pi-sdk-driver (a thin adapter to the pi coding agent), session-driver (shared session driver types), and catalogs (workspace/session catalog state). [@claim:clm_e6e3569065d57049a44c6ea05da0a4d19a33844dc507a599ba5687207a2c6d0b]
- The Electron app is split into a React renderer, a narrow preload IPC bridge, and a Node main process handling windowing, session supervision, worktrees, PTYs, notifications, and persistence. [@claim:clm_f55da37270386608e70c36267407f18c52354ebe18533e886ad85a2ec067a2cd]
<!-- rcw:end owner=source:src_8d371595d4755a8ba2f8172c7dfb834b block=evidence -->

## Researcher notes

