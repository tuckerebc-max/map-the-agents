---
access: public
aliases: []
claim_ids:
- clm_5495ba05242f8dcb8c464cc80b4d168b5c27f2897691973c04c86526136793b9
- clm_78c3e75eb41584e7ab49659c0d6993be4702580e4bfd6708fd319fe5324c6209
maturity: draft
page_id: pg_705ac381b16556c3a85123cb94f60e58
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_78856a089c08522cb50af67e5392a1b8
title: openchamber/openchamber/docs/REVERSE_PROXY.md @ 1636fd2bf8e4
updated_at: '2026-09-14T03:11:17Z'
---

# openchamber/openchamber/docs/REVERSE_PROXY.md @ 1636fd2bf8e4

<!-- rcw:begin owner=source:src_78856a089c08522cb50af67e5392a1b8 block=evidence -->
- The server exposes WebSocket routes (/api/event/ws, /api/global/event/ws, /api/terminal/ws) and SSE routes (/api/event, /api/global/event, /api/notifications/stream, /api/openchamber/events) that reverse proxies must pass through unbuffered. [@claim:clm_5495ba05242f8dcb8c464cc80b4d168b5c27f2897691973c04c86526136793b9]
- OpenChamber appears to gzip-compress HTTP responses with a 1 KB threshold while excluding SSE streaming routes from compression, per the reverse-proxy guidance. [@claim:clm_78c3e75eb41584e7ab49659c0d6993be4702580e4bfd6708fd319fe5324c6209]
<!-- rcw:end owner=source:src_78856a089c08522cb50af67e5392a1b8 block=evidence -->

## Researcher notes

