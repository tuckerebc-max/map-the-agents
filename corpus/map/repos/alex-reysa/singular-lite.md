# alex-reysa/singular-lite

Status: distilled - Freshness: stale
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7ef2c5299fa7 @ 3d6eae7a7b09983d

## Summary (orientation draft, not independently verified)

singular-lite documents a bash/Python multi-agent orchestration engine with a three-tier scheduling model, an explicit reconcile cycle, gate/audit/decider recovery routing, and a documented session-independence invariant for auditors. Security docs treat repo-configured commands and worktrees as an executable trust boundary.

## Source coverage

Source coverage (partial): 3 of 163 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes singular as a bash and Python orchestration engine that runs autonomous AI coding agents in parallel across a repository, using a three-tier scheduling model of an origin loop, area planners, and worker agents with git-worktree isolation. -- evidence: [README.md#L7-L12](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L7-L12)
- components (1 claim(s)):
  - [observation/documented] An agent-tiers table documents three roles: an L0 origin scheduler that runs the reconcile cycle, L1 area planners that stage batches of tasks per DAG node, and L2 workers that execute one task per isolated git worktree and produce a state packet for review. -- evidence: [README.md#L18-L22](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L18-L22)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are asked to run the test script before opening a PR, keep the generic engine free of project-specific rules, and avoid committing state, worktree, or evidence directories. -- evidence: [CONTRIBUTING.md#L7-L15](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/CONTRIBUTING.md#L7-L15)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Each reconcile cycle is documented as five ordered steps: importing staged task proposals, recovering stale leases, integrating completed worker branches, dispatching new tasks, and writing a state snapshot. -- evidence: [README.md#L28-L32](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L28-L32)
  - [observation/documented] With detached dispatch on by default, reconcile pre-leases frontier tasks and spawns each worker in its own session, returning quickly; a separate reaper process later attributes completions, failures, and crashes from dispatch records and worker exit files. -- evidence: [README.md#L83-L89](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L83-L89)
- tools-permissions (2 claim(s)):
  - [observation/documented] After each worker run, a configured gate command's result feeds an auditor model, and a decider maps the failure class and remaining retries to a recovery action - retry, amend-scope, escalate, or park - via a deterministic table before any model round-trip. -- evidence: [README.md#L43-L47](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L43-L47)
  - [observation/documented] The docs state an independence pin that always runs final-audit, paired-audit, re-critique, and critic-recheck fresh, regardless of session-routing settings, so no configuration lets an auditor grade work from a session that already formed an opinion on it. -- evidence: [README.md#L380-L386](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L380-L386)
- evaluation (1 claim(s)):
More evidence: [full detail](singular-lite.detail.md)

Metadata and full claim list: [full detail](singular-lite.detail.md)
Human notes ([notes](singular-lite.notes.md), never overwritten by build)

[Back to map index](../../index.md)
