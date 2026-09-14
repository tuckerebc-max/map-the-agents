---
access: public
aliases: []
claim_ids:
- clm_b916462f5c03094e21402d3237f0369b2dcc8baa35f813b05d6538c51c0597ae
- clm_d4f60a455fd7c8c3144c118644502e1dd488a051684758cb7c070e05425de8a3
- clm_d8eec0153141ea63c52567e4958c50d9d903eb666b13d3afee02b3790425a16a
- clm_ede2b000b3899b1ef050a5e4526d80d4c18de1bc3ee4549498eb6d257d0ccfbc
maturity: draft
page_id: pg_2d80cefa0b8b5446ad9d5ade1a67b669
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_04fd2151e4c35bf2be7a571fd807cb92
title: coder/xum/docs/hooks/tools.mdx @ fbbea2b16403
updated_at: '2026-09-14T03:41:45Z'
---

# coder/xum/docs/hooks/tools.mdx @ fbbea2b16403

<!-- rcw:begin owner=source:src_04fd2151e4c35bf2be7a571fd807cb92 block=evidence -->
- Tool hooks let users run their own scripts around tool executions: `.xum/tool_pre` runs before every tool and a non-zero exit blocks the tool with the error shown to the agent; `.xum/tool_post` runs after tools and reports failures via hook_output. [@claim:clm_b916462f5c03094e21402d3237f0369b2dcc8baa35f813b05d6538c51c0597ae]
- A `.xum/tool_env` file is sourced (not executed) before every bash tool call to configure the shell environment, affecting only bash tools; hooks must finish within 10 seconds or be terminated. [@claim:clm_d4f60a455fd7c8c3144c118644502e1dd488a051684758cb7c070e05425de8a3]
- Hooks receive environment variables such as XUM_TOOL, XUM_WORKSPACE_ID, and XUM_TOOL_INPUT_PATH; tool input is flattened into XUM_TOOL_INPUT_<...> variables with fields over 8KB omitted, and hooks are looked up first at project level (.xum/) then user level (~/.xum/). [@claim:clm_d8eec0153141ea63c52567e4958c50d9d903eb666b13d3afee02b3790425a16a]
- Windows support is in alpha, requires Git for Windows (WSL is explicitly not supported), and tool hooks are documented as experimental with expected breaking changes. [@claim:clm_ede2b000b3899b1ef050a5e4526d80d4c18de1bc3ee4549498eb6d257d0ccfbc]
<!-- rcw:end owner=source:src_04fd2151e4c35bf2be7a571fd807cb92 block=evidence -->

## Researcher notes

