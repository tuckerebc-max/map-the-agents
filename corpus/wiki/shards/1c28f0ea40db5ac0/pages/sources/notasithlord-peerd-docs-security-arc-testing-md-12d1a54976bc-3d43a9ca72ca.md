---
access: public
aliases: []
claim_ids:
- clm_402c631786821379e914a8231aadfd4c38c1200a4aa4fc1c09a17bf031dacaf9
- clm_47bd4b11d4833074141f3c11470f7d7ee0fefd90aa9243b3c9b4b295b36dedbb
maturity: draft
page_id: pg_8ae45164a14f530683ec3d43a9ca72ca
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_59e8ed91088259fd8c4792e06493c7c5
title: NotASithLord/peerd/docs/security/ARC-TESTING.md @ 12d1a54976bc
updated_at: '2026-09-14T02:23:22Z'
---

# NotASithLord/peerd/docs/security/ARC-TESTING.md @ 12d1a54976bc

<!-- rcw:begin owner=source:src_59e8ed91088259fd8c4792e06493c7c5 block=evidence -->
- Documented residual egress limits: Chrome DNR does not intercept worker-created WebSockets, private-network classification is lexical (no DNS resolution, so DNS rebinding is outside the check), and query strings/fragments are not a complete DLP boundary. [@claim:clm_402c631786821379e914a8231aadfd4c38c1200a4aa4fc1c09a17bf031dacaf9]
- Credentials, network rules, confirmations, and audit stay with the extension; egress controls include refusal of private-network/cloud-metadata targets, denylist checks, and redirect blocking, with per-operation scoped network policies. [@claim:clm_47bd4b11d4833074141f3c11470f7d7ee0fefd90aa9243b3c9b4b295b36dedbb]
<!-- rcw:end owner=source:src_59e8ed91088259fd8c4792e06493c7c5 block=evidence -->

## Researcher notes

