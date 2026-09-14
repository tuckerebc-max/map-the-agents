---
access: public
aliases: []
claim_ids:
- clm_05ead5e303fe0aa6818c350e3777463310d17849d8da645773f831ec8cc6d9d1
- clm_1ca2a64908f966c79e9e393fe9ceb99bbd05bab845401b9f80d2b3959f69bde5
- clm_3c8f1fd78531f4f707a264dbc25b58634b776715c51d27b8bbbc92181db2a2d6
- clm_4d2469188cca33a84190b73e85f0dfe5f2b3b8be6a8b5419247e1ae0703d6645
- clm_77821df021b828d4c1e714a6d3e20014cfa35c0a6e11819ac828ff95e8e2278b
- clm_982b0196c9f614c2b3ea75b14c96a1f92b4f8e3a43b48c6402cb2a7a90d60933
- clm_bab7457310437f50bdb1d1acc8d28207356647d461fdbd0d8cf97828d4d5d5c6
- clm_fcf34ef3a1f93d2898b179715e61a4817633c5f770ca70e9bef45fb51bb12cb8
maturity: draft
page_id: pg_aa5dbe887b7d5ba2b0cb3ae68163d4d5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_44392680481757d8a3daa80d6965b223
title: automazeio/vibeproxy/FACTORY_SETUP.md @ 083c13220691
updated_at: '2026-09-14T03:36:16Z'
---

# automazeio/vibeproxy/FACTORY_SETUP.md @ 083c13220691

<!-- rcw:begin owner=source:src_44392680481757d8a3daa80d6965b223 block=evidence -->
- When a -thinking-* model is used, VibeProxy automatically injects the anthropic-beta interleaved-thinking-2025-05-14 header, merging with existing beta headers without duplicates. [@claim:clm_05ead5e303fe0aa6818c350e3777463310d17849d8da645773f831ec8cc6d9d1]
- Invalid thinking suffixes (non-integer) are stripped and the vanilla model is used without thinking. [@claim:clm_1ca2a64908f966c79e9e393fe9ceb99bbd05bab845401b9f80d2b3959f69bde5]
- VibeProxy supports a custom model-name suffix pattern {model}-thinking-{NUMBER} that it intercepts, strips, and converts into a thinking token-budget parameter before forwarding to CLIProxyAPI. [@claim:clm_3c8f1fd78531f4f707a264dbc25b58634b776715c51d27b8bbbc92181db2a2d6]
- The proxy listens on localhost port 8317; Amp routes /auth/cli-login and /api/* to ampcode.com and /provider/* to CLIProxyAPI on port 8318. [@claim:clm_4d2469188cca33a84190b73e85f0dfe5f2b3b8be6a8b5419247e1ae0703d6645]
- The docs warn the approach may violate AI providers' terms of service, risking account suspension or bans, and that provider API changes could break it; use is at the user's own risk. [@claim:clm_77821df021b828d4c1e714a6d3e20014cfa35c0a6e11819ac828ff95e8e2278b]
- VibeProxy is built on CLIProxyAPIPlus (CLIProxyAPI), which provides the core OAuth handling, token management, and API routing; the binary is bundled in the app. [@claim:clm_982b0196c9f614c2b3ea75b14c96a1f92b4f8e3a43b48c6402cb2a7a90d60933]
- The server binds only to localhost (127.0.0.1) and all upstream traffic uses HTTPS, per the security notes. [@claim:clm_bab7457310437f50bdb1d1acc8d28207356647d461fdbd0d8cf97828d4d5d5c6]
- Authentication tokens are stored locally in ~/.cli-proxy-api/ with 0600 permissions and are auto-refreshed before expiration. [@claim:clm_fcf34ef3a1f93d2898b179715e61a4817633c5f770ca70e9bef45fb51bb12cb8]
<!-- rcw:end owner=source:src_44392680481757d8a3daa80d6965b223 block=evidence -->

## Researcher notes

