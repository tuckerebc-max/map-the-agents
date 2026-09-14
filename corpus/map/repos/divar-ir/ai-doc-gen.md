# divar-ir/ai-doc-gen

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bd3aba71a0c5 @ 8234197f8a7e2c0e

## Summary (orientation draft, not independently verified)

An AI documentation generator CLI that runs five concurrent analysis agents over a repository and generates README plus AI-assistant config files, with GitLab cronjob automation and a Claude Code plugin packaging. Evidence is README product documentation plus contributor instructions in AGENTS.md.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool analyzes repositories with five specialized analysis agents (code structure, dependencies, data flow, request flow, APIs) and generates a README plus AI assistant configuration files such as CLAUDE.md, AGENTS.md, and Cursor rules. -- evidence: [README.md#L3-L3](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L3-L3), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32)
- components (1 claim(s)):
  - [observation/documented] The architecture is layered: an argparse CLI entry point, command-specific handlers implementing an AbstractHandler interface, pydantic-ai agents with YAML/Jinja2 prompts, and a tool layer with file-reading and file-listing tools registered with every agent. -- evidence: [README.md#L184-L190](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L184-L190)
- design-choices (1 claim(s)):
  - [observation/documented] Configuration is layered with precedence from Pydantic defaults, then a .ai/config.yaml (or .yml) file in the target repository, then CLI flags. -- evidence: [README.md#L168-L168](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L168-L168)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must run ruff format and ruff check on src/ before submitting, follow a branch and commit-message convention (e.g. [Feature], [Fix]), and squash-merge feature branches into main. -- evidence: [AGENTS.md#L62-L64](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/AGENTS.md#L62-L64), [AGENTS.md#L24-L26](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/AGENTS.md#L24-L26)
  - [observation/documented] Repository development practice: the project has no automated tests; changes are verified manually by running the analyze, generate readme, and generate ai-rules commands against a test repository. -- evidence: [AGENTS.md#L52-L58](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/AGENTS.md#L52-L58)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repository ships as an installable Claude Code plugin providing three skills: analyze-codebase, generate-readme, and generate-ai-rules, installable via the plugin marketplace commands. -- evidence: [README.md#L47-L49](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L47-L49), [README.md#L40-L43](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L40-L43), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI exposes analyze, generate readme, and generate ai-rules commands taking a --repo-path argument, plus a cronjob analyze command; an ai-doc-gen console script exposes the same CLI. -- evidence: [README.md#L114-L114](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L114-L114), [README.md#L117-L118](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L117-L118), [README.md#L111-L111](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L111-L111), [README.md#L120-L120](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L120-L120), [README.md#L108-L108](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L108-L108)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Analyzer agents run in parallel through a configurable worker pool controlled by ANALYZER_MAX_WORKERS, where 0 means auto-detecting the CPU count; a --max-workers flag can cap concurrency. -- evidence: [README.md#L130-L130](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L130-L130), [README.md#L23-L32](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L23-L32)
- tools-permissions (1 claim(s)):
  - [observation/documented] Agents access the codebase through registered tools: FileReadTool for ranged file reading and ListFilesTool for filtered recursive listing, both registered with every agent. -- evidence: [README.md#L184-L190](https://github.com/divar-ir/ai-doc-gen/blob/bd3aba71a0c57aa43aef4020917989efc4507db3/README.md#L184-L190)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](ai-doc-gen.detail.md)

Metadata and full claim list: [full detail](ai-doc-gen.detail.md)
Human notes ([notes](ai-doc-gen.notes.md), never overwritten by build)

[Back to map index](../../index.md)
