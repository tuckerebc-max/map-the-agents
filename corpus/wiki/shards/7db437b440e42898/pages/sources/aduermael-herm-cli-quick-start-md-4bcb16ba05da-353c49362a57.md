---
access: public
aliases: []
claim_ids:
- clm_2fb5ad3688435dde152798d2ce208987413799752bd45cc5d99b5f00e0f7128d
- clm_980fd1e6782178c00af303b83b33d0c86f9200650be8081bf8168062765eecd0
- clm_f9b26289654df7b531464da0042f0bdc5515e4be9583255bc60dea59a9746a5f
maturity: draft
page_id: pg_877ea19f2da45e69aced353c49362a57
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6e2703f6896d543b8899a9e5944e28f0
title: aduermael/herm/CLI_QUICK_START.md @ 4bcb16ba05da
updated_at: '2026-09-14T01:29:52Z'
---

# aduermael/herm/CLI_QUICK_START.md @ 4bcb16ba05da

<!-- rcw:begin owner=source:src_6e2703f6896d543b8899a9e5944e28f0 block=evidence -->
- Documented CLI flags include --version, --debug, --prompt for headless mode, --cpsl to run with a CPSL local sandbox library, and --naked to run without Docker or CPSL. [@claim:clm_2fb5ad3688435dde152798d2ce208987413799752bd45cc5d99b5f00e0f7128d]
- Building from source requires Go 1.24+ and, for the default container backend, Docker; the repo uses git submodules (langdag for LLM client/orchestration and cpsl for the native sandbox backend) that must be initialized before building. [@claim:clm_980fd1e6782178c00af303b83b33d0c86f9200650be8081bf8168062765eecd0]
- In --naked host mode, commands run through a workspace-scoped sandbox requiring sandbox-exec (macOS) or bwrap (Linux); new command segments and outside-workspace paths prompt for approval, and approved permissions persist in .herm/permissions.json with user-editable command_regexes and path_regexes. [@claim:clm_f9b26289654df7b531464da0042f0bdc5515e4be9583255bc60dea59a9746a5f]
<!-- rcw:end owner=source:src_6e2703f6896d543b8899a9e5944e28f0 block=evidence -->

## Researcher notes

