---
access: public
aliases: []
claim_ids:
- clm_0ac38f5ead68ab71d3f9f64df8cf27b16796aebca0ab83673ae06b0722dec6b0
maturity: draft
page_id: pg_0d25b2ba52165c9f89968ae38552187f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aef02dcc5e6158c0b2e0ab1d4fd39212
title: cortexkit/aft/ARCHITECTURE.md @ c0c8e80220ac
updated_at: '2026-09-14T03:42:55Z'
---

# cortexkit/aft/ARCHITECTURE.md @ c0c8e80220ac

<!-- rcw:begin owner=source:src_aef02dcc5e6158c0b2e0ab1d4fd39212 block=evidence -->
- Under sandbox.enabled, first-party bash commands run through Landlock (Linux) or Seatbelt (macOS); unsupported non-Unix platforms fail closed with sandbox_unavailable, and a one-command host escape prompts via an escalation permission ask. [@claim:clm_0ac38f5ead68ab71d3f9f64df8cf27b16796aebca0ab83673ae06b0722dec6b0]
<!-- rcw:end owner=source:src_aef02dcc5e6158c0b2e0ab1d4fd39212 block=evidence -->

## Researcher notes

