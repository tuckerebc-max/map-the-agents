---
access: public
aliases: []
claim_ids:
- clm_0270bff2999b9c39fc4194091e796a3d89370c583c390b8821e1e4dbe90b530f
- clm_0d2fd09085052fbe4070a8dad70b35c230583b33f6f7b85c6f435fefb22daf1f
- clm_251f8c3a6d7bbee16e6799ae6c93dda4c268bdd0716f7b62703d3c368877d072
- clm_397f60455153d3ef1b4a7e4e47bb29194f3fdd93da0c9a6ecb15504e5a753915
- clm_5ab121a079c5034376db1f78cf1526943a23dfde72e7928495d0a374fd54dbd2
- clm_6b90ff9d224ba999ff0d4fdbdb24b0b4a83732cadc22826e6bab5e4a1b4cac05
- clm_927abcb32a4fd6176cc302fa5b1a5b1c0878a2e279c489e79c680220ebbfb611
- clm_b4c63bec5d0fa8f5b2b1e4b9689e5f2aa8e2bab70a06839b7cb0d60a076223c7
- clm_cf3fe1f77c2ec377089cda246bd6835295bd977cc8376d8d8a4f1f04df747ef8
- clm_ed7ba9ac84b9af261223676423343b7df889f41b6f6ba76b23b06590aaf3b4e9
maturity: draft
page_id: pg_d16a325e0a7b5a2484fcf5390164248d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8bf4a062790f5a19af7c33c7542aeafd
title: DeadWaveWave/demo2apk/README.md @ 1405c4405c96
updated_at: '2026-09-14T03:45:12Z'
---

# DeadWaveWave/demo2apk/README.md @ 1405c4405c96

<!-- rcw:begin owner=source:src_8bf4a062790f5a19af7c33c7542aeafd block=evidence -->
- Demo2APK is described as a one-click packaging tool that turns AI-generated demos or projects into installable APKs without requiring users to set up an Android development environment. [@claim:clm_0270bff2999b9c39fc4194091e796a3d89370c583c390b8821e1e4dbe90b530f]
- Repository development practice: local development runs pnpm install, a Redis container, pnpm build, then pnpm dev/worker/frontend in separate terminals serving ports 3000 and 5173. [@claim:clm_0d2fd09085052fbe4070a8dad70b35c230583b33f6f7b85c6f435fefb22daf1f]
- Users can customize app name, version, icon, and select Android permissions via the UI, defaulting to INTERNET only; optional PWA generation is available alongside the APK. [@claim:clm_251f8c3a6d7bbee16e6799ae6c93dda4c268bdd0716f7b62703d3c368877d072]
- Rate limiting is enabled by default at 5 requests per hour per IP, configurable or disableable via RATE_LIMIT_ENABLED and RATE_LIMIT_MAX environment variables. [@claim:clm_397f60455153d3ef1b4a7e4e47bb29194f3fdd93da0c9a6ecb15504e5a753915]
- Generated APKs and temp files are deleted after 2 hours by default, with a background cleanup worker scanning every 30 minutes; retention and cleanup are configurable via environment variables. [@claim:clm_5ab121a079c5034376db1f78cf1526943a23dfde72e7928495d0a374fd54dbd2]
- Prebuilt Docker images support only linux/amd64; macOS and ARM users are directed to local development mode instead. [@claim:clm_6b90ff9d224ba999ff0d4fdbdb24b0b4a83732cadc22826e6bab5e4a1b4cac05]
- Repository development practice: React/Vite projects targeting APK output are advised to add @vitejs/plugin-legacy with terser, set legacy targets like chrome >= 52 / android >= 5, and use a relative base ('./') to avoid blank screens. [@claim:clm_927abcb32a4fd6176cc302fa5b1a5b1c0878a2e279c489e79c680220ebbfb611]
- The tool auto-detects input type (HTML, React, ZIP) and picks a build strategy, supporting single files (.html/.js/.jsx/.ts/.tsx), pasted code, and ZIP archives of React/Vite or multi-file HTML projects. [@claim:clm_b4c63bec5d0fa8f5b2b1e4b9689e5f2aa8e2bab70a06839b7cb0d60a076223c7]
- Builds run through a queue backed by BullMQ and Redis, with configurable worker concurrency (default 2) and excess builds queued automatically. [@claim:clm_cf3fe1f77c2ec377089cda246bd6835295bd977cc8376d8d8a4f1f04df747ef8]
- The stated tech stack is React/Vite/Tailwind frontend, Node.js/Fastify/TypeScript backend, BullMQ with Redis for queuing, and Cordova, Capacitor, and Gradle for APK building. [@claim:clm_ed7ba9ac84b9af261223676423343b7df889f41b6f6ba76b23b06590aaf3b4e9]
<!-- rcw:end owner=source:src_8bf4a062790f5a19af7c33c7542aeafd block=evidence -->

## Researcher notes

