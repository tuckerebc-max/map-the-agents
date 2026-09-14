---
access: public
aliases: []
claim_ids:
- clm_07b4b9eb83f4db0adc9cde9a1b14fba384b7c1c968e62db921a2bbbf02308ee2
- clm_1552526c4e8e5e77a298131e763368e071259007856cc45e197a6218319e144f
- clm_2eb2b0957915324c71e58973483be6eb5106787eb2ba93b71b177c0edf04d411
- clm_8c6443d6c17272ceb8d414daa5b61333f83c0303bbeb96740e7a8c9f2afdf923
- clm_9b92fd737eedd4215096c41eab7893509e6b7571dd6b934aebcc650c4269d4b9
- clm_bd9f650e4c3d85dd5fdb4407f0d16710d10fb56eb61c8da9556d59a8c856aeac
- clm_bfdeab3a107ce81461a8fe3fb6f78574b97e8724f8ba46b4ad8238f5699cb808
- clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6
maturity: draft
page_id: pg_fe21c1864a95561dbd76bb9a0d13d3bf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9608b604f2ee55c68f7dd4bb98cace92
title: hotovo/aider-desk/README.md @ cb7ee89bf213
updated_at: '2026-09-14T02:04:46Z'
---

# hotovo/aider-desk/README.md @ cb7ee89bf213

<!-- rcw:begin owner=source:src_9608b604f2ee55c68f7dd4bb98cace92 block=evidence -->
- A smart context and memory engine uses vector embeddings (LanceDB) and repository mapping for semantic code search, with users able to pin documentation URLs and code symbols. [@claim:clm_07b4b9eb83f4db0adc9cde9a1b14fba384b7c1c968e62db921a2bbbf02308ee2]
- Tasks can be duplicated or forked to explore alternative paths, specific messages can be deleted from chat history to curate context, and Git worktrees give each task an isolated directory with a built-in merge workflow. [@claim:clm_1552526c4e8e5e77a298131e763368e071259007856cc45e197a6218319e144f]
- The product exposes a REST API for integrating AiderDesk with external tools and workflows, per the README capabilities list. [@claim:clm_2eb2b0957915324c71e58973483be6eb5106787eb2ba93b71b177c0edf04d411]
- Reusable expertise is packaged as Skills that load on demand with progressive disclosure to keep token usage lean; users can also inject custom shell commands, linters, and test suites into the AI's toolkit. [@claim:clm_8c6443d6c17272ceb8d414daa5b61333f83c0303bbeb96740e7a8c9f2afdf923]
- Chat history, task metadata, and settings are stored locally on the user's machine in a lightweight local database, keeping workspace data private and offline. [@claim:clm_9b92fd737eedd4215096c41eab7893509e6b7571dd6b934aebcc650c4269d4b9]
- The product features tool approval gates where users approve tools and authorize destructive actions; per the ADRs, all MCP tool invocations route through the ApprovalManager. [@claim:clm_bd9f650e4c3d85dd5fdb4407f0d16710d10fb56eb61c8da9556d59a8c856aeac]
- AiderDesk can connect to standard MCP servers for scoped access to external data, and can also expose itself as an MCP server to clients like Claude Desktop or Cursor. [@claim:clm_bfdeab3a107ce81461a8fe3fb6f78574b97e8724f8ba46b4ad8238f5699cb808]
- The frontend is built with React 19 and Tailwind CSS; the agent runtime depends on the Vercel AI SDK, with MCP support via @ai-sdk/mcp and @modelcontextprotocol/sdk. [@claim:clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6]
<!-- rcw:end owner=source:src_9608b604f2ee55c68f7dd4bb98cace92 block=evidence -->

## Researcher notes

