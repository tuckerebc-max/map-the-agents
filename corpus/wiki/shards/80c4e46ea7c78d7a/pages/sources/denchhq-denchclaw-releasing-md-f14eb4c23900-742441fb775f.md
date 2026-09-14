---
access: public
aliases: []
claim_ids:
- clm_896710952dbd1f408ea93c33d3dbeed041c1edc1d3fb2ab2b4048a7c1a8486c6
maturity: draft
page_id: pg_4b40db6b21af51768bfa742441fb775f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_af66fbb4b9c55d1e9f16f9dd1edea689
title: DenchHQ/DenchClaw/RELEASING.md @ f14eb4c23900
updated_at: '2026-09-14T03:45:14Z'
---

# DenchHQ/DenchClaw/RELEASING.md @ f14eb4c23900

<!-- rcw:begin owner=source:src_af66fbb4b9c55d1e9f16f9dd1edea689 block=evidence -->
- Repository development practice: releases are driven by package.json; pushing a version bump to main triggers .github/workflows/release.yml, which runs deploy.sh checks in validation mode before publishing to npm and creating a GitHub release, with reruns safe via existence checks. [@claim:clm_896710952dbd1f408ea93c33d3dbeed041c1edc1d3fb2ab2b4048a7c1a8486c6]
<!-- rcw:end owner=source:src_af66fbb4b9c55d1e9f16f9dd1edea689 block=evidence -->

## Researcher notes

