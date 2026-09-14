---
access: public
aliases: []
claim_ids:
- clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6
- clm_ed124be0cfc3618cb36dde9851403ce8fd6d40ce5dece7df95b743bdfd8c52f1
- clm_f3a4b28ad837cead0e510162283f8474745ef8141638cb2f2abed046a3b4b409
maturity: draft
page_id: pg_50c401096a15542a84959bf3cf6d7193
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2cfb556ae44e50a48a8474c2593a3ac4
title: hotovo/aider-desk/docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md
  @ cb7ee89bf213
updated_at: '2026-09-14T02:04:46Z'
---

# hotovo/aider-desk/docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md @ cb7ee89bf213

<!-- rcw:begin owner=source:src_2cfb556ae44e50a48a8474c2593a3ac4 block=evidence -->
- The frontend is built with React 19 and Tailwind CSS; the agent runtime depends on the Vercel AI SDK, with MCP support via @ai-sdk/mcp and @modelcontextprotocol/sdk. [@claim:clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6]
- The agent runtime is built on the Vercel AI SDK; SDK message parts are the runtime currency, while persistence uses AiderDesk's own ContextMessage types, converted at the agent boundary in src/main/agent/utils.ts. [@claim:clm_ed124be0cfc3618cb36dde9851403ce8fd6d40ce5dece7df95b743bdfd8c52f1]
- The ADRs note trade-offs: SDK upgrades can shift part/type shapes requiring a dedicated pass, and MCP connection lifecycle issues (restarts, timeouts, unauthorized states) must be handled robustly across process boundaries. [@claim:clm_f3a4b28ad837cead0e510162283f8474745ef8141638cb2f2abed046a3b4b409]
<!-- rcw:end owner=source:src_2cfb556ae44e50a48a8474c2593a3ac4 block=evidence -->

## Researcher notes

