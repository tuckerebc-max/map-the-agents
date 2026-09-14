# WEB HAMMER ROADMAP

## Status

Last updated: 2026-03-07

## Completed

- Initialized the `web-hammer` Bun workspace monorepo.
- Added the architecture source of truth in `ARCHITECTURE.md`.
- Scaffolded the Vite + React + TypeScript editor app in `apps/editor`.
- Created initial workspace packages for the editor core, geometry kernel, render pipeline, tool system, shared types, and workers.
- Wired a minimal editor shell that respects the architecture rule that React is UI-only and geometry lives outside React state.
- Declared and installed the initial dependency set from the architecture spec.
- Implemented the Phase 1 viewport baseline with a render-pipeline-derived scene, perspective editor camera rig, construction grid, and entity markers.
- Expanded `editor-core` with scene revision tracking, mutation helpers, selection actions, redoable commands, and richer editor events.
- Implemented Phase 3 brush reconstruction with triple-plane intersection, half-space classification, ordered face generation, and triangulated brush surfaces.
- Implemented Phase 4 editable mesh topology helpers with polygon-to-half-edge construction, topology validation, face traversal, and triangulation.
- Updated the viewport render path to consume reconstructed brush and mesh surfaces instead of placeholder geometry for authoring nodes.
- Started Phase 5 with object-level viewport hit testing, click-to-select, focus-on-double-click, empty-space clear, and scene-list/inspector selection sync.
- Expanded Phase 5 with BVH-accelerated object raycasting and Shift-drag marquee selection in the viewport.
- Swapped the viewport renderer to Three.js `WebGPURenderer`, fixed brush face shading by splitting brush surface vertices per face, and relaxed orbit controls to allow below-ground camera angles.
- Started Phase 6 with a transform tool baseline: snap-aware translation, duplication, mirror-by-axis, tool switching, and undo/redo shortcuts on top of the command stack.
- Started Phase 7 and Phase 8 baselines: center-split clip for axis-aligned brushes, object-level brush extrusion, mesh inflate/top-offset edits, and grid-based asset placement.
- Started Phase 9 with asset/material panels, brush material assignment, entity authoring actions, asset-driven placement, and a visible worker job queue for async editor tasks.
- Expanded Phase 9 so selected assets drive model placement, selected materials can be assigned to brushes with visible viewport color changes, and export/persistence jobs execute in a real Web Worker.
- Started Phase 10 with `.whmap` scene save/load plus baseline glTF and engine-scene export flows running through the worker pipeline.
- Revamped the editor UI around Tailwind and shadcn: added the `@/` app alias, replaced the old scaffold with a floating menu/toolbar/sidebar layout, moved styling to Tailwind-first components, and added drag-input-backed transform editing in the inspector.
- Moved async job visibility out of the inspector and into a dedicated bottom-bar status affordance with an idle/active icon and popover-backed active job list.
- Expanded the viewport transform workflow with live gizmos for translate/rotate/scale, `G`/`R`/`S` gizmo mode switching, snap-aware transform controls, and a custom snap-driven grid with reduced camera-motion flicker.
- Fixed the viewport gizmo/orbit interaction handoff so camera controls recover correctly after transform drags.
- Refined the construction grid so the full-scene sheet uses subtle gray major/minor lines and the visible cell spacing maps directly to the active snap size.
- Tuned the construction grid contrast so the snap-sized minor cells remain the primary visible grid, with major lines only as secondary guides.
- Expanded Phase 7 and Phase 8 into real canvas interactions: clip now previews snap-aware cut lines on brush faces and cuts on click, extrude exposes draggable face-center handles with live brush updates, and mesh edit now supports vertex/edge/face handle selection with translate/rotate/scale gizmos.
- Refined the in-canvas editing affordances so clip uses offset hover surfaces with visible cut previews, extrude uses slimmer direct-drag face handles instead of click-then-gizmo spheres, and mesh edit overlays render more editor-style vertex/edge/face markers.
- Extended subobject editing to box brushes so `Mesh Edit` can now target brush faces, edges, and vertices with snapped handle-based plane updates, not just editable mesh assets.
- Fixed subobject authoring ergonomics so brush/mesh edit gizmos align with their handle centers, `Shift`-click supports additive handle selection, and `Shift`-drag marquee can select multiple brush or mesh subobjects in `Mesh Edit`.
- Tightened subobject transform feedback so mesh/brush edit gizmos track the live edited selection center while dragging, keeping handles and transform anchors visually in sync during preview updates.
- Fixed stale mesh/brush edit overlay caching so face/edge/vertex outlines and knobs recompute from the current preview geometry instead of sticking to their pre-edit positions.
- Fixed mesh-edit transform-control remounting so `G`/`R`/`S` mode switches are reflected by the active subobject gizmo instead of leaving a stale translate gizmo onscreen.
- Replaced the broken bounds-based brush subobject transform approximation with a plane-based convex brush edit path that transforms selected brush vertices and recomputes incident planes for face/edge/vertex move, rotate, and scale.
- Fixed the brush subobject gizmo branch to actually consume the active transform mode, so brush face/edge/vertex editing now switches between `G` / `R` / `S` instead of silently staying on translate.
- Removed redundant viewport drag-lock coupling from `TransformControls` paths and deferred orbit disabling back to Drei’s built-in `dragging-changed` handling, reducing stuck-camera failures during mesh/brush gizmo edits.
- Stabilized convex brush subobject identity across preview updates by keying brush vertices and edges from incident face sets, reducing selection loss, gizmo disappearance, and stuck-camera failures when aggressive brush rotations approach collapsed states.
- Tightened convex brush plane recomputation so face/edge/vertex edits only rewrite the planes explicitly associated with the selected subobject, reducing drift, overreaction, and unintended opposite-face motion during brush rotation and scale.
- Refined convex brush plane selection again so face and edge rotate/scale only recompute incident planes whose transformed vertices actually leave their original planes, improving the face-parallel rotation axis, edge rotation reliability, and edge scaling behavior.
- Replaced the remaining brush plane-refit path for subobject rotate/scale with a convex-hull rebuild from transformed brush vertices, so face and edge edits can change topology when needed instead of drifting or incorrectly dragging the whole original plane set along.
- Fixed subobject drag jitter by freezing the mesh/brush transform gizmo anchor while preview edits rerender, so live move/rotate/scale no longer flicker between the baseline anchor and the preview-derived selection center during a drag.
- Removed the remaining drag-loop instability by letting the hidden gizmo target stay fully imperative during active drags and by freezing brush subobject handle topology at drag start, so preview rerenders no longer reset the control object or swap the selected baseline under the solver mid-gesture.
- Added real brush authoring entry points so new blockout brushes can be placed into the scene from the menu bar or scene panel instead of working only from the seeded demo brush.
- Expanded the in-canvas brush extrude tool from axis-aligned face offsetting to convex brush feature extrusion, including direct-drag edge extrusion handles alongside face extrusion handles.
- Added selection deletion as a real undoable editor command and wired `Delete` / `Backspace` plus the Edit menu to remove the current selection.
- Added a dedicated brush authoring tool with staged three-click box creation: click to anchor on a hit surface, click again to lock the base plane, click a third time to commit the extrusion, and `Escape` to cancel before placement.
- Expanded `Mesh Edit` topology operations with normal inversion on `N`, brush face deletion, two-edge cuts, adjacent-face merge on `M`, and interactive edge bevel on `B` with mouse-width control plus wheel-driven step count; topology-changing brush edits now promote the brush to an editable mesh on commit.
- Fixed promoted brush rendering so topology-edited brushes display as solid front-faced geometry instead of the old mesh wireframe fallback, making invert/cut/merge results render like authored surfaces instead of debug output.
- Refined edge beveling into a signed profile-aware operation: drag width can now go inward or outward, flat bevel is the default for architectural cuts, wheel adjusts segments, and `F` toggles between flat and round bevel profiles while the bevel gesture is active.
- Fixed delete-key precedence so `Delete` / `Backspace` in `Mesh Edit` no longer removes the whole selected object before subobject face deletion can run.
- Fixed `K` edge cuts so they split the selected source edges across all incident faces instead of only dividing the picked face, eliminating the old surviving-edge / T-junction topology bug.
- Fixed bevel preview readability by hiding the source object during the bevel gesture, rendering the preview with a distinct overlay material, and adding a visible wire overlay so segment counts are readable while dragging.
- Fixed edge bevel retopology for cube-style corner cases by rewriting the endpoint faces that share the beveled vertices, so adjacent cap faces no longer keep stale corner topology, and normalized the rebuilt polygon winding so bevel results stop mixing inward- and outward-facing normals.
- Corrected bevel endpoint-face stitching to use actual local edge-to-face adjacency instead of the previous vertex-membership heuristic, which fixes vertical and horizontal cube-edge bevels connecting to the wrong side of the strip or leaving cap faces detached from the new bevel.
- Suspended the normal mesh-edit gizmos during active bevel gestures and made the bevel cursor overlay non-blocking, so orbit controls recover immediately after bevel commit/cancel instead of staying frozen until the user leaves `Mesh Edit`.
- Corrected the bevel strip segment count so `steps = 1` now produces a single bridge face instead of the previous over-segmented result that was corrupting even simple cube-edge bevel topology.
- Removed manual disposal from the transient line overlay geometries used by mesh-edit face/edge previews, which stops the repeated WebGPU `LineBasicMaterial` vertex-buffer errors when entering or switching mesh-edit subobject modes.
- Fixed another bevel topology bug where endpoint-face rewrites were keyed off the handle’s sorted edge ids instead of the owning face’s local edge order; bevel caps now use the oriented edge endpoints, which stops one-sided cube bevels from twisting into giant crossed polygons.
- Tightened bevel face orientation by preserving expected normals for surviving planar faces during the rebuild instead of relying on a global-center winding heuristic for every polygon, which fixes the remaining intermittent inverted-face cases after bevel operations.
- Extended the viewport extrude tool to work on editable meshes as well as convex brushes, with direct face and edge extrusion handles for mesh-authored geometry.
- Stabilized brush and mesh extrude drags by freezing the active handle set during preview updates, preventing the first snapped preview step from unmounting the drag handle and handing control back to orbit mid-gesture.
- Fixed the extrude-handle interaction regression by making the drag-freeze callback stable across rerenders, so brush and mesh extrude knobs can actually stay engaged after pointer-down instead of cancelling their own drag immediately.
- Preserved caller-provided polygon winding in editable-mesh construction and corrected bevel edge replacement orientation for opposite-winding adjacent faces, fixing the cut-then-bevel case where neighboring faces could flip or collapse into bow-tie polygons.
- Reworked mesh face extrusion into a valid manifold result by replacing the source face with a cap plus side walls, and temporarily limited mesh extrude handles to faces while edge-extrude retopology is still pending.
- Hardened the WebGPU viewport render path for hot-updated topology edits by skipping mesh nodes with no renderable surface and avoiding manual disposal on frequently swapped scene/preview geometries.
- Added direct face and edge picking in `Mesh Edit` for both brushes and editable meshes by layering transparent face polygons and thickened edge hit areas over the existing handles, so rapid subobject selection no longer depends on clicking only the small knobs.
- Integrated extrusion into `Mesh Edit` as a shortcut-driven gesture: pressing `X` on the current face/edge selection now starts an in-place extrusion preview, mouse movement adjusts the depth, left click commits, and `Esc` cancels without relying on persistent extrude overlays.
- Added axis-lock support to the shortcut-driven `Mesh Edit` extrusion gesture so edge extrusions can be constrained to world `X`, `Y`, or `Z` while active, with a colored axis guide ray shown for the current lock; face extrusions continue to follow their face normal.

