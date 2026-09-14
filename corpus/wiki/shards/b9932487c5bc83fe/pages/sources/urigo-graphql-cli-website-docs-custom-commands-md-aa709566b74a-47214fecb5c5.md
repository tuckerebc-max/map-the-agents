---
access: public
aliases: []
claim_ids:
- clm_32f10a0f778c4da145c4ba86b8cab51e3ca03ec2f760442feda6804396366ab5
- clm_cdae27720466d25922ac09f521107c3a966a1a2363c3147211d1a7549e7548fa
maturity: draft
page_id: pg_b188494fda245b27a67d47214fecb5c5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8b068587ef5b52348e6bfab27deb01b4
title: Urigo/graphql-cli/website/docs/custom-commands.md @ aa709566b74a
updated_at: '2026-09-14T04:29:12Z'
---

# Urigo/graphql-cli/website/docs/custom-commands.md @ aa709566b74a

<!-- rcw:begin owner=source:src_8b068587ef5b52348e6bfab27deb01b4 block=evidence -->
- Plugin authors use the `defineCommand` utility from `@graphql-cli/common`, returning an object with `command` and `handler` (and optionally a Yargs `builder` for options); errors thrown in a handler report failure back to the CLI host. [@claim:clm_32f10a0f778c4da145c4ba86b8cab51e3ca03ec2f760442feda6804396366ab5]
- The CLI's command management is implemented with Yargs, and plugins/extensions are NodeJS modules written in JavaScript or TypeScript, loaded by name from `node_modules`. [@claim:clm_cdae27720466d25922ac09f521107c3a966a1a2363c3147211d1a7549e7548fa]
<!-- rcw:end owner=source:src_8b068587ef5b52348e6bfab27deb01b4 block=evidence -->

## Researcher notes

