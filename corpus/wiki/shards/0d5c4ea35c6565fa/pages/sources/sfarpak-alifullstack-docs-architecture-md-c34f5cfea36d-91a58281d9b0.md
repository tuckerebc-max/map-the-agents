---
access: public
aliases: []
claim_ids:
- clm_49a0589fea1c5337f79148f7c5f3bac3fc0f43cbcfd76179ea3c05b4f73437c8
- clm_abd49e09e6341098acb9293f5aa4af67e54811ca7eb79a95dc4e2e80e7614579
- clm_c20989b80e2b6f41b85e74cd7411d5620889402f272d8349028797a08938afbc
- clm_ca9f5f9f2c87b2eb058e09776795403a329eec0ba07805a5d6d3d36977116a0f
- clm_dbc9c924f27f4bea7ee61cfecf0978cba724dc9d2b9fe2f474a8200c0be24ef1
- clm_eea60684e3ef061c2f2b2f4e4dc2ee6cf431226acdc5b21ab9d5cc3e29a67920
maturity: draft
page_id: pg_aab2639267da52fead4591a58281d9b0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c753d63e5cea570eac7b3b89ae74132d
title: SFARPak/AliFullStack/docs/architecture.md @ c34f5cfea36d
updated_at: '2026-09-14T03:12:51Z'
---

# SFARPak/AliFullStack/docs/architecture.md @ c34f5cfea36d

<!-- rcw:begin owner=source:src_c753d63e5cea570eac7b3b89ae74132d block=evidence -->
- By default each LLM request includes the entire codebase as context; a Smart Context feature uses smaller models to filter important files, and agentic codebase search is avoided for cost reasons. [@claim:clm_49a0589fea1c5337f79148f7c5f3bac3fc0f43cbcfd76179ea3c05b4f73437c8]
- The system prompt instructs the LLM to respond using XML-like tags such as <alifullstack-write>, which a specialized Markdown parser renders in the UI and a response processor executes. [@claim:clm_abd49e09e6341098acb9293f5aa4af67e54811ca7eb79a95dc4e2e80e7614579]
- The architecture doc acknowledges AliFullStack is less agentic than tools like Cursor, which plan, search codebases, run linters/tests, and auto-fix code. [@claim:clm_c20989b80e2b6f41b85e74cd7411d5620889402f272d8349028797a08938afbc]
- The project deliberately simulates tool calling with XML-like tags instead of native function calling, citing support for many simultaneous calls and evidence that JSON-embedded code degrades quality. [@claim:clm_ca9f5f9f2c87b2eb058e09776795403a329eec0ba07805a5d6d3d36977116a0f]
- AliFullStack is an Electron desktop app with a sandboxed renderer process for the React UI and a privileged Node.js main process, communicating via IPC. [@claim:clm_dbc9c924f27f4bea7ee61cfecf0978cba724dc9d2b9fe2f474a8200c0be24ef1]
- The agentic loop is intentionally simple: typically a single LLM request per user prompt, with optional TypeScript auto-fix, avoiding complex multi-step agent workflows to control cost. [@claim:clm_eea60684e3ef061c2f2b2f4e4dc2ee6cf431226acdc5b21ab9d5cc3e29a67920]
<!-- rcw:end owner=source:src_c753d63e5cea570eac7b3b89ae74132d block=evidence -->

## Researcher notes

