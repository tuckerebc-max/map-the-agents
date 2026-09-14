# hoangsonww/forge-agentic-coding-cli -- full detail

[Back to orientation](forge-agentic-coding-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hoangsonww/forge-agentic-coding-cli/50e173d938063744014a3c5d9e7a2dd10fa748b8/67f90918cac0237a.json](../../../wiki/dossiers/hoangsonww/forge-agentic-coding-cli/50e173d938063744014a3c5d9e7a2dd10fa748b8/67f90918cac0237a.json)

## specifications (1 claim(s))

- [observation/documented] Forge is described as a local-first, plan-first, multi-agent, programmable software-engineering runtime where users pick and host the model and approve actions. -- evidence: [README.md#L7-L7](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L7-L7), [README.md#L47-L47](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L47-L47) (`clm_65d310024b1462ebaa0c8110e25ee99a934ecd857d5058cd6bae4fe2f1448c16`)

## components (1 claim(s))

- [observation/documented] The architecture defines six role-typed agents (planner, architect, executor, reviewer, debugger, memory) under src/agents, plus an orchestrator and agentic loop in src/core. -- evidence: [docs/ARCHITECTURE.md#L107-L120](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L107-L120), [docs/ARCHITECTURE.md#L55-L62](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L55-L62) (`clm_e6f94952e7b83f4fcb140d791d39e84b2bafc6a83e84021d874ad5962185e2d4`)

## design-choices (1 claim(s))

- [observation/documented] Modes carry enforceable budgets: e.g. fast allows 2 executor turns and 0 validation retries, heavy 8 turns and 2 retries, plan and audit disallow mutations. -- evidence: [README.md#L197-L215](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L197-L215), [docs/ARCHITECTURE.md#L250-L259](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L250-L259) (`clm_4af778d0d79f9ab775256ce8fb6f28a4883fe8039274d2e6cf176c2755d6bcc3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: README metrics are regenerated with 'bash scripts/metrics.sh' from docs/metrics.json, and contributor setup is pointed to docs/SETUP.md. -- evidence: [README.md#L1-L1](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L1-L1), [README.md#L255-L255](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L255-L255) (`clm_c96a92398785db0486c4bf504a7c374c1dbbb57c552ae303f22c74cfc5bc52f4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Forge ships multiple surfaces: a commander-based CLI (24 commands), a raw-mode REPL, an HTTP/WebSocket dashboard, a VS Code extension, and an MCP server via 'forge mcp serve'. -- evidence: [docs/ARCHITECTURE.md#L107-L120](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L107-L120), [docs/ARCHITECTURE.md#L473-L473](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L473-L473), [docs/ARCHITECTURE.md#L43-L49](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L43-L49) (`clm_bc8985490d6e8f4272a56baac96c9f5d2b86f61906c50b9e4df03695205d5cac`)
- [observation/documented] The MCP server exposes read-only tools (forge_status, forge_plan, forge_get_task, forge_list_tasks) by default; forge_run and forge_cancel_task require opt-in via --allow-execute or FORGE_MCP_ALLOW_EXECUTE=true. -- evidence: [docs/ARCHITECTURE.md#L581-L582](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L581-L582) (`clm_b238ccaeb9ece091962f41c9909581f12b83ec25306cad19c1ad3619138d51d8`)

## memory-state (1 claim(s))

- [observation/documented] Four memory tiers are documented: hot (per-task, cleared on completion), warm (SQLite recent-task metadata), cold (lazy file/grep/AST index), and learning (patterns with confidence, read by the planner). -- evidence: [docs/ARCHITECTURE.md#L291-L299](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L291-L299) (`clm_1d0999541735061d979772aff1d713bc60892e8ef85c26e803effada0d9f7b87`)

## orchestration (2 claim(s))

- [observation/documented] The agentic loop flows classify → plan → user approval → DAG execution with a validation gate, bounded retries, and a reviewer step before completion. -- evidence: [docs/ARCHITECTURE.md#L135-L156](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L135-L156), [docs/ARCHITECTURE.md#L158-L158](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L158-L158) (`clm_3c84fa73a87579d4dd5dce64b3e027d783f59cadc6e1cefd8f63a0e78e4d5371`)
- [observation/documented] Tasks move through a state machine (draft, planned, approved, scheduled, running, verifying, completed/failed/blocked/cancelled); illegal transitions throw state_invalid and terminal states re-enter only via forge resume. -- evidence: [docs/ARCHITECTURE.md#L204-L206](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L204-L206), [docs/ARCHITECTURE.md#L193-L197](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L193-L197), [docs/ARCHITECTURE.md#L164-L165](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L164-L165) (`clm_61dc062fdff850671fd58e448e4708fe1b13c2c9ea4f35e424b1defd78eb599d`)

## tools-permissions (2 claim(s))

- [observation/documented] Every tool invocation is risk-classified; low-risk reads auto-allow, medium/high risk prompts the user, sandbox violations hard-block, and critical shell commands are blocked regardless of preferences. -- evidence: [docs/ARCHITECTURE.md#L400-L401](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L400-L401), [docs/ARCHITECTURE.md#L428-L434](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L428-L434), [docs/ARCHITECTURE.md#L409-L414](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L409-L414) (`clm_7bc3fedf368b02481be35a73a2ba9a73e56e0d47d6ccbb00ec83130d17f0038c`)
- [observation/documented] Filesystem access is realpath-resolved and confined to projectRoot plus whitelisted extra roots, with always-forbidden targets like /etc/passwd and SSH keys; grants persist in a SQLite permission_grants table. -- evidence: [docs/ARCHITECTURE.md#L428-L434](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L428-L434) (`clm_7556f6bccf835d13668ec07db1e1e09c5440f9429bf0b49c989dc47e6d349ee4`)

## evaluation (1 claim(s))

- [inference/documented] The architecture claims capability-tier floors (e.g. 7B for single-file edits, hosted frontier for refactors) are 'measured empirically', suggesting some agent-performance evaluation was done, though no eval harness appears in the evidence. -- evidence: [docs/ARCHITECTURE.md#L379-L380](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L379-L380), [docs/ARCHITECTURE.md#L382-L388](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L382-L388) (`clm_14c2ec4ca1804a02c6b60d141348d71d53b2211492427c3d4c2d9c61ba774e2b`)

## dependencies (2 claim(s))

- [observation/documented] The runtime has 13 npm dependencies with zero optional, including @modelcontextprotocol/sdk, better-sqlite3, commander, undici, ws, yaml, and zod; Node.js >= 20 is required via package.json engines. -- evidence: [README.md#L251-L251](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L251-L251), [README.md#L242-L249](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L242-L249) (`clm_7266234cbaba90fccf6c19877c2bc9a0540a89d2f0a3fa20244a275b3068f12e`)
- [observation/documented] Forge auto-detects local providers (Ollama, LM Studio, vLLM, llama.cpp) on default ports; cloud providers (Anthropic, OpenAI-compatible, etc.) are opt-in rather than required. -- evidence: [README.md#L197-L215](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L197-L215), [docs/ARCHITECTURE.md#L324-L333](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L324-L333) (`clm_151c0f049be0b8941c038e6e50f43ceb47df0a47305ac940b31f69d338b59b8f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

