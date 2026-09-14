---
access: public
aliases: []
claim_ids:
- clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc
- clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592
maturity: draft
page_id: pg_14ce0ff9637955cc8d54e46737a1fefa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_55dfcec9a5085a97866e4ed74cec5710
title: mvanhorn/agentcookie/docs/consumption.md @ 57b53dfd9162
updated_at: '2026-09-14T04:10:49Z'
---

# mvanhorn/agentcookie/docs/consumption.md @ 57b53dfd9162

<!-- rcw:begin owner=source:src_55dfcec9a5085a97866e4ed74cec5710 block=evidence -->
- The product requires Tailscale and Chrome on both machines, and the Linux sink must bind a Tailscale 100.x address, refusing to start without the tailnet. [@claim:clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc]
- On Linux, a missing blocklist.yaml or omitted policy field means the sink ships nothing (allowlist-empty) as a security default; sync-all requires an explicit blocklist policy with an empty domains list, described as an operator choice rather than the code default. [@claim:clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592]
<!-- rcw:end owner=source:src_55dfcec9a5085a97866e4ed74cec5710 block=evidence -->

## Researcher notes

