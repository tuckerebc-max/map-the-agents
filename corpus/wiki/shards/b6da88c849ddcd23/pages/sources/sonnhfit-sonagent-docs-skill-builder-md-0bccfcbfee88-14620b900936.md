---
access: public
aliases: []
claim_ids:
- clm_0c811e8e3a9f7bb9e12337e7a7d8170fb74eec7cd22e16a42d79fa12c08403f0
- clm_9a74e32cec2c7a921ab996214ee4cc864f02058e25aa98992986e45d293bc5a5
- clm_c2f1da6be12dde276bab612886b68b82abbec9d8aa97527801943a4dc4b49a53
maturity: draft
page_id: pg_5975c073281a50e8a63414620b900936
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_41babfa38e0f542d897e7e3a06b28238
title: sonnhfit/SonAgent/docs/SKILL_BUILDER.md @ 0bccfcbfee88
updated_at: '2026-09-14T02:42:06Z'
---

# sonnhfit/SonAgent/docs/SKILL_BUILDER.md @ 0bccfcbfee88

<!-- rcw:begin owner=source:src_41babfa38e0f542d897e7e3a06b28238 block=evidence -->
- The SkillBuilder documentation acknowledges current limitations: generation is template-based, complex logic needs manual coding, LLM-based implementation generation is not yet present, and some Python features are restricted in the sandbox. [@claim:clm_0c811e8e3a9f7bb9e12337e7a7d8170fb74eec7cd22e16a42d79fa12c08403f0]
- SkillBuilder consists of a SandboxExecutor that runs code with restricted imports/builtins and no file or network access, a SkillGenerator using templates, and a user-facing SkillBuilder skill with create_simple_skill, generate_skill, and test_skill_code methods. [@claim:clm_9a74e32cec2c7a921ab996214ee4cc864f02058e25aa98992986e45d293bc5a5]
- The sandbox execution environment enforces whitelisted imports, a limited builtin set, no file-system modification, and restricted network access for unsaved skills, with syntax validation before execution. [@claim:clm_c2f1da6be12dde276bab612886b68b82abbec9d8aa97527801943a4dc4b49a53]
<!-- rcw:end owner=source:src_41babfa38e0f542d897e7e3a06b28238 block=evidence -->

## Researcher notes

