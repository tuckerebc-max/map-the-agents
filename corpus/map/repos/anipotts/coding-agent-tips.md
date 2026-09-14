# anipotts/coding-agent-tips

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit be596c140caf @ 96b1d751e3ede1b0

## Summary (orientation draft, not independently verified)

The snapshot is a documentation repository: an evidence-backed handbook about working with coding agents, published as a site (Astro/Bun) with contributor instructions in AGENTS.md. Nearly all substantive evidence describes repository development practice rather than a shipped agent runtime.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The handbook's framework separates the steering surface, the harness running the agent loop, the inference model, and orchestration for parallel work, and also covers permissions, review, and operating costs. -- evidence: [README.md#L19-L19](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L19-L19)
  - [observation/documented] The project defines an evidence taxonomy with four labels: tested, official source, analysis, and open question, with citations placed beside the claims they support. -- evidence: [README.md#L30-L30](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L30-L30), [README.md#L23-L28](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L23-L28)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: local verification is done with 'bun install --frozen-lockfile' followed by 'bun run verify', per the README. -- evidence: [README.md#L34-L37](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L34-L37)
  - [observation/documented] Repository development practice: contributors must run source, Astro, generated-route, Markdown, and shell checks before broad changes, plus bun and pytest test suites for archive or shared-runtime changes. -- evidence: [AGENTS.md#L45-L45](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L45-L45)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The handbook is published at agents.anipotts.com, with per-agent guides for codex, claude code, and grok plus handbook sections on setup, history, and method. -- evidence: [README.md#L7-L15](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L7-L15), [README.md#L5-L5](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L5-L5)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [inference/documented] The site appears to be built with Astro and Bun, with Python (pytest) used for some plugin tests, based on the tooling referenced in contributor instructions. -- evidence: [README.md#L34-L37](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L34-L37), [AGENTS.md#L45-L45](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L45-L45), [AGENTS.md#L47-L49](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L47-L49)
- limitations (1 claim(s)):
  - [observation/documented] The repository is MIT licensed and maintained by Ani Potts, who welcomes corrections backed by primary sources or reproducible field evidence. -- evidence: [README.md#L39-L39](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L39-L39), [README.md#L41-L41](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L41-L41)
- relevance (1 claim(s)):
  - [observation/documented] The repository is described as an evidence-backed guide to working with coding agents, aimed at audiences from students to engineers, organized by the scale and consequences of the work. -- evidence: [README.md#L3-L3](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L3-L3)

(4 additional claim(s) omitted for length; see [full detail](coding-agent-tips.detail.md) for every claim.)

Metadata and full claim list: [full detail](coding-agent-tips.detail.md)
Human notes ([notes](coding-agent-tips.notes.md), never overwritten by build)

[Back to map index](../../index.md)
