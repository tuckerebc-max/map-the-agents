---
access: public
aliases: []
claim_ids:
- clm_0a06aad296b9046fe8f2d030107618997089cf5fc5e61b4cdca1c40c401bb1a5
- clm_334e25b38984fe51b970be6520c331b9564a32f283547b38c3286e57e0ea24c0
- clm_7c408b454ab80018c5ec9d03ceba53567f3f6a962f5354f4aa049672830e7dda
- clm_7e1a43cb0f6aa65928d780e7926c044503100635297dbcfdd2da5e0786e2c98c
- clm_8ffae93eac7cf6da6818754083bf8106b27c9d55ae0f439ddef72c91c3d9e1ff
- clm_b672104f8c674fb6231b51f1fdf4820d1d8d6fdfb546f748947e7a12dff25716
- clm_e0c648a2e274629352267e907dfdaaffb1b847ab05064ee71cd6d0d72e48d32d
- clm_e82f2b87b0e646cd29f287d5d63d68542d6c190229d9c0f21a1384a9a8fd2a25
- clm_fd150437a2d27656e73624d9d5998cbc985f63e55200bcb462f4ad6cfbb6d643
maturity: draft
page_id: pg_6881967b83475869966e6c40d5992e00
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fad545b25a9f593f9d8d80d1f8396593
title: ashish200729/orbiteditor/ORBIT_CODEBASE_GUIDE.md @ 6acd0c1e9ae0
updated_at: '2026-09-14T01:35:26Z'
---

# ashish200729/orbiteditor/ORBIT_CODEBASE_GUIDE.md @ 6acd0c1e9ae0

<!-- rcw:begin owner=source:src_fad545b25a9f593f9d8d80d1f8396593 block=evidence -->
- Skills are reusable instruction packs loaded on demand via a skill tool, sourced from built-in, user (~/.orbit/skills), and project (.orbit/skills) registries. [@claim:clm_0a06aad296b9046fe8f2d030107618997089cf5fc5e61b4cdca1c40c401bb1a5]
- The LLM pipeline spans chatThreadService (threads/streaming/checkpoints), convertToLLMMessageService, sendLLMMessage impl/channel, modelCapabilities, and orbitSettingsTypes. [@claim:clm_334e25b38984fe51b970be6520c331b9564a32f283547b38c3286e57e0ea24c0]
- MCP servers extend agent mode with extra tools, configured at ~/.orbit-editor/mcp.json, with a built-in orbit-ide-browser server exposing 17 tools and toggleable via browserAutomationEnabled. [@claim:clm_7c408b454ab80018c5ec9d03ceba53567f3f6a962f5354f4aa049672830e7dda]
- Most of Orbit's code lives in src/vs/workbench/contrib/orbit/, per the codebase guide and contributing doc. [@claim:clm_7e1a43cb0f6aa65928d780e7926c044503100635297dbcfdd2da5e0786e2c98c]
- Orbit snapshots file state before each user message and LLM edit, letting users restore checkpoints to roll back changes. [@claim:clm_8ffae93eac7cf6da6818754083bf8106b27c9d55ae0f439ddef72c91c3d9e1ff]
- Orbit defines three chat modes — agent, plan, normal — with a capability matrix differing in file edit, terminal, plan tools, MCP, and subagent access. [@claim:clm_b672104f8c674fb6231b51f1fdf4820d1d8d6fdfb546f748947e7a12dff25716]
- LLM messages are sent from the Electron main process, which the guide says avoids CSP issues with local providers and eases node_modules use. [@claim:clm_e0c648a2e274629352267e907dfdaaffb1b847ab05064ee71cd6d0d72e48d32d]
- Apply has two modes: Fast Apply using Search/Replace blocks and Slow Apply that rewrites the whole file; Edit tool calls and Cmd+K reuse the same Apply machinery. [@claim:clm_e82f2b87b0e646cd29f287d5d63d68542d6c190229d9c0f21a1384a9a8fd2a25]
- A subagent system lets the main agent delegate bounded tasks to isolated child agents with restricted tool policies that return structured summaries; built-ins include explore, plan, and general. [@claim:clm_fd150437a2d27656e73624d9d5998cbc985f63e55200bcb462f4ad6cfbb6d643]
<!-- rcw:end owner=source:src_fad545b25a9f593f9d8d80d1f8396593 block=evidence -->

## Researcher notes

