# 2389-research/dippin-lang

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 1ef50f81ba75 @ 5334cb5b7378dda0

## Summary (orientation draft, not independently verified)

Dippin is a Go-based DSL and CLI toolchain for authoring AI pipeline workflows as a DOT replacement, with validation/lint diagnostics, analysis commands, bundling, LSP support, and DOT migration/export. Evidence is mostly README and docs/analysis.md documentation. Evidence coverage: 154 of 352 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 108 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The architecture centers on an ir.Workflow intermediate representation consumed by parser, validator, formatter, exporter, migrator, simulator, cost/coverage/doctor/optimize, diff, testrunner, and LSP packages. -- evidence: [README.md#L525-L546](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L525-L546), [README.md#L505-L521](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L505-L521), [README.md#L523-L523](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L523-L523)
  - [observation/documented] The validator performs 10 structural checks (DIP001–DIP010) and 46 semantic lint rules (DIP101–DIP162 range), with diagnostics styled after the Rust compiler including codes, locations, and suggested fixes. -- evidence: [README.md#L525-L546](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L525-L546), [README.md#L382-L392](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L382-L392), [README.md#L371-L371](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L371-L371), [README.md#L396-L426](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L396-L426)
- design-choices (2 claim(s)):
  - [observation/documented] Dippin is positioned as an authoring format replacing Graphviz DOT for AI pipelines, keeping DOT as the visualization target via export-dot while giving prompts, shell scripts, model config, and branching first-class syntax. -- evidence: [README.md#L9-L9](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L9-L9), [README.md#L5-L5](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L5-L5), [README.md#L37-L37](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L37-L37)
  - [observation/documented] The language uses explicit node keywords (agent, tool, human, parallel, fan_in, subgraph, manager_loop) instead of DOT shape overloading, and indented multiline blocks preserve content verbatim without escaping. -- evidence: [README.md#L268-L268](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L268-L268), [README.md#L310-L310](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L310-L310), [README.md#L275-L275](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L275-L275), [README.md#L261-L261](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L261-L261), [README.md#L27-L35](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L27-L35)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: a pre-commit hook (installed via 'just setup-hooks') enforces gocyclo ≤5, gocognit ≤7, gofmt formatting, go test with -race, and validation of all example .dip files; 'just check' runs the full suite. -- evidence: [README.md#L566-L566](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L566-L566), [README.md#L568-L574](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L568-L574), [README.md#L556-L562](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L556-L562)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The dippin CLI offers authoring commands (parse, validate, lint, check, fmt, new, export-dot, migrate, validate-migration) plus analysis, bundle, and editor tooling subcommands. -- evidence: [README.md#L144-L156](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L144-L156), [README.md#L160-L165](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L160-L165), [README.md#L169-L174](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L169-L174), [README.md#L130-L140](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L130-L140)
  - [observation/documented] Analysis commands exit 0/1/2 for ok/errors/usage, while bundle commands use a finer ladder including integrity error (2), I/O error (3), and cancelled (4). -- evidence: [README.md#L176-L176](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L176-L176)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The product includes a scenario test runner (dippin test) that executes .test.json suites against the simulator, and simulate supports --scenario and --all-paths to exercise workflow execution paths without real LLM calls. -- evidence: [README.md#L444-L446](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L444-L446), [README.md#L144-L156](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L144-L156), [README.md#L450-L452](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L450-L452), [README.md#L430-L430](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L430-L430)
More evidence: [full detail](dippin-lang.detail.md)

Metadata and full claim list: [full detail](dippin-lang.detail.md)
Human notes ([notes](dippin-lang.notes.md), never overwritten by build)

[Back to map index](../../index.md)
