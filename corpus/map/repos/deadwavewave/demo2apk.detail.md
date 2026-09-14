# deadwavewave/demo2apk -- full detail

[Back to orientation](demo2apk.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/deadwavewave/demo2apk/1405c4405c96e8ee5e8143f47c39d28203fc6e89/df9b1e3a27b62d02.json](../../../wiki/dossiers/deadwavewave/demo2apk/1405c4405c96e8ee5e8143f47c39d28203fc6e89/df9b1e3a27b62d02.json)

## specifications (1 claim(s))

- [observation/documented] Demo2APK is described as a one-click packaging tool that turns AI-generated demos or projects into installable APKs without requiring users to set up an Android development environment. -- evidence: [README.md#L13-L13](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L13-L13) (`clm_0270bff2999b9c39fc4194091e796a3d89370c583c390b8821e1e4dbe90b530f`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (4 claim(s))

- [observation/documented] The tool auto-detects input type (HTML, React, ZIP) and picks a build strategy, supporting single files (.html/.js/.jsx/.ts/.tsx), pasted code, and ZIP archives of React/Vite or multi-file HTML projects. -- evidence: [README.md#L31-L46](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L31-L46) (`clm_b4c63bec5d0fa8f5b2b1e4b9689e5f2aa8e2bab70a06839b7cb0d60a076223c7`)
- [observation/documented] Users can customize app name, version, icon, and select Android permissions via the UI, defaulting to INTERNET only; optional PWA generation is available alongside the APK. -- evidence: [README.md#L31-L46](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L31-L46) (`clm_251f8c3a6d7bbee16e6799ae6c93dda4c268bdd0716f7b62703d3c368877d072`)
- [observation/documented] Rate limiting is enabled by default at 5 requests per hour per IP, configurable or disableable via RATE_LIMIT_ENABLED and RATE_LIMIT_MAX environment variables. -- evidence: [README.md#L165-L166](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L165-L166), [README.md#L172-L172](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L172-L172), [README.md#L175-L176](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L175-L176), [README.md#L163-L163](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L163-L163) (`clm_397f60455153d3ef1b4a7e4e47bb29194f3fdd93da0c9a6ecb15504e5a753915`)
- [observation/documented] Generated APKs and temp files are deleted after 2 hours by default, with a background cleanup worker scanning every 30 minutes; retention and cleanup are configurable via environment variables. -- evidence: [README.md#L189-L189](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L189-L189), [README.md#L198-L200](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L198-L200), [README.md#L182-L183](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L182-L183) (`clm_5ab121a079c5034376db1f78cf1526943a23dfde72e7928495d0a374fd54dbd2`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local development runs pnpm install, a Redis container, pnpm build, then pnpm dev/worker/frontend in separate terminals serving ports 3000 and 5173. -- evidence: [README.md#L111-L111](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L111-L111), [README.md#L117-L120](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L117-L120), [README.md#L114-L114](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L114-L114), [README.md#L108-L108](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L108-L108) (`clm_0d2fd09085052fbe4070a8dad70b35c230583b33f6f7b85c6f435fefb22daf1f`)
- [observation/documented] Repository development practice: React/Vite projects targeting APK output are advised to add @vitejs/plugin-legacy with terser, set legacy targets like chrome >= 52 / android >= 5, and use a relative base ('./') to avoid blank screens. -- evidence: [README.md#L60-L67](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L60-L67), [README.md#L50-L50](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L50-L50), [README.md#L52-L54](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L52-L54) (`clm_927abcb32a4fd6176cc302fa5b1a5b1c0878a2e279c489e79c680220ebbfb611`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The REST API exposes GET /health, POST /api/build/html, POST /api/build/zip, GET /api/build/:taskId/status, GET /api/build/:taskId/download, and DELETE /api/build/:taskId, using multipart/form-data uploads and JSON responses. -- evidence: [docs/API.md#L5-L6](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L5-L6), [docs/API.md#L10-L17](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L10-L17) (`clm_a22a0ce6b7cbcd7776363bf09bed70ec71149088007629f5f80fb8049c7af4b6`)
- [observation/documented] Build endpoints accept optional appName, appId, and publishPwa fields; appName defaults differ per endpoint (MyVibeApp for HTML, MyReactApp for ZIP). -- evidence: [docs/API.md#L45-L50](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L45-L50), [docs/API.md#L69-L74](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L69-L74) (`clm_1e318b7f7c0a936b6e02535323d8fdf44258d2fa9f79256818bcbd9e5a3c48ec`)
- [observation/documented] Task status queries return pending, active, completed, or failed states, with progress including a message and percentage. -- evidence: [docs/API.md#L87-L91](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L87-L91), [docs/API.md#L95-L108](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L95-L108) (`clm_6180aefa02712763c546bc0b570b9d9c7348b61f9ab2aef449ac7845977f0566`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Builds run through a queue backed by BullMQ and Redis, with configurable worker concurrency (default 2) and excess builds queued automatically. -- evidence: [README.md#L208-L209](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L208-L209), [README.md#L223-L227](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L223-L227), [README.md#L204-L204](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L204-L204) (`clm_cf3fe1f77c2ec377089cda246bd6835295bd977cc8376d8d8a4f1f04df747ef8`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stated tech stack is React/Vite/Tailwind frontend, Node.js/Fastify/TypeScript backend, BullMQ with Redis for queuing, and Cordova, Capacitor, and Gradle for APK building. -- evidence: [README.md#L223-L227](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L223-L227) (`clm_ed7ba9ac84b9af261223676423343b7df889f41b6f6ba76b23b06590aaf3b4e9`)

## limitations (2 claim(s))

- [observation/documented] Prebuilt Docker images support only linux/amd64; macOS and ARM users are directed to local development mode instead. -- evidence: [DEPLOYMENT.md#L5-L5](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/DEPLOYMENT.md#L5-L5), [README.md#L77-L77](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L77-L77), [DEPLOYMENT.md#L37-L37](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/DEPLOYMENT.md#L37-L37) (`clm_6b90ff9d224ba999ff0d4fdbdb24b0b4a83732cadc22826e6bab5e4a1b4cac05`)
- [observation/documented] Google does not publish Linux ARM64 Android build-tools (notably aapt2), so ARM64 Docker builds rely on a temporary Rosetta x86_64 emulation workaround that is slower than native. -- evidence: [docs/ARM64_BUILD_ISSUES.md#L53-L54](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/ARM64_BUILD_ISSUES.md#L53-L54), [docs/ARM64_BUILD_ISSUES.md#L17-L17](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/ARM64_BUILD_ISSUES.md#L17-L17), [docs/ARM64_BUILD_ISSUES.md#L46-L46](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/ARM64_BUILD_ISSUES.md#L46-L46) (`clm_2a37f5bbc9ec7a5de37a77de719d276b15e81f79e00e41d47f8ec971053c6474`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

