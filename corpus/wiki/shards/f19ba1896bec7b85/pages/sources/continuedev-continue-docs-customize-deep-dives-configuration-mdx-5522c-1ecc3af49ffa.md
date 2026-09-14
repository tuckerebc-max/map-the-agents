---
access: public
aliases: []
claim_ids:
- clm_08a1e1cdf234c9db83ebef6554a72b39e3866ed045c17e295af6ac029efa0cd8
- clm_83ca78537b40bc9481f2493212ed4bcb03bf2661f7c885378b838a101c15d7a0
- clm_a3e393526097aad75f6d81295342d9aeb3a4c008e5a02cbfedd29f17293332ab
maturity: draft
page_id: pg_f2f8a17569fa5fd9a9611ecc3af49ffa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ff692ef8ec3951d2b40c65f104848892
title: continuedev/continue/docs/customize/deep-dives/configuration.mdx @ 5522c6f44ca0
updated_at: '2026-09-14T01:44:07Z'
---

# continuedev/continue/docs/customize/deep-dives/configuration.mdx @ 5522c6f44ca0

<!-- rcw:begin owner=source:src_ff692ef8ec3951d2b40c65f104848892 block=evidence -->
- In the IDE extensions, configuration is reached from the Continue Chat sidebar (cmd/ctrl+L in VS Code, cmd/ctrl+J in JetBrains) via the Agent selector's gear icon. [@claim:clm_08a1e1cdf234c9db83ebef6554a72b39e3866ed045c17e295af6ac029efa0cd8]
- User-level configuration lives in `~/.continue/config.yaml` (or `%USERPROFILE%\.continue\config.yaml` on Windows), and saving it in the IDE triggers an automatic config refresh. [@claim:clm_83ca78537b40bc9481f2493212ed4bcb03bf2661f7c885378b838a101c15d7a0]
- Legacy configuration methods are deprecated: `config.json`, workspace-level `.continuerc.json` (with a `mergeBehavior` of merge or overwrite), and programmatic `config.ts` exporting `modifyConfig`. [@claim:clm_a3e393526097aad75f6d81295342d9aeb3a4c008e5a02cbfedd29f17293332ab]
<!-- rcw:end owner=source:src_ff692ef8ec3951d2b40c65f104848892 block=evidence -->

## Researcher notes

