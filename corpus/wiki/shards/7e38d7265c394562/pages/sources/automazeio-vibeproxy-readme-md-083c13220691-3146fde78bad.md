---
access: public
aliases: []
claim_ids:
- clm_67cff387cb084f210552ee6a206d247a3144b2988d37b028466c44fe9bc452ea
- clm_6efbb2bee8d58a96595c15b4a097df464bbf24f615f1a118a2331b6d8d9eac0a
- clm_7dd0a1f0c84cdae1d84dc655a5af37530b11c8adbd35eccf469d1c48464957f2
- clm_982b0196c9f614c2b3ea75b14c96a1f92b4f8e3a43b48c6402cb2a7a90d60933
- clm_f2ed4425d9833dae9312eb707ad4d498dc777c463e8ce2e4d0154e09d24797ab
maturity: draft
page_id: pg_a1f69e7151075e0896073146fde78bad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a29bd8a3e4335410a61e3cf5f87c9b2f
title: automazeio/vibeproxy/README.md @ 083c13220691
updated_at: '2026-09-14T03:36:16Z'
---

# automazeio/vibeproxy/README.md @ 083c13220691

<!-- rcw:begin owner=source:src_a29bd8a3e4335410a61e3cf5f87c9b2f block=evidence -->
- ServerManager controls the cli-proxy-api server process and OAuth authentication; AuthStatus monitors ~/.cli-proxy-api/ for auth files with real-time updates when files are added or removed. [@claim:clm_67cff387cb084f210552ee6a206d247a3144b2988d37b028466c44fe9bc452ea]
- The app consists of Swift sources (AppDelegate, ServerManager, SettingsView, AuthStatus) plus a bundled cli-proxy-api-plus binary, config.yaml, and icon resources inside the .app. [@claim:clm_6efbb2bee8d58a96595c15b4a097df464bbf24f615f1a118a2331b6d8d9eac0a]
- Multiple accounts per provider are supported with automatic round-robin distribution and failover when rate-limited; provider enable/disable toggles hot-reload instantly without restart. [@claim:clm_7dd0a1f0c84cdae1d84dc655a5af37530b11c8adbd35eccf469d1c48464957f2]
- VibeProxy is built on CLIProxyAPIPlus (CLIProxyAPI), which provides the core OAuth handling, token management, and API routing; the binary is bundled in the app. [@claim:clm_982b0196c9f614c2b3ea75b14c96a1f92b4f8e3a43b48c6402cb2a7a90d60933]
- The Intel build is marked untested with users asked to report issues; the app requires macOS 13 (Ventura) or later. [@claim:clm_f2ed4425d9833dae9312eb707ad4d498dc777c463e8ce2e4d0154e09d24797ab]
<!-- rcw:end owner=source:src_a29bd8a3e4335410a61e3cf5f87c9b2f block=evidence -->

## Researcher notes

