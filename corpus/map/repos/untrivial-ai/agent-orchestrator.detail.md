# untrivial-ai/agent-orchestrator -- full detail

[Back to orientation](agent-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/untrivial-ai/agent-orchestrator/ab968d5e761469eb32c1b4dc780cde721a9998de/37c4c6e5838d45b4.json](../../../wiki/dossiers/untrivial-ai/agent-orchestrator/ab968d5e761469eb32c1b4dc780cde721a9998de/37c4c6e5838d45b4.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Git-backed workers each get their own branch and worktree, while Scratch workers get AO-managed branchless directories, to keep parallel work isolated. -- evidence: [README.md#L33-L33](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L33-L33), [README.md#L87-L91](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L87-L91) (`clm_3ed626fe47f66e8f81668920ffa6602fe8f4c36ff6363abc00e07b4cbfa00908`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs coding agents to keep changes small, follow Go package boundaries, run lint/typecheck/test commands locally, use conventional commits, and keep one issue per PR. -- evidence: [AGENTS.md#L3-L3](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L3-L3), [AGENTS.md#L94-L102](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L94-L102), [AGENTS.md#L17-L23](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L17-L23), [AGENTS.md#L154-L158](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L154-L158) (`clm_f523ae3be9839090f05b870e30378905c921494629d35e21d4f0999cc2ea2485`)
- [observation/documented] Repository development practice: API contracts are code-first; contributors edit Go DTO/spec sources and regenerate openapi.yaml and frontend TypeScript types, and CI fails if committed generated files drift. -- evidence: [AGENTS.md#L148-L148](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L148-L148), [AGENTS.md#L122-L122](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L122-L122), [AGENTS.md#L131-L133](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/AGENTS.md#L131-L133) (`clm_4886f5770b3c3bf498df6a19cf059244a11cd3425c6a26c8361378888ad0b8a8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (1 claim(s))

- [observation/documented] The orchestrator keeps a project-scoped conversation preserving goals, decisions, and constraints, and combines it with repository context and live AO state like active workers, PRs, CI, and reviews. -- evidence: [README.md#L66-L66](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L66-L66) (`clm_0f5e16ef79b24897be70caca500bbb08f107c45fd3d8d64dab462de53bc615c8`)

## orchestration (1 claim(s))

- [observation/documented] A project orchestrator agent handles planning and delegation: it breaks plans into tasks, spawns or redirects workers, passes context, and tracks progress, while workers own implementation and PRs. -- evidence: [README.md#L68-L68](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L68-L68), [README.md#L64-L64](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L64-L64) (`clm_f870a9b0d41c80f59633913f4d9addaf93b11e1bece277f4f9a4d090540a1fcd`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product advertises support for 27 coding agents through one supervised workflow, with named examples including Claude Code, Codex, Cursor, Aider, and GitHub Copilot. -- evidence: [README.md#L131-L177](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L131-L177), [README.md#L129-L129](https://github.com/Untrivial-ai/agent-orchestrator/blob/ab968d5e761469eb32c1b4dc780cde721a9998de/README.md#L129-L129) (`clm_3ef25d32d49392879a2fbfbe85a600b49a5b46dc188d9ed015fe8b58a73fafba`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

