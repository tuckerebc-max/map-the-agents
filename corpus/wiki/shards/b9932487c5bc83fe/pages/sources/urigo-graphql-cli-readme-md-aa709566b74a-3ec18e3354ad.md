---
access: public
aliases: []
claim_ids:
- clm_072e51fbae25e526773295d0a2ff9b7074f1170dbbc16e4b5e953a7fe92f7a4b
- clm_28e8e225fdd459e68eb3490e69de9e28102b9bcb45ea232186142099fec1bc18
- clm_44353a70114b0bb994101b14d91c3b34c5f316e383e786a86cde357ee6d7fb70
- clm_5f15ce7e7b9ef3f951eeecaa96d46cdd6337ac19bba5df7aa3044993f49a4b65
- clm_621c23f0fed67734c41c074db6bcb4c673b05de82d83594ffb333eeb39c5ec51
- clm_85d2e6c5e459a9c4debfe69bc38d8c3634831d5484052752daa242f1f613ee2b
- clm_979f780a01d6ddc74c5dbb28b6bef53bc0897f685bdd1211cd6bc80c1e430529
maturity: draft
page_id: pg_3544946196db568c982b3ec18e3354ad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_78a5f297319957d4a23a3a6411b76b72
title: Urigo/graphql-cli/README.md @ aa709566b74a
updated_at: '2026-09-14T04:29:12Z'
---

# Urigo/graphql-cli/README.md @ aa709566b74a

<!-- rcw:begin owner=source:src_78a5f297319957d4a23a3a6411b76b72 block=evidence -->
- Plugins are configured through the `extensions` field of the project's GraphQL Config file (`.graphqlrc.yml`), as shown for codegen and diff (`baseSchema`) settings. [@claim:clm_072e51fbae25e526773295d0a2ff9b7074f1170dbbc16e4b5e953a7fe92f7a4b]
- Documented commands include init, codegen (GraphQL Code Generator), generate (Graphback), coverage and diff (GraphQL Inspector), similar and validate (GraphQL Inspector), and serve, which serves a GraphQL server with an in-memory database. [@claim:clm_28e8e225fdd459e68eb3490e69de9e28102b9bcb45ea232186142099fec1bc18]
- Repository development practice: contributors are directed to read the CONTRIBUTING.md guidelines, and the README invites feedback and plugin contributions via the project's Discord channel. [@claim:clm_44353a70114b0bb994101b14d91c3b34c5f316e383e786a86cde357ee6d7fb70]
- The `diff` command compares the configured schema against another schema given on the command line as a URL, Git reference, or local file pointer, e.g. `graphql diff git:origin/master:schema.graphql`. [@claim:clm_5f15ce7e7b9ef3f951eeecaa96d46cdd6337ac19bba5df7aa3044993f49a4b65]
- The CLI is built around GraphQL Config: the config file tells the tools where GraphQL documents and operations live, and the `schema` field accepts URL endpoints, Git URLs, or local file globs and is used by all commands and plugins. [@claim:clm_621c23f0fed67734c41c074db6bcb4c673b05de82d83594ffb333eeb39c5ec51]
- The CLI exposes an `init` command that asks prompt questions and generates a project with a GraphQL Config setup, and can also generate a project from an existing `.graphqlrc.yml` file's instructions. [@claim:clm_85d2e6c5e459a9c4debfe69bc38d8c3634831d5484052752daa242f1f613ee2b]
- Each GraphQL CLI command is a separate npm package installed under the `@graphql-cli/[COMMAND-NAME]` naming scheme, so users can add their own plugins or maintained ones. [@claim:clm_979f780a01d6ddc74c5dbb28b6bef53bc0897f685bdd1211cd6bc80c1e430529]
<!-- rcw:end owner=source:src_78a5f297319957d4a23a3a6411b76b72 block=evidence -->

## Researcher notes

