---
access: public
aliases: []
claim_ids:
- clm_5f15ce7e7b9ef3f951eeecaa96d46cdd6337ac19bba5df7aa3044993f49a4b65
- clm_621c23f0fed67734c41c074db6bcb4c673b05de82d83594ffb333eeb39c5ec51
maturity: draft
page_id: pg_c15c44de6a2d5edb963b764bae04c3fe
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bf8290ae18535524bfde9ce592462495
title: Urigo/graphql-cli/docs/MIGRATION.md @ aa709566b74a
updated_at: '2026-09-14T04:29:12Z'
---

# Urigo/graphql-cli/docs/MIGRATION.md @ aa709566b74a

<!-- rcw:begin owner=source:src_bf8290ae18535524bfde9ce592462495 block=evidence -->
- The `diff` command compares the configured schema against another schema given on the command line as a URL, Git reference, or local file pointer, e.g. `graphql diff git:origin/master:schema.graphql`. [@claim:clm_5f15ce7e7b9ef3f951eeecaa96d46cdd6337ac19bba5df7aa3044993f49a4b65]
- The CLI is built around GraphQL Config: the config file tells the tools where GraphQL documents and operations live, and the `schema` field accepts URL endpoints, Git URLs, or local file globs and is used by all commands and plugins. [@claim:clm_621c23f0fed67734c41c074db6bcb4c673b05de82d83594ffb333eeb39c5ec51]
<!-- rcw:end owner=source:src_bf8290ae18535524bfde9ce592462495 block=evidence -->

## Researcher notes

