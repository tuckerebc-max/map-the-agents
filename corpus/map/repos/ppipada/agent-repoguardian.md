# ppipada/agent-repoguardian

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: flexigpt/agent-repoguardian (github id 803137479).
Latest snapshot: commit d4c397259072 @ 4bfd542db638737c

## Summary (orientation draft, not independently verified)

The project is described as an AI agent that performs security scans and vulnerability analysis of code. A completed todo item records an eval processor that takes a view JSON as input, converts eval items into scan-specific items, and runs them across multiple eval items.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is described as an AI agent that performs security scans and vulnerability analysis of code. -- evidence: [README.md#L3-L3](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/README.md#L3-L3)
- components (3 claim(s)):
  - [observation/documented] A completed todo item records an eval processor that takes a view JSON as input, converts eval items into scan-specific items, and runs them across multiple eval items. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25)
  - [observation/documented] A code scanner component takes a scan item as input and performs an LLM-based scan, with OpenAI and Anthropic provider capability and batching marked as done. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25)
- design-choices (1 claim(s)):
  - [observation/documented] The detection prompt is designed to work in a chain-of-thought manner to detect, verify, and score issues. -- evidence: [todo.md#L31-L37](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L31-L37)
- workflows (1 claim(s)):
  - [inference/documented] The todo suggests an earlier 'solver' scaffolding for orchestration, prompts, and results was planned for evaluation with the OpenAI eval framework, though these items are struck through and unchecked. -- evidence: [todo.md#L3-L3](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L3-L3), [todo.md#L5-L8](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L5-L8)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Completed pipeline items cover multiple eval types (simple query, batching with code-item segregation, tagged plus query, categorization) and running evals across multiple eval sets. -- evidence: [todo.md#L39-L39](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L39-L39), [todo.md#L29-L29](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L29-L29), [todo.md#L31-L37](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L31-L37)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The todo records metric collection from eval runs including token metrics, while accuracy metrics and an eval report script remain unchecked. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](agent-repoguardian.detail.md) for every claim.)

Metadata and full claim list: [full detail](agent-repoguardian.detail.md)
Human notes ([notes](agent-repoguardian.notes.md), never overwritten by build)

[Back to map index](../../index.md)
