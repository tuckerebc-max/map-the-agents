# renaissance-innovation-labs/jacob-ai -- full detail

[Back to orientation](jacob-ai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/renaissance-innovation-labs/jacob-ai/bd0e26461466991aee873f74896f4902387b9f47/b95445b127d3ee29.json](../../../wiki/dossiers/renaissance-innovation-labs/jacob-ai/bd0e26461466991aee873f74896f4902387b9f47/b95445b127d3ee29.json)

## specifications (1 claim(s))

- [observation/documented] JACoB (Just Another Coding Bot) is an open-source AI tool that automates coding tasks, converts Figma designs into deployable code, and integrates into existing developer workflows. -- evidence: [README.md#L27-L27](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L27-L27) (`clm_01e71e4702e758b7dd80fe6444df948dfd3328bdbedb69d063be5ce806e68f0f`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Per-project behavior is configured via a jacob.config file generated with 'npx jacob-setup create', specifying project details and build environment variables. -- evidence: [README.md#L163-L165](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L163-L165) (`clm_599bedf9da939d82beae33cb7158bdb8e6372a56abf5a30df5bda5f52a81afbb`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local setup involves creating .env from .env.example, running docker compose, npm install, npm run db create/migrate, verifying with npm test, and launching with npm run dev. -- evidence: [README.md#L176-L185](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L176-L185), [README.md#L189-L189](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L189-L189), [README.md#L199-L201](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L199-L201), [README.md#L193-L193](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L193-L193), [README.md#L197-L197](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L197-L197) (`clm_3c90c5c84ce8c5f8eef9495f403e41791993ecae8ea3521ce0f9610ae4052814`)
- [observation/documented] Repository development practice: the README describes using GitHub's webhook redeliver feature to replay events against the local instance for debugging and iteration. -- evidence: [README.md#L223-L223](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L223-L223), [README.md#L229-L229](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L229-L229) (`clm_e5c3e82993e4837617736ee602b7eb73de200f7bd51d6931972ca1e57571bd8f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The product is delivered as a custom GitHub app, a Figma plugin, and a command-line tool for setting configuration options. -- evidence: [README.md#L115-L115](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L115-L115) (`clm_2538c1f14f81963df1c6c74aff14b0b6a90b2f10dc8d72062f97a4d27f77b3c1`)

## memory-state (1 claim(s))

- [observation/documented] The local version does not store the codebase; hosted logs with code snippets are retained 14 days, GitHub app tokens expire after 8 hours and are not saved in the database. -- evidence: [README.md#L111-L111](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L111-L111) (`clm_2c27258808a9bf7e8a25448ed04c259033351a8e07f1d5c350ca42ae17e05d91`)

## orchestration (1 claim(s))

- [observation/documented] Local infrastructure runs RabbitMQ and Postgres via Docker Compose, and GitHub webhooks are proxied to the local server through smee.io. -- evidence: [README.md#L189-L189](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L189-L189), [README.md#L159-L159](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L159-L159) (`clm_612d0227e64f675cf51e48639a2ea475fada7ea45e3571d15ed8ab995fac05bb`)

## tools-permissions (1 claim(s))

- [observation/documented] The GitHub app is configured with read/write permissions for issues, pull requests, and contents, and subscribes to issue, comment, and pull-request webhook events. -- evidence: [README.md#L137-L155](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L137-L155) (`clm_d2e035e901de65d314f66e3326889be2e9d24599a5816b1d786de0ade2291daf`)

## evaluation (1 claim(s))

- [observation/documented] The team evaluated JACoB via the JACoB Arena, where developers compared it against top design-to-code tools and human benchmarks, reportedly outperforming seven such tools. -- evidence: [README.md#L72-L72](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L72-L72) (`clm_75b2cac5faae10fe7601fc8c391ac8ea9a2934aee8b4693462ca61ae78e18e7a`)

## dependencies (2 claim(s))

- [observation/documented] The codebase is built with Next.js, NextAuth.js, Tailwind CSS, tRPC, and Orchid ORM. -- evidence: [README.md#L119-L123](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L119-L123) (`clm_2bc710bfd8367bb2936d2771ddc6cdce02d4d7a3cefbb4a8b731d51b42aaec53`)
- [observation/documented] Self-hosting requires GitHub and Figma accounts, Node.js, Docker and Docker Compose, an OpenAI account, and a PortKey account. -- evidence: [README.md#L127-L131](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L127-L131) (`clm_903824559fd500c4aed7b7b4502c7ffbaf489ba004242c7225686ef040c5d4dd`)

## limitations (1 claim(s))

- [observation/documented] Due to context window and model constraints, JACoB targets smaller tasks and currently works best with TypeScript/JavaScript, Next.js, Tailwind, and Figma designs. -- evidence: [README.md#L76-L80](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L76-L80) (`clm_cde2a48ea961707f7a249875a300d97a161baa13e8039a78159ab983653e3966`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

