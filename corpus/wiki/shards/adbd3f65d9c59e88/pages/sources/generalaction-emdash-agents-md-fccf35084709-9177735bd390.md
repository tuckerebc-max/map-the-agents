---
access: public
aliases: []
claim_ids:
- clm_02abb82eb315375260f135cd7ac118e1a718adb2f167faae6a06a6494712bebb
- clm_19fa31ca829cb9298196219c6f446d30c9136399ad70d71914fb43d3d128b84b
maturity: draft
page_id: pg_8d99b6d589125cf6a2f39177735bd390
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_543dca668cd857a484c06368309ca913
title: generalaction/emdash/AGENTS.md @ fccf35084709
updated_at: '2026-09-14T01:50:03Z'
---

# generalaction/emdash/AGENTS.md @ fccf35084709

<!-- rcw:begin owner=source:src_543dca668cd857a484c06368309ca913 block=evidence -->
- Repository development practice: the repo is a pnpm workspace monorepo; only pnpm on PATH is needed since package.json pins pnpm 10.28.2 and Node 24.14.0 with onFail download, so the toolchain self-provisions. [@claim:clm_02abb82eb315375260f135cd7ac118e1a718adb2f167faae6a06a6494712bebb]
- Repository development practice: the merge gate is four root commands (format, lint, typecheck, test) run via pnpm/Nx, with CI running a code-consistency workflow using nx affected on touched projects and dependents, and browser Vitest projects skipped in CI. [@claim:clm_19fa31ca829cb9298196219c6f446d30c9136399ad70d71914fb43d3d128b84b]
<!-- rcw:end owner=source:src_543dca668cd857a484c06368309ca913 block=evidence -->

## Researcher notes

