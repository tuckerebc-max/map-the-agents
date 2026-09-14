# danau5tin/tbench-agentic-data-pipeline

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4489453eb3c2 @ e0d4b0f95d30ce67

## Summary (orientation draft, not independently verified)

README-only evidence describes a multi-agent data-generation pipeline (idea, builder, review agents) coordinated by a Task Manager, producing validated Terminal-Bench-style training datapoints. No source code is present in the snapshot, so claims are documentation-based.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] Idea generation agents take Terminal Bench seed tasks, generate multiple variations, select the best ideas, and output draft specifications to a shared workspace; refinement criteria are withheld until after brainstorming to maximize creativity. -- evidence: [README.md#L95-L95](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L95-L95), [README.md#L91-L93](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L91-L93)
  - [observation/documented] Builder agents turn draft specifications into complete executable datapoints, iterating on a validation script until the Dockerfile builds, tests fail initially, dependencies are present, and test weights sum to 1.0. -- evidence: [README.md#L102-L106](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L102-L106), [README.md#L98-L100](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L98-L100)
- design-choices (1 claim(s)):
  - [observation/documented] Design rationale given: separate agent types for focus and parallel scaling, a shared filesystem instead of message passing for simplicity and debuggability, and a Task Manager for coordination, failure recovery, and monitoring. -- evidence: [README.md#L227-L229](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L227-L229), [README.md#L232-L234](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L232-L234), [README.md#L222-L224](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L222-L224)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Task Manager exposes an API where agents claim tasks by type (e.g. get_next_task with an agent ID and task_types) and complete them with results via complete_task. -- evidence: [README.md#L127-L128](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L127-L128), [README.md#L121-L121](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L121-L121)
  - [observation/documented] Each generated datapoint is a directory containing prompt.md, a dockerfile (Ubuntu 24.04 or similar), tests.py pytest functions, weights.json, and a files/ directory with resources such as broken code and config files. -- evidence: [README.md#L142-L151](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L142-L151)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The pipeline runs three specialized agent stages (idea generation, datapoint building, quality review), with agents working independently in parallel and coordinated by a central Task Manager that prevents duplication and handles failures. -- evidence: [README.md#L45-L45](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L45-L45), [README.md#L51-L51](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L51-L51), [README.md#L47-L49](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L47-L49)
  - [observation/documented] The Task Manager provides atomic task claiming to avoid collisions, automatic timeout recovery, parent-child task tracking, and real-time status monitoring. -- evidence: [README.md#L130-L134](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L130-L134)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [inference/documented] The reported outcomes (331 validated datapoints, 100% Docker-validated environments, category and technology breakdowns) suggest the pipeline's output quality was measured, though these figures are README-reported rather than harness-verified. -- evidence: [README.md#L58-L61](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L58-L61), [README.md#L65-L74](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L65-L74), [README.md#L77-L80](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L77-L80)
- dependencies (1 claim(s)):
More evidence: [full detail](tbench-agentic-data-pipeline.detail.md)

Metadata and full claim list: [full detail](tbench-agentic-data-pipeline.detail.md)
Human notes ([notes](tbench-agentic-data-pipeline.notes.md), never overwritten by build)

[Back to map index](../../index.md)
