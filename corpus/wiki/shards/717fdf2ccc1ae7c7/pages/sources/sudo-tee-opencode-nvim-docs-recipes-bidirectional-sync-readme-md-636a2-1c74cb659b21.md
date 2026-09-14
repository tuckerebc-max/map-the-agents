---
access: public
aliases: []
claim_ids:
- clm_a82290514b057ff325c8033eb9f424dff77f5beeb654cfe8cc9aabefb63f2d42
maturity: draft
page_id: pg_66080be617255ae987621c74cb659b21
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d6d33359706c5c2ab71ac78ee9ad846e
title: sudo-tee/opencode.nvim/docs/recipes/bidirectional-sync/README.md @ 636a26425227
updated_at: '2026-09-14T04:24:22Z'
---

# sudo-tee/opencode.nvim/docs/recipes/bidirectional-sync/README.md @ 636a26425227

<!-- rcw:begin owner=source:src_d6d33359706c5c2ab71ac78ee9ad846e block=evidence -->
- A bidirectional-sync recipe shares one HTTP server (default port 4096) between the opencode TUI and the nvim plugin so session state persists across switches; the TUI attaches via 'opencode attach' and the server stays alive until manually killed. [@claim:clm_a82290514b057ff325c8033eb9f424dff77f5beeb654cfe8cc9aabefb63f2d42]
<!-- rcw:end owner=source:src_d6d33359706c5c2ab71ac78ee9ad846e block=evidence -->

## Researcher notes

