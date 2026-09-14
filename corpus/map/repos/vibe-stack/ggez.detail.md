# vibe-stack/ggez -- full detail

[Back to orientation](ggez.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vibe-stack/ggez/45ed541cb163ef98694467758f60d5533373ac60/92db4f9d292a1e0d.json](../../../wiki/dossiers/vibe-stack/ggez/45ed541cb163ef98694467758f60d5533373ac60/92db4f9d292a1e0d.json)

## specifications (2 claim(s))

- [observation/documented] GGEZ is described as a framework for vibe-coding Three.js games, aiming to be a 'Next.js for Three.js games' with runtime packages, editors, and an orchestration layer. -- evidence: [README.md#L3-L3](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L3-L3), [README.md#L5-L5](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L5-L5) (`clm_bd5a3bdca0d96ff951231b97983f06f31d43d801e1e858632a1d299c58f9b099`)
- [observation/documented] The project is MIT licensed, per the README's license section pointing to the LICENSE file. -- evidence: [README.md#L181-L181](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L181-L181) (`clm_b82fbd5e43bc85df1d913d4731af5ed5d70ea9e91935119525b9510ad2f36071`)

## components (2 claim(s))

- [observation/documented] The repo ships apps including an orchestrator entrypoint, a world editor (formerly Trident), an animation editor, a docs website, and a vanilla Three.js playground. -- evidence: [README.md#L38-L42](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L38-L42) (`clm_2a53e6b88617a7e5c612f36a03a4fbe717e355ade585c208bc5b741e956646fd`)
- [observation/documented] Packages include three-runtime for scene loading, editor-core (document model, commands, selection, events), geometry-kernel, render-pipeline, game-dev, and shared scene types. -- evidence: [README.md#L46-L52](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L46-L52) (`clm_8148596ab356c0ae900090cdc3ba02c2e857ea5467b1e77b72130a6f005d7c06`)

## design-choices (6 claim(s))

- [observation/documented] The editor spec targets a browser-based Source-2-style level editor with brush solids, editable meshes, and instanced models, optimized for rapid blockout and iteration in the Hammer/Radiant/TrenchBroom lineage. -- evidence: [ARCHITECTURE.md#L33-L37](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L33-L37), [ARCHITECTURE.md#L23-L23](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L23-L23), [ARCHITECTURE.md#L13-L14](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L13-L14), [ARCHITECTURE.md#L16-L21](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L16-L21), [ARCHITECTURE.md#L184-L189](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L184-L189) (`clm_f736a5309c7206c1b67f509ed4a71f63b2edb71839349a96effa6331c983690c`)
- [observation/documented] The spec's editor core separates authoring state from React: a SceneDocument (nodes, entities, materials, assets, layers) with CommandStack, Selection, and EventBus, where React must not store geometry state. -- evidence: [ARCHITECTURE.md#L150-L150](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L150-L150), [ARCHITECTURE.md#L138-L144](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L138-L144), [ARCHITECTURE.md#L134-L134](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L134-L134), [ARCHITECTURE.md#L132-L132](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L132-L132), [ARCHITECTURE.md#L152-L161](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L152-L161) (`clm_7bf47cf6c7988db929c7e14d6a8ec7b1bdcba6da63b75e5e956bfbe9df89b743`)
- [observation/documented] Brushes are specified as convex solids defined by plane half-spaces (not vertex meshes), with faces derived from planes and reconstruction via triple-plane intersection, inside tests, and angle-sorted face vertices. -- evidence: [ARCHITECTURE.md#L235-L241](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L235-L241), [ARCHITECTURE.md#L243-L243](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L243-L243), [ARCHITECTURE.md#L197-L197](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L197-L197), [ARCHITECTURE.md#L201-L203](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L201-L203), [ARCHITECTURE.md#L195-L195](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L195-L195), [ARCHITECTURE.md#L318-L323](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L318-L323), [ARCHITECTURE.md#L253-L258](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L253-L258) (`clm_f9588202b54036b98a3a465277cdb8bf6e34528857c9af585b53c2d839eb4118`)
- [observation/documented] The spec calls for a half-edge mesh structure (vertex, twin, next, face) enabling edge traversal, loop selection, face extrusion, and vertex editing, with earcut triangulation for rendering. -- evidence: [ARCHITECTURE.md#L398-L406](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L398-L406), [ARCHITECTURE.md#L431-L433](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L431-L433), [ARCHITECTURE.md#L389-L394](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L389-L394), [ARCHITECTURE.md#L427-L427](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L427-L427), [ARCHITECTURE.md#L374-L381](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L374-L381) (`clm_df00c99db16ffbaac144f4c1cf6b3260da08031d1389b6eca92a7af37a2b2304`)
- [observation/documented] The spec defines a JSON-based .whmap editor save format and an export pipeline targeting GLTF and an engine format (USD optional) with transform baking, mesh merging, and collision generation. -- evidence: [ARCHITECTURE.md#L649-L649](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L649-L649), [ARCHITECTURE.md#L665-L670](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L665-L670), [ARCHITECTURE.md#L657-L661](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L657-L661), [ARCHITECTURE.md#L633-L635](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L633-L635) (`clm_d0b889d521d7f6c6b87974348fef8299c2e0887cfe7533787672b4ab70353c0d`)
- [inference/documented] ARCHITECTURE.md appears to be an AI-generated specification document (it addresses a coding agent and offers further help), so its contents are design intent rather than verified implemented behavior. -- evidence: [ARCHITECTURE.md#L1-L2](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L1-L2), [ARCHITECTURE.md#L806-L806](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L806-L806), [ARCHITECTURE.md#L804-L804](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L804-L804) (`clm_18f9c0a16daae8fc5dee7bc0d75dd459ffbf9e1699bc8481b52fdc8f94d4ca5e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local setup is clone, `bun install`, and `bun run start` (which starts the orchestrator); individual apps run via `bun run dev`, `dev:animation-editor`, `dev:website`, and `dev:three-vanilla`, with build and typecheck scripts also provided. -- evidence: [README.md#L114-L122](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L114-L122), [README.md#L98-L103](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L98-L103), [README.md#L79-L79](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L79-L79), [README.md#L107-L110](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L107-L110), [README.md#L70-L75](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L70-L75) (`clm_5608e00cb7500a2b2ff7c81c01711d5acac8f0ccfd4cc4a78318d041ac3ba27d`)
- [observation/documented] Repository development practice: no environment variables are required for normal local use; AI generation in the world editor needs FAL_KEY in apps/editor/.env.local, used only by local editor server routes. -- evidence: [README.md#L152-L152](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L152-L152), [README.md#L154-L156](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L154-L156), [README.md#L150-L150](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L150-L150), [README.md#L158-L158](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L158-L158) (`clm_450c65e7a74de4e0be6d43daa65f641bf11259b71e52d1b310ef2ba63af0ebc9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The orchestrator is the normal local entrypoint: it opens the world and animation editors, starts/stops game projects, and lets users switch between tools and the running game; it builds missing editor previews before starting their preview servers. -- evidence: [README.md#L92-L92](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L92-L92), [README.md#L85-L85](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L85-L85), [README.md#L87-L90](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L87-L90), [README.md#L79-L79](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L79-L79) (`clm_66868d2105ceab751d0218fb6981e767fbd528fbc1f6ed22f538160081956b09`)
- [observation/documented] Docs describe a build pipeline converting .whmap files into runtime artifacts for vanilla Three.js projects, with runtime scenes kept under src/scenes/<scene-id>/ and discovered by @ggez/game-dev. -- evidence: [README.md#L143-L146](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L143-L146), [docs/vanilla-three/build-pipeline.md#L3-L3](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/docs/vanilla-three/build-pipeline.md#L3-L3) (`clm_6405069baf337b6c2ad6e8828bd03119e7983730f08d7d5d08b5c9141ca5edf4`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The spec's stack lists Vite/React/TypeScript, three with @react-three/fiber and drei, earcut and clipper2-ts, three-mesh-bvh, valtio and xstate, plus Web Workers via comlink. -- evidence: [ARCHITECTURE.md#L97-L99](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L97-L99), [ARCHITECTURE.md#L74-L78](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L74-L78), [ARCHITECTURE.md#L103-L106](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L103-L106), [ARCHITECTURE.md#L90-L93](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L90-L93), [ARCHITECTURE.md#L110-L113](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L110-L113), [ARCHITECTURE.md#L82-L86](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/ARCHITECTURE.md#L82-L86) (`clm_8874c4fc8493ab77708eba589b0cdba48c3fe2800e3b2f0b54cf1af6e7db3b79`)
- [observation/documented] Running GGEZ requires Bun 1.3 or newer on macOS, Linux, or Windows with a modern browser; a Fal API key is needed only for AI-assisted generation features. -- evidence: [README.md#L60-L64](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L60-L64) (`clm_512a636f795cb3d6a44f14b6d134c2099184b7d5e23f9faa77a375a5fb6aae6f`)

## limitations (1 claim(s))

- [observation/documented] This is the first public alpha release; the README warns of breaking API changes, renamed APIs, moved files, and workflow churn until at least beta, and notes the docs are mostly outdated. -- evidence: [README.md#L9-L9](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L9-L9), [README.md#L11-L11](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L11-L11), [README.md#L171-L175](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L171-L175), [README.md#L56-L56](https://github.com/vibe-stack/ggez/blob/45ed541cb163ef98694467758f60d5533373ac60/README.md#L56-L56) (`clm_250a47935a151d4b1d95bd63a1172838b9249f0e4698739db1b5b2c801e2ebd0`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

