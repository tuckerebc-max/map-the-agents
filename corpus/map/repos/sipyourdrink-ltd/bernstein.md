# sipyourdrink-ltd/bernstein

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: chernistry/bernstein (github id 1188762020).
Latest snapshot: commit ce5c5217c1dc @ fa9ff58cd4c4ac48

## Summary (orientation draft, not independently verified)

The snapshot is README and architecture documentation for Bernstein, an Apache-2.0 beta 'governance layer for AI agents' built around a deterministic Python scheduler, per-task git worktrees, and offline-verifiable audit/lineage records. Evidence is documentation-only; no source code slices are present. Evidence coverage: 109 of 337 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 615 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] A janitor verifies task completion via concrete signals (files exist, tests pass, content matches) and moves tasks to done/ or failed/ without trusting agent claims; a separate LLM reviewer runs afterward and can push corrections back into the queue. -- evidence: [docs/architecture/ARCHITECTURE.md#L132-L132](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L132-L132), [docs/architecture/ARCHITECTURE.md#L136-L136](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L136-L136)
  - [observation/documented] The Task Server is a FastAPI REST application on port 8052 exposing /tasks, /status, and /metrics, with routes split across roughly 70 modules in core/routes/ and state checkpointed to .sdd/runtime/tasks.jsonl. -- evidence: [docs/architecture/ARCHITECTURE.md#L108-L108](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L108-L108), [docs/architecture/ARCHITECTURE.md#L15-L33](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L15-L33)
- design-choices (2 claim(s)):
  - [observation/documented] The orchestrator is deterministic Python with no model in the coordination loop; only one planning LLM call happens up front, and the same plan replays to a byte-identical task graph. -- evidence: [README.md#L40-L40](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L40-L40), [docs/architecture/ARCHITECTURE.md#L7-L7](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L7-L7), [docs/architecture/ARCHITECTURE.md#L205-L220](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L205-L220)
  - [observation/documented] All state is stored as files under .sdd/ with no databases or hidden memory, chosen for inspectability, recoverability, auditability, and git-friendliness; runtime state under .sdd/runtime/ is ephemeral. -- evidence: [docs/architecture/ARCHITECTURE.md#L51-L54](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L51-L54), [docs/architecture/ARCHITECTURE.md#L56-L56](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L56-L56), [docs/architecture/ARCHITECTURE.md#L49-L49](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L49-L49)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI surface includes bernstein init, -g, live, run plan.yaml, stop, workflow run/resume, replay/lineage/audit verification commands, and bernstein verify receipt for offline receipt checking. -- evidence: [README.md#L196-L203](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L196-L203), [README.md#L135-L140](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L135-L140), [README.md#L148-L151](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L148-L151), [README.md#L165-L175](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L165-L175), [README.md#L209-L212](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L209-L212)
  - [observation/documented] Runs are declared in YAML manifests defining phases, roles, node dependencies, conditional edges, and retry policies; workflow resume validates the manifest digest at start and refuses a changed spec. -- evidence: [README.md#L61-L68](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L61-L68), [README.md#L98-L106](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L98-L106), [README.md#L55-L55](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L55-L55), [README.md#L214-L214](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L214-L214)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Pluggable sandbox backends implement a SandboxBackend/SandboxSession protocol; first-party options are worktree (default), docker, e2b Firecracker microVMs, and modal serverless containers, with third parties registering via an entry-point group. -- evidence: [docs/architecture/ARCHITECTURE.md#L242-L261](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L242-L261)
More evidence: [full detail](bernstein.detail.md)

Metadata and full claim list: [full detail](bernstein.detail.md)
Human notes ([notes](bernstein.notes.md), never overwritten by build)

[Back to map index](../../index.md)
