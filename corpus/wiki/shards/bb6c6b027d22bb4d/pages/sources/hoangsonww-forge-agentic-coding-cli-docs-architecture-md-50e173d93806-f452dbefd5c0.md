---
access: public
aliases: []
claim_ids:
- clm_14c2ec4ca1804a02c6b60d141348d71d53b2211492427c3d4c2d9c61ba774e2b
- clm_151c0f049be0b8941c038e6e50f43ceb47df0a47305ac940b31f69d338b59b8f
- clm_1d0999541735061d979772aff1d713bc60892e8ef85c26e803effada0d9f7b87
- clm_3c84fa73a87579d4dd5dce64b3e027d783f59cadc6e1cefd8f63a0e78e4d5371
- clm_4af778d0d79f9ab775256ce8fb6f28a4883fe8039274d2e6cf176c2755d6bcc3
- clm_61dc062fdff850671fd58e448e4708fe1b13c2c9ea4f35e424b1defd78eb599d
- clm_7556f6bccf835d13668ec07db1e1e09c5440f9429bf0b49c989dc47e6d349ee4
- clm_7bc3fedf368b02481be35a73a2ba9a73e56e0d47d6ccbb00ec83130d17f0038c
- clm_b238ccaeb9ece091962f41c9909581f12b83ec25306cad19c1ad3619138d51d8
- clm_bc8985490d6e8f4272a56baac96c9f5d2b86f61906c50b9e4df03695205d5cac
- clm_e6f94952e7b83f4fcb140d791d39e84b2bafc6a83e84021d874ad5962185e2d4
maturity: draft
page_id: pg_74f27b35b72d59e9938af452dbefd5c0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c986852811ef5211a8516914c424402b
title: hoangsonww/Forge-Agentic-Coding-CLI/docs/ARCHITECTURE.md @ 50e173d93806
updated_at: '2026-09-14T02:03:25Z'
---

# hoangsonww/Forge-Agentic-Coding-CLI/docs/ARCHITECTURE.md @ 50e173d93806

<!-- rcw:begin owner=source:src_c986852811ef5211a8516914c424402b block=evidence -->
- The architecture claims capability-tier floors (e.g. 7B for single-file edits, hosted frontier for refactors) are 'measured empirically', suggesting some agent-performance evaluation was done, though no eval harness appears in the evidence. [@claim:clm_14c2ec4ca1804a02c6b60d141348d71d53b2211492427c3d4c2d9c61ba774e2b]
- Forge auto-detects local providers (Ollama, LM Studio, vLLM, llama.cpp) on default ports; cloud providers (Anthropic, OpenAI-compatible, etc.) are opt-in rather than required. [@claim:clm_151c0f049be0b8941c038e6e50f43ceb47df0a47305ac940b31f69d338b59b8f]
- Four memory tiers are documented: hot (per-task, cleared on completion), warm (SQLite recent-task metadata), cold (lazy file/grep/AST index), and learning (patterns with confidence, read by the planner). [@claim:clm_1d0999541735061d979772aff1d713bc60892e8ef85c26e803effada0d9f7b87]
- The agentic loop flows classify → plan → user approval → DAG execution with a validation gate, bounded retries, and a reviewer step before completion. [@claim:clm_3c84fa73a87579d4dd5dce64b3e027d783f59cadc6e1cefd8f63a0e78e4d5371]
- Modes carry enforceable budgets: e.g. fast allows 2 executor turns and 0 validation retries, heavy 8 turns and 2 retries, plan and audit disallow mutations. [@claim:clm_4af778d0d79f9ab775256ce8fb6f28a4883fe8039274d2e6cf176c2755d6bcc3]
- Tasks move through a state machine (draft, planned, approved, scheduled, running, verifying, completed/failed/blocked/cancelled); illegal transitions throw state_invalid and terminal states re-enter only via forge resume. [@claim:clm_61dc062fdff850671fd58e448e4708fe1b13c2c9ea4f35e424b1defd78eb599d]
- Filesystem access is realpath-resolved and confined to projectRoot plus whitelisted extra roots, with always-forbidden targets like /etc/passwd and SSH keys; grants persist in a SQLite permission_grants table. [@claim:clm_7556f6bccf835d13668ec07db1e1e09c5440f9429bf0b49c989dc47e6d349ee4]
- Every tool invocation is risk-classified; low-risk reads auto-allow, medium/high risk prompts the user, sandbox violations hard-block, and critical shell commands are blocked regardless of preferences. [@claim:clm_7bc3fedf368b02481be35a73a2ba9a73e56e0d47d6ccbb00ec83130d17f0038c]
- The MCP server exposes read-only tools (forge_status, forge_plan, forge_get_task, forge_list_tasks) by default; forge_run and forge_cancel_task require opt-in via --allow-execute or FORGE_MCP_ALLOW_EXECUTE=true. [@claim:clm_b238ccaeb9ece091962f41c9909581f12b83ec25306cad19c1ad3619138d51d8]
- Forge ships multiple surfaces: a commander-based CLI (24 commands), a raw-mode REPL, an HTTP/WebSocket dashboard, a VS Code extension, and an MCP server via 'forge mcp serve'. [@claim:clm_bc8985490d6e8f4272a56baac96c9f5d2b86f61906c50b9e4df03695205d5cac]
- The architecture defines six role-typed agents (planner, architect, executor, reviewer, debugger, memory) under src/agents, plus an orchestrator and agentic loop in src/core. [@claim:clm_e6f94952e7b83f4fcb140d791d39e84b2bafc6a83e84021d874ad5962185e2d4]
<!-- rcw:end owner=source:src_c986852811ef5211a8516914c424402b block=evidence -->

## Researcher notes

