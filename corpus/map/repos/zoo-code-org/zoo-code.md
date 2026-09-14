# zoo-code-org/zoo-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ba46d1f34a5b @ 2a1006e3c37b084d

## Summary (orientation draft, not independently verified)

Evidence shows Zoo Code is a VS Code extension AI coding assistant continuing Roo Code, with documented modes, provider/model support, a privacy policy, and a repository-side bounded model-checking verification suite plus migration/cherry-pick workflow notes. Evidence coverage: 120 of 129 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The product is described as an AI-powered dev team inside the editor that can generate and refactor code, write documentation, answer codebase questions, automate tasks, and use MCP servers. -- evidence: [README.md#L83-L89](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L83-L89), [README.md#L14-L14](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L14-L14)
  - [observation/documented] Zoo Code continues development of Roo Code after the Roo team wound down, with a core team of former Roo contributors planning model updates, bug fixes, and features. -- evidence: [README.md#L18-L30](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L18-L30)
- components (1 claim(s)):
  - [observation/documented] Additions over Roo Code include Semble semantic code search, stronger orchestrator delegation with parent/child task recovery, and a Destructive Command Guard that blocks dangerous commands during autonomous runs. -- evidence: [README.md#L41-L47](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L41-L47)
- design-choices (3 claim(s)):
  - [observation/documented] The assistant operates through modes: Code, Architect, Ask, Debug, and user-defined Custom Modes for specialized team workflows. -- evidence: [README.md#L95-L99](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L95-L99), [README.md#L83-L89](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L83-L89)
  - [observation/documented] Per the privacy policy, telemetry is enabled by default but can be opted out via settings, and users can run models locally to avoid sending data to third parties. -- evidence: [PRIVACY.md#L62-L65](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/PRIVACY.md#L62-L65)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: local setup uses pnpm install, the extension runs via VS Code F5 debugging with hot reload, and VSIX builds install through pnpm install:vsix or manual code --install-extension. -- evidence: [README.md#L144-L145](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L144-L145), [README.md#L141-L142](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L141-L142), [README.md#L129-L131](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L129-L131), [README.md#L174-L183](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L174-L183), [README.md#L151-L153](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L151-L153)
  - [observation/documented] Repository development practice: a bounded TypeScript model-check suite (pnpm lifecycle:model-check) runs six submodels covering task delegation, shared-store concurrency, provider handoff, cleanup, parser scoping, and completion persistence, and is the model-check entry point in the compile CI job. -- evidence: [docs/architecture/task-lifecycle-model.md#L3-L3](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L3-L3), [docs/architecture/task-lifecycle-model.md#L18-L18](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L18-L18), [docs/architecture/task-lifecycle-model.md#L11-L16](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L11-L16)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Zoo Code is distributed as a VS Code extension (a VS Code Marketplace badge and VSIX installation instructions appear in the README). -- evidence: [README.md#L1-L10](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L1-L10), [README.md#L174-L183](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L174-L183), [README.md#L149-L149](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L149-L149)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](zoo-code.detail.md)

Metadata and full claim list: [full detail](zoo-code.detail.md)
Human notes ([notes](zoo-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
