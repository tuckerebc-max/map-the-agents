---
access: public
aliases: []
claim_ids:
- clm_23fc9875d2e536a0021c76d856a7548e540004ef8e3b90fccbfdcbea24d96743
- clm_3190afb783f44a3eb2985ee3cc353803ef9af2a39b57c3ba098855c90129f2dc
- clm_4cbd1e6ec2e2d69019d4a124f1955aaa9cf52ad885e123bfea8e2fad296f78e0
maturity: draft
page_id: pg_ffbb26206a3a58ffb0f3d071c046017c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c32bc15fefff5c039ea319078f183c7c
title: marcusschiesser/edge-pi/AGENTS.md @ c4b694c4abb1
updated_at: '2026-09-14T02:16:18Z'
---

# marcusschiesser/edge-pi/AGENTS.md @ c4b694c4abb1

<!-- rcw:begin owner=source:src_c32bc15fefff5c039ea319078f183c7c block=evidence -->
- Repository development practice: parallel agents must stage only their own files with explicit paths, never use `git add -A`, and avoid destructive commands like `git reset --hard` or `git stash`. [@claim:clm_23fc9875d2e536a0021c76d856a7548e540004ef8e3b90fccbfdcbea24d96743]
- Repository development practice: AGENTS.md forbids running `npm run dev`, `npm run build`, or `npm test`, requires `npm run check` after code changes, and forbids committing unless the user asks. [@claim:clm_3190afb783f44a3eb2985ee3cc353803ef9af2a39b57c3ba098855c90129f2dc]
- Repository development practice: releases use Changesets with lockstep versioning via fixed groups, using `npm run changeset`, `npm run version`, and `npm run release`. [@claim:clm_4cbd1e6ec2e2d69019d4a124f1955aaa9cf52ad885e123bfea8e2fad296f78e0]
<!-- rcw:end owner=source:src_c32bc15fefff5c039ea319078f183c7c block=evidence -->

## Researcher notes

