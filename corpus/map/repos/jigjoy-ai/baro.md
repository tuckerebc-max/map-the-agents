# jigjoy-ai/baro

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f9a610774532 @ a7f091ec4bf6f132

## Summary (orientation draft, not independently verified)

baro is an autonomous software-factory CLI (npm package baro-ai) that compiles a goal into a machine-checkable contract, plans a DAG of stories, runs story agents in parallel across isolated git worktrees, and gates merges behind tests, builds, an evidence critic, and write-surface ownership. Documentation also details a collective coordination mode, runtime DAG replanning, and a paired A/B experiment harness. Evidence coverage: 107 of 172 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture is described as a Rust TUI host plus a TypeScript orchestrator whose bounded contexts communicate over the Mozaik event bus, with machine gates in front of every merge. -- evidence: [README.md#L80-L80](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L80-L80)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the experiment guide instructs preparing a clean git repo with an unexecuted prd.json whose stories have concrete acceptance criteria and test commands, and installing workspace dependencies with npm install before running trials. -- evidence: [docs/collective-experiment.md#L143-L143](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L143-L143), [docs/collective-experiment.md#L179-L182](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L179-L182)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is installed globally via npm as baro-ai and is invoked as `baro "<goal>"` inside a repository, opening a TUI where intake asks questions, the user confirms the plan, and the run proceeds. -- evidence: [README.md#L27-L30](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L27-L30), [README.md#L32-L32](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L32-L32), [README.md#L18-L20](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L18-L20)
  - [observation/documented] CLI commands include headless detached runs printing a run id, `watch` and `logs` for following runs, `runs`/`stop` for listing and stopping, `--resume` (never re-plans), `--continue` (always re-plans), `--doctor`, `login`, and `connect`. -- evidence: [README.md#L46-L58](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L46-L58), [README.md#L36-L42](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L36-L42)
- memory-state (1 claim(s)):
  - [observation/documented] Proposal IDs act as idempotency keys: exact re-delivery returns the remembered decision without reapplying, reuse with different content is rejected, and applied decisions can be restored from the PRD's runtimeGraph metadata when a host resumes the same runId. -- evidence: [docs/collective-experiment.md#L75-L87](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L75-L87)
- orchestration (4 claim(s)):
  - [observation/documented] Goals are compiled by an architect into machine-checkable invariants before coding, split into a DAG of stories built in parallel across isolated git worktrees, with runtime replanning able to add and rewire stories mid-run and failed gates spawning remediation stories. -- evidence: [README.md#L8-L11](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L8-L11), [README.md#L82-L91](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L82-L91)
  - [observation/documented] Collective coordination is the CLI default; a legacy Conductor mode (one owner of DAG levels, retries, completion) can be selected with `--coordination legacy` for A/B comparison. -- evidence: [docs/collective-experiment.md#L7-L7](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L7-L7), [docs/collective-experiment.md#L5-L5](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L5-L5)
More evidence: [full detail](baro.detail.md)

Metadata and full claim list: [full detail](baro.detail.md)
Human notes ([notes](baro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
