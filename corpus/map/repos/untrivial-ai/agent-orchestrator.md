# untrivial-ai/agent-orchestrator

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ab968d5e7614 @ 37c4c6e5838d45b4

## Summary (orientation draft, not independently verified)

Git-backed workers each get their own branch and worktree, while Scratch workers get AO-managed branchless directories, to keep parallel work isolated. A project orchestrator agent handles planning and delegation: it breaks plans into tasks, spawns or redirects workers, passes context, and tracks progress, while workers own implementation and PRs.

## Source coverage

Source coverage (partial): 3 of 63 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Git-backed workers each get their own branch and worktree, while Scratch workers get AO-managed branchless directories, to keep parallel work isolated. -- evidence: [README.md#L33-L33](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L33-L33), [README.md#L87-L91](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L87-L91)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs coding agents to keep changes small, follow Go package boundaries, run lint/typecheck/test commands locally, use conventional commits, and keep one issue per PR. -- evidence: [AGENTS.md#L3-L3](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L3-L3), [AGENTS.md#L94-L102](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L94-L102), [AGENTS.md#L17-L23](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L17-L23), [AGENTS.md#L154-L158](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L154-L158)
  - [observation/documented] Repository development practice: API contracts are code-first; contributors edit Go DTO/spec sources and regenerate openapi.yaml and frontend TypeScript types, and CI fails if committed generated files drift. -- evidence: [AGENTS.md#L148-L148](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L148-L148), [AGENTS.md#L122-L122](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L122-L122), [AGENTS.md#L131-L133](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L131-L133)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state (1 claim(s)):
  - [observation/documented] The orchestrator keeps a project-scoped conversation preserving goals, decisions, and constraints, and combines it with repository context and live AO state like active workers, PRs, CI, and reviews. -- evidence: [README.md#L66-L66](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L66-L66)
- orchestration (1 claim(s)):
  - [observation/documented] A project orchestrator agent handles planning and delegation: it breaks plans into tasks, spawns or redirects workers, passes context, and tracks progress, while workers own implementation and PRs. -- evidence: [README.md#L68-L68](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L68-L68), [README.md#L64-L64](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L64-L64)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The product advertises support for 27 coding agents through one supervised workflow, with named examples including Claude Code, Codex, Cursor, Aider, and GitHub Copilot. -- evidence: [README.md#L131-L177](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L131-L177), [README.md#L129-L129](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L129-L129)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](agent-orchestrator.detail.md).

Metadata and full claim list: [full detail](agent-orchestrator.detail.md)
Human notes ([notes](agent-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
