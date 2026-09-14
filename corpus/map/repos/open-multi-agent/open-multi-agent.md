# open-multi-agent/open-multi-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit eaeb420c4364 @ fccf7ae5c773ed7e

## Summary (orientation draft, not independently verified)

Selected evidence records: The core package exposes three run modes: runAgent() for a single agent, runTasks() for an explicit pipeline, and runTeam() which plans from a goal. An OpenMultiAgent instance is constructed with a default provider/model and an onToolCall callback that can return 'suspend' for consequential tool calls or 'allow' otherwise.

## Source coverage

Source coverage (partial): 6 of 47 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Consequential actions pause for durable approvals: a suspend request is stored beside the checkpoint, bound to a SHA-256 hash of what the reviewer saw, decisions are atomic and first-wins, and tampered requests fail closed. -- evidence: [README.md#L91-L91](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L91-L91)
  - [observation/documented] The runtime records every model block, tool call, and context rewrite in a journal; verifyRun() checks offline that each block reproduces byte for byte, reporting evicted windows as inconclusive rather than failures. -- evidence: [README.md#L97-L97](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L97-L97)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: issues and pull requests are welcome, with CONTRIBUTING.md covering workspace boundaries, validation, and submission guidance. -- evidence: [README.md#L204-L204](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L204-L204)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The core package exposes three run modes: runAgent() for a single agent, runTasks() for an explicit pipeline, and runTeam() which plans from a goal. -- evidence: [README.md#L87-L87](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L87-L87)
  - [observation/documented] An OpenMultiAgent instance is constructed with a default provider/model and an onToolCall callback that can return 'suspend' for consequential tool calls or 'allow' otherwise. -- evidence: [README.md#L63-L69](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L63-L69), [README.md#L60-L61](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L60-L61)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
  - [observation/documented] runTeam() uses one model call to turn a goal into a task graph with assignees and dependencies, a deterministic scheduler executes it, and a second call writes the final answer; the coordinator is not consulted mid-run. -- evidence: [README.md#L150-L150](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L150-L150)
  - [observation/documented] Adaptive recovery is opt-in via recovery.mode 'repairable': a Replanner or onTaskOutcome callback proposes a PlanPatch, OMA validates it, an optional onPlanPatch gate approves it, and the patch is applied atomically before the triggering task completes. -- evidence: [docs/adaptive-recovery.md#L9-L18](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L9-L18), [docs/adaptive-recovery.md#L3-L5](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/docs/adaptive-recovery.md#L3-L5)
- tools-permissions (1 claim(s)):
  - [observation/documented] Egress policy supports 'offline' or 'allowlist' modes checked before a built-in adapter connects; child policies can only tighten parents, unenforceable transports fail closed, and process/ACP backends sit outside the policy. -- evidence: [README.md#L109-L111](https://github.com/open-multi-agent/open-multi-agent/blob/eaeb420c4364e8d63757a7bbdc412655ed6c9420/README.md#L109-L111)
- evaluation (1 claim(s)):
More evidence: [full detail](open-multi-agent.detail.md)

Metadata and full claim list: [full detail](open-multi-agent.detail.md)
Human notes ([notes](open-multi-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
