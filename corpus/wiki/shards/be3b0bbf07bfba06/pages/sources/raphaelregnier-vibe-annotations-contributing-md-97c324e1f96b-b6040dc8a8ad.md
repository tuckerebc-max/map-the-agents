---
access: public
aliases: []
claim_ids:
- clm_385e457ccc591b904ed3eaa19947993db1acbba7cf9df4fdda33f80418a6e3eb
- clm_840a5fcb776024078b3264c3f566bbf41d69c1678208e855ff79e913465b6a61
- clm_c363f505e7e7992284634b5f6e74709d475f03491e2778a6da1c27cb648a9d2f
maturity: draft
page_id: pg_bb761ea153e85744b91db6040dc8a8ad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_53b81b2303105dd6abb41c42cf2e6caf
title: RaphaelRegnier/vibe-annotations/CONTRIBUTING.md @ 97c324e1f96b
updated_at: '2026-09-14T04:17:17Z'
---

# RaphaelRegnier/vibe-annotations/CONTRIBUTING.md @ 97c324e1f96b

<!-- rcw:begin owner=source:src_53b81b2303105dd6abb41c42cf2e6caf block=evidence -->
- Repository development practice: pull requests should branch from main, include tests where code should be tested, keep the test suite passing, and follow existing code style; commit messages use present tense, imperative mood, and a first line of 72 characters or less. [@claim:clm_385e457ccc591b904ed3eaa19947993db1acbba7cf9df4fdda33f80418a6e3eb]
- Repository development practice: contributors work in a pnpm workspace with packages for extension, server, and website; the extension is built with WXT (pnpm dev gives live reload, load unpacked from .output/chrome-mv3), and the server runs via node lib/server.js or bin/cli.js start against 127.0.0.1:3846. [@claim:clm_840a5fcb776024078b3264c3f566bbf41d69c1678208e855ff79e913465b6a61]
- Repository development practice: the npm server package is published automatically by a GitHub Action when changes to packages/server/** land on main, with version bumps in packages/server/package.json for intentional releases; the Chrome extension is published to the Web Store by maintainers only. [@claim:clm_c363f505e7e7992284634b5f6e74709d475f03491e2778a6da1c27cb648a9d2f]
<!-- rcw:end owner=source:src_53b81b2303105dd6abb41c42cf2e6caf block=evidence -->

## Researcher notes

