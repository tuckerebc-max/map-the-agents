# urigo/graphql-cli -- full detail

[Back to orientation](graphql-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/urigo/graphql-cli/aa709566b74a3ee177c54f7dca909c1c4f75a598/a1fae112f055a480.json](../../../wiki/dossiers/urigo/graphql-cli/aa709566b74a3ee177c54f7dca909c1c4f75a598/a1fae112f055a480.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Documented commands include init, codegen (GraphQL Code Generator), generate (Graphback), coverage and diff (GraphQL Inspector), similar and validate (GraphQL Inspector), and serve, which serves a GraphQL server with an in-memory database. -- evidence: [README.md#L91-L96](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L91-L96), [README.md#L105-L107](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L105-L107) (`clm_28e8e225fdd459e68eb3490e69de9e28102b9bcb45ea232186142099fec1bc18`)

## design-choices (3 claim(s))

- [observation/documented] Each GraphQL CLI command is a separate npm package installed under the `@graphql-cli/[COMMAND-NAME]` naming scheme, so users can add their own plugins or maintained ones. -- evidence: [README.md#L56-L56](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L56-L56) (`clm_979f780a01d6ddc74c5dbb28b6bef53bc0897f685bdd1211cd6bc80c1e430529`)
- [observation/documented] Plugins are configured through the `extensions` field of the project's GraphQL Config file (`.graphqlrc.yml`), as shown for codegen and diff (`baseSchema`) settings. -- evidence: [README.md#L100-L103](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L100-L103), [README.md#L58-L58](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L58-L58), [README.md#L60-L85](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L60-L85) (`clm_072e51fbae25e526773295d0a2ff9b7074f1170dbbc16e4b5e953a7fe92f7a4b`)
- [observation/documented] The CLI is built around GraphQL Config: the config file tells the tools where GraphQL documents and operations live, and the `schema` field accepts URL endpoints, Git URLs, or local file globs and is used by all commands and plugins. -- evidence: [docs/MIGRATION.md#L31-L31](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/docs/MIGRATION.md#L31-L31), [README.md#L33-L33](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L33-L33), [docs/MIGRATION.md#L27-L29](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/docs/MIGRATION.md#L27-L29) (`clm_621c23f0fed67734c41c074db6bcb4c673b05de82d83594ffb333eeb39c5ec51`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to read the CONTRIBUTING.md guidelines, and the README invites feedback and plugin contributions via the project's Discord channel. -- evidence: [README.md#L8-L9](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L8-L9), [README.md#L121-L121](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L121-L121), [README.md#L113-L113](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L113-L113) (`clm_44353a70114b0bb994101b14d91c3b34c5f316e383e786a86cde357ee6d7fb70`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The CLI exposes an `init` command that asks prompt questions and generates a project with a GraphQL Config setup, and can also generate a project from an existing `.graphqlrc.yml` file's instructions. -- evidence: [README.md#L35-L35](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L35-L35), [README.md#L50-L50](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L50-L50), [README.md#L37-L39](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L37-L39), [README.md#L41-L41](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L41-L41) (`clm_85d2e6c5e459a9c4debfe69bc38d8c3634831d5484052752daa242f1f613ee2b`)
- [observation/documented] The `codegen` command runs GraphQL Code Generator with no positional arguments, supporting options `--config`/`-c`, `--watch`/`-w`, `--require`/`-r`, `--overwrite`/`-o`, `--silent`/`-s`, and `--project`/`-p`. -- evidence: [website/docs/codegen.md#L63-L63](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/codegen.md#L63-L63), [website/docs/codegen.md#L67-L74](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/codegen.md#L67-L74), [website/docs/codegen.md#L57-L59](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/codegen.md#L57-L59) (`clm_e290a127ca32f945e7675e72cb8b4ecf24629815ed547f5e623775d81e1398fa`)
- [observation/documented] The `coverage` command takes DOCUMENTS and SCHEMA arguments defaulting to the GraphQL Config file's `documents` and `schema` properties, with options including `--write`, `--deprecated`, `--token`, and `--header`. -- evidence: [website/docs/coverage.md#L40-L42](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/coverage.md#L40-L42), [website/docs/coverage.md#L53-L60](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/coverage.md#L53-L60), [website/docs/coverage.md#L46-L49](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/coverage.md#L46-L49) (`clm_204e17db33abf1a41bc6f41792fa78d972d4a19ab3754738d97efe0ae8f3a037`)
- [observation/documented] The `diff` command compares the configured schema against another schema given on the command line as a URL, Git reference, or local file pointer, e.g. `graphql diff git:origin/master:schema.graphql`. -- evidence: [README.md#L91-L96](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L91-L96), [docs/MIGRATION.md#L88-L91](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/docs/MIGRATION.md#L88-L91), [docs/MIGRATION.md#L82-L86](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/docs/MIGRATION.md#L82-L86) (`clm_5f15ce7e7b9ef3f951eeecaa96d46cdd6337ac19bba5df7aa3044993f49a4b65`)
- [observation/documented] Plugin authors use the `defineCommand` utility from `@graphql-cli/common`, returning an object with `command` and `handler` (and optionally a Yargs `builder` for options); errors thrown in a handler report failure back to the CLI host. -- evidence: [website/docs/custom-commands.md#L110-L110](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L110-L110), [website/docs/custom-commands.md#L39-L48](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L39-L48), [website/docs/custom-commands.md#L27-L27](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L27-L27), [website/docs/custom-commands.md#L77-L98](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L77-L98), [website/docs/custom-commands.md#L115-L125](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L115-L125) (`clm_32f10a0f778c4da145c4ba86b8cab51e3ca03ec2f760442feda6804396366ab5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The CLI's command management is implemented with Yargs, and plugins/extensions are NodeJS modules written in JavaScript or TypeScript, loaded by name from `node_modules`. -- evidence: [website/docs/custom-commands.md#L11-L11](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L11-L11), [website/docs/custom-commands.md#L13-L13](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L13-L13) (`clm_cdae27720466d25922ac09f521107c3a966a1a2363c3147211d1a7549e7548fa`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

