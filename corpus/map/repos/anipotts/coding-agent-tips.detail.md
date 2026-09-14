# anipotts/coding-agent-tips -- full detail

[Back to orientation](coding-agent-tips.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/anipotts/coding-agent-tips/be596c140cafa5d19386f2e72ed80c564b4de2d6/96b1d751e3ede1b0.json](../../../wiki/dossiers/anipotts/coding-agent-tips/be596c140cafa5d19386f2e72ed80c564b4de2d6/96b1d751e3ede1b0.json)

## specifications (2 claim(s))

- [observation/documented] The handbook's framework separates the steering surface, the harness running the agent loop, the inference model, and orchestration for parallel work, and also covers permissions, review, and operating costs. -- evidence: [README.md#L19-L19](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L19-L19) (`clm_71b5cdaf35bb985340bb81898ab05c7fe3a6713c48be738f710b04635a0fb986`)
- [observation/documented] The project defines an evidence taxonomy with four labels: tested, official source, analysis, and open question, with citations placed beside the claims they support. -- evidence: [README.md#L30-L30](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L30-L30), [README.md#L23-L28](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L23-L28) (`clm_f0dc479c714c6a9250cf6c33a420aaf59f92e3e1092f2a4a05550a37f368f64e`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: local verification is done with 'bun install --frozen-lockfile' followed by 'bun run verify', per the README. -- evidence: [README.md#L34-L37](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L34-L37) (`clm_35c5a37429ba75e014939e2d8774833d2bf957d24b11b9d2243fcb49520ecce4`)
- [observation/documented] Repository development practice: contributors must run source, Astro, generated-route, Markdown, and shell checks before broad changes, plus bun and pytest test suites for archive or shared-runtime changes. -- evidence: [AGENTS.md#L45-L45](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L45-L45) (`clm_2fd48a09f13c54a01efe7b6c0221677c4e49d3effe9b8f1b34ffac317d8230d0`)
- [observation/documented] Repository development practice: protected pull requests require a GitHub-recognized committer identity, and GitHub's verified=true result is the merge gate rather than local cryptographic verification. -- evidence: [AGENTS.md#L47-L49](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L47-L49) (`clm_f7ae0c6f8e518287eddbea9224f8d97897781c11ae63404babcda9ed2dbbce07`)
- [observation/documented] Repository development practice: editorial rules require separating tested behavior, official facts, analysis, and open questions; recording primary sources in editorial/sources.json; and avoiding vendor benchmarks as quality evidence. -- evidence: [AGENTS.md#L7-L18](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L7-L18) (`clm_8ad9f6101ce8c62f04a0d34550c7e3fe20e919d25022d540426b4a7cfbb21b18`)
- [observation/documented] Repository development practice: canonical file ownership is defined (design.md, content/handbook, content/guides, editorial/sources.json, src/site.ts), and 'bun run sync:readme' must be run after changing guide titles or evidence labels. -- evidence: [AGENTS.md#L22-L32](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L22-L32) (`clm_b6a2307a76874030517435707d97166a8a73e42f47b77e440bdbb891d19741a8`)
- [observation/documented] Repository development practice: review criteria include factual support, taxonomy, safety, maintenance cost, and whether recommendations follow from evidence, not engagement-optimized prose. -- evidence: [AGENTS.md#L53-L53](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L53-L53) (`clm_6c6d165343c02b6d58a30aa2198b05c216ef5fcd20bab60abcb19cfb7030547d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The handbook is published at agents.anipotts.com, with per-agent guides for codex, claude code, and grok plus handbook sections on setup, history, and method. -- evidence: [README.md#L7-L15](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L7-L15), [README.md#L5-L5](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L5-L5) (`clm_1deec3aa27843eb6e0cad028ec23cff2e106c6834c313f738a38b6688b1270a3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The site appears to be built with Astro and Bun, with Python (pytest) used for some plugin tests, based on the tooling referenced in contributor instructions. -- evidence: [README.md#L34-L37](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L34-L37), [AGENTS.md#L45-L45](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L45-L45), [AGENTS.md#L47-L49](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/AGENTS.md#L47-L49) (`clm_11d82a0e4cd34b67a5f46c5c267fb49e869984c6ba619abec0468b9a13ad02f2`)

## limitations (1 claim(s))

- [observation/documented] The repository is MIT licensed and maintained by Ani Potts, who welcomes corrections backed by primary sources or reproducible field evidence. -- evidence: [README.md#L39-L39](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L39-L39), [README.md#L41-L41](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L41-L41) (`clm_e57b8196b3d8d7b84aa696bd6a773914251de23e4631ad2624abd7ce4dc8e7a7`)

## relevance (1 claim(s))

- [observation/documented] The repository is described as an evidence-backed guide to working with coding agents, aimed at audiences from students to engineers, organized by the scale and consequences of the work. -- evidence: [README.md#L3-L3](https://github.com/anipotts/coding-agent-tips/blob/be596c140cafa5d19386f2e72ed80c564b4de2d6/README.md#L3-L3) (`clm_547ae3be3c6dfb301cea796b379d2d65b7f9c82089cb20945f9c419ad56e5f49`)

