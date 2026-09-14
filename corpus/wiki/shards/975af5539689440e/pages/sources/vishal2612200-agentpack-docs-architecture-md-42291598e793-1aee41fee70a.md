---
access: public
aliases: []
claim_ids:
- clm_31a43498fcc175add0626d3b0ef99e249e6a755dd4dd2caeb270755320d7adc5
- clm_4a0658aa6790e099b39e55a1973d2d0082225b27bf4bdaffb309fb0fe08ee30e
- clm_86ffd3cc21d7e346af668407533985f08d124640693d211af44f8ce51a352949
- clm_d116c0cf96861979462133c2f4327d28977f0d3c53fd629c4727657b85bb339d
- clm_fbe419f399197dcb2bf30310a246f3c4f107f3b0e4b7b47405025bae25d03ec4
maturity: draft
page_id: pg_2baff3e932b15aff80831aee41fee70a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_726435eba8ae58038bb664f838d3c28f
title: vishal2612200/agentpack/docs/architecture.md @ 42291598e793
updated_at: '2026-09-14T04:30:29Z'
---

# vishal2612200/agentpack/docs/architecture.md @ 42291598e793

<!-- rcw:begin owner=source:src_726435eba8ae58038bb664f838d3c28f block=evidence -->
- Sessions are thread-scoped by default: when host session/thread environment variables are present, commands and MCP tools use isolated state under .agentpack/threads/<id>/, with --thread global as a legacy opt-out. [@claim:clm_31a43498fcc175add0626d3b0ef99e249e6a755dd4dd2caeb270755320d7adc5]
- Adapters render agent-specific context files (Claude, Cursor, Windsurf, Codex, Antigravity, generic), while separate installers configure each tool's repo files such as CLAUDE.md, .cursorrules, and AGENTS.md. [@claim:clm_4a0658aa6790e099b39e55a1973d2d0082225b27bf4bdaffb309fb0fe08ee30e]
- Generated context, receipts, task state, snapshots, and memory are stored locally under .agentpack/, and summary caches are keyed by file hash so only changed files are re-summarized. [@claim:clm_86ffd3cc21d7e346af668407533985f08d124640693d211af44f8ce51a352949]
- The architecture is a local pipeline: scan with .agentignore, build offline summaries and a Tree-sitter semantic graph, score files for the task, select by value per token, redact secrets at materialization, and cache a pack registry with block IDs. [@claim:clm_d116c0cf96861979462133c2f4327d28977f0d3c53fd629c4727657b85bb339d]
- The MCP server exposes tools including start_task, pack_context, get_context, explain, related, stats, and delta, per the package layout documentation. [@claim:clm_fbe419f399197dcb2bf30310a246f3c4f107f3b0e4b7b47405025bae25d03ec4]
<!-- rcw:end owner=source:src_726435eba8ae58038bb664f838d3c28f block=evidence -->

## Researcher notes

