---
access: public
aliases: []
claim_ids:
- clm_0e62889ea81350963a827d5b27535a93ddd0c3a318d54a58b1241741cc2aca2c
- clm_1998c197a235053dba156a5b5715d51791b7297d28707cff0744e86639051dd1
- clm_30b49378fa7be3341529dc148e09ddb4567e000c8ad2af473d6cce3e5a358de4
- clm_8d0ac02a03ee4384318e38132f61956406d7eb4e58ea9b3bd515e889ce5483b2
- clm_e7f90bae5ffc00a9572e7dab1ba4435578342d45b9999b123ace762c72a09bb6
maturity: draft
page_id: pg_e9c62a32ae0453269ec00800ab4df233
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_88a49f5801595300b756d9478ca508b7
title: honeydew-ai/honeydew-ai-coding-agents-plugins/README.md @ 36797d906d0a
updated_at: '2026-09-14T03:57:08Z'
---

# honeydew-ai/honeydew-ai-coding-agents-plugins/README.md @ 36797d906d0a

<!-- rcw:begin owner=source:src_88a49f5801595300b756d9478ca508b7 block=evidence -->
- Supported data warehouses are Snowflake, Databricks, and BigQuery. [@claim:clm_0e62889ea81350963a827d5b27535a93ddd0c3a318d54a58b1241741cc2aca2c]
- A Claude-specific release zip packages the plugin in claude.ai's expected layout, with .claude-plugin/plugin.json at the zip root alongside .mcp.json, hooks/, assets/, and skill markdown files. [@claim:clm_1998c197a235053dba156a5b5715d51791b7297d28707cff0744e86639051dd1]
- The plugin is distributed through agent-specific marketplaces: Claude Code and Copilot CLI use /plugin marketplace add, Codex uses codex plugin marketplace add, Cursor uses a Team Marketplace dashboard, and Gemini CLI uses gemini extensions install. [@claim:clm_30b49378fa7be3341529dc148e09ddb4567e000c8ad2af473d6cce3e5a358de4]
- Prerequisites are a coding agent with plugin/skill or MCP support (e.g., Claude Code, Codex, Cursor, Copilot CLI, Gemini CLI) and a Honeydew AI workspace with the Honeydew MCP server configured. [@claim:clm_8d0ac02a03ee4384318e38132f61956406d7eb4e58ea9b3bd515e889ce5483b2]
- Skills are written as agent-agnostic markdown documentation that any MCP-capable coding agent can consume as prompts or instructions, rather than being tied to one agent's plugin format. [@claim:clm_e7f90bae5ffc00a9572e7dab1ba4435578342d45b9999b123ace762c72a09bb6]
<!-- rcw:end owner=source:src_88a49f5801595300b756d9478ca508b7 block=evidence -->

## Researcher notes

