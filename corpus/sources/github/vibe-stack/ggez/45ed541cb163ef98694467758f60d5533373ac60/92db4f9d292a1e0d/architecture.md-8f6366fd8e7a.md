Below is a **complete single specification document** you can give directly to a coding agent or keep as the project’s `ARCHITECTURE.md`.
It includes the **full editor architecture + the geometry kernel specification** used by classic level editors (Hammer / Radiant / TrenchBroom lineage), but modernized for a **Source-2-style hybrid editor**.

---

# WEB HAMMER

## Architecture & Geometry Kernel Specification

**Project name:**
`web-hammer`

**Goal:**
Create a **browser-based Source-2-style level editor** for designing game levels quickly using:

* brush solids
* mesh editing
* asset placement
* entity logic
* realtime viewport
* AI-assisted level generation

The editor is optimized for **rapid level blockout and iteration**, similar to Hammer but modernized for web workflows.

---

# 1. Core Design Principles

## 1.1 Hybrid geometry system

The editor must support **three primary geometry types**:

```
Brush solids (convex)
Editable polygon meshes
Instanced models
```

Each type has a different internal representation.

Brushes are best for:

```
walls
floors
rooms
corridors
collision volumes
blockout
```

Meshes are best for:

```
complex shapes
organic geometry
detail geometry
```

Models are best for:

```
props
prefabs
environment assets
```

---

# 2. Technology Stack

## Core

```
Vite
React
TypeScript
```

## Rendering

```
three
@react-three/fiber
@react-three/drei
```

## Geometry utilities

```
earcut
clipper2-ts
```

## Spatial acceleration

```
three-mesh-bvh
```

## State

```
valtio
xstate
```

## Workers

```
Web Workers
comlink
```

---

# 3. High-Level Architecture

The editor consists of four major systems:

```
Editor Core
Geometry Kernel
Render Pipeline
Tool System
```

---

# 4. Editor Core

The editor core stores **authoring state**.

React must NOT store geometry state.

Instead:

```
EditorCore
 ├ SceneDocument
 ├ CommandStack
 ├ Selection
 └ EventBus
```

---

## 4.1 Scene Document

The scene document is the source of truth.

```
SceneDocument
{
 nodes: Map<NodeID, GeometryNode>
 entities: Map<EntityID, Entity>
 materials: Map<MaterialID, Material>
 assets: Map<AssetID, Asset>
 layers: Map<LayerID, Layer>
}
```

---

## 4.2 Geometry Nodes

```
GeometryNode =
 BrushNode
 MeshNode
 ModelNode
```

---

# 5. Geometry Kernel

This is the most critical part of the editor.

The kernel implements the **mathematical rules of level geometry**.

Inspired by the geometry kernels used in:

```
Quake editors
Radiant
Hammer
TrenchBroom
```

---

# 6. Brush Geometry Kernel

Brushes are **convex solids defined by planes**.

Brushes are NOT stored as vertex meshes.

Instead:

```
Brush = intersection of half-spaces
```

---

## 6.1 Plane Definition

A plane is defined as:

```
ax + by + cz + d = 0
```

Representation:

```
Plane
{
 normal: Vec3
 distance: number
}
```

Where:

```
distance = plane offset from origin
```

---

## 6.2 Brush Definition

```
Brush
{
 planes: Plane[]
 faces: Face[]
}
```

Faces are derived from planes.

---

# 7. Brush Reconstruction Algorithm

The algorithm used by classic level editors.

Steps:

```
for each plane
  compute intersection with all other plane pairs
  find vertices that lie inside all halfspaces
  build polygon for that plane
```

Pseudo:

```
for plane P
  vertices = []

  for plane A
    for plane B
       v = intersection(P, A, B)

       if insideBrush(v)
           vertices.push(v)

  polygon = sortVertices(vertices)
```

---

## 7.1 Triple Plane Intersection

Compute vertex from three planes:

```
P1
P2
P3
```

Solve linear system:

```
N1·x + d1 = 0
N2·x + d2 = 0
N3·x + d3 = 0
```

Use determinant method.

---

## 7.2 Inside Test

Check if vertex is inside brush:

```
for each plane
 if dot(normal, vertex) + d > epsilon
   reject
```

---

## 7.3 Face Vertex Ordering

Vertices must be sorted.

Algorithm:

