# codingthefuturewithai/software-dev-prompt-library -- full detail

[Back to orientation](software-dev-prompt-library.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/5866d6f2/3ab23530/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/8878b550b3069202.json](../../../wiki/dossiers/5866d6f2/3ab23530/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/8878b550b3069202.json)

## specifications (1 claim(s))

- [observation/documented] Metadata files provide AI assistant compatibility, SDLC phase information, complexity ratings, and usage guidelines for each prompt. -- evidence: [PROJECT_ORGANIZATION.md#L64-L69](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L64-L69) (`clm_84c12ff5dab5dfabd876bc436e359448bf6912d602a26dd1b8e10752aaaeaf18`)

## components (2 claim(s))

- [observation/documented] The prompts directory is organized into nine categories (architecture, code-analysis, coding, documentation, learning, maintenance, planning, requirements, testing), each split into general and assistant-specific subdirectories. -- evidence: [PROJECT_ORGANIZATION.md#L4-L33](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L4-L33) (`clm_bface0404703c3040f37a1462d334d9eda0e7099c769d1869fc95e7035df1a90`)
- [observation/documented] Workflows are organized into general sprint and maintenance workflows plus assistant-specific ones for aider, github-copilot, and claude, each with sprint and maintenance subfolders. -- evidence: [PROJECT_ORGANIZATION.md#L36-L51](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L36-L51) (`clm_be723d5177ac8187b19f9a729f849be0fc488d8134a8593f88a89dbc0b5b6a66`)

## design-choices (1 claim(s))

- [observation/documented] Prompt guidelines call for one primary task per prompt with clear scope boundaries, defined output formats, validation rules, and prompts designed to fit into chains. -- evidence: [docs/guides/prompt-guidelines.md#L35-L39](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L35-L39), [docs/guides/prompt-guidelines.md#L27-L31](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L27-L31), [docs/guides/prompt-guidelines.md#L15-L19](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L15-L19) (`clm_dc068f6b6aa294e286d3f3259ec8d966d5ec73b71e12871dc85ed97e80368dfa`)

## workflows (3 claim(s))

- [observation/documented] The getting-started guide describes two main workflows: a project-scaffolding sprint chain for new projects and a post-scaffolding sprint chain for adding features, both located under workflows/assistant-specific/aider/sprint and designed for the aider assistant. -- evidence: [docs/guides/getting-started.md#L63-L64](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L63-L64), [docs/guides/getting-started.md#L58-L60](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L58-L60), [docs/guides/getting-started.md#L55-L55](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L55-L55) (`clm_cb8bd3a23e9fabca0b2193744e4541a86b50ee23993afb3f33f485814b701b1d`)
- [observation/documented] Repository development practice: contributors are instructed to follow prompt guidelines, provide both .md and .meta.md files, test prompts across AI models and project types, and maintain language and framework agnosticism. -- evidence: [README.md#L92-L96](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L92-L96) (`clm_0fdc1b68f55a864bc234d9514c42abdadae751e5091a309060342564a36f4d6a`)
- [observation/documented] Repository development practice: prompt guidelines instruct authors to test prompts individually across AI models and project types, and to test chains for input/output flow, integrity, and progress tracking; this is author guidance rather than an automated eval harness. -- evidence: [docs/guides/prompt-guidelines.md#L87-L91](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L87-L91), [docs/guides/prompt-guidelines.md#L81-L85](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L81-L85) (`clm_ad89621ad80e4a256407ac6ef478ab6edba6d112a0ae61ad9ce4a4af6d46045d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Each prompt consists of two files: a .md file containing AI instructions and a .meta.md file containing usage documentation. -- evidence: [README.md#L43-L45](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L43-L45), [docs/guides/prompt-guidelines.md#L10-L13](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L10-L13) (`clm_90b8ec99fd3146e6318343fd5a1ead1dd0e427fdd7370ac699f88b89739f0686`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Workflows are described as connected chains of prompts with defined input/output dependencies between phases, verification points for chain integrity, and progress tracking. -- evidence: [README.md#L13-L18](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L13-L18), [PROJECT_ORGANIZATION.md#L54-L61](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L54-L61) (`clm_2ce3f634547b7afeedfd6de36f5e58e65e4e56201244d648345401fa16db5042`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] The library is marked as a work in progress; the post-scaffolding sprint workflow prompts are described as the most rigorously tested, while many individual prompts are not yet part of a defined workflow or fully tested. -- evidence: [README.md#L3-L7](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L3-L7) (`clm_2d1196673ede719abac486746d7e8517c9f2b0e8b7c7494beeb241a4c40c6eb3`)
- [observation/documented] The workflows and prompts are described as beta and tested only with the aider AI coding assistant; support for other assistants such as Cursor and Codeium's Windsurf is planned for future updates. -- evidence: [docs/guides/getting-started.md#L66-L67](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L66-L67) (`clm_959c70e5684c6151e0d89d653d2c55c832081f07a052dd97288206602db10b53`)

## relevance (1 claim(s))

- [observation/documented] The library targets AI-assisted software development across phases from project inception to maintenance, aiming for language- and framework-agnostic, modular, single-purpose prompts that chain together for complex tasks. -- evidence: [docs/guides/getting-started.md#L32-L35](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L32-L35), [README.md#L9-L9](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L9-L9), [README.md#L73-L79](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L73-L79) (`clm_e5fc2b3d0cd62cb37994037ff21be274a0a1808830cd40d2ce48a419c3f32327`)

