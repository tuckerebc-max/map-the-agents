# matteraiorg/orbital-extension

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ac82a92110ac @ 9ba36631393dad88

## Summary (orientation draft, not independently verified)

README and CHANGELOG describe Orbital, an AI coding agent distributed as a VS Code/Cursor/Windsurf extension and dedicated IDE, with agentic tools, dynamic model catalog, and a changelog detailing tool-execution, search, and file-edit behavior. Development setup (pnpm, contributing guide) appears only as contributor guidance. Evidence coverage: 103 of 384 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The product exposes agentic tools including fileEdit, executeCommand, read_multi_file, writeToFile, searchFiles, web_search, web_fetch, newTask, updateTodoList, and code-structure analysis tools. -- evidence: [README.md#L71-L73](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L71-L73), [README.md#L66-L67](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L66-L67), [README.md#L54-L54](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L54-L54), [README.md#L77-L78](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L77-L78), [README.md#L58-L62](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L58-L62)
  - [observation/documented] A generate_file native tool produces file artifacts (PDF, DOCX, PPTX, XLSX, CSV, MD, TXT, HTML) via the MatterAI backend, holding binaries in memory until the user explicitly saves to the Downloads folder. -- evidence: [CHANGELOG.md#L69-L69](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L69-L69)
- design-choices (3 claim(s)):
  - [observation/documented] Models are fetched from the backend /v1/models endpoint and registered into the client registry, refreshing on window focus, via a refresh button, and through a 10-minute background poller. -- evidence: [CHANGELOG.md#L23-L23](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L23-L23)
  - [observation/documented] File-edit tools require old_string to match exactly one location copied verbatim from a current read, and replace_all must be set intentionally after verifying all occurrences should change. -- evidence: [CHANGELOG.md#L108-L111](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L108-L111)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the axon-code repository and run pnpm install to set up the development environment, and the README points to a CONTRIBUTING.md guide. -- evidence: [README.md#L168-L168](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L168-L168), [README.md#L174-L174](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L174-L174), [README.md#L177-L178](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L177-L178)
- skills-patterns (1 claim(s)):
  - [observation/documented] A /create-skill command lets users describe a workflow in plain language and creates or updates a reusable skill under .orb/skills/<skill-name>/ with supporting scripts and assets. -- evidence: [CHANGELOG.md#L201-L201](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L201-L201)
- interfaces (1 claim(s)):
  - [observation/documented] Orbital ships as a dedicated AI-first IDE plus extensions for VS Code, Cursor, and Windsurf; JetBrains IDEs and a CLI are listed as coming soon. -- evidence: [README.md#L45-L50](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L45-L50)
- memory-state (1 claim(s)):
  - [observation/documented] AGENTS.md project memory is loaded from the repo-level .orb/ directory (alongside project root and legacy .orbital/), shared between the IDE extension and the OrbCode CLI. -- evidence: [CHANGELOG.md#L209-L212](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L209-L212)
- orchestration (1 claim(s)):
  - [observation/documented] Independent read-only tools (read_file, search_files, list_files, list_code_definition_names, codebase_search, lsp) run concurrently up to 4 at a time, with results committed in model order; mutating and interactive tools stay serialized. -- evidence: [CHANGELOG.md#L36-L36](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L36-L36)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](orbital-extension.detail.md)

Metadata and full claim list: [full detail](orbital-extension.detail.md)
Human notes ([notes](orbital-extension.notes.md), never overwritten by build)

[Back to map index](../../index.md)
