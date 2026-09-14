# joinwell52-ai/joinwell52

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6961492e9a46 @ 2a0fd4110d4ba967

## Summary (orientation draft, not independently verified)

The snapshot is a README plus a Chinese architecture draft for the joinwell52/TMPA research repository: it documents TMPA Core S1.0 specifications, an executable Reference Reader with a C01–C14 conformance runner, author-run CodeFlowMu V1.8.0 evidence, and a draft digital-employee architecture. Most product claims come from documentation rather than inspected code, and the evidence explicitly bounds its own conformance claims. Evidence coverage: 145 of 390 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 746 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] TMPA Core Specification S1.0 is presented as the normative layer defining objects, authority, lifecycle, Reader behavior, and conformance requirements, with criteria labeled C01–C14. -- evidence: [README.md#L52-L56](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L52-L56), [README.md#L231-L243](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L231-L243)
- components (2 claim(s)):
  - [observation/documented] The repository ships TMPA Core S1.0 machine schemas, fixtures, profiles, an author-produced Reference Reader, and a C01–C14 conformance runner. -- evidence: [README.md#L258-L258](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L258-L258)
  - [observation/documented] CodeFlowMu is described as a local PM/DEV/QA/OPS AI development team with a PC control center and a mobile PWA, distributed as a proprietary free Windows x64 preview from a separate distribution repository. -- evidence: [README.md#L75-L75](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L75-L75), [README.md#L310-L310](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L310-L310)
- design-choices (1 claim(s)):
  - [observation/documented] TMPA Core is described as storage-neutral: files, database rows, object-store items, or events may carry the same governance semantics, with durable state kept outside model sessions and a Reader reconstructing governance state. -- evidence: [README.md#L254-L254](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L254-L254), [README.md#L249-L252](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L249-L252)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The Reference Reader is run via npm commands: `npm run demo` for a demo delivery and `npm run tmpa:s1.0:conformance` for the conformance runner, after `npm ci`. -- evidence: [README.md#L262-L268](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L262-L268)
- memory-state (1 claim(s)):
  - [observation/documented] TMPA moves durable work facts out of volatile model memory so lifecycle, authority, conflict, and audit state can be reconstructed from inspectable evidence across asynchronous execution. -- evidence: [README.md#L172-L172](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L172-L172)
- orchestration (1 claim(s)):
  - [inference/documented] The V0.3.1 draft architecture proposes a five-layer design (FCoP fact layer, TMPA Reader, Runtime, definition/deployment, instance) coordinated by asynchronous fact loops rather than a synchronous all-agents-online pipeline; it is explicitly a draft, not a stable specification. -- evidence: [docs/zh/digital-employee/architecture.md#L86-L92](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L86-L92), [docs/zh/digital-employee/architecture.md#L17-L17](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L17-L17), [docs/zh/digital-employee/architecture.md#L94-L94](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L94-L94)
- tools-permissions (1 claim(s)):
  - [inference/documented] The draft proposes each execution role be bounded by a default-deny Capability Envelope/Sandbox Boundary limiting tools, paths, network, and credentials, plus a negative list of contextual business rules; as draft target language, this is not confirmed shipped behavior. -- evidence: [docs/zh/digital-employee/architecture.md#L149-L150](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L149-L150)
More evidence: [full detail](joinwell52.detail.md)

Metadata and full claim list: [full detail](joinwell52.detail.md)
Human notes ([notes](joinwell52.notes.md), never overwritten by build)

[Back to map index](../../index.md)
