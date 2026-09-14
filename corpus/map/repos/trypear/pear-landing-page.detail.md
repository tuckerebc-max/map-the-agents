# trypear/pear-landing-page -- full detail

[Back to orientation](pear-landing-page.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/trypear/pear-landing-page/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/407d8d5d50c3ee39.json](../../../wiki/dossiers/trypear/pear-landing-page/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/407d8d5d50c3ee39.json)

## specifications (2 claim(s))

- [observation/documented] The repository is the landing page website for PearAI, described as an open-source AI-powered code editor, published at trypear.ai. -- evidence: [README.md#L37-L37](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L37-L37), [README.md#L3-L18](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L3-L18) (`clm_82708ac8f181bd633a7e3e49a883aa29db55740f31b1b2ca712fa2b18b4750b1`)
- [observation/documented] The code is licensed under Apache License 2.0, with copyright 2024 attributed to PEAR CREATIONS. -- evidence: [LICENSE.txt#L2-L4](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/LICENSE.txt#L2-L4), [LICENSE.txt#L190-L190](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/LICENSE.txt#L190-L190), [LICENSE.txt#L192-L194](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/LICENSE.txt#L192-L194) (`clm_472e88df8faa8132e39d5798ed4705328832b21a2ed6574323c9ae0b5f2860e6`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] A planning document proposes adding i18n support for Japanese rather than separate translated pages, citing maintainability, easier addition of languages, DRY code, and better SEO handling. -- evidence: [japanese-implementation-plan.md#L9-L13](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L9-L13), [japanese-implementation-plan.md#L5-L5](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L5-L5) (`clm_c22f100d2faeefe964969e583c0f6698e3d71604739e0c1ce184eea177b1cbc8`)
- [observation/documented] The i18n plan calls for Next.js i18n configuration in next.config.js, a translation file structure with type safety, a language selector with persisted preference, and testing with native Japanese speakers. -- evidence: [japanese-implementation-plan.md#L25-L27](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L25-L27), [japanese-implementation-plan.md#L65-L67](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L65-L67), [japanese-implementation-plan.md#L71-L74](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L71-L74), [japanese-implementation-plan.md#L19-L21](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L19-L21) (`clm_47b955bb6f1cb418a4a0b7f8caa962be7527041f0f6be95d8c3eac0ef04bbc92`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: local setup requires Yarn, cloning the repo, and running 'yarn install' to install NPM packages. -- evidence: [README.md#L63-L71](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L63-L71), [README.md#L56-L59](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L56-L59) (`clm_c2e050d6a9ae8e6c981ae2ce372afe30b6891017d66693fb66b70e70e70e7408`)
- [observation/documented] Repository development practice: the project is run locally with 'yarn dev' and viewed at http://localhost:3000. -- evidence: [README.md#L100-L104](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L100-L104), [README.md#L98-L98](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L98-L98) (`clm_580300d4da0d6e66e977f328c4a70f6663d33fb6b505befcd78093d05030c4f3`)
- [observation/documented] Repository development practice: configuration requires environment variables in a .env.local file, including NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY for the Supabase backend. -- evidence: [README.md#L88-L88](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L88-L88), [README.md#L75-L75](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L75-L75), [README.md#L79-L80](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L79-L80) (`clm_a6b8c23d8af6152b189159f7eccb747aa283f95f2d1488ed022b2cfd4729502f`)
- [observation/documented] Repository development practice: a pre-commit hook automatically runs Prettier, ESLint, and a project build on each pushed commit; Prettier, ESLint, and JS/TS Nightly extensions are recommended. -- evidence: [README.md#L108-L112](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L108-L112) (`clm_21406c6940b753b151aedd64c26e55ab65a3c4606406158bddd7ea98c9a95ed8`)
- [observation/documented] Repository development practice: contributions follow a fork-clone-branch workflow, creating a new branch and installing dependencies before making changes. -- evidence: [README.md#L122-L138](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L122-L138), [README.md#L120-L120](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L120-L120) (`clm_4e241d6a5b663061563f683ae52ee899a2984ccc8400a61fddba7b8894970795`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README lists Next.js, Vercel, Tailwind CSS, and TypeScript as the technologies the project is built with. -- evidence: [README.md#L43-L46](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L43-L46), [README.md#L149-L157](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/README.md#L149-L157) (`clm_e96d5f8503d57af74d56df20cd4a96ceb9f56b6d69e322df38862dd717a7a71f`)

## limitations (1 claim(s))

- [inference/documented] The i18n plan is a proposal awaiting approval; Japanese support appears to be planned rather than already implemented in this snapshot. -- evidence: [japanese-implementation-plan.md#L87-L89](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L87-L89), [japanese-implementation-plan.md#L85-L85](https://github.com/trypear/pear-landing-page/blob/7e52467a58c4b2e7678a8d9aebd1604cfa3494ed/japanese-implementation-plan.md#L85-L85) (`clm_5a1456017a9e4f6fe5d3d683a0e0b8d3cbb074926347cecd5e412aa5bf051ac3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

