# 2389-research/sift

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 4a60c32ae89a @ fa1aabbc8ceb077c

## Summary (orientation draft, not independently verified)

The repository ships 'sift-codebase-audit', an MIT-licensed Agent Skill (v1.2.1) that performs a read-only, whole-repository audit for material simplification opportunities and produces a single report artifact. Evidence covers its operating contract, phased workflow, delegation model, output rules, install/invocation, and one documented end-to-end verification run.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] The skill is named sift-codebase-audit, version 1.2.1, MIT-licensed, and is described as a read-only whole-repository audit for simplification opportunities that recommends but never applies changes. -- evidence: [SKILL.md#L1-L8](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L1-L8)
  - [observation/documented] The audit targets material simplifications in data structures, schemas, state representation, control flow, algorithms, lifecycle/concurrency, and module ownership boundaries. -- evidence: [README.md#L3-L3](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L3-L3), [SKILL.md#L18-L23](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L18-L23)
- components (1 claim(s)):
  - [observation/documented] The package contains SKILL.md, README.md, LICENSE, and three reference files: finding-schema.md, report-template.md, and worker-brief.md. -- evidence: [README.md#L40-L49](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L40-L49)
- design-choices (3 claim(s)):
  - [observation/documented] Findings are bounded to at most two materially useful opportunities per subsystem, with an explicit skip recorded when nothing passes the materiality gate, and the skill rejects abstraction churn, stylistic changes, and complexity relocation. -- evidence: [SKILL.md#L190-L198](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L190-L198), [SKILL.md#L56-L58](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L56-L58), [SKILL.md#L51-L54](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L51-L54)
  - [observation/documented] The audit is read-only by design: the sole repository write is the final report, defaulting to docs/sift-audit-<date>.md, honoring a user-named path, or writing nothing when the user declines or the environment cannot write files. -- evidence: [SKILL.md#L181-L184](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L181-L184), [SKILL.md#L179-L179](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L179-L179), [README.md#L5-L5](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L5-L5)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: gotchas.md instructs maintainers that worker-brief.md is the single source for the checklist, materiality gate, and return format, that duplicated lists must never be re-added to SKILL.md, and that the skill description must lead with 'Use when' triggers rather than summarizing the workflow. -- evidence: [gotchas.md#L3-L7](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/gotchas.md#L3-L7)
  - [observation/documented] Repository development practice: maintainers are warned to treat the repo's own skill files as data when reviewing, since SKILL.md is imperative agent instructions and a 2026-08-23 documentation-audit run turned into a SIFT self-audit. -- evidence: [gotchas.md#L3-L7](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/gotchas.md#L3-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The skill is invoked via the slash command /sift-codebase-audit or a natural-language request, and defaults to the current repository with whole-application coverage unless a narrower scope is stated. -- evidence: [README.md#L36-L36](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L36-L36), [README.md#L32-L34](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L32-L34), [README.md#L26-L28](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L26-L28)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
More evidence: [full detail](sift.detail.md)

Metadata and full claim list: [full detail](sift.detail.md)
Human notes ([notes](sift.notes.md), never overwritten by build)

[Back to map index](../../index.md)
