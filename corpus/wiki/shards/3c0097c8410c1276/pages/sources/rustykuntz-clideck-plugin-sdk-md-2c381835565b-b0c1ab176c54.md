---
access: public
aliases: []
claim_ids:
- clm_5661d5f17fa58f91fc1ad22afa96997623fcc17d670d37744522f4b6fd6bd167
- clm_b41f7b6e4b076487810bfa75625b880c113570ad8c9eaffc1d760c576b5bd236
- clm_e6400827251b143bdcd8a7b94e99971203d7c7e0bb3aba6272671c416147014d
maturity: draft
page_id: pg_e70a42b1afa350f69c26b0c1ab176c54
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e98b3f88acf95c0f8330670e93a222cd
title: rustykuntz/clideck/PLUGIN-SDK.md @ 2c381835565b
updated_at: '2026-09-14T02:37:44Z'
---

# rustykuntz/clideck/PLUGIN-SDK.md @ 2c381835565b

<!-- rcw:begin owner=source:src_e98b3f88acf95c0f8330670e93a222cd block=evidence -->
- Plugin backends run as arbitrary local code with the user's filesystem and network authority; worker isolation protects against accidental crashes but is explicitly not a malicious-code sandbox. [@claim:clm_5661d5f17fa58f91fc1ad22afa96997623fcc17d670d37744522f4b6fd6bd167]
- Plugin client code runs in a dedicated Worker, never in the CliDeck window, and cannot query or mutate host DOM; secret setting values are never sent to the browser, only a configured flag. [@claim:clm_b41f7b6e4b076487810bfa75625b880c113570ad8c9eaffc1d760c576b5bd236]
- Plugins are self-contained folders with a clideck-plugin.json manifest plus optional server.js, client.js, and public/ assets; installation validates and atomically copies the folder into the plugin directory and never runs npm. [@claim:clm_e6400827251b143bdcd8a7b94e99971203d7c7e0bb3aba6272671c416147014d]
<!-- rcw:end owner=source:src_e98b3f88acf95c0f8330670e93a222cd block=evidence -->

## Researcher notes

