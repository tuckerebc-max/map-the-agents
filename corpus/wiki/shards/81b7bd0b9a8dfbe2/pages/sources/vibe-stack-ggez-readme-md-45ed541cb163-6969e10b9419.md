---
access: public
aliases: []
claim_ids:
- clm_250a47935a151d4b1d95bd63a1172838b9249f0e4698739db1b5b2c801e2ebd0
- clm_2a53e6b88617a7e5c612f36a03a4fbe717e355ade585c208bc5b741e956646fd
- clm_450c65e7a74de4e0be6d43daa65f641bf11259b71e52d1b310ef2ba63af0ebc9
- clm_512a636f795cb3d6a44f14b6d134c2099184b7d5e23f9faa77a375a5fb6aae6f
- clm_5608e00cb7500a2b2ff7c81c01711d5acac8f0ccfd4cc4a78318d041ac3ba27d
- clm_6405069baf337b6c2ad6e8828bd03119e7983730f08d7d5d08b5c9141ca5edf4
- clm_66868d2105ceab751d0218fb6981e767fbd528fbc1f6ed22f538160081956b09
- clm_8148596ab356c0ae900090cdc3ba02c2e857ea5467b1e77b72130a6f005d7c06
- clm_b82fbd5e43bc85df1d913d4731af5ed5d70ea9e91935119525b9510ad2f36071
- clm_bd5a3bdca0d96ff951231b97983f06f31d43d801e1e858632a1d299c58f9b099
maturity: draft
page_id: pg_4367783e510c5588bb3a6969e10b9419
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_026969a9f66755ad94b41283dbec204c
title: vibe-stack/ggez/README.md @ 45ed541cb163
updated_at: '2026-09-14T04:30:23Z'
---

# vibe-stack/ggez/README.md @ 45ed541cb163

<!-- rcw:begin owner=source:src_026969a9f66755ad94b41283dbec204c block=evidence -->
- This is the first public alpha release; the README warns of breaking API changes, renamed APIs, moved files, and workflow churn until at least beta, and notes the docs are mostly outdated. [@claim:clm_250a47935a151d4b1d95bd63a1172838b9249f0e4698739db1b5b2c801e2ebd0]
- The repo ships apps including an orchestrator entrypoint, a world editor (formerly Trident), an animation editor, a docs website, and a vanilla Three.js playground. [@claim:clm_2a53e6b88617a7e5c612f36a03a4fbe717e355ade585c208bc5b741e956646fd]
- Repository development practice: no environment variables are required for normal local use; AI generation in the world editor needs FAL_KEY in apps/editor/.env.local, used only by local editor server routes. [@claim:clm_450c65e7a74de4e0be6d43daa65f641bf11259b71e52d1b310ef2ba63af0ebc9]
- Running GGEZ requires Bun 1.3 or newer on macOS, Linux, or Windows with a modern browser; a Fal API key is needed only for AI-assisted generation features. [@claim:clm_512a636f795cb3d6a44f14b6d134c2099184b7d5e23f9faa77a375a5fb6aae6f]
- Repository development practice: local setup is clone, `bun install`, and `bun run start` (which starts the orchestrator); individual apps run via `bun run dev`, `dev:animation-editor`, `dev:website`, and `dev:three-vanilla`, with build and typecheck scripts also provided. [@claim:clm_5608e00cb7500a2b2ff7c81c01711d5acac8f0ccfd4cc4a78318d041ac3ba27d]
- Docs describe a build pipeline converting .whmap files into runtime artifacts for vanilla Three.js projects, with runtime scenes kept under src/scenes/<scene-id>/ and discovered by @ggez/game-dev. [@claim:clm_6405069baf337b6c2ad6e8828bd03119e7983730f08d7d5d08b5c9141ca5edf4]
- The orchestrator is the normal local entrypoint: it opens the world and animation editors, starts/stops game projects, and lets users switch between tools and the running game; it builds missing editor previews before starting their preview servers. [@claim:clm_66868d2105ceab751d0218fb6981e767fbd528fbc1f6ed22f538160081956b09]
- Packages include three-runtime for scene loading, editor-core (document model, commands, selection, events), geometry-kernel, render-pipeline, game-dev, and shared scene types. [@claim:clm_8148596ab356c0ae900090cdc3ba02c2e857ea5467b1e77b72130a6f005d7c06]
- The project is MIT licensed, per the README's license section pointing to the LICENSE file. [@claim:clm_b82fbd5e43bc85df1d913d4731af5ed5d70ea9e91935119525b9510ad2f36071]
- GGEZ is described as a framework for vibe-coding Three.js games, aiming to be a 'Next.js for Three.js games' with runtime packages, editors, and an orchestration layer. [@claim:clm_bd5a3bdca0d96ff951231b97983f06f31d43d801e1e858632a1d299c58f9b099]
<!-- rcw:end owner=source:src_026969a9f66755ad94b41283dbec204c block=evidence -->

## Researcher notes

