---
access: public
aliases: []
claim_ids:
- clm_ab2f6ab52b0f8017b7999413b4b354e9b677cab8c8b6095addd9526241b3e7ca
- clm_ba95cf42718fa9c3fa5c76de85ce4d5951458f61707cfb0b24eeb10e6c452daa
- clm_d5ae1a55633b923136eb1490946c05a8cb0dc2fd4f5069d00a5e0e5e10d8bc90
maturity: draft
page_id: pg_2b76c52baa495625943e22c3957eca8d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_98699008b741510daeb169a6ce6b63e9
title: langchain-ai/deepagents/AGENTS.md @ c08cae693e00
updated_at: '2026-09-14T02:10:56Z'
---

# langchain-ai/deepagents/AGENTS.md @ c08cae693e00

<!-- rcw:begin owner=source:src_98699008b741510daeb169a6ce6b63e9 block=evidence -->
- Repository development practice: contributors follow Conventional Commits with scopes, branch naming of username/scope/description, a PR template with a release-note summary, and unit tests split into tests/unit_tests and tests/integration_tests with warnings treated as errors. [@claim:clm_ab2f6ab52b0f8017b7999413b4b354e9b677cab8c8b6095addd9526241b3e7ca]
- Repository development practice: public API changes must preserve exported signatures, add new parameters as keyword-only with defaults, and mark experimental features with docstring warnings. [@claim:clm_ba95cf42718fa9c3fa5c76de85ce4d5951458f61707cfb0b24eeb10e6c452daa]
- Repository development practice: the monorepo layout includes libs/deepagents, libs/code, libs/acp, libs/talon, libs/evals, and partner packages, with benchmarks run via package bench and bench-memory Make targets rather than pytest directly. [@claim:clm_d5ae1a55633b923136eb1490946c05a8cb0dc2fd4f5069d00a5e0e5e10d8bc90]
<!-- rcw:end owner=source:src_98699008b741510daeb169a6ce6b63e9 block=evidence -->

## Researcher notes

