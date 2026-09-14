---
access: public
aliases: []
claim_ids:
- clm_27e6c8fc29e55278d28f76e82b75d2911eee62f6bfd4f55e4ecd99c502c99983
maturity: draft
page_id: pg_69483bf43cd7569f90744fbeebaeabd3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_661f330dbc4d588184d2aa83e609b2af
title: sahil87/run-kit/docs/findings/relay-mux-hol.md @ 65653f4d91c5
updated_at: '2026-09-14T02:37:21Z'
---

# sahil87/run-kit/docs/findings/relay-mux-hol.md @ 65653f4d91c5

<!-- rcw:begin owner=source:src_661f330dbc4d588184d2aa83e609b2af block=evidence -->
- A measured spike concluded the terminal relay mux must use per-stream bounded send queues with a non-FIFO scheduler: a shared FIFO made echo RTT 1.66s under flood at 1 Mbps, while per-stream queues held it to 32ms with no throughput cost. [@claim:clm_27e6c8fc29e55278d28f76e82b75d2911eee62f6bfd4f55e4ecd99c502c99983]
<!-- rcw:end owner=source:src_661f330dbc4d588184d2aa83e609b2af block=evidence -->

## Researcher notes

