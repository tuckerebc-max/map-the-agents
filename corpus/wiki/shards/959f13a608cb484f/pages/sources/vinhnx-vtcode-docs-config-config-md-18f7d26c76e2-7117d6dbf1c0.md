---
access: public
aliases: []
claim_ids:
- clm_0318e6798c363c9641107dd48e241fd62305b43e7c61e6e9182808db47b777ef
- clm_162178fbb2ce931ce2e8e56772ac5136101131a67ab3b9465378587ac3b73c5c
- clm_663bfe81efe3364e76cb4773e59ac35b9d050340db2ddc8ec8612fe76ca3cd33
- clm_caa9a1ab5e14a82f06aaa03c7761877c88dbc28176966cac348494764dcc4a4a
maturity: draft
page_id: pg_20b8e42bc6555c499a707117d6dbf1c0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5774b46e756b59c487a8c1654de38cd9
title: vinhnx/VTCode/docs/config/config.md @ 18f7d26c76e2
updated_at: '2026-09-14T03:21:46Z'
---

# vinhnx/VTCode/docs/config/config.md @ 18f7d26c76e2

<!-- rcw:begin owner=source:src_5774b46e756b59c487a8c1654de38cd9 block=evidence -->
- Feature flags include human_in_the_loop (tool approval prompts, default true) and mcp_enabled (default false), toggled via the [features] table in vtcode.toml. [@claim:clm_0318e6798c363c9641107dd48e241fd62305b43e7c61e6e9182808db47b777ef]
- Interactive sessions live-reload watched config changes with debouncing; safe settings apply without restart, and malformed edits keep the last valid configuration with a warning. [@claim:clm_162178fbb2ce931ce2e8e56772ac5136101131a67ab3b9465378587ac3b73c5c]
- Configuration uses vtcode.toml at workspace or platform config-directory layers, with environment-variable overrides and a legacy $VTCODE_HOME path kept as a migration source. [@claim:clm_663bfe81efe3364e76cb4773e59ac35b9d050340db2ddc8ec8612fe76ca3cd33]
- The agent.provider setting supports many providers including openai, anthropic, google, deepseek, ollama, lmstudio, and others, with per-provider base_url and API-key environment variables configurable. [@claim:clm_caa9a1ab5e14a82f06aaa03c7761877c88dbc28176966cac348494764dcc4a4a]
<!-- rcw:end owner=source:src_5774b46e756b59c487a8c1654de38cd9 block=evidence -->

## Researcher notes

