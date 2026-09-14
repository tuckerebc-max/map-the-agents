# shinpr/agentic-code

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a3f058520173 @ 43776da81f0dea8e

## Summary (orientation draft, not independently verified)

The package ships an AGENTS.md entry point plus .agents directories for tasks, workflows, skills, and context-maps mapping tasks to skills. Work routing is based on decision burden rather than file count: Small work runs directly, Medium requires design and a work plan, Large requires a PRD with separate design decisions.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The package ships an AGENTS.md entry point plus .agents directories for tasks, workflows, skills, and context-maps mapping tasks to skills. -- evidence: [README.md#L15-L21](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L15-L21)
  - [observation/documented] Defined tasks include task-analysis, prd-creation, technical-design, acceptance-test-generation, work-planning, implementation, quality-assurance, code-review, technical-document-review, and integration-test-review, each owning one kind of result. -- evidence: [README.md#L89-L89](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L89-L89), [README.md#L91-L102](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L91-L102)
- design-choices (2 claim(s)):
  - [observation/documented] Work routing is based on decision burden rather than file count: Small work runs directly, Medium requires design and a work plan, Large requires a PRD with separate design decisions. -- evidence: [README.md#L23-L23](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L23-L23), [README.md#L25-L29](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L25-L29), [README.md#L31-L31](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L31-L31)
  - [observation/documented] The workflow is strict about requirements, user authority, irreversible actions, accepted durable decisions, and completion evidence, while letting the agent resolve reversible repository-local choices itself. -- evidence: [README.md#L81-L81](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L81-L81)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the installed AGENTS.md instructs the agent to inspect project structure, load the metacognition skill for the session, and route requests through task-analysis or direct execution before loading task definitions. -- evidence: [AGENTS.md#L25-L26](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L25-L26), [AGENTS.md#L18-L19](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L18-L19), [AGENTS.md#L23-L23](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L23-L23)
  - [observation/documented] Repository development practice: before completion the agent must confirm outcome and exit conditions, run applicable repository checks, record verification evidence and remaining limitations, and update affected documentation. -- evidence: [AGENTS.md#L82-L85](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L82-L85), [AGENTS.md#L80-L80](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L80-L80)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills hold reusable judgment for coding, testing, documentation, implementation strategy, and metacognition, and are loaded only when a selected task needs them rather than at startup. -- evidence: [README.md#L110-L110](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L110-L110)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI is invoked as npx agentic-code with a project name to scaffold a repository, and a skills subcommand supporting --codex, --cursor, --project, and --path options. -- evidence: [README.md#L138-L140](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L138-L140), [README.md#L120-L120](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L120-L120), [README.md#L114-L114](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L114-L114), [README.md#L130-L130](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L130-L130), [README.md#L39-L42](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L39-L42), [README.md#L123-L124](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L123-L124)
  - [observation/documented] The skills subcommand installs only .agents/skills/ and does not install the full AGENTS.md workflow. -- evidence: [README.md#L114-L114](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L114-L114)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A workflow file, .agents/workflows/agentic-coding.md, coordinates Medium/Large work across requirements, design, planning, implementation, QA, and review while preserving the approved outcome. -- evidence: [README.md#L106-L106](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L106-L106)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agentic-code.detail.md)

Metadata and full claim list: [full detail](agentic-code.detail.md)
Human notes ([notes](agentic-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
