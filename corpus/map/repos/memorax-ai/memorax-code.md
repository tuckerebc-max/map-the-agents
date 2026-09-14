# memorax-ai/memorax-code

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1525c20fbcad @ 916cf8e021cf3d6f

## Summary (orientation draft, not independently verified)

MemoraX Code is a local memory layer for coding-agent clients: a Backend integrates seven clients through six adapters and a shared runtime, owning local memory, repo scope, trace, lifecycle and update scheduling while excluding model execution, credentials and transcript creation. Memory splits into Coding, Repo, Personal and Procedure categories; trace capture is on by default; a detached updater installs new versions after setup; search-on-turn-start is off by default. Documented limits cover Trae's missing headless Repo Memory worker and a Mark ID registration-order restriction. CONTRIBUTING.md/AGENTS.md describe repository development practice. Evidence: 5 of 10 candidate files stored; 5 omitted by byte budget; selection incomplete.

## Source coverage

Source coverage (partial): 5 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The system integrates seven coding clients with one local Backend, a capability-oriented modular monolith, surrounded by six client deployment adapters, a shared runtime source layer, and an npm assembly/CLI layer. -- evidence: [ARCHITECTURE.md#L28-L32](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L28-L32), [ARCHITECTURE.md#L36-L39](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L36-L39)
  - [observation/documented] The Backend owns the local memory service, repository scope, trace, lifecycle, and update scheduling, but must not own model execution, provider credentials, or native transcript creation. -- evidence: [ARCHITECTURE.md#L126-L138](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L126-L138)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to read CONTRIBUTING.md before making changes, and AGENTS.md defines working rules for coding agents, runtime/data invariants, and Git handoff requirements. -- evidence: [ARCHITECTURE.md#L9-L18](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L9-L18), [README.md#L356-L358](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L356-L358)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Adapter Hooks and plugins communicate with the Backend via versioned, client-qualified local HTTP commands carrying JSON and token headers, with a request deadline and optional cancellation; the transport does not retry or start the Backend. -- evidence: [ARCHITECTURE.md#L147-L165](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L147-L165)
- memory-state (3 claim(s)):
  - [observation/documented] Memory is divided into four categories: Coding Memory (engineering lessons), Repo Memory (repository knowledge), Personal Memory (user preferences), and Procedure Memory (reusable task steps). -- evidence: [README.md#L235-L240](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L235-L240)
  - [observation/documented] Personal and Procedure Memory stay in the current repository under .repo_memory/; writes compare existing content so equivalent requests make no change and conflicts update or supersede entries. -- evidence: [README.md#L242-L250](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L242-L250)
- orchestration (2 claim(s)):
  - [observation/documented] After setup, the managed Backend schedules a detached updater that locks, resolves a channel target, installs an exact published version via the package-replacement path, and reuses non-interactive setup reconciliation. -- evidence: [ARCHITECTURE.md#L262-L275](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L262-L275), [ARCHITECTURE.md#L301-L309](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L301-L309)
More evidence: [full detail](memorax-code.detail.md)

Metadata and full claim list: [full detail](memorax-code.detail.md)
Human notes ([notes](memorax-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
