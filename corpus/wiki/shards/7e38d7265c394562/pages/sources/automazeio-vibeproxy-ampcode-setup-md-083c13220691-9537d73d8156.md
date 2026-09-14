---
access: public
aliases: []
claim_ids:
- clm_4d2469188cca33a84190b73e85f0dfe5f2b3b8be6a8b5419247e1ae0703d6645
- clm_7dd0a1f0c84cdae1d84dc655a5af37530b11c8adbd35eccf469d1c48464957f2
maturity: draft
page_id: pg_6702886ef45b5fba83409537d73d8156
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_63fc338067e55fa3b7fcfbb093d44299
title: automazeio/vibeproxy/AMPCODE_SETUP.md @ 083c13220691
updated_at: '2026-09-14T03:36:16Z'
---

# automazeio/vibeproxy/AMPCODE_SETUP.md @ 083c13220691

<!-- rcw:begin owner=source:src_63fc338067e55fa3b7fcfbb093d44299 block=evidence -->
- The proxy listens on localhost port 8317; Amp routes /auth/cli-login and /api/* to ampcode.com and /provider/* to CLIProxyAPI on port 8318. [@claim:clm_4d2469188cca33a84190b73e85f0dfe5f2b3b8be6a8b5419247e1ae0703d6645]
- Multiple accounts per provider are supported with automatic round-robin distribution and failover when rate-limited; provider enable/disable toggles hot-reload instantly without restart. [@claim:clm_7dd0a1f0c84cdae1d84dc655a5af37530b11c8adbd35eccf469d1c48464957f2]
<!-- rcw:end owner=source:src_63fc338067e55fa3b7fcfbb093d44299 block=evidence -->

## Researcher notes

