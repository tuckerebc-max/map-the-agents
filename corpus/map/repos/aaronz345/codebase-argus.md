# aaronz345/codebase-argus

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 71922e7555f3 @ 3d55409f5967b792

## Summary (orientation draft, not independently verified)

Selected evidence records: The README describes the tool as a review desk for maintainers that inspects pull requests, failing CI logs, and long-lived fork syncs using one shared set of signals: patches, checks, files, branch state, policy gates, provider consensus, and local git simulations. An at-a-glance table documents five distinct workflows - PR review, CI review, autofix planning, downstream fork sync, and agent handoff - each with its own input shape and output type.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 7 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

7 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes the tool as a review desk for maintainers that inspects pull requests, failing CI logs, and long-lived fork syncs using one shared set of signals: patches, checks, files, branch state, policy gates, provider consensus, and local git simulations. -- evidence: [README.md#L36-L39](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L36-L39)
- components (1 claim(s)):
  - [observation/documented] An at-a-glance table documents five distinct workflows - PR review, CI review, autofix planning, downstream fork sync, and agent handoff - each with its own input shape and output type. -- evidence: [README.md#L79-L85](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L79-L85)
- design-choices (1 claim(s)):
  - [observation/documented] A planning document describes an intended architecture where pr-review.ts keeps responsibility for normalized review results, while new, separately focused helpers would own policy parsing, evidence extraction, tribunal aggregation, and workflow generation. -- evidence: [docs/superpowers/plans/2026-05-06-maintainer-firewall-mvp.md#L7-L7](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/docs/superpowers/plans/2026-05-06-maintainer-firewall-mvp.md#L7-L7)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A README permission table lists pull requests and issues with read/write access; contents, checks, actions and metadata have read access. -- evidence: [README.md#L295-L302](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L295-L302)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] A write-model table documents narrow write behavior: the hosted demo is read-only, GitHub App reviews post comment-level PR reviews, and the sync command runs dry-run unless --execute, --push, or --create-pr is explicitly passed. -- evidence: [README.md#L451-L458](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L451-L458)
  - [observation/documented] Documented webhook behavior includes verifying the X-Hub-Signature-256 header before handling a payload, and skipping draft pull requests as well as PRs labeled argus:paused. -- evidence: [README.md#L337-L343](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L337-L343)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] The case study frames its own output as a review aid rather than an approval, noting that pull-request state and code can change after the reviewed snapshot was taken. -- evidence: [docs/case-studies/cowagent-2965.md#L34-L34](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/docs/case-studies/cowagent-2965.md#L34-L34)
More evidence: [full detail](codebase-argus.detail.md)

Metadata and full claim list: [full detail](codebase-argus.detail.md)
Human notes ([notes](codebase-argus.notes.md), never overwritten by build)

[Back to map index](../../index.md)