```
1 compute face center
2 compute tangent axes
3 project vertices
4 sort by angle
```

---

# 8. Brush Editing Operations

Supported operations:

```
create primitive
clip
extrude
hollow
split
merge
```

---

## 8.1 Clip Tool

Clip brush by plane.

Algorithm:

```
split brush planes
reconstruct faces
```

---

## 8.2 Extrude Face

Steps:

```
duplicate face plane
offset plane
add side planes
rebuild brush
```

---

# 9. Mesh Geometry Kernel

Mesh nodes support polygon editing.

Representation:

```
EditableMesh
{
 vertices
 halfEdges
 faces
}
```

---

## 9.1 Half-Edge Structure

Half-edge topology allows:

```
fast edge traversal
loop selection
face extrusion
vertex editing
```

Structure:

```
HalfEdge
{
 vertex
 twin
 next
 face
}
```

---

# 10. Mesh Editing Operations

Supported operations:

```
extrude face
delete face
merge vertices
split edge
loop cut
bevel
```

---

# 11. Triangulation

Faces must be triangulated for rendering.

Use:

```
earcut
```

Process:

```
polygon vertices
 → earcut
 → triangle indices
```

---

# 12. Render Pipeline

Rendering uses Three.js.

Pipeline:

```
authoring geometry
 → triangulation
 → BufferGeometry
 → BVH build
 → render
```

---

# 13. BVH Acceleration

Use:

```
three-mesh-bvh
```

Purpose:

```
fast raycasting
selection
collision queries
```

---

# 14. Selection System

Selection supports:

```
object
face
edge
vertex
```

Methods:

```
raycast
marquee selection
```

---

# 15. Tool System

Tools operate on editor core.

Tools:

```
select
transform
clip
extrude
mesh edit
asset place
```

Use `xstate` to model tool states.

Example:

```
idle
hover
drag
commit
cancel
```

---

# 16. Transform System

Transform operations:

```
move
rotate
scale
duplicate
mirror
```

Grid snapping:

```
1
2
4
8
16
32
```

---

# 17. Asset System

Assets represent external resources.

```
Asset
{
 id
 type
 path
 metadata
}
```

Types:

```
model
material
prefab
```

---

# 18. Entity System

Entities represent gameplay objects.

Examples:

```
spawn
trigger
light
sound
script
```

Structure:

```
Entity
{
 id
 type
 transform
 properties
}
```

---

# 19. Worker System

Heavy tasks run in workers.

Workers:

```
geometryWorker
meshWorker
navWorker
exportWorker
```

Tasks:

```
triangulation
brush rebuild
navmesh
export
```

---

# 20. File Format

Editor save format:

```
.whmap
```

Structure:

```
{
 scene
 nodes
 entities
 materials
 assets
}
```

JSON based.

---

# 21. Export Pipeline

Export targets:

```
GLTF
engine format
USD (optional)
```

Steps:

```
bake transforms
merge meshes
generate collision
export
```

---

# 22. Performance Requirements

Target performance:

```
60 FPS viewport
1000+ objects
fast selection
incremental rebuilds
```

Strategies:

```
dirty node rebuilds
worker tasks
BVH acceleration
```

---

# 23. Development Roadmap

## Phase 1

Viewport:

```
R3F canvas
camera
grid
scene
```

---

## Phase 2

Editor core:

```
scene document
selection
command stack
```

---

## Phase 3

Brush kernel.

---

## Phase 4

Mesh kernel.

---

## Phase 5

Selection system.

---

## Phase 6

Transform tools.

---

## Phase 7

Brush editing tools.

---

## Phase 8

Mesh editing tools.

---

## Phase 9

Materials and assets.

---

## Phase 10

Export pipeline.

---

# 24. Future Extensions

Possible advanced systems:

```
AI level generation
collaborative editing
procedural geometry tools
navmesh generation
terrain sculpting
```

---

# 25. Key Implementation Rules

Always follow:

```
React is UI only
geometry lives in core
derived render meshes
worker heavy tasks
incremental rebuild
```

---

# END OF SPEC

This document defines the **complete architecture and geometry kernel rules** needed to build a **Source-2-style web level editor**.

---

If you want, I can also give you one more thing that will help massively when building this:

**the 7 algorithms Hammer/Radiant editors rely on that most people miss** (face splitting, plane snapping, epsilon handling, etc.). Those are the things that usually break custom level editors.
