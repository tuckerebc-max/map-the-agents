# ralph-workflow/ralph-workflow

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3d9d847f41fe @ b4e9678f061e3d05

## Summary (orientation draft, not independently verified)

Ralph Workflow is a documented open-source AI agent orchestrator that runs a plan-build-verify-fix loop with a selectable coding agent backend, requiring Python 3.12+ and licensed AGPL-3.0-or-later. Repository development practice (AGENTS.md, CLA.md) mandates trunk-based commits, a 60-second test budget under make verify, a fabrication guard, and a CLA for contributions.

## Source coverage

Source coverage (partial): 3 of 40 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Ralph Workflow is described as a free, open-source AI agent orchestrator for coding work that takes one well-specified task and runs a Ralph loop with the user's chosen coding agent. -- evidence: [README.md#L3-L8](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L3-L8)
- components (1 claim(s)):
  - [observation/documented] The product ships nine built-in agent backends: Claude Code, Claude Code headless, Codex, OpenCode, Nanocoder, AGY, Pi, Cursor, and Kimi; the user authenticates one locally and the tool uses it. -- evidence: [README.md#L48-L53](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L48-L53)
- design-choices (1 claim(s)):
  - [observation/documented] The Ralph Loop pattern is attributed to Geoffrey Huntley (ghuntley.com/ralph), with Ralph Workflow positioned as an independent reference implementation of that pattern. -- evidence: [README.md#L71-L73](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L71-L73)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md mandates trunk-based development with all work committed directly to main, forbids branch creation and pull requests, and permits commits only via `ralph --generate-commit`. -- evidence: [AGENTS.md#L202-L213](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L202-L213), [AGENTS.md#L217-L217](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L217-L217)
  - [observation/documented] Repository development practice: contributors must run `make verify` from ralph-workflow/ before completion; it must pass in full with no unrelated-failure exemptions, and a red gate is owned by whoever next observes it. -- evidence: [AGENTS.md#L244-L245](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L244-L245), [AGENTS.md#L44-L45](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L44-L45), [AGENTS.md#L54-L54](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L54-L54), [AGENTS.md#L239-L242](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L239-L242)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A checkout install provides an `rdev` launcher whose `--version` ends in -build, deliberately leaving any globally installed `ralph` command in place; native Windows users are directed to install the published package via pipx or pip. -- evidence: [README.md#L31-L32](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L31-L32), [README.md#L36-L44](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L36-L44)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The core orchestration is a Ralph loop of plan, build, verify, and fix stages run with the selected coding agent, after which the user returns to inspect the result. -- evidence: [README.md#L3-L8](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L3-L8)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The runtime requires Python 3.12 or newer and is described as local-first; the project is licensed AGPL-3.0-or-later and published on PyPI. -- evidence: [README.md#L64-L69](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L64-L69)
- limitations (1 claim(s)):
More evidence: [full detail](ralph-workflow.detail.md)

Metadata and full claim list: [full detail](ralph-workflow.detail.md)
Human notes ([notes](ralph-workflow.notes.md), never overwritten by build)

[Back to map index](../../index.md)
