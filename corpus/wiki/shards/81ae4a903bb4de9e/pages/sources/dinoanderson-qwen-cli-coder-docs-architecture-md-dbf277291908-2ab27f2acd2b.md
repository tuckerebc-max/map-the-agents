---
access: public
aliases: []
claim_ids:
- clm_1613ed4107f98da202d1486a05090d0d29a4bffaae3d06ccd4a0de860d7dbcba
- clm_da2338b44673550ad1b62d8095e5089bcd522cc178bc0a8b2cdb0fd18c5afe46
maturity: draft
page_id: pg_d0b24492bdda5d928e342ab27f2acd2b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_16d8c179d7fe5a08b13fb542c9f932df
title: dinoanderson/qwen_cli_coder/docs/architecture.md @ dbf277291908
updated_at: '2026-09-14T01:46:09Z'
---

# dinoanderson/qwen_cli_coder/docs/architecture.md @ dbf277291908

<!-- rcw:begin owner=source:src_16d8c179d7fe5a08b13fb542c9f932df block=evidence -->
- Tools that modify the filesystem or run shell commands require user approval before execution; read-only operations may proceed without confirmation. [@claim:clm_1613ed4107f98da202d1486a05090d0d29a4bffaae3d06ccd4a0de860d7dbcba]
- Architecture splits a user-facing CLI package (packages/cli) from a backend core package (packages/core) that handles API calls, prompt construction, and tool execution. [@claim:clm_da2338b44673550ad1b62d8095e5089bcd522cc178bc0a8b2cdb0fd18c5afe46]
<!-- rcw:end owner=source:src_16d8c179d7fe5a08b13fb542c9f932df block=evidence -->

## Researcher notes