## Next

- Phase 5: build hit testing, raycasting, and marquee selection on top of BVH-backed render data.
  Current gap: face/edge/vertex hit testing, deeper BVH query plumbing, and robust multi-mode marquee behavior are still missing.
- Phase 6: implement transform tools, snapping, duplication, and mirror workflows.
  Current gap: transform gizmos now exist for translate/rotate/scale, but transform-space controls, multi-object gizmo editing, and richer snapping rules are still missing.
- Phase 7: add brush editing operations such as clip, split, hollow, merge, and face extrusion.
  Current gap: clipping and extrusion now work for axis-aligned box brushes in-canvas, but arbitrary-plane clipping, hollow/merge flows, and non-box brush editing are still missing.
- Phase 8: add mesh editing tools such as extrude, bevel, split edge, loop cut, and merge vertices.
  Current gap: vertex/edge/face subobject selection and full translate/rotate/scale editing now work for editable meshes and convex brush subobjects, and the first topology-changing ops are in place with flat/round edge beveling, but face extrude polish, weld/merge-vertex tools, dedicated split-edge/loop-cut UX, and deeper validation/polish for arbitrary brush edits are still missing.
- Phase 9: add materials, assets, entity authoring, and worker-backed async jobs.
  Current gap: richer asset catalogs, direct entity selection/editing, and real worker-backed geometry/nav rebuild jobs are still missing; only export/persistence currently runs in a real Web Worker.
- Phase 10: implement `.whmap` persistence plus GLTF and engine export flows.
  Current gap: `.whmap` is a baseline full-scene snapshot format, glTF export is JSON-only with embedded buffers and placeholder model geometry, and engine export is still a simple scene interchange format rather than a packaged runtime build.
- Continue the editor UI pass.
  Current gap: contextual menus are still mostly presentational, the canvas overlays need additional polish on small screens, and several shadcn primitives still carry default styles that should be tightened further as the toolset expands.

## Notes

- Keep geometry authoritative inside workspace packages, not React components.
- Prefer worker-backed incremental rebuilds for heavy geometry and export tasks.
- Treat `ARCHITECTURE.md` as the source of truth when the roadmap and implementation diverge.
