---
access: public
aliases: []
claim_ids:
- clm_4146b20f4d3b8b612adbebad9cfcb6be6f99753dbfbce39a85929787c7711a8b
- clm_852977b1e6615537e33b5cf81dca6d38365ce2fc233fc5f3e75cc80ed3ab156f
maturity: draft
page_id: pg_ef2225f712fc523797cb4a5599db668e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_29843589b61e55849a8ccbb29df449b5
title: aannoo/hcom/src/commands/relay.rs @ fabb309b57cb
updated_at: '2026-09-14T01:58:54Z'
---

# aannoo/hcom/src/commands/relay.rs @ fabb309b57cb

<!-- rcw:begin owner=source:src_29843589b61e55849a8ccbb29df449b5 block=evidence -->
- The relay command implementation parses --broker and --password flags, pings brokers over TCP/TLS, and derives relay health states (connected, starting, stale, waiting, error) from a shared RelayHealth type. [@claim:clm_4146b20f4d3b8b612adbebad9cfcb6be6f99753dbfbce39a85929787c7711a8b]
- Join tokens encode relay_id and broker URL and always carry a PSK (v0x04); legacy PSK-less tokens are rejected by relay_connect, and status shows only a key fingerprint. [@claim:clm_852977b1e6615537e33b5cf81dca6d38365ce2fc233fc5f3e75cc80ed3ab156f]
<!-- rcw:end owner=source:src_29843589b61e55849a8ccbb29df449b5 block=evidence -->

## Researcher notes

