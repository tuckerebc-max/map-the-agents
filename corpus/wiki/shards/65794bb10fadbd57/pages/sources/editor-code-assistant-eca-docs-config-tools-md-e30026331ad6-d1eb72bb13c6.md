---
access: public
aliases: []
claim_ids:
- clm_0eab46df40bddd7555e009676fe811f0cf24613ad4038b8be85e26296b909ab8
- clm_53d48f2581e309b150970a6e2ae6a2b9a4c64cfddc8c3acaf2d93c273d0cc84a
- clm_d6e51bd0e157050c65bac269326ace240333014f81612bda305d3a63d2e4461d
maturity: draft
page_id: pg_57226f27c6e152e0a9bed1eb72bb13c6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b107abf72ecc5e23a4054c09d6ccef48
title: editor-code-assistant/eca/docs/config/tools.md @ e30026331ad6
updated_at: '2026-09-14T01:47:30Z'
---

# editor-code-assistant/eca/docs/config/tools.md @ e30026331ad6

<!-- rcw:begin owner=source:src_b107abf72ecc5e23a4054c09d6ccef48 block=evidence -->
- MCP servers are configured via an `mcpServers` key supporting stdio commands and HTTP (streamable or SSE) URLs, with OAuth discovery, static Authorization headers, and a `disabled` flag. [@claim:clm_0eab46df40bddd7555e009676fe811f0cf24613ad4038b8be85e26296b909ab8]
- Custom tools are defined in config with a description, a command string containing {{argument_name}} placeholders replaced by LLM-supplied values, and a schema of parameters. [@claim:clm_53d48f2581e309b150970a6e2ae6a2b9a4c64cfddc8c3acaf2d93c273d0cc84a]
- ECA supports three tool types: native tools (edit_file, write_file, read, etc.), configured MCP servers, and user-defined custom CLI tools. [@claim:clm_d6e51bd0e157050c65bac269326ace240333014f81612bda305d3a63d2e4461d]
<!-- rcw:end owner=source:src_b107abf72ecc5e23a4054c09d6ccef48 block=evidence -->

## Researcher notes

