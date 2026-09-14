---
access: public
aliases: []
claim_ids:
- clm_480027dceffab8387cd4e6f137c4e4000d2e01c942ca21d43dfd440fac4d33fb
- clm_678ba0783d1b892060edc42a069e4f41b9b62d173e8bcbc803e80e3812eb98f6
- clm_88e327d845e8cf0a9d80c8b1987b52295573e0bbd7f024ed555958ff70fda8a3
maturity: draft
page_id: pg_deb0613a971c5bf990576182833a7c88
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ccfbe069f86c50da825cf1a154a54a0d
title: JuliusBrussee/cavemem/docs/mcp.md @ 166078dd7c46
updated_at: '2026-09-14T04:02:15Z'
---

# JuliusBrussee/cavemem/docs/mcp.md @ 166078dd7c46

<!-- rcw:begin owner=source:src_ccfbe069f86c50da825cf1a154a54a0d block=evidence -->
- Search is hybrid: SQLite FTS5 BM25 keyword matching blended with a local vector index, weighted by the tunable search.alpha setting (default 0.5). [@claim:clm_480027dceffab8387cd4e6f137c4e4000d2e01c942ca21d43dfd440fac4d33fb]
- The MCP server exposes search, timeline, get_observations, and list_sessions, plus an opt-in enrich tool; search and timeline return compact results while get_observations fetches full bodies. [@claim:clm_678ba0783d1b892060edc42a069e4f41b9b62d173e8bcbc803e80e3812eb98f6]
- The enrich tool is off by default and unregistered when disabled, so no network call occurs; when enabled it enforces SSRF protections, rejecting private, loopback, link-local, and unique-local targets including obfuscated numeric forms. [@claim:clm_88e327d845e8cf0a9d80c8b1987b52295573e0bbd7f024ed555958ff70fda8a3]
<!-- rcw:end owner=source:src_ccfbe069f86c50da825cf1a154a54a0d block=evidence -->

## Researcher notes

