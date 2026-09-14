# trypear/pear-landing-page

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7e52467a58c4 @ 407d8d5d50c3ee39

## Summary (orientation draft, not independently verified)

Selected evidence records: The repository is the landing page website for PearAI, described as an open-source AI-powered code editor, published at trypear.ai. The README lists Next.js, Vercel, Tailwind CSS, and TypeScript as the technologies the project is built with.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The repository is the landing page website for PearAI, described as an open-source AI-powered code editor, published at trypear.ai. -- evidence: [README.md#L37-L37](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L37-L37), [README.md#L3-L18](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L3-L18)
  - [observation/documented] The code is licensed under Apache License 2.0, with copyright 2024 attributed to PEAR CREATIONS. -- evidence: [LICENSE.txt#L2-L4](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/LICENSE.txt#L2-L4), [LICENSE.txt#L190-L190](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/LICENSE.txt#L190-L190), [LICENSE.txt#L192-L194](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/LICENSE.txt#L192-L194)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] A planning document proposes adding i18n support for Japanese rather than separate translated pages, citing maintainability, easier addition of languages, DRY code, and better SEO handling. -- evidence: [japanese-implementation-plan.md#L9-L13](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L9-L13), [japanese-implementation-plan.md#L5-L5](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L5-L5)
  - [observation/documented] The i18n plan calls for Next.js i18n configuration in next.config.js, a translation file structure with type safety, a language selector with persisted preference, and testing with native Japanese speakers. -- evidence: [japanese-implementation-plan.md#L25-L27](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L25-L27), [japanese-implementation-plan.md#L65-L67](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L65-L67), [japanese-implementation-plan.md#L71-L74](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L71-L74), [japanese-implementation-plan.md#L19-L21](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L19-L21)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: local setup requires Yarn, cloning the repo, and running 'yarn install' to install NPM packages. -- evidence: [README.md#L63-L71](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L63-L71), [README.md#L56-L59](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L56-L59)
  - [observation/documented] Repository development practice: the project is run locally with 'yarn dev' and viewed at http://localhost:3000. -- evidence: [README.md#L100-L104](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L100-L104), [README.md#L98-L98](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L98-L98)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README lists Next.js, Vercel, Tailwind CSS, and TypeScript as the technologies the project is built with. -- evidence: [README.md#L43-L46](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L43-L46), [README.md#L149-L157](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L149-L157)
- limitations (1 claim(s)):
  - [inference/documented] The i18n plan is a proposal awaiting approval; Japanese support appears to be planned rather than already implemented in this snapshot. -- evidence: [japanese-implementation-plan.md#L87-L89](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L87-L89), [japanese-implementation-plan.md#L85-L85](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L85-L85)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](pear-landing-page.detail.md) for every claim.)

Metadata and full claim list: [full detail](pear-landing-page.detail.md)
Human notes ([notes](pear-landing-page.notes.md), never overwritten by build)

[Back to map index](../../index.md)
