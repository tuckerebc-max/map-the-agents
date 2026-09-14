---
access: public
aliases: []
claim_ids:
- clm_300fac2017e23e353be305cb27401a8f2c09f52995941a2fee0206d0185c98e3
- clm_bd9f650e4c3d85dd5fdb4407f0d16710d10fb56eb61c8da9556d59a8c856aeac
- clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6
- clm_f3a4b28ad837cead0e510162283f8474745ef8141638cb2f2abed046a3b4b409
maturity: draft
page_id: pg_5f486e3af7c25335bfff5e60497f5393
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6eb6a1aaed025462852f9a25d7dea77f
title: hotovo/aider-desk/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md
  @ cb7ee89bf213
updated_at: '2026-09-14T02:04:46Z'
---

# hotovo/aider-desk/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md @ cb7ee89bf213

<!-- rcw:begin owner=source:src_6eb6a1aaed025462852f9a25d7dea77f block=evidence -->
- MCP is the standard tool boundary: servers connect via stdio or HTTP transports, tools are namespaced as <server><sep><tool>, and every invocation passes through the ApprovalManager. [@claim:clm_300fac2017e23e353be305cb27401a8f2c09f52995941a2fee0206d0185c98e3]
- The product features tool approval gates where users approve tools and authorize destructive actions; per the ADRs, all MCP tool invocations route through the ApprovalManager. [@claim:clm_bd9f650e4c3d85dd5fdb4407f0d16710d10fb56eb61c8da9556d59a8c856aeac]
- The frontend is built with React 19 and Tailwind CSS; the agent runtime depends on the Vercel AI SDK, with MCP support via @ai-sdk/mcp and @modelcontextprotocol/sdk. [@claim:clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6]
- The ADRs note trade-offs: SDK upgrades can shift part/type shapes requiring a dedicated pass, and MCP connection lifecycle issues (restarts, timeouts, unauthorized states) must be handled robustly across process boundaries. [@claim:clm_f3a4b28ad837cead0e510162283f8474745ef8141638cb2f2abed046a3b4b409]
<!-- rcw:end owner=source:src_6eb6a1aaed025462852f9a25d7dea77f block=evidence -->

## Researcher notes

