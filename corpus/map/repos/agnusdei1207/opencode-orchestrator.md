# agnusdei1207/opencode-orchestrator

Status: distilled - Freshness: stale
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a8f318192275 @ 7bfa1754a814c040

## Summary (orientation draft, not independently verified)

README and ADR evidence describe OpenCode Orchestrator v1.7.17, an OpenCode plugin coordinating a Commander/Planner/Worker/Reviewer mission loop with local-first memory and a bundled Rust CLI, while AGENT_MEMORY records that the formerly documented Knowledge RAG subsystem was decommissioned. Development commands appear only as contributor workflow guidance. Evidence coverage: 151 of 248 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 37 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] OpenCode Orchestrator is an MIT-licensed npm package (opencode-orchestrator) at version 1.7.17, described as multi-agent mission control for OpenCode with four agent roles. -- evidence: [README.md#L192-L192](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L192-L192), [README.md#L6-L14](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L6-L14), [README.md#L33-L35](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L33-L35), [README.md#L1-L4](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L1-L4)
- components (2 claim(s)):
  - [observation/documented] The architecture defines four agents: Commander (orchestrates missions and loop state), Planner (orders file-level tasks), Worker (isolated TDD edits), and Reviewer (verifies test evidence and builds). -- evidence: [README.md#L156-L161](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L156-L161)
  - [observation/documented] A bundled Rust CLI provides an optional multi-session TCP shell listener TUI for authorized testing environments, invoked as orchestrator shell-listener with --bind and --port flags. -- evidence: [README.md#L169-L171](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L169-L171), [README.md#L167-L167](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L167-L167)
- design-choices (1 claim(s)):
  - [observation/documented] Memory is local-first: an on-disk Ebbinghaus decay model combining BM25, tags, and graph connections, explicitly avoiding external vector databases. -- evidence: [docs/adr/0001-second-brain-knowledge-graph-rag.md#L9-L11](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/docs/adr/0001-second-brain-knowledge-graph-rag.md#L9-L11), [README.md#L24-L27](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L24-L27)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors verify the TypeScript side with npm run build, npx tsc --noEmit, and npm test, and the Rust side with cargo test --workspace plus clippy with -D warnings. -- evidence: [README.md#L184-L186](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L184-L186), [README.md#L179-L181](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L179-L181)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Users start a mission with /task <objective>, halt it with /stop or /cancel, and pause loop continuation with Esc interrupt; missions persist under .opencode/. -- evidence: [README.md#L112-L116](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L112-L116), [README.md#L108-L110](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L108-L110)
  - [observation/documented] Plugin options include per-agent concurrency limits (commander, planner, worker, reviewer) and missionLoop toggles for ledger and markdownMemory, configured in opencode.jsonc. -- evidence: [README.md#L75-L96](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L75-L96)
- memory-state (1 claim(s)):
  - [observation/documented] Mission-loop state is synced to markdown notes such as scratchpad.md, knowledge-map.canvas, and episodic notes, which were made self-contained with a lightweight inline frontmatter parser. -- evidence: [AGENT_MEMORY.md#L38-L40](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/AGENT_MEMORY.md#L38-L40), [AGENT_MEMORY.md#L11-L29](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/AGENT_MEMORY.md#L11-L29)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] ADR-0001 established a constraint of no GPU, no external model, and no external API, keeping the knowledge plane CPU-only and local. -- evidence: [docs/adr/0001-second-brain-knowledge-graph-rag.md#L23-L26](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/docs/adr/0001-second-brain-knowledge-graph-rag.md#L23-L26)
- limitations (1 claim(s)):
More evidence: [full detail](opencode-orchestrator.detail.md)

Metadata and full claim list: [full detail](opencode-orchestrator.detail.md)
Human notes ([notes](opencode-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
