---
access: public
aliases: []
claim_ids:
- clm_3d0712c05a1e7f49d8d5954b704782016e2303fa49e2e250ebc40853505571a6
- clm_90805b7f9e27885ba75f0f5a0e5fd913c03e2fc9120de0dc2cb1d2d3586e58b5
- clm_acd70e486d81f3d2b6d1217f8ffc5231724c6904c8f82cbeda1313accf9a5c67
maturity: draft
page_id: pg_41ffabd70f0f5fe3a93986116b9a2a93
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_759154be5d595b6db65558f087fd2d98
title: labring/sealos/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md
  @ 1e97ffc47589
updated_at: '2026-09-14T04:04:55Z'
---

# labring/sealos/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md @ 1e97ffc47589

<!-- rcw:begin owner=source:src_759154be5d595b6db65558f087fd2d98 block=evidence -->
- All services authenticate using kubeconfig as the application identity, giving a consistent experience across browser, sealos CLI, and third-party clients. [@claim:clm_3d0712c05a1e7f49d8d5954b704782016e2303fa49e2e250ebc40853505571a6]
- Sealos applications use a front-end/back-end separation architecture, with front-ends able to serve independently via SSR rather than being bound to a monolith. [@claim:clm_90805b7f9e27885ba75f0f5a0e5fd913c03e2fc9120de0dc2cb1d2d3586e58b5]
- App Launchpad is a deployment tool for single images, and Terminal provides command-line services like a single-machine OS terminal; apps can call Kubernetes services or CRD controllers. [@claim:clm_acd70e486d81f3d2b6d1217f8ffc5231724c6904c8f82cbeda1313accf9a5c67]
<!-- rcw:end owner=source:src_759154be5d595b6db65558f087fd2d98 block=evidence -->

## Researcher notes

