# get-convex/chef -- full detail

[Back to orientation](chef.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/get-convex/chef/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/3abf79f07186783f.json](../../../wiki/dossiers/get-convex/chef/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/3abf79f07186783f.json)

## specifications (1 claim(s))

- [observation/documented] Chef is described as an AI app builder that creates full-stack web apps with a built-in database, zero-config auth, file uploads, real-time UIs, and background workflows. -- evidence: [README.md#L8-L9](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L8-L9) (`clm_0670296ae09a0c895e1b825d8681cc2d2f1d1b6e96a0370f2255ba6a82db4fb7`)

## components (2 claim(s))

- [observation/documented] The chef-agent directory handles the agentic loop by injecting system prompts, defining tools, and calling model providers. -- evidence: [README.md#L112-L112](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L112-L112) (`clm_90ef85dd5ae41a7e79fcaec7358ecf21ffb0a14c4e86dba84e9645fc2e491d5d`)
- [observation/documented] The repository includes a template directory used as the starting point for all Chef projects, and a convex directory storing chats and user metadata. -- evidence: [README.md#L116-L116](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L116-L116), [README.md#L118-L118](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L118-L118) (`clm_0df19dfd222069de6306dff2c54b94d7a675bd28cb82315aa46523c64c61e6ba`)

## design-choices (2 claim(s))

- [observation/documented] Chef's capabilities come from being built on Convex, whose APIs the README describes as an ideal fit for code generation. -- evidence: [README.md#L11-L11](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L11-L11) (`clm_d316a8049b80ea00fca82483af7aaf9d81614463c6a19d0dcfe77e4545892437`)
- [observation/documented] The project is a fork of the stable branch of bolt.diy. -- evidence: [README.md#L17-L17](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L17-L17) (`clm_1b45ab38e4fca47cba084a492a14345bdc6735dfca5e6111b9209516a60460ba`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: local setup uses nvm, pnpm, a VITE_CONVEX_URL placeholder, and 'npx convex dev --once' to provision a Convex project, then 'pnpm run dev' plus 'npx convex dev'. -- evidence: [README.md#L50-L57](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L50-L57), [README.md#L97-L98](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L97-L98), [README.md#L93-L94](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L93-L94) (`clm_404d2b59580c2a2890972343f16a66b3648f4810b8eb8721d1c8b730f94c7a6b`)
- [observation/documented] Repository development practice: PRs target main; a commit queue blocks on tests, formatting, lints, and typechecking via pnpm scripts, and the repo has very few tests and no e2e tests. -- evidence: [DEVELOPMENT.md#L7-L9](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L7-L9), [DEVELOPMENT.md#L64-L64](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L64-L64), [DEVELOPMENT.md#L54-L56](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L54-L56) (`clm_517774d1a3f69bda0cb73709cda6d527e69ce9cd80229dec3204f77936572398`)
- [observation/documented] Repository development practice: releases push main to staging, then merge staging into release after agent evals run (~10 min) with a 100% isSuccess rate expected. -- evidence: [DEVELOPMENT.md#L68-L68](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L68-L68), [DEVELOPMENT.md#L84-L88](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L84-L88), [DEVELOPMENT.md#L76-L79](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L76-L79) (`clm_faed0a1823692c0b7e3e15ffe0eac06e75ae640ba2e2c733bed35dea274f712c`)
- [observation/documented] Repository development practice: contributors should format JavaScript with eslint and markdown with prettier, and large or fundamental changes are generally unlikely to be accepted as community contributions. -- evidence: [CONTRIBUTING.md#L7-L9](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/CONTRIBUTING.md#L7-L9), [CONTRIBUTING.md#L18-L24](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/CONTRIBUTING.md#L18-L24) (`clm_2ae77ed19a087d15b0f27ba79b2128f263e5bd4714a46ef1f767126626fdf65a`)
- [observation/documented] Repository development practice: DEVELOPMENT.md is aimed at Convex employees and is not a supported workflow for external users. -- evidence: [DEVELOPMENT.md#L3-L3](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L3-L3) (`clm_6fb78f14f6e4d6374f81ccfe2a8d85f01ce26dd486904ae7ee12b95533315487`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Chef is offered as a hosted webapp at chef.convex.dev with a free tier, and can also be run locally following README instructions. -- evidence: [README.md#L23-L24](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L23-L24) (`clm_afd88c5743746e471c7c033fe1cc90bd8d6a72e8335cf1ea96a63c0c5709ca20`)
- [observation/documented] A chefshot directory defines a CLI interface for interacting with the Chef webapp. -- evidence: [README.md#L114-L114](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L114-L114) (`clm_6e1f21bd72601b31658df6431dc11ead267b76a0b7d4c7c27a455aee47ff2ff3`)

## memory-state (1 claim(s))

- [inference/documented] Chef appears to use a WebContainer-style environment: a documented debug global exposes 'chefWebContainer' as the unix-ish container where tooling and generated code run. -- evidence: [DEVELOPMENT.md#L130-L135](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/DEVELOPMENT.md#L130-L135) (`clm_49f6c636c0003b5ddb6337a5f288229250be2ac13c919890a7d2954e712bb804`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Chef ships with an authentication configuration tied to Convex's internal control plane for user accounts; forks for production must replace it with their own auth. -- evidence: [README.md#L29-L29](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L29-L29), [README.md#L26-L27](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L26-L27) (`clm_c497889471984295119a9ff21cd91ab811eb9e4e79efa60673fca5f7dcf48c86`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Local code generation is enabled by supplying API keys for providers including Anthropic, Google, OpenAI, and xAI, either via env file or the Chef settings page. -- evidence: [README.md#L87-L87](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L87-L87), [README.md#L80-L85](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L80-L85), [README.md#L78-L78](https://github.com/get-convex/chef/blob/d8a6cb6a6f226133fdc63ed5f59d04cacb9b06cc/README.md#L78-L78) (`clm_7f2c53642a70c9c21ed2a2562831f851b3a40b5b3e916304a0ed9369c66a54b4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

