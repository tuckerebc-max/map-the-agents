---
access: public
aliases: []
claim_ids:
- clm_517d94e14589086c60f2ce90add1156d1dc387cc9f931e3474190eed7a296b61
- clm_5c485a14b23d2dbf192107ce1eb2a28d83862ccd53d84dab190da0762a5a8abd
- clm_86a718931ea50333c5e020fd9ab2571215d14f38c4aff7760ee476f5155e7292
- clm_87fa7e9c7c1f6b35ff6f5a908ff1fae5cf80902fe8ba7bd5f4d211b6ca3215ee
- clm_d4eff823ec7e80f52ec8973fffbc4edf532ffd723263acc87a4053b18620cc99
maturity: draft
page_id: pg_1d57bf3dc2ae5ed1b2d0b91d021064f5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a9b297bc8d68578598373d237b375077
title: AaronZ345/codebase-argus/README.md @ 71922e7555f3
updated_at: '2026-09-14T02:48:54Z'
---

# AaronZ345/codebase-argus/README.md @ 71922e7555f3

<!-- rcw:begin owner=source:src_a9b297bc8d68578598373d237b375077 block=evidence -->
- A README permission table lists pull requests and issues with read/write access; contents, checks, actions and metadata have read access. [@claim:clm_517d94e14589086c60f2ce90add1156d1dc387cc9f931e3474190eed7a296b61]
- The README describes the tool as a review desk for maintainers that inspects pull requests, failing CI logs, and long-lived fork syncs using one shared set of signals: patches, checks, files, branch state, policy gates, provider consensus, and local git simulations. [@claim:clm_5c485a14b23d2dbf192107ce1eb2a28d83862ccd53d84dab190da0762a5a8abd]
- An at-a-glance table documents five distinct workflows - PR review, CI review, autofix planning, downstream fork sync, and agent handoff - each with its own input shape and output type. [@claim:clm_86a718931ea50333c5e020fd9ab2571215d14f38c4aff7760ee476f5155e7292]
- Documented webhook behavior includes verifying the X-Hub-Signature-256 header before handling a payload, and skipping draft pull requests as well as PRs labeled argus:paused. [@claim:clm_87fa7e9c7c1f6b35ff6f5a908ff1fae5cf80902fe8ba7bd5f4d211b6ca3215ee]
- A write-model table documents narrow write behavior: the hosted demo is read-only, GitHub App reviews post comment-level PR reviews, and the sync command runs dry-run unless --execute, --push, or --create-pr is explicitly passed. [@claim:clm_d4eff823ec7e80f52ec8973fffbc4edf532ffd723263acc87a4053b18620cc99]
<!-- rcw:end owner=source:src_a9b297bc8d68578598373d237b375077 block=evidence -->

## Researcher notes

