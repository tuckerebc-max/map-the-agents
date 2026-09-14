---
access: public
aliases: []
claim_ids:
- clm_72d9e90bdaef7eebba65b8b86bda525a0280233a303bbe6d406751aed04323fc
- clm_f2e250d0fbb169ddeb3093a3b99ded31a0cf541cc04fd8cccbbea61779a93f97
maturity: draft
page_id: pg_e0fd6aa030bd54f79f485f28544063d3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_301b6c9ef94959088ee8f498eef6091a
title: kuafuai/aipexbase/docs/INSTALL.md @ bf523cfa479f
updated_at: '2026-09-14T04:03:49Z'
---

# kuafuai/aipexbase/docs/INSTALL.md @ bf523cfa479f

<!-- rcw:begin owner=source:src_301b6c9ef94959088ee8f498eef6091a block=evidence -->
- Docker Compose deployment is the recommended install method; prerequisites are Linux, Docker, and Docker Compose v2.5+, started with docker-compose up -d. [@claim:clm_72d9e90bdaef7eebba65b8b86bda525a0280233a303bbe6d406751aed04323fc]
- External reverse-proxy setups are supported with nginx snippets routing /baas-api and /mcp to port 8080, with long-connection timeouts (86400s) and buffering disabled for the MCP route. [@claim:clm_f2e250d0fbb169ddeb3093a3b99ded31a0cf541cc04fd8cccbbea61779a93f97]
<!-- rcw:end owner=source:src_301b6c9ef94959088ee8f498eef6091a block=evidence -->

## Researcher notes

