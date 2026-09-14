---
access: public
aliases: []
claim_ids:
- clm_006251e8c615219542ada5fe0d94d139066eb8ec73a2104309346dab373758bb
- clm_270198b2b776df947f08acd01cb1e60efeae5f9e8ca94e259d8ee91105451e5e
- clm_d288e5546590be60c259addfee056fb21dbb12611d1a4e5acf584cb807fdc5ed
maturity: draft
page_id: pg_4b054c84d0005b1bacca7caafae440c4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_59a55bda968d5344973e2bc76f7bf8fa
title: minmaxflow/mini-kode/docs/tools.md @ 4e7f9767e5ca
updated_at: '2026-09-14T02:19:14Z'
---

# minmaxflow/mini-kode/docs/tools.md @ 4e7f9767e5ca

<!-- rcw:begin owner=source:src_59a55bda968d5344973e2bc76f7bf8fa block=evidence -->
- MCP servers are configured via .mini-kode/mcp.json with stdio and http transports; tools from connected servers are auto-registered, and ${ENV_VAR} references in args and headers are resolved from the environment. [@claim:clm_006251e8c615219542ada5fe0d94d139066eb8ec73a2104309346dab373758bb]
- Built-in tools include fileRead, fileEdit, listFiles, grep, glob, bash, architect, todo_read, todo_write, and fetch, plus dynamically registered MCP tools; fileEdit, bash, fetch, and MCP tools are marked as requiring permission. [@claim:clm_270198b2b776df947f08acd01cb1e60efeae5f9e8ca94e259d8ee91105451e5e]
- Tools implement a shared Tool<Input, Output> interface with a readonly flag; read-only tools run concurrently while writing tools run sequentially, and writing tools check permissions, pausing until the user approves. [@claim:clm_d288e5546590be60c259addfee056fb21dbb12611d1a4e5acf584cb807fdc5ed]
<!-- rcw:end owner=source:src_59a55bda968d5344973e2bc76f7bf8fa block=evidence -->

## Researcher notes

