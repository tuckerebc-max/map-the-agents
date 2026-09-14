# runvendo/vendo

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4d149938d7d3 @ d1f8bb85b9842298

## Summary (orientation draft, not independently verified)

Selected evidence records: Vendo is an embedded agent for B2B SaaS that acts through the host product's own API as the signed-in user and renders generated UI in a sandboxed, brand-native surface without touching host source code. Generated components run in an iframe jail with connect-src 'none', escalating to a sandboxed server only when needed.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vendo is an embedded agent for B2B SaaS that acts through the host product's own API as the signed-in user and renders generated UI in a sandboxed, brand-native surface without touching host source code. -- evidence: [README.md#L9-L11](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L9-L11)
- components (1 claim(s)):
  - [observation/documented] The npm package @vendoai/vendo is the default composition (vendoai is a thin alias), with subpath exports /core and /ui providing shared types/schemas and headless React hooks plus an in-jail component kit. -- evidence: [README.md#L105-L106](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L105-L106), [README.md#L108-L112](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L108-L112)
- design-choices (3 claim(s)):
  - [observation/documented] Generated components run in an iframe jail with connect-src 'none', escalating to a sandboxed server only when needed. -- evidence: [README.md#L92-L92](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L92-L92)
  - [observation/documented] Telemetry is anonymous and opt-out, build/dev-side only, never firing from a deployed production app; events carry only counts and enums, never source code, paths, prompts, keys, or raw error messages. -- evidence: [TELEMETRY.md#L3-L3](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L3-L3), [TELEMETRY.md#L24-L24](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L24-L24), [TELEMETRY.md#L52-L52](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L52-L52)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors branch from main and open PRs; the local gate is pnpm typecheck && pnpm lint plus the test files covering touched code, with CI's green check as the gate of record and releases handled by CI-only tag-and-release workflows. -- evidence: [CONTRIBUTING.md#L62-L67](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L62-L67), [CONTRIBUTING.md#L20-L37](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L20-L37), [CLAUDE.md#L51-L79](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CLAUDE.md#L51-L79)
  - [observation/documented] Repository development practice: the repo is a turbo monorepo requiring Node 22+ and pnpm 11; PRs are merged publicly then imported into a private monorepo by a maintainer-run upstream-import workflow. -- evidence: [CONTRIBUTING.md#L13-L16](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L13-L16), [CONTRIBUTING.md#L56-L58](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L56-L58), [CONTRIBUTING.md#L41-L43](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L41-L43), [CONTRIBUTING.md#L45-L49](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L45-L49)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI offers `vendo init` for setup and an optional `vendo doctor` checkup whose printed codes link to exact fixes; a backend package exposes `agent()` and `chat()` without mounting Vendo's CLI or UI. -- evidence: [README.md#L72-L76](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L72-L76), [README.md#L78-L82](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L78-L82), [README.md#L46-L49](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L46-L49)
- memory-state (1 claim(s)):
  - [observation/documented] PGlite at .vendo/data serves as the zero-config store, and production runs the same schema on Postgres. -- evidence: [README.md#L98-L99](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L98-L99)
- orchestration (1 claim(s)):
More evidence: [full detail](vendo.detail.md)

Metadata and full claim list: [full detail](vendo.detail.md)
Human notes ([notes](vendo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
