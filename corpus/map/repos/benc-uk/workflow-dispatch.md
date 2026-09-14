# benc-uk/workflow-dispatch

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 78e99d70d9ac @ 3eb4093669280522

## Summary (orientation draft, not independently verified)

The evidence documents benc-uk/workflow-dispatch, a GitHub Action that triggers other workflows via the workflow_dispatch event, with inputs for workflow targeting, cross-repo dispatch, tokens, and optional wait/polling behavior. All evidence is README documentation; no code slices are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The intended use case is chaining workflows, e.g. a CI build workflow triggering a CD deploy workflow, allowing separate CI/CD workflows that pass data between them. -- evidence: [README.md#L6-L6](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L6-L6)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (9 claim(s)):
  - [observation/documented] The action triggers another GitHub Actions workflow using the workflow_dispatch event, and the target workflow must be configured for that event type. -- evidence: [README.md#L3-L4](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L3-L4)
  - [observation/documented] The required `workflow` input accepts the target workflow's name, filename, or ID, and all three forms are used when looking up the workflow. -- evidence: [README.md#L24-L24](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L24-L24)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] By default the standard GITHUB_TOKEN is used, so users no longer need to supply their own token; cross-repo dispatch requires a PAT with repo rights passed via a secret. -- evidence: [README.md#L55-L55](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L55-L55), [README.md#L53-L53](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L53-L53)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] Workflows triggered by this action appear in the GitHub UI as "manually triggered", since the action simulates the manual workflow_dispatch trigger. -- evidence: [README.md#L14-L14](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L14-L14)
- relevance: unknown (no source-linked claim submitted for this facet)

(7 additional claim(s) omitted for length; see [full detail](workflow-dispatch.detail.md) for every claim.)

Metadata and full claim list: [full detail](workflow-dispatch.detail.md)
Human notes ([notes](workflow-dispatch.notes.md), never overwritten by build)

[Back to map index](../../index.md)
