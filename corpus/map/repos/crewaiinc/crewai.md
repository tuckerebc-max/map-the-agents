# crewaiinc/crewai

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: joaomdmoura/crewai (github id 710601088).
Latest snapshot: commit 894898f84c4a @ 0d6e6df1020dcd85

## Summary (orientation draft, not independently verified)

The evidence consists solely of README slices for crewAIInc/crewAI, documenting an open-source Python multi-agent orchestration framework built around Crews (autonomous role-based collaboration) and Flows (event-driven workflows), a JSON-first CLI project scaffold, LLM connectivity, telemetry, and contributor workflows. Evidence coverage: 149 of 179 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 3 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] CrewAI is described as an open-source Python framework for building production-ready multi-agent workflows, offering high-level abstractions and low-level APIs. -- evidence: [README.md#L58-L59](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L58-L59)
  - [observation/documented] CrewAI requires Python >=3.10 and <3.14 and uses UV for dependency management and package handling. -- evidence: [README.md#L196-L196](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L196-L196), [README.md#L202-L202](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L202-L202)
- components (1 claim(s)):
  - [observation/documented] New crew projects are JSON-first: agents live in `agents/*.jsonc`, tasks and crew settings in `crew.jsonc`, with optional `knowledge/`, `skills/`, and `tools/` directories; a `--classic` flag yields the older Python/YAML scaffold. -- evidence: [README.md#L261-L261](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L261-L261), [README.md#L283-L283](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L283-L283), [README.md#L269-L281](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L269-L281), [README.md#L285-L287](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L285-L287)
- design-choices (1 claim(s)):
  - [observation/documented] The framework offers two complementary models: Crews for autonomous, role-based agent collaboration, and Flows for event-driven workflows with precise control and state management. -- evidence: [README.md#L681-L681](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L681-L681), [README.md#L176-L176](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L176-L176), [README.md#L169-L169](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L169-L169), [README.md#L61-L62](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L61-L62)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run `uv sync --all-groups --all-extras`, install pre-commit hooks, run tests with `uv run pytest lib/crewai/tests/ -x -q`, and type-check with `uv run mypy lib/`. -- evidence: [README.md#L562-L567](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L562-L567), [README.md#L574-L575](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L574-L575), [README.md#L571-L571](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L571-L571)
  - [observation/documented] Repository development practice: docs under `docs/edge/` publish immediately under the Edge version selector and are frozen into immutable `docs/v<X.Y.Z>/` snapshots at release; CI rejects PRs modifying frozen snapshots without a `[docs-freeze]` title prefix. -- evidence: [README.md#L579-L588](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L579-L588)
- skills-patterns (1 claim(s)):
  - [observation/documented] Official CrewAI Skills can be installed for AI coding agents (Claude Code plugins or `npx skills add crewaiinc/skills`), covering scaffolding, agent/task design, and a docs MCP query skill. -- evidence: [README.md#L134-L134](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L134-L134), [README.md#L122-L127](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L122-L127), [README.md#L129-L132](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L129-L132), [README.md#L114-L120](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L114-L120)
- interfaces (3 claim(s)):
  - [observation/documented] Flows support logical operators `or_` and `and_` combined with `@start`, `@listen`, and `@router` decorators to build complex triggering conditions and conditional routing. -- evidence: [README.md#L499-L506](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L499-L506), [README.md#L442-L443](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L442-L443), [README.md#L523-L527](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L523-L527), [README.md#L439-L440](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L439-L440)
  - [observation/documented] The CrewAI CLI supports `crewai create crew <name>`, `crewai install`, and `crewai run`, and is installed via `uv tool install crewai`. -- evidence: [README.md#L661-L663](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L661-L663), [README.md#L263-L265](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L263-L265), [README.md#L226-L228](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L226-L228), [README.md#L665-L665](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L665-L665), [README.md#L379-L382](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L379-L382)
- memory-state (1 claim(s)):
More evidence: [full detail](crewai.detail.md)

Metadata and full claim list: [full detail](crewai.detail.md)
Human notes ([notes](crewai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
