---
access: public
aliases: []
claim_ids:
- clm_38f589340cab9f702f267afa51b4abc3e707adcfb205437a7506c0a4ff3efb48
- clm_b8b92e706647bc2da089c036db9800cd51594a2cea2e1193fd673d4bb526f71b
- clm_c14e7f109651ea3e49cff611ddc04cb7cde8f774ee49df32be11ebec6d009c7c
maturity: draft
page_id: pg_a89bb244a81756d2a0fe3938311c3a96
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4ba6cf74f1dd501f98e64915aec34081
title: 233i/ore-code/docs/API_AND_COMPATIBILITY.md @ b36da0c05720
updated_at: '2026-09-14T01:58:37Z'
---

# 233i/ore-code/docs/API_AND_COMPATIBILITY.md @ b36da0c05720

<!-- rcw:begin owner=source:src_4ba6cf74f1dd501f98e64915aec34081 block=evidence -->
- Runtime events are designed to be append-only from a reader's perspective, with new event types added in the protocol package first and older sessions expected to load when optional fields are missing. [@claim:clm_38f589340cab9f702f267afa51b4abc3e707adcfb205437a7506c0a4ff3efb48]
- The workspace includes packages for protocol event schemas, tool specs with approval policy, agent engine with model adapters, JSONL session/artifact state storage, and a scenario-replay harness. [@claim:clm_b8b92e706647bc2da089c036db9800cd51594a2cea2e1193fd673d4bb526f71b]
- Repository development practice: contributors use Node 22 (pinned in .node-version), pnpm 11.x, Rust stable, and Tauri 2 prerequisites; local checks run via pnpm ci:local plus per-package test/typecheck/lint filters. [@claim:clm_c14e7f109651ea3e49cff611ddc04cb7cde8f774ee49df32be11ebec6d009c7c]
<!-- rcw:end owner=source:src_4ba6cf74f1dd501f98e64915aec34081 block=evidence -->

## Researcher notes

