# vibe-stack/ggez

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 45ed541cb163 @ 92db4f9d292a1e0d

## Summary (orientation draft, not independently verified)

GGEZ is an early public alpha framework for vibe-coding Three.js games, shipping an orchestrator, world editor, animation editor, runtime packages, and a Source-2-style editor specification; most product statements come from README and ARCHITECTURE.md documentation rather than code inspection. Evidence coverage: 239 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] GGEZ is described as a framework for vibe-coding Three.js games, aiming to be a 'Next.js for Three.js games' with runtime packages, editors, and an orchestration layer. -- evidence: [README.md#L3-L3](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L3-L3), [README.md#L5-L5](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L5-L5)
  - [observation/documented] The project is MIT licensed, per the README's license section pointing to the LICENSE file. -- evidence: [README.md#L181-L181](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L181-L181)
- components (2 claim(s)):
  - [observation/documented] The repo ships apps including an orchestrator entrypoint, a world editor (formerly Trident), an animation editor, a docs website, and a vanilla Three.js playground. -- evidence: [README.md#L38-L42](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L38-L42)
  - [observation/documented] Packages include three-runtime for scene loading, editor-core (document model, commands, selection, events), geometry-kernel, render-pipeline, game-dev, and shared scene types. -- evidence: [README.md#L46-L52](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L46-L52)
- design-choices (6 claim(s)):
  - [observation/documented] The editor spec targets a browser-based Source-2-style level editor with brush solids, editable meshes, and instanced models, optimized for rapid blockout and iteration in the Hammer/Radiant/TrenchBroom lineage. -- evidence: [ARCHITECTURE.md#L33-L37](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L33-L37), [ARCHITECTURE.md#L23-L23](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L23-L23), [ARCHITECTURE.md#L13-L14](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L13-L14), [ARCHITECTURE.md#L16-L21](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L16-L21), [ARCHITECTURE.md#L184-L189](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L184-L189)
  - [observation/documented] The spec's editor core separates authoring state from React: a SceneDocument (nodes, entities, materials, assets, layers) with CommandStack, Selection, and EventBus, where React must not store geometry state. -- evidence: [ARCHITECTURE.md#L150-L150](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L150-L150), [ARCHITECTURE.md#L138-L144](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L138-L144), [ARCHITECTURE.md#L134-L134](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L134-L134), [ARCHITECTURE.md#L132-L132](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L132-L132), [ARCHITECTURE.md#L152-L161](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L152-L161)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local setup is clone, `bun install`, and `bun run start` (which starts the orchestrator); individual apps run via `bun run dev`, `dev:animation-editor`, `dev:website`, and `dev:three-vanilla`, with build and typecheck scripts also provided. -- evidence: [README.md#L114-L122](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L114-L122), [README.md#L98-L103](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L98-L103), [README.md#L79-L79](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L79-L79), [README.md#L107-L110](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L107-L110), [README.md#L70-L75](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L70-L75)
  - [observation/documented] Repository development practice: no environment variables are required for normal local use; AI generation in the world editor needs FAL_KEY in apps/editor/.env.local, used only by local editor server routes. -- evidence: [README.md#L152-L152](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L152-L152), [README.md#L154-L156](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L154-L156), [README.md#L150-L150](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L150-L150), [README.md#L158-L158](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L158-L158)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The orchestrator is the normal local entrypoint: it opens the world and animation editors, starts/stops game projects, and lets users switch between tools and the running game; it builds missing editor previews before starting their preview servers. -- evidence: [README.md#L92-L92](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L92-L92), [README.md#L85-L85](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L85-L85), [README.md#L87-L90](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L87-L90), [README.md#L79-L79](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L79-L79)
More evidence: [full detail](ggez.detail.md)

Metadata and full claim list: [full detail](ggez.detail.md)
Human notes ([notes](ggez.notes.md), never overwritten by build)

[Back to map index](../../index.md)
