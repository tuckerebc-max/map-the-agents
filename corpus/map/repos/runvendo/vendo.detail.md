# runvendo/vendo -- full detail

[Back to orientation](vendo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/runvendo/vendo/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/d1f8bb85b9842298.json](../../../wiki/dossiers/runvendo/vendo/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/d1f8bb85b9842298.json)

## specifications (1 claim(s))

- [observation/documented] Vendo is an embedded agent for B2B SaaS that acts through the host product's own API as the signed-in user and renders generated UI in a sandboxed, brand-native surface without touching host source code. -- evidence: [README.md#L9-L11](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L9-L11) (`clm_0439fe278b5f000b295c49b89f010875e5d73395fb216a5a60d5ecc760885200`)

## components (1 claim(s))

- [observation/documented] The npm package @vendoai/vendo is the default composition (vendoai is a thin alias), with subpath exports /core and /ui providing shared types/schemas and headless React hooks plus an in-jail component kit. -- evidence: [README.md#L105-L106](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L105-L106), [README.md#L108-L112](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L108-L112) (`clm_4eb31c13b6105610e0931d75aee87361fa5b49b4650e417becc8e6fe72b56117`)

## design-choices (3 claim(s))

- [observation/documented] Generated components run in an iframe jail with connect-src 'none', escalating to a sandboxed server only when needed. -- evidence: [README.md#L92-L92](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L92-L92) (`clm_8471d28b3fc8babfa88846d5467c8eb94d234ff4466defc381217d5f026619a3`)
- [observation/documented] Telemetry is anonymous and opt-out, build/dev-side only, never firing from a deployed production app; events carry only counts and enums, never source code, paths, prompts, keys, or raw error messages. -- evidence: [TELEMETRY.md#L3-L3](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L3-L3), [TELEMETRY.md#L24-L24](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L24-L24), [TELEMETRY.md#L52-L52](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L52-L52) (`clm_b37db2c05958b89995ff627e90b4134fdc34bbf3ef42e193febae7a0e5c4e0f6`)
- [observation/documented] Telemetry identity is a random UUID stored in ~/.vendo/telemetry.json, and projectIdHash is a salted one-way SHA-256 of the git origin URL or package name, omitted when neither exists. -- evidence: [TELEMETRY.md#L58-L58](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L58-L58), [TELEMETRY.md#L56-L56](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/TELEMETRY.md#L56-L56) (`clm_dcadf3e9c155c41dfc11e3fc4f6f6ff8dea9e498dc320b2ddde6913ca7f70091`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors branch from main and open PRs; the local gate is pnpm typecheck && pnpm lint plus the test files covering touched code, with CI's green check as the gate of record and releases handled by CI-only tag-and-release workflows. -- evidence: [CONTRIBUTING.md#L62-L67](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L62-L67), [CONTRIBUTING.md#L20-L37](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L20-L37), [CLAUDE.md#L51-L79](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CLAUDE.md#L51-L79) (`clm_135d50fe0c8fa4e894bcef14b801493a5e5e7c714018a3e5c23a11e7181f13b4`)
- [observation/documented] Repository development practice: the repo is a turbo monorepo requiring Node 22+ and pnpm 11; PRs are merged publicly then imported into a private monorepo by a maintainer-run upstream-import workflow. -- evidence: [CONTRIBUTING.md#L13-L16](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L13-L16), [CONTRIBUTING.md#L56-L58](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L56-L58), [CONTRIBUTING.md#L41-L43](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L41-L43), [CONTRIBUTING.md#L45-L49](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/CONTRIBUTING.md#L45-L49) (`clm_610757db68efc13a5c146f0270bdc8ffdc2a2ae12ae9d34c44191ddaf9e9cc13`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The CLI offers `vendo init` for setup and an optional `vendo doctor` checkup whose printed codes link to exact fixes; a backend package exposes `agent()` and `chat()` without mounting Vendo's CLI or UI. -- evidence: [README.md#L72-L76](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L72-L76), [README.md#L78-L82](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L78-L82), [README.md#L46-L49](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L46-L49) (`clm_f1fed25b9a55101fb5d39eefb74c7715133c9ba39dcea1e1b6e52d4d9569ebb6`)

## memory-state (1 claim(s))

- [observation/documented] PGlite at .vendo/data serves as the zero-config store, and production runs the same schema on Postgres. -- evidence: [README.md#L98-L99](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L98-L99) (`clm_b50087df7adedc04d45031a8a88eba5e3c09c6827ac7be3b1c0d2704bbb1a532`)

## orchestration (1 claim(s))

- [observation/documented] Vendo runs a streaming agent that works with any AI SDK LanguageModel, and extracts the host API into tools the agent executes as the signed-in user. -- evidence: [README.md#L88-L88](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L88-L88), [README.md#L90-L90](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L90-L90) (`clm_c5639129a9e23d32896f707cc01f258322d3f8d36af5094e9587a83ae588dd84`)

## tools-permissions (1 claim(s))

- [observation/documented] Policy, approvals, grants, breakers, and audit sit at one execution choke point; app machines reach host tools only through a guarded tool proxy. -- evidence: [README.md#L94-L96](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L94-L96) (`clm_766686a1a7b330f1e8f970ec65f01190238bddb6f95fb6ee4a849f0269abb820`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Cloud-gated features (sharing, publishing, org overlays, pinning) activate with VENDO_API_KEY while the open-source blocks remain self-hosted. -- evidence: [README.md#L114-L115](https://github.com/runvendo/vendo/blob/4d149938d7d3dbbe87f46b92e5d4bf0152ec5b6c/README.md#L114-L115) (`clm_47af5f31c1074fb53e676ab9da528757714a9f6a157f96390752708f51867b2f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

