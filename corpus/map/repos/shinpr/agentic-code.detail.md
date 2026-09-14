# shinpr/agentic-code -- full detail

[Back to orientation](agentic-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shinpr/agentic-code/a3f058520173fd8e777c4aed77e9c45c38aed1c2/43776da81f0dea8e.json](../../../wiki/dossiers/shinpr/agentic-code/a3f058520173fd8e777c4aed77e9c45c38aed1c2/43776da81f0dea8e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The package ships an AGENTS.md entry point plus .agents directories for tasks, workflows, skills, and context-maps mapping tasks to skills. -- evidence: [README.md#L15-L21](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L15-L21) (`clm_b33a47b64c8836d7cfcedd04334edf1e0709f31a18c91aa990b6a9da9bb1dfa2`)
- [observation/documented] Defined tasks include task-analysis, prd-creation, technical-design, acceptance-test-generation, work-planning, implementation, quality-assurance, code-review, technical-document-review, and integration-test-review, each owning one kind of result. -- evidence: [README.md#L89-L89](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L89-L89), [README.md#L91-L102](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L91-L102) (`clm_cf72b2dbd166de8a4b2adec7a290147922ff4675f9b97dd1991126d7e1a83d26`)

## design-choices (2 claim(s))

- [observation/documented] Work routing is based on decision burden rather than file count: Small work runs directly, Medium requires design and a work plan, Large requires a PRD with separate design decisions. -- evidence: [README.md#L23-L23](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L23-L23), [README.md#L25-L29](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L25-L29), [README.md#L31-L31](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L31-L31) (`clm_02f5fd2c253e825e0a8aa44d8a1b96febc49c05efaae643680fe09485b17989e`)
- [observation/documented] The workflow is strict about requirements, user authority, irreversible actions, accepted durable decisions, and completion evidence, while letting the agent resolve reversible repository-local choices itself. -- evidence: [README.md#L81-L81](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L81-L81) (`clm_1940a2f98617d0f6b71bd0a0ae9310b26ebb10fedeac57b20bdb6e9f35c5a7be`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the installed AGENTS.md instructs the agent to inspect project structure, load the metacognition skill for the session, and route requests through task-analysis or direct execution before loading task definitions. -- evidence: [AGENTS.md#L25-L26](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L25-L26), [AGENTS.md#L18-L19](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L18-L19), [AGENTS.md#L23-L23](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L23-L23) (`clm_c52a90e4d63c359feaa94f4c7c34fffbc0c3531d060dad71d8c88c6e2d5cb8ec`)
- [observation/documented] Repository development practice: before completion the agent must confirm outcome and exit conditions, run applicable repository checks, record verification evidence and remaining limitations, and update affected documentation. -- evidence: [AGENTS.md#L82-L85](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L82-L85), [AGENTS.md#L80-L80](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L80-L80) (`clm_5b6c0343738355956eaaf67a877742cfb739e3ce720fb152d79a581e1258fe02`)
- [observation/documented] Repository development practice: review findings are treated as candidates to apply, decline, or return for user decision, and a repeated preference without new evidence does not block progress. -- evidence: [AGENTS.md#L76-L76](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L76-L76), [AGENTS.md#L72-L74](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L72-L74), [AGENTS.md#L70-L70](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/AGENTS.md#L70-L70) (`clm_387ce9b27fceff70365e2f48e32a6c33eba90226dce597c29137528f0e6486ec`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills hold reusable judgment for coding, testing, documentation, implementation strategy, and metacognition, and are loaded only when a selected task needs them rather than at startup. -- evidence: [README.md#L110-L110](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L110-L110) (`clm_0b825dc8e3ed9bbf076d2fe22a1588f596b5baaf8223e691b1c703c0684f5a4e`)

## interfaces (2 claim(s))

- [observation/documented] The CLI is invoked as npx agentic-code with a project name to scaffold a repository, and a skills subcommand supporting --codex, --cursor, --project, and --path options. -- evidence: [README.md#L138-L140](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L138-L140), [README.md#L120-L120](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L120-L120), [README.md#L114-L114](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L114-L114), [README.md#L130-L130](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L130-L130), [README.md#L39-L42](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L39-L42), [README.md#L123-L124](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L123-L124) (`clm_ee74d541f0ff2c4eb3ed33185826a9450349a6549f9bcf7b77eac6bbd78662eb`)
- [observation/documented] The skills subcommand installs only .agents/skills/ and does not install the full AGENTS.md workflow. -- evidence: [README.md#L114-L114](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L114-L114) (`clm_da31861f806aa9555077f0478e224a7048ad3050780a9c5f08fa20b942433fac`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A workflow file, .agents/workflows/agentic-coding.md, coordinates Medium/Large work across requirements, design, planning, implementation, QA, and review while preserving the approved outcome. -- evidence: [README.md#L106-L106](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L106-L106) (`clm_d325936df5b0a2204e2f97f3534c69b2d7ed42415d4d04f8db8c6a703cccfc20`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool requires Node.js 22 or later, per the Quick Start section. -- evidence: [README.md#L35-L35](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L35-L35) (`clm_d7273e45d6be4e3b40fa1d09d146ea6cee2a296c5d7239522b38575eff827689`)

## limitations (2 claim(s))

- [observation/documented] The framework adds process and context overhead, so direct agent execution is usually cheaper for well-scoped fixes, disposable experiments, or one-shot scripts with clear safe boundaries. -- evidence: [README.md#L170-L170](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L170-L170) (`clm_a51b632c4c0307e4d78e93045120506aa215ebda0ac0a805e32ed4107a8792ce`)
- [observation/documented] The core is language-agnostic but TypeScript-specific references are included; other languages rely on repository-native commands until language-specific guidance is added. -- evidence: [README.md#L174-L174](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L174-L174) (`clm_940dff58a86bc5f6ae54f44aa4fe75d95ee06bd0a8ab380df4e5ee377f8452c5`)

## relevance (1 claim(s))

- [observation/documented] The workflow targets tools that read repository-level AGENTS.md instructions, with Cursor, Codex CLI, and Gemini CLI cited as common examples, and exact discovery behavior depends on tool version. -- evidence: [README.md#L146-L146](https://github.com/shinpr/agentic-code/blob/a3f058520173fd8e777c4aed77e9c45c38aed1c2/README.md#L146-L146) (`clm_828fce4a09620854a69b2f42493983cf37b2e73f7cb02c9a1a142caab89be8df`)

