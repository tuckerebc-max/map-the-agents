# agentsmd/agents.md

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d001185d792e @ dc191f78ddacbe4c

## Summary (orientation draft, not independently verified)

The repository hosts the AGENTS.md open format for guiding AI coding agents, plus a Next.js website, and its own AGENTS.md/README give contributor instructions for agent-assisted development. Evidence is mostly development practice; the format's purpose is documented but no runtime product behavior is shown.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AGENTS.md is described as a simple, open format for guiding coding agents, acting as a dedicated, predictable place to give AI agents context and instructions about a project. -- evidence: [README.md#L7-L8](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L7-L8), [README.md#L5-L5](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The repository includes a basic Next.js website hosted at agents.md that explains the project's goals and features examples. -- evidence: [README.md#L37-L38](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L37-L38)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (7 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to use the dev server (npm/pnpm/yarn run dev) and never run the production build inside an agent session, since it disables hot reload and can leave the dev server inconsistent. -- evidence: [AGENTS.md#L10-L15](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L10-L15)
  - [observation/documented] Repository development practice: when adding or updating dependencies, update the relevant lockfile and restart the dev server so Next.js picks up the changes. -- evidence: [AGENTS.md#L19-L19](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L19-L19), [AGENTS.md#L21-L22](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L21-L22)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The format is realized as a markdown file (a minimal example is shown in the README), analogous to a README but aimed at agents. -- evidence: [README.md#L10-L10](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L10-L10), [README.md#L7-L8](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L7-L8), [README.md#L12-L12](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L12-L12)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](agents.md.detail.md) for every claim.)

Metadata and full claim list: [full detail](agents.md.detail.md)
Human notes ([notes](agents.md.notes.md), never overwritten by build)

[Back to map index](../../index.md)
