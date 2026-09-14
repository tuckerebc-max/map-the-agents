---
access: public
aliases: []
claim_ids:
- clm_34b07f73b02a43578c752819348d39c44dc33ad06275e6004bf563c83c46b3e0
- clm_d764a6d731b7050577da4e9535a392caad46ed70569d61df72c0fe49b643b2d6
- clm_dd0b22ed9f0d7ab2c083cd5146fc9df32524619e98c6b7e4397e831b45158a1f
maturity: draft
page_id: pg_73652a81a92b54bebb3e473f9f6cda49
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_59514b538a1a5efd8843e2f8a517943d
title: microsoft/amplifier/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md @ 28588b93886d
updated_at: '2026-09-14T02:19:10Z'
---

# microsoft/amplifier/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md @ 28588b93886d

<!-- rcw:begin owner=source:src_59514b538a1a5efd8843e2f8a517943d block=evidence -->
- Delegated child sessions resolve their provider by spawn-time precedence: caller provider_preferences, then agent overlay preferences (possibly written from model_role by a routing hook), then parent mount-plan defaults. [@claim:clm_34b07f73b02a43578c752819348d39c44dc33ad06275e6004bf563c83c46b3e0]
- Routing matrices map semantic model roles to ordered provider/model candidates, but routing applies only when the composed bundle mounts a routing strategy such as the routing-matrix hook. [@claim:clm_d764a6d731b7050577da4e9535a392caad46ed70569d61df72c0fe49b643b2d6]
- The architecture distinguishes a provider module (a vendor-protocol adapter) from configured provider instances, so one module can back multiple instances with unique IDs, accounts, models, and priorities. [@claim:clm_dd0b22ed9f0d7ab2c083cd5146fc9df32524619e98c6b7e4397e831b45158a1f]
<!-- rcw:end owner=source:src_59514b538a1a5efd8843e2f8a517943d block=evidence -->

## Researcher notes

