# we0-dev/we0

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3258d6d8348e @ 9ab7fe1cb37b46b8

## Summary (orientation draft, not independently verified)

Evidence consists solely of the English and Chinese README files for we0-dev/we0, describing We0.ai as an AI website builder with multi-agent site generation, legacy coding-workspace features, and local development instructions. No source code is present in the snapshot, so all claims are documentation-based.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] We0.ai is described as an AI website builder that turns natural-language requirements into websites that can be designed, edited, deployed, SEO-optimized, and continuously operated. -- evidence: [README.md#L5-L5](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L5-L5), [docs/README.zh.md#L5-L5](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The legacy we0 project is described as an open-source AI coding workspace with browser-based WebContainer debugging, design-to-code conversion, existing-project editing, and desktop clients for Windows and macOS. -- evidence: [README.md#L122-L127](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L122-L127), [README.md#L113-L114](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L113-L114), [docs/README.zh.md#L125-L130](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L125-L130), [docs/README.zh.md#L116-L117](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L116-L117)
- design-choices (1 claim(s)):
  - [observation/documented] The product is positioned as delivering full websites rather than static pages, including frontend, backend, CMS, SEO, domain, and deployment workflows. -- evidence: [README.md#L20-L24](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L20-L24), [docs/README.zh.md#L20-L24](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L20-L24)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves installing pnpm globally, running pnpm install in each workspace, copying .env.example to .env, and starting with pnpm dev:next and pnpm dev:client from the repo root. -- evidence: [docs/README.zh.md#L149-L151](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L149-L151), [README.md#L190-L193](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L190-L193), [README.md#L147-L149](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L147-L149), [docs/README.zh.md#L165-L165](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L165-L165), [README.md#L163-L163](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L163-L163), [docs/README.zh.md#L192-L195](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L192-L195)
  - [observation/documented] Repository development practice: the web editor is built via scripts/wedev-build.sh, and troubleshooting notes suggest deleting the client workspace if Electron errors on second run or running pnpm run electron:dev if preview is missing. -- evidence: [docs/README.zh.md#L199-L202](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L199-L202), [docs/README.zh.md#L213-L214](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L213-L214), [README.md#L197-L200](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L197-L200), [README.md#L211-L212](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L211-L212)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Legacy we0 offered two interaction modes: Builder mode for code generation, editing, and preview, and Chat mode for general LLM conversation. -- evidence: [README.md#L122-L127](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L122-L127), [docs/README.zh.md#L125-L130](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L125-L130)
  - [observation/documented] The README's feature comparison claims We0.ai supports DeepSeek and MCP, WeChat Mini Program developer tool preview, and existing-project import, which it marks as absent in v0 and bolt.new. -- evidence: [README.md#L84-L98](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L84-L98), [docs/README.zh.md#L87-L101](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L87-L101)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The README says We0.ai coordinates multiple AI agents across the delivery workflow, covering requirement understanding, page planning, visual design, code generation, CMS management, SEO configuration, domain binding, deployment, and content iteration. -- evidence: [docs/README.zh.md#L7-L7](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/docs/README.zh.md#L7-L7), [README.md#L7-L7](https://github.com/we0-dev/we0/blob/3258d6d8348e56e8580bcbec8e42a3894d6113d6/README.md#L7-L7)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](we0.detail.md)

Metadata and full claim list: [full detail](we0.detail.md)
Human notes ([notes](we0.notes.md), never overwritten by build)

[Back to map index](../../index.md)
