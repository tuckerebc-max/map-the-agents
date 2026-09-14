---
access: public
aliases: []
claim_ids:
- clm_06a47d8b815a11a11d63da1f0fda96959422e1493a01fef878f0593124a05f8d
- clm_1044290e3e54ffa96294ef734e6292c9db6720574e2542bf2b07d5be7f26ee19
- clm_ece22aadb879f8f6abcc37cab2e3011a63cfdaefd538b85ce0ab5b993ac69bdc
maturity: draft
page_id: pg_d917194e7d1d53008ee3dcd8e9d12348
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4971cfbe1898572aadd09b2cbc430a69
title: openinterpreter/openinterpreter/docs/config.md @ 860153a5318d
updated_at: '2026-09-14T02:27:12Z'
---

# openinterpreter/openinterpreter/docs/config.md @ 860153a5318d

<!-- rcw:begin owner=source:src_4971cfbe1898572aadd09b2cbc430a69 block=evidence -->
- Custom OpenAI-compatible providers can be defined under `[model_providers.<id>]` with base_url, env_key, and wire_api (responses or chat), and credentials should come from environment variables or a credential store. [@claim:clm_06a47d8b815a11a11d63da1f0fda96959422e1493a01fef878f0593124a05f8d]
- MCP servers are configured under `[mcp_servers]` supporting stdio commands and streamable HTTP servers via `url`, with per-server default tool approval modes. [@claim:clm_1044290e3e54ffa96294ef734e6292c9db6720574e2542bf2b07d5be7f26ee19]
- Configuration is read from TOML files at user level (`~/.openinterpreter/config.toml`) and trusted project level (`.openinterpreter/config.toml`), with CLI `-c` overrides applying per invocation. [@claim:clm_ece22aadb879f8f6abcc37cab2e3011a63cfdaefd538b85ce0ab5b993ac69bdc]
<!-- rcw:end owner=source:src_4971cfbe1898572aadd09b2cbc430a69 block=evidence -->

## Researcher notes

