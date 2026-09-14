# thesylvester/crispy

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a0abb0bac65b @ 717deaf69b8a7ffb

## Summary (orientation draft, not independently verified)

The codebase is organized into three layers: core (src/core/) owning state and logic, host (src/host/) as a thin RPC router, and webview (src/webview/) for UI. Core includes vendor-agnostic transcript types, per-vendor adapters, a session-channel pub/sub multiplexer, session-manager orchestration, and an activity-index that owns all ~/.crispy/ disk I/O.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (5 claim(s)):
  - [observation/documented] The codebase is organized into three layers: core (src/core/) owning state and logic, host (src/host/) as a thin RPC router, and webview (src/webview/) for UI. -- evidence: [CLAUDE.md#L14-L16](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L14-L16), [architecture.md#L3-L4](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L3-L4)
  - [observation/documented] Core includes vendor-agnostic transcript types, per-vendor adapters, a session-channel pub/sub multiplexer, session-manager orchestration, and an activity-index that owns all ~/.crispy/ disk I/O. -- evidence: [architecture.md#L8-L11](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L8-L11), [CLAUDE.md#L25-L34](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L25-L34)
- design-choices (1 claim(s)):
  - [observation/documented] Core is written in a functional style: free functions with module-level state rather than classes, and the webview derives all state client-side from channel events with no direct file I/O. -- evidence: [CLAUDE.md#L57-L59](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L57-L59), [CLAUDE.md#L22-L23](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L22-L23), [architecture.md#L13-L14](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L13-L14)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm run typecheck, npm test (e2e pipeline test), npm run test:unit (vitest), and npm run dev for a dev server at localhost:3456, with visual checks via a browser-qa sub-agent. -- evidence: [CLAUDE.md#L170-L170](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L170-L170), [CLAUDE.md#L163-L166](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L163-L166), [CLAUDE.md#L172-L174](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L172-L174)
  - [observation/documented] Repository development practice: CLAUDE.md forbids business logic in the host, vendor fields in transcript.ts, edits to generated Codex protocol files, and writes to ~/.crispy/ outside activity-index.ts. -- evidence: [CLAUDE.md#L75-L108](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L75-L108)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The webview talks to the host over a JSON-RPC protocol via a SessionService interface with dual transports: VS Code postMessage and WebSocket. -- evidence: [architecture.md#L34-L42](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L34-L42), [architecture.md#L66-L76](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L66-L76)
  - [observation/documented] SessionService method groups cover session lifecycle (list/load/create/fork/close), agent control (send, interrupt, setModel, setPermissions), approvals, subscriptions, and file operations. -- evidence: [architecture.md#L66-L76](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L66-L76)
- memory-state (1 claim(s)):
  - [observation/documented] Agent memory indexes every session transcript locally with full-text and semantic search, backfills existing Claude Code and Codex transcripts, and recall results show match provenance with date/recency filters. -- evidence: [README.md#L75-L78](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L75-L78), [README.md#L57-L65](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L57-L65), [README.md#L13-L18](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L13-L18)
- orchestration (1 claim(s)):
  - [observation/documented] /superthink pits Claude and Codex against each other on the same question and converges into a unified verdict, with sub-agents opening as live watchable tabs; /super-implement, /reflect, /handoff, and /spec-mode support planning workflows. -- evidence: [README.md#L13-L18](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L13-L18), [README.md#L93-L97](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L93-L97)
- tools-permissions (2 claim(s)):
More evidence: [full detail](crispy.detail.md)

Metadata and full claim list: [full detail](crispy.detail.md)
Human notes ([notes](crispy.notes.md), never overwritten by build)

[Back to map index](../../index.md)
