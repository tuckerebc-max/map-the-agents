# agentsmesh/agentsmesh

Status: distilled - Freshness: stale
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1f90b14194d0 @ fdb5f6b69465f402

## Summary (orientation draft, not independently verified)

Selected evidence records: Server side comprises a Go backend (Gin+GORM) handling auth, pod lifecycle, tickets, billing and runner-cert PKI; a WebSocket Relay for terminal data; and a self-hosted Go runner daemon that spawns PTY pods. Client side includes a Rust core of 10 crates compiled to WASM for web/desktop and exposed to iOS via UniFFI, plus Next.js web, Electron desktop, SwiftUI/TCA iOS, and a web-admin console.

## Source coverage

Source coverage (partial): 3 of 26 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Server side comprises a Go backend (Gin+GORM) handling auth, pod lifecycle, tickets, billing and runner-cert PKI; a WebSocket Relay for terminal data; and a self-hosted Go runner daemon that spawns PTY pods. -- evidence: [README.md#L84-L88](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L84-L88)
  - [observation/documented] Client side includes a Rust core of 10 crates compiled to WASM for web/desktop and exposed to iOS via UniFFI, plus Next.js web, Electron desktop, SwiftUI/TCA iOS, and a web-admin console. -- evidence: [README.md#L92-L98](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L92-L98)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture splits control plane from data plane: orchestration travels over gRPC with mTLS while terminal I/O streams through a stateless Relay cluster, so the backend never handles PTY bytes. -- evidence: [README.md#L76-L76](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L76-L76), [README.md#L63-L63](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L63-L63)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The runner CLI exposes login (with --headless and --server options), run, and service install/start subcommands. -- evidence: [README.md#L116-L118](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L116-L118), [README.md#L134-L136](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L134-L136), [README.md#L128-L130](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L128-L130), [README.md#L140-L143](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L140-L143), [README.md#L122-L124](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L122-L124)
  - [observation/documented] Pods communicate over channels with @mentions within a bound mesh topology, and tickets on a Kanban board can be bound to pods with progress and MR/PR tracking. -- evidence: [README.md#L67-L72](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L67-L72)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Runners advertise capacity (max_concurrent_pods) and pods are scheduled onto a chosen runner or an available one from the pool; each pod gets an isolated Git worktree sandbox, private credentials, and its own branch. -- evidence: [README.md#L55-L61](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L55-L61)
  - [observation/documented] An Autopilot control agent watches a pod, sends the next instruction when it goes idle, enforces iteration caps, keeps decision history, and supports human takeover and handback. -- evidence: [README.md#L55-L61](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L55-L61), [README.md#L67-L72](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L67-L72)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](agentsmesh.detail.md)

Metadata and full claim list: [full detail](agentsmesh.detail.md)
Human notes ([notes](agentsmesh.notes.md), never overwritten by build)

[Back to map index](../../index.md)
