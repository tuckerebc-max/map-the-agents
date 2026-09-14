---
access: public
aliases: []
claim_ids:
- clm_4df4c55fe6b47733f3208fd5ea5929f9553efab2a9311583bdcc1ec9a90d9975
- clm_853f95f046657846674dd79451c0ab71264a5c331c03595fe56301e8157950bc
maturity: draft
page_id: pg_c0c22fe3daac5b5784f77978772ce335
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1e881265e22e5188bb66425f1da7e0bf
title: fireproof-storage/fireproof/CHANGELOG.md @ 404e6c5c7f28
updated_at: '2026-09-14T03:51:26Z'
---

# fireproof-storage/fireproof/CHANGELOG.md @ 404e6c5c7f28

<!-- rcw:begin owner=source:src_1e881265e22e5188bb66425f1da7e0bf block=evidence -->
- From version 0.19 onward the database format is stated to be stable with no backward-compatibility breaks, though internal APIs changed between the 0.19 and 0.20 series. [@claim:clm_4df4c55fe6b47733f3208fd5ea5929f9553efab2a9311583bdcc1ec9a90d9975]
- The 0.20 series changes the Gateway interface to pass semantic runtime objects instead of Uint8Arrays and Url, renames Database to Ledger with no functional change, replaces memfs with a memory:// URL scheme, and adds a GatewayInterceptor for logging, encryption, or compression. [@claim:clm_853f95f046657846674dd79451c0ab71264a5c331c03595fe56301e8157950bc]
<!-- rcw:end owner=source:src_1e881265e22e5188bb66425f1da7e0bf block=evidence -->

## Researcher notes

