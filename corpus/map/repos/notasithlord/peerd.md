# notasithlord/peerd

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 12d1a54976bc @ c54f3ca7139dac7c

## Summary (orientation draft, not independently verified)

peerd is a browser-extension agent runtime (Chromium and Firefox) built on WebExtension/browser primitives, with five extension modules, keyless per-environment actors, vault/egress security, and documented Firefox capability gaps. Evidence covers product architecture, security boundaries, App-actor interfaces, dependencies, and development workflows. Evidence coverage: 98 of 115 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 22 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] peerd is described as a general-purpose agent runtime built on browser primitives (Workers, origins, sandboxing, OPFS, WASM/WASI, WebRTC, WebAuthn, WebExtensions) that runs inside Chrome and Firefox. -- evidence: [README.md#L24-L24](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L24-L24)
- components (1 claim(s)):
  - [observation/documented] The extension has five main modules, each exposing its public API via index.js: peerd-provider (model adapters), peerd-egress (vault, network policy, denylist, audit), peerd-engine (WebVM/Notebook/App/headless execution), peerd-runtime (agent loop, actors, tools, sessions, memory, permissions), and peerd-distributed (preview-only P2P). -- evidence: [README.md#L151-L157](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L151-L157), [README.md#L148-L149](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L148-L149)
- design-choices (1 claim(s)):
  - [observation/documented] The source extension is vanilla JavaScript with ES modules running directly when loaded unpacked, with no development bundler or transpiler; release packaging with Bun minifies only a disposable staging copy and preserves module boundaries and vendored bytes. -- evidence: [README.md#L166-L172](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L166-L172)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: development uses Bun commands (bun install, gen:dev, test, typecheck, lint, e2e:verify, preflight) across three test surfaces (Bun unit tests, in-browser Chrome/Gecko tests, live Chrome E2E), plus a red-team suite; generated files like extension/manifest.json must not be hand-edited and CI checks them for drift. -- evidence: [README.md#L213-L215](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L213-L215), [README.md#L174-L183](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L174-L183), [README.md#L187-L193](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L187-L193), [README.md#L195-L198](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L195-L198)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Apps integrate via window.peerd APIs: agent.open() reveals a trusted drawer only during real user activation, agent.expose() declares observe/act semantic adapters, and peerd.data provides bounded JSON persistence (1 MB per write) mapped to data/<key>.json in the App's working tree. -- evidence: [docs/APP-ACTORS.md#L120-L125](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L120-L125), [docs/APP-ACTORS.md#L113-L118](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L113-L118), [docs/APP-ACTORS.md#L16-L18](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L16-L18), [docs/APP-ACTORS.md#L20-L24](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L20-L24), [docs/APP-ACTORS.md#L81-L109](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L81-L109)
  - [observation/documented] App manifests use peerd.json with fields like kind, entry, agent (kind bound-app, profile, surface, name, instructions, runtime), and capabilities; a conforming Git repository places peerd.json and its entry file at the root. -- evidence: [docs/APP-ACTORS.md#L151-L154](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L151-L154), [docs/APP-ACTORS.md#L61-L76](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/docs/APP-ACTORS.md#L61-L76)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions, memory, skills, goals, review, and checkpoints live in the extension; a local vault holds secrets and protected security records, with passphrase unlock always available and passkey unlock dependent on WebAuthn PRF support. -- evidence: [README.md#L142-L144](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L142-L144), [README.md#L135-L140](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L135-L140), [README.md#L38-L54](https://github.com/NotASithLord/peerd/blob/12d1a54976bc07c4c8a4e9875f694964bd3a65b3/README.md#L38-L54)
- orchestration (1 claim(s)):
More evidence: [full detail](peerd.detail.md)

Metadata and full claim list: [full detail](peerd.detail.md)
Human notes ([notes](peerd.notes.md), never overwritten by build)

[Back to map index](../../index.md)
