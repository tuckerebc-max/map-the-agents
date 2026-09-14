---
access: public
aliases: []
claim_ids:
- clm_18f9c0a16daae8fc5dee7bc0d75dd459ffbf9e1699bc8481b52fdc8f94d4ca5e
- clm_7bf47cf6c7988db929c7e14d6a8ec7b1bdcba6da63b75e5e956bfbe9df89b743
- clm_8874c4fc8493ab77708eba589b0cdba48c3fe2800e3b2f0b54cf1af6e7db3b79
- clm_d0b889d521d7f6c6b87974348fef8299c2e0887cfe7533787672b4ab70353c0d
- clm_df00c99db16ffbaac144f4c1cf6b3260da08031d1389b6eca92a7af37a2b2304
- clm_f736a5309c7206c1b67f509ed4a71f63b2edb71839349a96effa6331c983690c
- clm_f9588202b54036b98a3a465277cdb8bf6e34528857c9af585b53c2d839eb4118
maturity: draft
page_id: pg_9580dfa988635b278ff56f83246482a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_731870357a8550ed8bdfa12dfc9d9b3d
title: vibe-stack/ggez/ARCHITECTURE.md @ 45ed541cb163
updated_at: '2026-09-14T04:30:23Z'
---

# vibe-stack/ggez/ARCHITECTURE.md @ 45ed541cb163

<!-- rcw:begin owner=source:src_731870357a8550ed8bdfa12dfc9d9b3d block=evidence -->
- ARCHITECTURE.md appears to be an AI-generated specification document (it addresses a coding agent and offers further help), so its contents are design intent rather than verified implemented behavior. [@claim:clm_18f9c0a16daae8fc5dee7bc0d75dd459ffbf9e1699bc8481b52fdc8f94d4ca5e]
- The spec's editor core separates authoring state from React: a SceneDocument (nodes, entities, materials, assets, layers) with CommandStack, Selection, and EventBus, where React must not store geometry state. [@claim:clm_7bf47cf6c7988db929c7e14d6a8ec7b1bdcba6da63b75e5e956bfbe9df89b743]
- The spec's stack lists Vite/React/TypeScript, three with @react-three/fiber and drei, earcut and clipper2-ts, three-mesh-bvh, valtio and xstate, plus Web Workers via comlink. [@claim:clm_8874c4fc8493ab77708eba589b0cdba48c3fe2800e3b2f0b54cf1af6e7db3b79]
- The spec defines a JSON-based .whmap editor save format and an export pipeline targeting GLTF and an engine format (USD optional) with transform baking, mesh merging, and collision generation. [@claim:clm_d0b889d521d7f6c6b87974348fef8299c2e0887cfe7533787672b4ab70353c0d]
- The spec calls for a half-edge mesh structure (vertex, twin, next, face) enabling edge traversal, loop selection, face extrusion, and vertex editing, with earcut triangulation for rendering. [@claim:clm_df00c99db16ffbaac144f4c1cf6b3260da08031d1389b6eca92a7af37a2b2304]
- The editor spec targets a browser-based Source-2-style level editor with brush solids, editable meshes, and instanced models, optimized for rapid blockout and iteration in the Hammer/Radiant/TrenchBroom lineage. [@claim:clm_f736a5309c7206c1b67f509ed4a71f63b2edb71839349a96effa6331c983690c]
- Brushes are specified as convex solids defined by plane half-spaces (not vertex meshes), with faces derived from planes and reconstruction via triple-plane intersection, inside tests, and angle-sorted face vertices. [@claim:clm_f9588202b54036b98a3a465277cdb8bf6e34528857c9af585b53c2d839eb4118]
<!-- rcw:end owner=source:src_731870357a8550ed8bdfa12dfc9d9b3d block=evidence -->

## Researcher notes

