# iamunbounded/devctx

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7308ec5a514e @ 1681c23458a06fb3

## Summary (orientation draft, not independently verified)

Selected evidence records: DevContext is documented as a CLI tool that automatically captures and restores AI coding context, scoped to the current repo and branch. Core commands are init, save (with a non-interactive --auto mode), resume (generates an AI prompt and copies to clipboard), log, and diff; these are described as working locally with zero dependencies.

## Source coverage

Source coverage (partial): 1 of 1 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The tool is designed to work with any AI coding tool by managing the prompt itself, described as the universal interface for LLMs; agents without MCP can run save/resume/log via terminal access as a fallback. -- evidence: [README.md#L104-L104](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L104-L104), [README.md#L115-L115](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L115-L115)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] DevContext is documented as a CLI tool that automatically captures and restores AI coding context, scoped to the current repo and branch. -- evidence: [README.md#L15-L15](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L15-L15)
  - [observation/documented] Core commands are init, save (with a non-interactive --auto mode), resume (generates an AI prompt and copies to clipboard), log, and diff; these are described as working locally with zero dependencies. -- evidence: [README.md#L50-L58](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L50-L58)
- memory-state (1 claim(s)):
  - [observation/documented] Context is stored in a .devctx/ folder in the repo; each entry captures task, goal, approaches tried (and failures), key architectural decisions, and where work left off. -- evidence: [README.md#L108-L113](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L108-L113)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Installation is via npm (npm install -g devctx), and the watch feature uses the chokidar library. -- evidence: [README.md#L61-L66](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L61-L66), [README.md#L27-L29](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L27-L29)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](devctx.detail.md) for every claim.)

Metadata and full claim list: [full detail](devctx.detail.md)
Human notes ([notes](devctx.notes.md), never overwritten by build)

[Back to map index](../../index.md)
