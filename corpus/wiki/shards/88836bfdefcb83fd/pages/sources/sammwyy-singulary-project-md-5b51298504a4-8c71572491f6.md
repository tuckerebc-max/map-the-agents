---
access: public
aliases: []
claim_ids:
- clm_35065921992e004b63afc5b65fdd405026d2a867d0eca8cd5d0ee2338084c472
- clm_5bdfb26ef1e354f8cbbe5e8baa9786fcfc96754272cc7bd00ca44506ff399ed3
- clm_5c1bcd742bb9dad38d3646a731a70163d67878a6e7d4c1fd23eaa9adf832ed1e
- clm_f239b708e01d83ee9c63082dc710844c3f8cf8c799b35469ad4ed159f7cd1b57
maturity: draft
page_id: pg_5effa74a015b5a7697ca8c71572491f6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3a2fe95fd7fc5e1e9be358dbc96bf5d5
title: sammwyy/singulary/PROJECT.md @ 5b51298504a4
updated_at: '2026-09-14T02:38:43Z'
---

# sammwyy/singulary/PROJECT.md @ 5b51298504a4

<!-- rcw:begin owner=source:src_3a2fe95fd7fc5e1e9be358dbc96bf5d5 block=evidence -->
- The spec calls for both single-user mode (first user becomes instance admin owning everything) and multi-user organization mode with teams, roles, groups, permissions, shared keys, quotas, and scoped environments. [@claim:clm_35065921992e004b63afc5b65fdd405026d2a867d0eca8cd5d0ee2338084c472]
- The project specification targets a self-hostable alternative to tools like v0, Lovable, Bolt, Replit Agent, or Cursor-style agents, emphasizing local-first development, BYOK access, Docker-based execution, multi-project workspaces, and auditable AI-driven changes. [@claim:clm_5bdfb26ef1e354f8cbbe5e8baa9786fcfc96754272cc7bd00ca44506ff399ed3]
- The specification envisions a permissioned tool system (filesystem, shell, docker, env, database, network tools) with risk levels and approval requirements, and states the agent should never have raw unrestricted access; this is a design goal, not verified runtime behavior. [@claim:clm_5c1bcd742bb9dad38d3646a731a70163d67878a6e7d4c1fd23eaa9adf832ed1e]
- The spec describes a snapshot-based filesystem where every AI change should be reversible, using content-addressed blobs, tree objects, diffs, branching, and restore operations similar to Git internally; this is stated as a design target rather than confirmed implemented behavior. [@claim:clm_f239b708e01d83ee9c63082dc710844c3f8cf8c799b35469ad4ed159f7cd1b57]
<!-- rcw:end owner=source:src_3a2fe95fd7fc5e1e9be358dbc96bf5d5 block=evidence -->

## Researcher notes

