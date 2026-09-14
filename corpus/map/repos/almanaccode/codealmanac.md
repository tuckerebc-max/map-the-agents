# almanaccode/codealmanac

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0f153501f40a @ 7b563da85011a057

## Summary (orientation draft, not independently verified)

Selected evidence records: Read commands accept --wiki <name> to target another registered local wiki; by default they target the exact current directory when it is a registered repository root. The serve command opens a read-only local web viewer rendering pages, search, topics, backlinks, and file-reference navigation, with --no-open and --wiki options.

## Source coverage

Source coverage (partial): 3 of 395 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The wiki is plain markdown stored in the repo under almanac/, indexed locally and reviewed in Git like other code changes; a repo counts as a wiki when almanac/topics.yaml and almanac/README.md exist. -- evidence: [README.md#L19-L22](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L19-L22), [README.md#L280-L281](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L280-L281)
  - [observation/documented] The product is local-only: no hosted login, connect, or upload commands, no public SDK or MCP package, and no alternate wiki roots beyond almanac/. -- evidence: [README.md#L417-L431](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L417-L431), [README.md#L415-L415](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L415-L415), [README.md#L433-L435](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L433-L435)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Read commands accept --wiki <name> to target another registered local wiki; by default they target the exact current directory when it is a registered repository root. -- evidence: [README.md#L126-L128](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L126-L128)
  - [observation/documented] The serve command opens a read-only local web viewer rendering pages, search, topics, backlinks, and file-reference navigation, with --no-open and --wiki options. -- evidence: [README.md#L352-L356](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L352-L356)
- memory-state (1 claim(s)):
  - [observation/documented] Derived local state lives under ~/.codealmanac/, including a main database recording repositories, runs, run events, worker locks, and sync state, plus per-repo index databases. -- evidence: [README.md#L287-L290](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L287-L290), [README.md#L292-L294](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L292-L294), [README.md#L285-L285](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L285-L285)
- orchestration (3 claim(s)):
  - [observation/documented] Lifecycle commands (init, ingest, garden) queue runs and start a local worker; jobs can be listed, shown, logged, attached to, or cancelled, and records persist after the starting terminal closes. -- evidence: [README.md#L214-L214](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L214-L214), [README.md#L217-L217](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L217-L217), [README.md#L206-L207](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L206-L207), [README.md#L159-L161](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L159-L161), [README.md#L220-L220](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L220-L220), [README.md#L226-L230](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L226-L230), [README.md#L211-L211](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L211-L211), [README.md#L223-L224](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L223-L224)
  - [observation/documented] Setup installs three macOS launchd jobs: Sync every 5 hours scanning agent conversations, Garden every 24 hours reviewing wikis, and Update every 24 hours installing safe CLI updates. -- evidence: [README.md#L63-L67](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L63-L67), [README.md#L60-L61](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L60-L61)
- tools-permissions (1 claim(s)):
  - [observation/documented] Lifecycle agents run with broad, non-interactive filesystem permissions; the almanac/ boundary is described as an instruction and commit policy rather than an OS sandbox. -- evidence: [README.md#L137-L141](https://github.com/AlmanacCode/codealmanac/blob/0f153501f40a6596fe7c47dc6198eda149363135/README.md#L137-L141)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](codealmanac.detail.md)

Metadata and full claim list: [full detail](codealmanac.detail.md)
Human notes ([notes](codealmanac.notes.md), never overwritten by build)

[Back to map index](../../index.md)
