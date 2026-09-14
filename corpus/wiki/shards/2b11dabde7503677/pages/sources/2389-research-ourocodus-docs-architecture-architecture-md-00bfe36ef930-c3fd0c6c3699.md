---
access: public
aliases: []
claim_ids:
- clm_0480c25b52d33b5fbdda40c1ef3b3a383e561a89b9eefffbf46288b2e3978741
- clm_750f941f7ad8c7803cba3d1d6a3997e3781df6d1a7567df52c47f03c262d9f08
- clm_796bcf743257a469b337f9591a1331a8b564054489e3dd088da95d749bebdeab
maturity: draft
page_id: pg_7eec3232543e5e658143c3fd0c6c3699
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b3744b94d16c521ca1982b5bef9d4bd2
title: 2389-research/ourocodus/docs/architecture/ARCHITECTURE.md @ 00bfe36ef930
updated_at: '2026-09-14T01:28:48Z'
---

# 2389-research/ourocodus/docs/architecture/ARCHITECTURE.md @ 00bfe36ef930

<!-- rcw:begin owner=source:src_b3744b94d16c521ca1982b5bef9d4bd2 block=evidence -->
- Each AgentSession has three isolation layers (git worktree, read-only credentials, Docker container) orchestrated by an AgentContainerLauncher. [@claim:clm_0480c25b52d33b5fbdda40c1ef3b3a383e561a89b9eefffbf46288b2e3978741]
- The relay spawns multiple concurrent agents with user-chosen identifiers; agents can be spawned or terminated independently, and one agent's failure does not terminate the session. [@claim:clm_750f941f7ad8c7803cba3d1d6a3997e3781df6d1a7567df52c47f03c262d9f08]
- The project is at Phase 1 (foundation/proof of concept) focused on validating multi-agent communication and concurrent isolated work; the PWA client is planned while demos exist currently. [@claim:clm_796bcf743257a469b337f9591a1331a8b564054489e3dd088da95d749bebdeab]
<!-- rcw:end owner=source:src_b3744b94d16c521ca1982b5bef9d4bd2 block=evidence -->

## Researcher notes

