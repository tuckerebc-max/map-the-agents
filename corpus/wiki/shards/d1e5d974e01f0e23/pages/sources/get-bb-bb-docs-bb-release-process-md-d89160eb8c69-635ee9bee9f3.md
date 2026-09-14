---
access: public
aliases: []
claim_ids:
- clm_0ce995e32acc8707441989253083228a0e6804525be143f00ccfd61e41940faa
- clm_103d011baae5db64a94b7b50507d05f4a067940e79a9bf4f4d3406c85e4a6f4a
- clm_2feef4ac65a69fb17b4b15e74bfd8f66a92a9cd63ba15a62920c425e80f29cb5
- clm_4bb392bbb4b23f7bc77e611db1f4644ccebdedefaf8a626b4681d5e7963e0e33
- clm_dcd90f7b77db69dc9b504d015a134812a81bc52a360533c5a829f4b480771666
maturity: draft
page_id: pg_fdfefc70352e5db6a5f2635ee9bee9f3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1b162a17d5b954598ea054463464911e
title: get-bb/bb/docs/bb-release-process.md @ d89160eb8c69
updated_at: '2026-09-14T01:51:21Z'
---

# get-bb/bb/docs/bb-release-process.md @ d89160eb8c69

<!-- rcw:begin owner=source:src_1b162a17d5b954598ea054463464911e block=evidence -->
- Repository development practice: release validation includes a version-lockstep check, turbo typecheck/test for several packages, a bb-app tarball smoke task, and git diff --check before committing. [@claim:clm_0ce995e32acc8707441989253083228a0e6804525be143f00ccfd61e41940faa]
- Repository development practice: releases ship two outputs from one commit — the bb-app npm package via publish-bb-app.yml and the desktop app via build-desktop.yml — and a release is not complete until both are published at the same locked version. [@claim:clm_103d011baae5db64a94b7b50507d05f4a067940e79a9bf4f4d3406c85e4a6f4a]
- Repository development practice: the @get-bb/plugin-sdk publishes via an idempotent publish-if-missing job, with a CI guard that fails when a published version's packed tarball differs from the local build. [@claim:clm_2feef4ac65a69fb17b4b15e74bfd8f66a92a9cd63ba15a62920c425e80f29cb5]
- Repository development practice: a scheduled nightly channel publishes a next-patch prerelease under the npm nightly dist-tag and builds a separately installable bb Nightly desktop app without moving stable latest pointers. [@claim:clm_4bb392bbb4b23f7bc77e611db1f4644ccebdedefaf8a626b4681d5e7963e0e33]
- The project is relevant to agent-runtime work: an agentic IDE with plugin/marketplace concepts, a Codex provider plugin adapter, and a published plugin SDK. [@claim:clm_dcd90f7b77db69dc9b504d015a134812a81bc52a360533c5a829f4b480771666]
<!-- rcw:end owner=source:src_1b162a17d5b954598ea054463464911e block=evidence -->

## Researcher notes

