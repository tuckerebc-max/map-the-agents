---
access: public
aliases: []
claim_ids:
- clm_627a2a8ef85d6de427eeba0cb35bf6e2164fc753a18c3b43b02b00e481c57cc3
maturity: draft
page_id: pg_b8b10213000250c29e6bb0c30ed6d564
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_75b12db71e5a50f982b3a4a5aceb354c
title: mattolson/agent-sandbox/docs/git.md @ 5df0b4bc6c57
updated_at: '2026-09-14T04:08:39Z'
---

# mattolson/agent-sandbox/docs/git.md @ 5df0b4bc6c57

<!-- rcw:begin owner=source:src_75b12db71e5a50f982b3a4a5aceb354c block=evidence -->
- SSH port 22 is blocked to prevent proxy-bypassing tunnels, and the container's system git config rewrites SSH GitHub URLs to HTTPS; the image ships Git 2.50.1 with worktree.useRelativePaths=true. [@claim:clm_627a2a8ef85d6de427eeba0cb35bf6e2164fc753a18c3b43b02b00e481c57cc3]
<!-- rcw:end owner=source:src_75b12db71e5a50f982b3a4a5aceb354c block=evidence -->

## Researcher notes

