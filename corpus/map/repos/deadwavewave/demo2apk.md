# deadwavewave/demo2apk

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1405c4405c96 @ df9b1e3a27b62d02

## Summary (orientation draft, not independently verified)

Demo2APK is a self-hostable web service that packages uploaded HTML/JS/React/ZIP projects into installable Android APKs via a Cordova/Capacitor/Gradle pipeline, with a REST API, Redis/BullMQ build queue, and configurable rate limiting and file retention. Evidence is documentation-only (README, API docs, deployment and ARM64 notes); no source code or eval harness appears in the snapshot. Evidence coverage: 209 of 306 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Demo2APK is described as a one-click packaging tool that turns AI-generated demos or projects into installable APKs without requiring users to set up an Android development environment. -- evidence: [README.md#L13-L13](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L13-L13)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (4 claim(s)):
  - [observation/documented] The tool auto-detects input type (HTML, React, ZIP) and picks a build strategy, supporting single files (.html/.js/.jsx/.ts/.tsx), pasted code, and ZIP archives of React/Vite or multi-file HTML projects. -- evidence: [README.md#L31-L46](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L31-L46)
  - [observation/documented] Users can customize app name, version, icon, and select Android permissions via the UI, defaulting to INTERNET only; optional PWA generation is available alongside the APK. -- evidence: [README.md#L31-L46](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L31-L46)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local development runs pnpm install, a Redis container, pnpm build, then pnpm dev/worker/frontend in separate terminals serving ports 3000 and 5173. -- evidence: [README.md#L111-L111](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L111-L111), [README.md#L117-L120](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L117-L120), [README.md#L114-L114](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L114-L114), [README.md#L108-L108](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L108-L108)
  - [observation/documented] Repository development practice: React/Vite projects targeting APK output are advised to add @vitejs/plugin-legacy with terser, set legacy targets like chrome >= 52 / android >= 5, and use a relative base ('./') to avoid blank screens. -- evidence: [README.md#L60-L67](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L60-L67), [README.md#L50-L50](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L50-L50), [README.md#L52-L54](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L52-L54)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The REST API exposes GET /health, POST /api/build/html, POST /api/build/zip, GET /api/build/:taskId/status, GET /api/build/:taskId/download, and DELETE /api/build/:taskId, using multipart/form-data uploads and JSON responses. -- evidence: [docs/API.md#L5-L6](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L5-L6), [docs/API.md#L10-L17](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L10-L17)
  - [observation/documented] Build endpoints accept optional appName, appId, and publishPwa fields; appName defaults differ per endpoint (MyVibeApp for HTML, MyReactApp for ZIP). -- evidence: [docs/API.md#L45-L50](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L45-L50), [docs/API.md#L69-L74](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/docs/API.md#L69-L74)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Builds run through a queue backed by BullMQ and Redis, with configurable worker concurrency (default 2) and excess builds queued automatically. -- evidence: [README.md#L208-L209](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L208-L209), [README.md#L223-L227](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L223-L227), [README.md#L204-L204](https://github.com/DeadWaveWave/demo2apk/blob/1405c4405c96e8ee5e8143f47c39d28203fc6e89/README.md#L204-L204)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](demo2apk.detail.md)

Metadata and full claim list: [full detail](demo2apk.detail.md)
Human notes ([notes](demo2apk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
