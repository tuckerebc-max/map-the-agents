---
access: public
aliases: []
claim_ids:
- clm_060003b334feee4cddf876978ffc53b64a5dacca9898cd2aef0df35b2cddc67b
- clm_0eb584d15c32d9fff22c924f023a6f20b4292f4de364a71bdf55a90e8740cde6
- clm_30d3b35379f60d8f0917647627dcfc8073b0a1728cb175477537cf0a191f75df
- clm_b3edc6e7356fbf196323c375ff47fe6508351c9179b362c1d562d50b700d7cba
- clm_e774cb2c29cd89db77b6cabfb3c6b2e48ad61363f1387f8db0c26747d047eb6f
maturity: draft
page_id: pg_debe52a8838a53688fa2e8dc9167d446
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9dc02ab6ad355f8394ccf0310fcb90be
title: 2389-research/claude-plugins/docs/index.md @ 017d34612ebf
updated_at: '2026-09-14T03:28:23Z'
---

# 2389-research/claude-plugins/docs/index.md @ 017d34612ebf

<!-- rcw:begin owner=source:src_9dc02ab6ad355f8394ccf0310fcb90be block=evidence -->
- The thrifty plugin is documented as benchmarked at roughly 64% lower cost than Opus at equal quality, suggesting some agent-performance evaluation exists, though no eval harness appears in the evidence. [@claim:clm_060003b334feee4cddf876978ffc53b64a5dacca9898cd2aef0df35b2cddc67b]
- The binary-re plugin relies on radare2, Ghidra, GDB, and QEMU for hypothesis-driven ELF analysis across ARM64, ARMv7, and x86_64. [@claim:clm_0eb584d15c32d9fff22c924f023a6f20b4292f4de364a71bdf55a90e8740cde6]
- Plugins can be installed in any agent (Claude Code, Cursor, Codex) via vercel-labs/skills using 'npx skills add 2389-research/<plugin>'. [@claim:clm_30d3b35379f60d8f0917647627dcfc8073b0a1728cb175477537cf0a191f75df]
- The speed-run plugin uses a hosted LLM (Cerebras) for token-efficient parallel code generation, claiming about 60% token savings, and includes an MCP server. [@claim:clm_b3edc6e7356fbf196323c375ff47fe6508351c9179b362c1d562d50b700d7cba]
- The catalog includes plugins such as simmer (iterative refinement with investigation-first judges), test-kitchen (parallel implementation exploration), thrifty (tiered Sonnet/Haiku delegation), and binary-re (ELF reverse engineering). [@claim:clm_e774cb2c29cd89db77b6cabfb3c6b2e48ad61363f1387f8db0c26747d047eb6f]
<!-- rcw:end owner=source:src_9dc02ab6ad355f8394ccf0310fcb90be block=evidence -->

## Researcher notes

