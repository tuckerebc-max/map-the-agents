---
access: public
aliases: []
claim_ids:
- clm_0c1e8b1727b2369bea28ee665b8c5c46397b0549360167ac6975f26838ac72ec
- clm_0fb483d109a6d3668ab4c3cac45e750fcf87df99406d9ba22054c4d49b978b08
- clm_174fa0a8e1a842a417ca147f719565003602fa21b7d77d74e2b35bd3e7d71fed
- clm_1adbb1af3c774d72309311ac5268568cafc9d046fe9fdb7e857bbd21449a9931
- clm_28aed2305aabe5fcec9a78e2b2b544b3af0fb80f64ffc429cc521a71d0daba97
- clm_2fd128af5415c7e715618e7b7afab17d2ecd27b47f6488b5bb5401fe5772f135
- clm_3111abc15676e846333aa1b8e37670ef148377248af2bcd5c6c523da314c7b89
- clm_493c0713e4078726bbed7dbd1f75914fdc4dcbc37bfd43ad037bb50a68a56226
- clm_61492b0dd6dd118f9f2b57464ef53adbfaf1b2aab1b5d998e08ce2e8120fe346
- clm_8d1eb2dc0ec8d91044c7c85a3755392bcb507b0c13abfa565b2bccd776bafbdf
- clm_a47ca7bdb9492ee21a6444950553ca90cb6f3c3d7f92e515d34973013e6a9890
- clm_b2792dc9c28d2b7d2ef9b9c1cb89c889f0dc72432f316fe49a612c0e23693b60
maturity: draft
page_id: pg_888178062900589abd20f597134e0368
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bec2cf81ca2256b7aa32676cfb1b111b
title: steveclarke/real-world-rails/README.md @ 45eb4c732feb
updated_at: '2026-09-14T04:23:18Z'
---

# steveclarke/real-world-rails/README.md @ 45eb4c732feb

<!-- rcw:begin owner=source:src_bec2cf81ca2256b7aa32676cfb1b111b block=evidence -->
- Repository development practice: contributions are accepted either by opening an issue with a GitHub URL or by submitting a PR after running bin/add; candidate apps must be open source, Rails-based, actively maintained or high quality, and real-world rather than demos. [@claim:clm_0c1e8b1727b2369bea28ee665b8c5c46397b0549360167ac6975f26838ac72ec]
- Setup requires git-lfs to be installed, and getting started consists of cloning the repo and running bin/setup. [@claim:clm_0fb483d109a6d3668ab4c3cac45e750fcf87df99406d9ba22054c4d49b978b08]
- Provided scripts include bin/setup (with --full and --reset flags), bin/update, bin/status, bin/add for adding apps by GitHub URL, and bin/verify which requires the gh CLI. [@claim:clm_174fa0a8e1a842a417ca147f719565003602fa21b7d77d74e2b35bd3e7d71fed]
- The README points to related collections including Real World Nuxt, Real World Ruby Apps, Real World Sinatra, and Real World Django. [@claim:clm_1adbb1af3c774d72309311ac5268568cafc9d046fe9fdb7e857bbd21449a9931]
- The repo ships a /real-world-rails skill for AI coding agents, installable via npx skills add steveclarke/real-world-rails, that teaches agents to search across all included codebases. [@claim:clm_28aed2305aabe5fcec9a78e2b2b544b3af0fb80f64ffc429cc521a71d0daba97]
- Running bin/setup clones all 200+ repositories as git submodules, using roughly 10 GB of disk; bin/setup --full fetches complete git history at about 29 GB. [@claim:clm_2fd128af5415c7e715618e7b7afab17d2ecd27b47f6488b5bb5401fe5772f135]
- The project aggregates over 200 active, open source Rails apps and engines in one repository for developers to learn from. [@claim:clm_3111abc15676e846333aa1b8e37670ef148377248af2bcd5c6c523da314c7b89]
- The full list of included apps and engines with descriptions lives in repos.md, which lists entries such as Discourse, Mastodon, GitLab CE, and Canvas LMS with links and short descriptions. [@claim:clm_493c0713e4078726bbed7dbd1f75914fdc4dcbc37bfd43ad037bb50a68a56226]
- The analyses/ directory is git-ignored so users can store their own research notes without them being committed or appearing in pull requests. [@claim:clm_61492b0dd6dd118f9f2b57464ef53adbfaf1b2aab1b5d998e08ce2e8120fe346]
- The project's stated motivation is that aggregating production codebases in one directory makes cross-app pattern research dramatically more useful for AI coding agents than manual grep or custom scripts. [@claim:clm_8d1eb2dc0ec8d91044c7c85a3755392bcb507b0c13abfa565b2bccd776bafbdf]
- Submodules are updated automatically by a weekly GitHub Action that opens a PR; after merging, users pull and run git submodule update, or run bin/update for immediate updates. [@claim:clm_a47ca7bdb9492ee21a6444950553ca90cb6f3c3d7f92e515d34973013e6a9890]
- It is described as an actively maintained continuation of eliotsykes/real-world-rails. [@claim:clm_b2792dc9c28d2b7d2ef9b9c1cb89c889f0dc72432f316fe49a612c0e23693b60]
<!-- rcw:end owner=source:src_bec2cf81ca2256b7aa32676cfb1b111b block=evidence -->

## Researcher notes

