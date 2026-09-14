# urigo/graphql-cli

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit aa709566b74a @ a1fae112f055a480

## Summary (orientation draft, not independently verified)

Selected evidence records: The CLI exposes an `init` command that asks prompt questions and generates a project with a GraphQL Config setup, and can also generate a project from an existing `.graphqlrc.yml` file's instructions. The `codegen` command runs GraphQL Code Generator with no positional arguments, supporting options `--config`/`-c`, `--watch`/`-w`, `--require`/`-r`, `--overwrite`/`-o`, `--silent`/`-s`, and `--project`/`-p`.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Documented commands include init, codegen (GraphQL Code Generator), generate (Graphback), coverage and diff (GraphQL Inspector), similar and validate (GraphQL Inspector), and serve, which serves a GraphQL server with an in-memory database. -- evidence: [README.md#L91-L96](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L91-L96), [README.md#L105-L107](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L105-L107)
- design-choices (3 claim(s)):
  - [observation/documented] Each GraphQL CLI command is a separate npm package installed under the `@graphql-cli/[COMMAND-NAME]` naming scheme, so users can add their own plugins or maintained ones. -- evidence: [README.md#L56-L56](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L56-L56)
  - [observation/documented] Plugins are configured through the `extensions` field of the project's GraphQL Config file (`.graphqlrc.yml`), as shown for codegen and diff (`baseSchema`) settings. -- evidence: [README.md#L100-L103](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L100-L103), [README.md#L58-L58](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L58-L58), [README.md#L60-L85](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L60-L85)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to read the CONTRIBUTING.md guidelines, and the README invites feedback and plugin contributions via the project's Discord channel. -- evidence: [README.md#L8-L9](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L8-L9), [README.md#L121-L121](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L121-L121), [README.md#L113-L113](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L113-L113)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI exposes an `init` command that asks prompt questions and generates a project with a GraphQL Config setup, and can also generate a project from an existing `.graphqlrc.yml` file's instructions. -- evidence: [README.md#L35-L35](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L35-L35), [README.md#L50-L50](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L50-L50), [README.md#L37-L39](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L37-L39), [README.md#L41-L41](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/README.md#L41-L41)
  - [observation/documented] The `codegen` command runs GraphQL Code Generator with no positional arguments, supporting options `--config`/`-c`, `--watch`/`-w`, `--require`/`-r`, `--overwrite`/`-o`, `--silent`/`-s`, and `--project`/`-p`. -- evidence: [website/docs/codegen.md#L63-L63](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/codegen.md#L63-L63), [website/docs/codegen.md#L67-L74](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/codegen.md#L67-L74), [website/docs/codegen.md#L57-L59](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/codegen.md#L57-L59)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The CLI's command management is implemented with Yargs, and plugins/extensions are NodeJS modules written in JavaScript or TypeScript, loaded by name from `node_modules`. -- evidence: [website/docs/custom-commands.md#L11-L11](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L11-L11), [website/docs/custom-commands.md#L13-L13](https://github.com/Urigo/graphql-cli/blob/aa709566b74a3ee177c54f7dca909c1c4f75a598/website/docs/custom-commands.md#L13-L13)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](graphql-cli.detail.md) for every claim.)

Metadata and full claim list: [full detail](graphql-cli.detail.md)
Human notes ([notes](graphql-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
