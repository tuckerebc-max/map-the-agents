# cloudflare/vibesdk -- full detail

[Back to orientation](vibesdk.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cloudflare/vibesdk/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/b32132cd1ca47fd1.json](../../../wiki/dossiers/cloudflare/vibesdk/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/b32132cd1ca47fd1.json)

## specifications (2 claim(s))

- [observation/documented] VibeSDK is described as an open-source agentic platform for building and deploying full-stack applications on Cloudflare, with a hosted demo at build.cloudflare.dev. -- evidence: [README.md#L3-L3](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L3-L3), [README.md#L7-L7](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L7-L7) (`clm_9edb720ea8bae704540ba778d8b2fd0ddab91c4e4586cc2286f41adeaefd22d0`)
- [observation/documented] Users build apps by describing what they want and answering clarifying questions while the agent plans, edits files, deploys previews, inspects errors, and iterates with the human in the loop. -- evidence: [README.md#L15-L15](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L15-L15) (`clm_fcfcfeafca14000d0e05e799db222ca626e0515d30aaf44126ab80a417d2a38e`)

## components (1 claim(s))

- [observation/documented] The architecture comprises a ThinkAgent Durable Object running the model-and-tool loop, a SpaceDO workspace per project, Cloudflare Artifacts for git history and restore points, a Worker Loader for Dynamic Worker previews, and a generated App Durable Object Facet with SQLite. -- evidence: [README.md#L34-L41](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L34-L41) (`clm_94a04e26ea207c07d22ce0d485d65286df9d06156211a8a138edc085dbab4a46`)

## design-choices (1 claim(s))

- [observation/documented] Feature settings are dashboard-managed rather than committed in wrangler.jsonc, with keep_vars: true preserving production values across deploys; listed toggles default to off while ENABLE_EMAIL_AUTH defaults to on. -- evidence: [README.md#L116-L116](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L116-L116) (`clm_8fad8a7021adb74686f4ba2e3e0dab0764eef50385d5bfc6b1d7b357cde8f28e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork and clone, run bun install and bun run setup, follow AGENTS.md, then run bun run typecheck, lint, and test before opening a pull request describing the change and its validation. -- evidence: [README.md#L151-L155](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L151-L155) (`clm_47110c0fca0e665b4a38b848e0dacd231107f36a4f472547a987288f72c2565d`)
- [observation/documented] Repository development practice: local development uses Node.js 18+, Bun, and commands such as bun run dev, build, typecheck, lint, and test, with bun run deploy building, migrating, and deploying via .prod.vars. -- evidence: [README.md#L120-L129](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L120-L129), [README.md#L96-L98](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L96-L98) (`clm_794da97cd7fbe66face7a05a67606d00119d8be1a65facca41a4e8f3fcecc5dd`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Previews are produced by bundling each committed deployment with @cloudflare/worker-bundler and loading it through the Worker Loader binding; SpaceDO serves static assets while backend requests and WebSockets are forwarded to the generated App Facet. -- evidence: [README.md#L60-L60](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L60-L60) (`clm_bc232e434c2866ccfea3b9097c650df0fc29fe0c196dccbd4ec08e7f359aeaa2`)

## memory-state (2 claim(s))

- [observation/documented] Each generated application gets isolated SQLite-backed storage via a Durable Object Facet, with database inspection and reset controls available to users. -- evidence: [README.md#L21-L30](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L21-L30), [README.md#L60-L60](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L60-L60) (`clm_8b456beb70aa3563a60317763a6d14e17a3ce07e6d4f563d9a9cc13c82beb954`)
- [observation/documented] Rollback restores a selected commit into the current branch, creates a new commit, and redeploys without rewriting existing history, using Cloudflare Artifacts as the version-history layer. -- evidence: [README.md#L64-L64](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L64-L64), [docs/architecture-diagrams.md#L20-L20](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/docs/architecture-diagrams.md#L20-L20) (`clm_1c04ce76d55cc863498d3343071da4a6e57dac7c0a4b605ec50ec15e62080911`)

## orchestration (1 claim(s))

- [observation/documented] ThinkAgent runs an iterative model-and-tool loop, managing conversation history, streaming, and skills; its explicit tools edit the workspace, create restore points, deploy previews, inspect browser logs, and ask clarifying questions, while bash access is disabled. -- evidence: [README.md#L56-L56](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L56-L56) (`clm_b266d8afaafce287057a065a89a686166376d70c71c51784947580f8444a912d`)

## tools-permissions (1 claim(s))

- [observation/documented] The product's tool model uses explicit workspace and product tools with workspace bash access disabled, and preview URLs use signed, branch-scoped access for authorization. -- evidence: [README.md#L56-L56](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L56-L56), [README.md#L133-L138](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L133-L138) (`clm_d2d6e9deed8413ceabb48152c0a037f356912150c29cc495c6b1399233050a9c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Model providers are routed through Cloudflare AI Gateway with centralized observability and caching; deploying requires a Cloudflare account, Workers Paid plan, Workers for Platforms access for production previews, and an API token. -- evidence: [README.md#L21-L30](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L21-L30), [README.md#L84-L88](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L84-L88) (`clm_7b0167b183fffdf93959a8459a370a3e31f9f97705574ebc75e70d9888883d32`)

## limitations (1 claim(s))

- [observation/documented] The docs explicitly state the older phase-based sandbox architecture diagrams are retired historical context and must not be used to describe the current Think, SpaceDO, Artifacts, Worker Loader, and App Facet implementation. -- evidence: [docs/architecture-diagrams.md#L24-L24](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/docs/architecture-diagrams.md#L24-L24) (`clm_85ce3c4ba0262f1ad835c9303782c658bead9f3d1baeb8bd76c20211849e6723`)

## relevance (1 claim(s))

- [observation/documented] VibeSDK is MIT-licensed, and support is available through GitHub issues, GitHub discussions, and the Cloudflare Developers Discord. -- evidence: [README.md#L170-L170](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L170-L170), [README.md#L147-L147](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L147-L147) (`clm_270924ac5fadd22b3221e4231b0fc73e5ed35fe99c3bc52caa0b27461314b125`)

