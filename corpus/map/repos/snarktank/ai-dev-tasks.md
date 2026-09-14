# snarktank/ai-dev-tasks

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit efbffaac10e6 @ 26353fabe4d41e58

## Summary (orientation draft, not independently verified)

The repository is a small collection of markdown prompt files (create-prd.md, generate-tasks.md) intended to be used with AI coding assistants to structure feature development: generate a PRD, then a task list, then implement task-by-task with user review. Evidence is documentation and prompt-file content only; no runtime code is shown.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Both prompt files state the PRD and task list are written for a junior developer, requiring explicit, unambiguous, jargon-light requirements. -- evidence: [generate-tasks.md#L70-L70](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/generate-tasks.md#L70-L70), [create-prd.md#L69-L69](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L69-L69)
- workflows (3 claim(s)):
  - [observation/documented] The documented workflow is: create a PRD, generate a task list from it, then have the AI work through tasks one sub-task at a time with user review between steps. -- evidence: [README.md#L61-L61](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L61-L61), [README.md#L69-L69](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L69-L69), [README.md#L11-L13](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L11-L13)
  - [observation/documented] Repository development practice: contributions are accepted via opening an issue to discuss changes and submitting pull requests with enhancements. -- evidence: [README.md#L125-L126](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L125-L126)
- skills-patterns (7 claim(s)):
  - [observation/documented] The repo ships markdown prompt files meant to be referenced inside AI coding assistants (e.g., via @create-prd.md) to steer their behavior, rather than executable code. -- evidence: [README.md#L3-L3](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L3-L3), [README.md#L30-L34](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L30-L34), [README.md#L27-L28](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L27-L28), [README.md#L89-L90](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L89-L90)
  - [observation/documented] create-prd.md instructs the AI to ask 3-5 essential clarifying questions, formatted as numbered questions with lettered options so the user can reply with selections like '1A, 2C'. -- evidence: [create-prd.md#L9-L12](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L9-L12), [create-prd.md#L27-L29](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/create-prd.md#L27-L29)
- interfaces (1 claim(s)):
  - [observation/documented] The intended interface is file-tagging in an AI IDE/CLI: users reference the markdown files and generated PRDs with @-mentions such as @create-prd.md and @MyFeature-PRD.md. -- evidence: [README.md#L46-L49](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L46-L49), [README.md#L30-L34](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L30-L34), [README.md#L115-L117](https://github.com/snarktank/ai-dev-tasks/blob/efbffaac10e68c94e14aaa587c79b7d5015b5ebd/README.md#L115-L117)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(6 additional claim(s) omitted for length; see [full detail](ai-dev-tasks.detail.md) for every claim.)

Metadata and full claim list: [full detail](ai-dev-tasks.detail.md)
Human notes ([notes](ai-dev-tasks.notes.md), never overwritten by build)

[Back to map index](../../index.md)
