# lucasduys/forge

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 642c60b104f0 @ 6c3a4dda31584cbd

## Summary (orientation draft, not independently verified)

Selected evidence records: The brainstorm phase turns a one-line idea into an R-numbered spec with testable acceptance criteria, and every task must map to at least one R-number. Tasks execute in their own git worktrees with TDD, and passing tasks are squash-merged atomically; a streaming topological scheduler dispatches tasks as soon as their dependencies complete.

## Source coverage

Source coverage (partial): 6 of 41 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The brainstorm phase turns a one-line idea into an R-numbered spec with testable acceptance criteria, and every task must map to at least one R-number. -- evidence: [README.md#L121-L121](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L121-L121), [README.md#L39-L43](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L39-L43)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The pipeline is strictly sequential (brainstorm → plan → execute), enforced programmatically via an approval gate, frontier validation, and validateWorkflowPrerequisites(); users cannot skip phases or bypass the approval gate. -- evidence: [docs/architecture.md#L96-L103](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L96-L103), [README.md#L121-L121](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L121-L121)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, create a feature branch, make changes, run tests via node scripts/run-tests.cjs, and open a pull request, with details in CONTRIBUTING.md. -- evidence: [README.md#L212-L216](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L212-L216), [README.md#L218-L218](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L218-L218)
- skills-patterns (1 claim(s)):
  - [observation/documented] Three cross-cutting skills run automatically across agents: Karpathy guardrails inlined into executor/reviewer/planner, graphify knowledge-graph integration, and DESIGN.md design-system support — the latter two degrade gracefully when their inputs are absent. -- evidence: [docs/architecture.md#L85-L92](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L85-L92), [docs/architecture.md#L76-L83](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L76-L83), [docs/architecture.md#L70-L74](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L70-L74)
- interfaces (2 claim(s)):
  - [observation/documented] Users drive Forge through slash commands such as /forge brainstorm, /forge plan, /forge execute --autonomy full, plus read-only /forge watch and /forge status --json, and /forge resume for recovery. -- evidence: [README.md#L62-L66](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L62-L66), [README.md#L166-L177](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L166-L177)
  - [observation/documented] Collaboration defines a transport interface (read, cas, del, list, publish/subscribe/sendTargeted) with two backends: Ably WebSocket pub/sub (sub-second) and a zero-setup polling backend over a git branch (~2.5s). -- evidence: [docs/architecture.md#L115-L115](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L115-L115), [docs/architecture.md#L117-L120](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L117-L120)
- memory-state (1 claim(s)):
  - [observation/documented] Loop state lives on disk in a .forge directory rather than in the conversation, so crashes, context resets, and OOMs can recover by restarting the state machine from disk. -- evidence: [README.md#L45-L45](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L45-L45)
- orchestration (1 claim(s)):
  - [observation/documented] Tasks execute in their own git worktrees with TDD, and passing tasks are squash-merged atomically; a streaming topological scheduler dispatches tasks as soon as their dependencies complete. -- evidence: [docs/architecture.md#L27-L64](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L27-L64), [README.md#L39-L43](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/README.md#L39-L43), [docs/architecture.md#L9-L9](https://github.com/LucasDuys/forge/blob/642c60b104f0d5dae9782dd4b54f12df407c9697/docs/architecture.md#L9-L9)
- tools-permissions (1 claim(s)):
More evidence: [full detail](forge.detail.md)

Metadata and full claim list: [full detail](forge.detail.md)
Human notes ([notes](forge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
