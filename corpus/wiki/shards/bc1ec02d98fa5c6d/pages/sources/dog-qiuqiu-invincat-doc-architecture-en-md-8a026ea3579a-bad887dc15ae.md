---
access: public
aliases: []
claim_ids:
- clm_70318a9f4bd124c571269dc995a5b6d5d9f3ade61602339fb46c698f1d01cf53
- clm_70e242a815658fb666d835516dcef64a98452e034e82f6e5d82d3828b2b7dd71
- clm_b5aae266459120dffad5efd8b7c0f413115035e6d15e1751c689f99fb4482685
- clm_c19110a154cc7f2e96fccca5068880a5cdb5189932ff81c9932858a6d6915b94
- clm_c389cfa7030c09cd1461982c9f298920b67c3b35af8b413438c42436db3b840b
- clm_d5403586f8815c3d71e206417782d5cc64957cc4425109b42b43f0ab1618339f
maturity: draft
page_id: pg_3bb7ab36505e5b588fd8bad887dc15ae
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6beca8f1ded65be2850c3c252ddf2f60
title: dog-qiuqiu/invincat/doc/ARCHITECTURE_EN.md @ 8a026ea3579a
updated_at: '2026-09-14T03:06:54Z'
---

# dog-qiuqiu/invincat/doc/ARCHITECTURE_EN.md @ 8a026ea3579a

<!-- rcw:begin owner=source:src_6beca8f1ded65be2850c3c252ddf2f60 block=evidence -->
- The package supports both interactive Textual TUI and non-interactive runtime paths, plus a local LangGraph server mode and ACP startup wiring, selected from parsed CLI arguments. [@claim:clm_70318a9f4bd124c571269dc995a5b6d5d9f3ade61602339fb46c698f1d01cf53]
- MCP integration includes server loading/connection, tool wrapping, and an MCP server trust policy module (mcp/trust.py). [@claim:clm_70e242a815658fb666d835516dcef64a98452e034e82f6e5d82d3828b2b7dd71]
- Middleware includes approve_plan and ask_user interrupt protocols, auto memory refresh, project-scoped file management tools (file_info, mkdir, move_file, copy_file, delete_file), micro_compaction of old messages, and token state tracking. [@claim:clm_b5aae266459120dffad5efd8b7c0f413115035e6d15e1751c689f99fb4482685]
- Model selection is per-call switchable through LangGraph runtime context via configurable_model, and model profiles persist as TOML configuration with thread-level model preferences. [@claim:clm_c19110a154cc7f2e96fccca5068880a5cdb5189932ff81c9932858a6d6915b94]
- The runtime is a Textual TUI over a DeepAgents/LangGraph agent: cli assembles startup, agent builds the agent with tools/middleware/backend/system prompt, textual_adapter converts agent streams to UI messages, and widgets render chat, tool calls, approvals, and selectors. [@claim:clm_c389cfa7030c09cd1461982c9f298920b67c3b35af8b413438c42436db3b840b]
- The scheduler subsystem parses natural-language time expressions into cron/once schedules, stores tasks in SQLite with schema migrations, exposes schedule tools via ScheduleMiddleware, and supports WeCom delivery of scheduled results. [@claim:clm_d5403586f8815c3d71e206417782d5cc64957cc4425109b42b43f0ab1618339f]
<!-- rcw:end owner=source:src_6beca8f1ded65be2850c3c252ddf2f60 block=evidence -->

## Researcher notes

