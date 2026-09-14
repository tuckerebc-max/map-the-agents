---
access: public
aliases: []
claim_ids:
- clm_1ef04899217fa6667c30c97a3de62703f1d78382fa0be15dc5f95d2b6724bcb0
- clm_57355eea2390faede08f2688b72e0b50df89906f7c21502b884ad075fe92308f
- clm_8d2e9bbfc045e4d13132539c6bce05481791cbc8e4cf66c1f532e07205886c69
- clm_f4d6ef52c761d440c13bde67502350cfdd03d2ff01b6822d842bc1d65e6c1692
maturity: draft
page_id: pg_6fd5e250df485b868c9831129058c888
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e2aff4b140035e008eb4fc7f576a6011
title: amrit110/oli/docs/src/api.md @ 18cf418cb0ee
updated_at: '2026-09-14T02:48:46Z'
---

# amrit110/oli/docs/src/api.md @ 18cf418cb0ee

<!-- rcw:begin owner=source:src_e2aff4b140035e008eb4fc7f576a6011 block=evidence -->
- The API docs state the server has no built-in authentication and should be treated as a trusted component, recommending a sandboxed deployment and passing model API keys through environment variables. [@claim:clm_1ef04899217fa6667c30c97a3de62703f1d78382fa0be15dc5f95d2b6724bcb0]
- The server exposes a JSON-RPC 2.0 API over stdio, documented to include a cancel_task method for stopping the current or a named task and a clear_conversation method for resetting conversation history. [@claim:clm_57355eea2390faede08f2688b72e0b50df89906f7c21502b884ad075fe92308f]
- The API docs state the server can be extended with additional JSON-RPC methods by editing main.rs and registering them, citing language-server-protocol integration or MCP support as example use cases. [@claim:clm_8d2e9bbfc045e4d13132539c6bce05481791cbc8e4cf66c1f532e07205886c69]
- The documented get_tasks method returns each task's id, description, status, tool count, and separate input and output token counts. [@claim:clm_f4d6ef52c761d440c13bde67502350cfdd03d2ff01b6822d842bc1d65e6c1692]
<!-- rcw:end owner=source:src_e2aff4b140035e008eb4fc7f576a6011 block=evidence -->

## Researcher notes

