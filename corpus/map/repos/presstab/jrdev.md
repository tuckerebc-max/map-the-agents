# presstab/jrdev

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6fa64e9aa863 @ e89fbd92ce10e510

## Summary (orientation draft, not independently verified)

JrDev is a terminal-based AI coding assistant with a six-phase /code agent pipeline, a persistent project context system stored in .jrdev, isolated chat threads, and named model profiles for cost-aware model switching. Evidence is documentation-based; no eval harness or product-side permission model beyond change confirmations is documented.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] JrDev uses named model profiles (advanced_reasoning, advanced_coding, intermediate_reasoning, quick_reasoning, intent_router, low_cost_search) to match model cost and capability to each task; defaults depend on the provided API key and are customizable. -- evidence: [README.md#L70-L70](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L70-L70), [README.md#L72-L77](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L72-L77), [README.md#L79-L79](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L79-L79)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] JrDev runs in the user's current working directory, started by entering 'jrdev' in a project directory, with commands like /init and /code typed into a Command Input field. -- evidence: [README.md#L36-L36](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L36-L36), [docs/code.md#L6-L8](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L6-L8)
  - [observation/documented] The /projectcontext command supports subcommands on|off, status, list, view <filepath>, update, refresh <filepath>, add <filepath>, and remove <filepath> for managing project context. -- evidence: [docs/project_context.md#L23-L29](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L23-L29)
- memory-state (3 claim(s)):
  - [observation/documented] The /init command builds persistent project context: a file tree scan, AI-selected key files (up to 20), machine-readable file summaries in .jrdev/context/, plus generated jrdev_conventions.md and jrdev_overview.md in .jrdev. -- evidence: [docs/project_context.md#L13-L17](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L13-L17)
  - [observation/documented] An index.json in .jrdev tracks context files, their last modification times, and summary file paths; /projectcontext update and refresh handle outdated files. -- evidence: [docs/project_context.md#L35-L38](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L35-L38), [docs/project_context.md#L23-L29](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/project_context.md#L23-L29)
- orchestration (3 claim(s)):
  - [observation/documented] The /code agent runs a six-phase pipeline: Analyze, Fetch Context, Plan, Execute, Review, and Validate, ending with files updated on disk. -- evidence: [docs/code.md#L40-L75](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L40-L75)
  - [observation/documented] If the Review phase finds changes insufficient, the pipeline returns to the Analyze phase with the failed review, forming an agentic loop; a passing review proceeds to validation. -- evidence: [docs/code.md#L164-L168](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L164-L168)
- tools-permissions (1 claim(s)):
  - [observation/documented] The tool can modify project files and prompts for confirmation unless in 'Accept All' mode; execute-phase diffs offer Accept, Accept All, Edit, No, or Request Change options. -- evidence: [README.md#L83-L83](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/README.md#L83-L83), [docs/code.md#L138-L150](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/docs/code.md#L138-L150)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt lists openai, anthropic, google-genai, pydantic, httpx, textual[syntax], tiktoken and others, with pyreadline3, windows-curses, and colorama gated to Windows. -- evidence: [requirements.txt#L1-L14](https://github.com/presstab/jrdev/blob/6fa64e9aa8639ce9877280c32cf930e51a4c7dc4/requirements.txt#L1-L14)
- limitations (1 claim(s)):
More evidence: [full detail](jrdev.detail.md)

Metadata and full claim list: [full detail](jrdev.detail.md)
Human notes ([notes](jrdev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
