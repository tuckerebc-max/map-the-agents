# codingthefuturewithai/software-dev-prompt-library

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2caeefbce8d0 @ 8878b550b3069202

## Summary (orientation draft, not independently verified)

The repository is a documented prompt library for AI-assisted software development, organized into categorized prompts and workflow chains, with metadata files and guides; it is marked work-in-progress and beta, tested only with aider.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Metadata files provide AI assistant compatibility, SDLC phase information, complexity ratings, and usage guidelines for each prompt. -- evidence: [PROJECT_ORGANIZATION.md#L64-L69](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L64-L69)
- components (2 claim(s)):
  - [observation/documented] The prompts directory is organized into nine categories (architecture, code-analysis, coding, documentation, learning, maintenance, planning, requirements, testing), each split into general and assistant-specific subdirectories. -- evidence: [PROJECT_ORGANIZATION.md#L4-L33](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L4-L33)
  - [observation/documented] Workflows are organized into general sprint and maintenance workflows plus assistant-specific ones for aider, github-copilot, and claude, each with sprint and maintenance subfolders. -- evidence: [PROJECT_ORGANIZATION.md#L36-L51](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L36-L51)
- design-choices (1 claim(s)):
  - [observation/documented] Prompt guidelines call for one primary task per prompt with clear scope boundaries, defined output formats, validation rules, and prompts designed to fit into chains. -- evidence: [docs/guides/prompt-guidelines.md#L35-L39](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L35-L39), [docs/guides/prompt-guidelines.md#L27-L31](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L27-L31), [docs/guides/prompt-guidelines.md#L15-L19](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L15-L19)
- workflows (3 claim(s)):
  - [observation/documented] The getting-started guide describes two main workflows: a project-scaffolding sprint chain for new projects and a post-scaffolding sprint chain for adding features, both located under workflows/assistant-specific/aider/sprint and designed for the aider assistant. -- evidence: [docs/guides/getting-started.md#L63-L64](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L63-L64), [docs/guides/getting-started.md#L58-L60](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L58-L60), [docs/guides/getting-started.md#L55-L55](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/getting-started.md#L55-L55)
  - [observation/documented] Repository development practice: contributors are instructed to follow prompt guidelines, provide both .md and .meta.md files, test prompts across AI models and project types, and maintain language and framework agnosticism. -- evidence: [README.md#L92-L96](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L92-L96)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Each prompt consists of two files: a .md file containing AI instructions and a .meta.md file containing usage documentation. -- evidence: [README.md#L43-L45](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L43-L45), [docs/guides/prompt-guidelines.md#L10-L13](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/docs/guides/prompt-guidelines.md#L10-L13)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Workflows are described as connected chains of prompts with defined input/output dependencies between phases, verification points for chain integrity, and progress tracking. -- evidence: [README.md#L13-L18](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L13-L18), [PROJECT_ORGANIZATION.md#L54-L61](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/PROJECT_ORGANIZATION.md#L54-L61)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (2 claim(s)):
  - [observation/documented] The library is marked as a work in progress; the post-scaffolding sprint workflow prompts are described as the most rigorously tested, while many individual prompts are not yet part of a defined workflow or fully tested. -- evidence: [README.md#L3-L7](https://github.com/codingthefuturewithai/software-dev-prompt-library/blob/2caeefbce8d007f55286e2e7af4e0573f1d8ac68/README.md#L3-L7)
More evidence: [full detail](software-dev-prompt-library.detail.md)

Metadata and full claim list: [full detail](software-dev-prompt-library.detail.md)
Human notes ([notes](software-dev-prompt-library.notes.md), never overwritten by build)

[Back to map index](../../index.md)
