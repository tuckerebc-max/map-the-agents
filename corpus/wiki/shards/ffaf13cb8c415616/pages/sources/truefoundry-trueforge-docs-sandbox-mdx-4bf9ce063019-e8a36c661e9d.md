---
access: public
aliases: []
claim_ids:
- clm_71eb11687ed624c56a63f5257d4ea9dafd37e2ddd22d6a0a63ec72b619e9c768
- clm_7b4d2344119d1b2a05de17c62ee1d9f80c5d801f6e2c39e7e3c00a1e43fab86c
- clm_e18d3f2a282a09a65796cd0920ade1ac22a786c0da091bcc1af20e09b6a22071
maturity: draft
page_id: pg_2283bdcda1a6580fa444e8a36c661e9d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d535d729c6e054c3ab4c07de8de30322
title: truefoundry/trueforge/docs/sandbox.mdx @ 4bf9ce063019
updated_at: '2026-09-14T03:19:56Z'
---

# truefoundry/trueforge/docs/sandbox.mdx @ 4bf9ce063019

<!-- rcw:begin owner=source:src_d535d729c6e054c3ab4c07de8de30322 block=evidence -->
- Daytona is documented as the only sandbox provider supported today, with support for additional providers planned. [@claim:clm_71eb11687ed624c56a63f5257d4ea9dafd37e2ddd22d6a0a63ec72b619e9c768]
- MCP tool connectivity supports remote servers with header auth or OAuth, including in-chat authorization; sandbox provider configuration requires a Daytona API key with snapshot-create permission, and the sandbox is off by default per agent. [@claim:clm_7b4d2344119d1b2a05de17c62ee1d9f80c5d801f6e2c39e7e3c00a1e43fab86c]
- TrueForge adopts a 'sandbox as tool' pattern: the agent loop and credentials stay in the harness while the sandbox only runs code, file, and shell operations, is provisioned on demand, and never holds model or MCP credentials. [@claim:clm_e18d3f2a282a09a65796cd0920ade1ac22a786c0da091bcc1af20e09b6a22071]
<!-- rcw:end owner=source:src_d535d729c6e054c3ab4c07de8de30322 block=evidence -->

## Researcher notes

