---
access: public
aliases: []
claim_ids:
- clm_2e5de9ecaf5b2e1081e5fc58deca443b55b93e3f6ae545a826150b128686b37e
- clm_4ae8bc2bf1ebacf4a76ea5354c118c460b99f65b67ea6ee2b91b989d19fb2016
- clm_4c76e9b1001fa64c9bca01293770aa7eb012d21325439fe7f8873bd98b62e68d
- clm_5b3a2e05f63d08c11182108e4872e10ebfcdae7df1395e0b3e0e421fc3f3cfa5
- clm_6cd3834602276491824aa1eae9a8d624e08eaf935b24e454b46271236679968e
maturity: draft
page_id: pg_37e8c0b6f10a595a805e5fa5fc0f65a5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_df9eee72339a527ba13f5036cd481d8b
title: dinoanderson/qwen_cli_coder/docs/cli/configuration.md @ dbf277291908
updated_at: '2026-09-14T01:46:09Z'
---

# dinoanderson/qwen_cli_coder/docs/cli/configuration.md @ dbf277291908

<!-- rcw:begin owner=source:src_df9eee72339a527ba13f5036cd481d8b block=evidence -->
- MCP servers are configured via mcpServers settings; same-named tools from multiple servers are prefixed with the server alias to avoid conflicts. [@claim:clm_2e5de9ecaf5b2e1081e5fc58deca443b55b93e3f6ae545a826150b128686b37e]
- Settings support coreTools and excludeTools lists to restrict which built-in tools the model can use, plus an autoAccept option to skip confirmation for safe tools. [@claim:clm_4ae8bc2bf1ebacf4a76ea5354c118c460b99f65b67ea6ee2b91b989d19fb2016]
- Configuration uses ~/.qwen/settings.json (user) and .qwen/settings.json (project, overriding user), with a five-layer precedence ending in command-line arguments. [@claim:clm_4c76e9b1001fa64c9bca01293770aa7eb012d21325439fe7f8873bd98b62e68d]
- A sandbox setting (default false) enables tool execution inside a pre-built Qwen-cli-sandbox Docker image, and MCP server configs can set a trust flag bypassing tool confirmations. [@claim:clm_5b3a2e05f63d08c11182108e4872e10ebfcdae7df1395e0b3e0e421fc3f3cfa5]
- A checkpointing feature (disabled by default) can save and restore conversation and file states, enabling a /restore command when enabled. [@claim:clm_6cd3834602276491824aa1eae9a8d624e08eaf935b24e454b46271236679968e]
<!-- rcw:end owner=source:src_df9eee72339a527ba13f5036cd481d8b block=evidence -->

## Researcher notes

