# dnouri/pilish

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: dnouri/pi-coding-agent (github id 1125438750).
Latest snapshot: commit 894d1e7be124 @ 5f45544ad87d0a76

## Summary (orientation draft, not independently verified)

The snapshot's only evidence is the AGENTS.md contributor guide, which documents Pilish as an Emacs frontend for the pi coding agent, its module architecture, test/benchmark/lint commands, and coding conventions. All claims below are repository development practice drawn from that guide.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 1 facet(s); 12 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (12 claim(s)):
  - [observation/documented] Repository development practice: the guide describes Pilish as an Emacs frontend for the pi coding agent with a two-window UI (markdown chat buffer plus prompt composition buffer) communicating with the pi CLI via JSON-over-stdio RPC. -- evidence: [AGENTS.md#L3-L5](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L3-L5)
  - [observation/documented] Repository development practice: the guide documents ten production source modules forming an acyclic dependency DAG, plus an optional Evil integration module, with the internal require edges listed explicitly. -- evidence: [AGENTS.md#L9-L10](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L9-L10), [AGENTS.md#L12-L22](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L12-L22), [AGENTS.md#L24-L25](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L24-L25)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(10 additional claim(s) omitted for length; see [full detail](pilish.detail.md) for every claim.)

Metadata and full claim list: [full detail](pilish.detail.md)
Human notes ([notes](pilish.notes.md), never overwritten by build)

[Back to map index](../../index.md)
