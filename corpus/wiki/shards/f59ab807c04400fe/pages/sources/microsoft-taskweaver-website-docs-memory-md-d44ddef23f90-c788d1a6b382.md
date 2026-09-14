---
access: public
aliases: []
claim_ids:
- clm_40d8986fa5da28efbff70827ee87237f9817d18e424d619b5df06072ce1f0d6f
- clm_57168a4273beb7921e705cb4291ec282b5d9e6f2c90ad6b8aed04951555fa87f
- clm_6060f9975e9a49c013a25c77253d1df82e520bbffe6a51cee50227af4cb264b1
- clm_65617be7cc443092f16b715769d1c8ba4c472c67e2cc8a14e50d89c7ac331e0d
- clm_d85f192d45fff6877b53c81a35024e91c2e8c587342b861ab086c11abcf961ba
maturity: draft
page_id: pg_d60a4aa1db98535e9a37c788d1a6b382
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a2d788c97d10553dac4a814bfe21c334
title: microsoft/TaskWeaver/website/docs/memory.md @ d44ddef23f90
updated_at: '2026-09-14T04:09:13Z'
---

# microsoft/TaskWeaver/website/docs/memory.md @ d44ddef23f90

<!-- rcw:begin owner=source:src_a2d788c97d10553dac4a814bfe21c334 block=evidence -->
- Shared information is stored as attachments inside posts rather than a separate structure so that, if a round fails, its shared entries can be filtered out by round status, analogous to transaction logging. [@claim:clm_40d8986fa5da28efbff70827ee87237f9817d18e424d619b5df06072ce1f0d6f]
- The fixed star-topology orchestration is acknowledged by the docs as a limitation, though it preserves role independence. [@claim:clm_57168a4273beb7921e705cb4291ec282b5d9e6f2c90ad6b8aed04951555fa87f]
- Roles are orchestrated in a star topology with the Planner at the center: the User interacts only with the Planner, which plans and instructs peripheral roles, each of which knows only the Planner. [@claim:clm_6060f9975e9a49c013a25c77253d1df82e520bbffe6a51cee50227af4cb264b1]
- The memory module stores conversation history between the user and roles plus a shared memory of information purposefully shared between roles; implementation is in taskweaver/memory/memory.py. [@claim:clm_65617be7cc443092f16b715769d1c8ba4c472c67e2cc8a14e50d89c7ac331e0d]
- Shared memory entries are attachments on posts with fields type, content, scope ('round' or 'conversation'), and id; round-scoped entries expire with the round, and later entries with the same type from a role overwrite earlier ones. [@claim:clm_d85f192d45fff6877b53c81a35024e91c2e8c587342b861ab086c11abcf961ba]
<!-- rcw:end owner=source:src_a2d788c97d10553dac4a814bfe21c334 block=evidence -->

## Researcher notes

