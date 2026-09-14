# hoangsonww/forge-agentic-coding-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 50e173d93806 @ 67f90918cac0237a

## Summary (orientation draft, not independently verified)

Forge is a local-first, plan-first multi-agent coding CLI runtime (TypeScript/Node 20+) with six role-typed agents, a task state machine, permission/sandbox model, four memory tiers, and multiple surfaces (CLI, REPL, dashboard, VS Code extension, MCP server). Evidence is documentation-heavy; no source code slices are present. Evidence coverage: 141 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Forge is described as a local-first, plan-first, multi-agent, programmable software-engineering runtime where users pick and host the model and approve actions. -- evidence: [README.md#L7-L7](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L7-L7), [README.md#L47-L47](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L47-L47)
- components (1 claim(s)):
  - [observation/documented] The architecture defines six role-typed agents (planner, architect, executor, reviewer, debugger, memory) under src/agents, plus an orchestrator and agentic loop in src/core. -- evidence: [docs/ARCHITECTURE.md#L107-L120](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L107-L120), [docs/ARCHITECTURE.md#L55-L62](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L55-L62)
- design-choices (1 claim(s)):
  - [observation/documented] Modes carry enforceable budgets: e.g. fast allows 2 executor turns and 0 validation retries, heavy 8 turns and 2 retries, plan and audit disallow mutations. -- evidence: [README.md#L197-L215](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L197-L215), [docs/ARCHITECTURE.md#L250-L259](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L250-L259)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: README metrics are regenerated with 'bash scripts/metrics.sh' from docs/metrics.json, and contributor setup is pointed to docs/SETUP.md. -- evidence: [README.md#L1-L1](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L1-L1), [README.md#L255-L255](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/README.md#L255-L255)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Forge ships multiple surfaces: a commander-based CLI (24 commands), a raw-mode REPL, an HTTP/WebSocket dashboard, a VS Code extension, and an MCP server via 'forge mcp serve'. -- evidence: [docs/ARCHITECTURE.md#L107-L120](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L107-L120), [docs/ARCHITECTURE.md#L473-L473](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L473-L473), [docs/ARCHITECTURE.md#L43-L49](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L43-L49)
  - [observation/documented] The MCP server exposes read-only tools (forge_status, forge_plan, forge_get_task, forge_list_tasks) by default; forge_run and forge_cancel_task require opt-in via --allow-execute or FORGE_MCP_ALLOW_EXECUTE=true. -- evidence: [docs/ARCHITECTURE.md#L581-L582](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L581-L582)
- memory-state (1 claim(s)):
  - [observation/documented] Four memory tiers are documented: hot (per-task, cleared on completion), warm (SQLite recent-task metadata), cold (lazy file/grep/AST index), and learning (patterns with confidence, read by the planner). -- evidence: [docs/ARCHITECTURE.md#L291-L299](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L291-L299)
- orchestration (2 claim(s)):
  - [observation/documented] The agentic loop flows classify → plan → user approval → DAG execution with a validation gate, bounded retries, and a reviewer step before completion. -- evidence: [docs/ARCHITECTURE.md#L135-L156](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L135-L156), [docs/ARCHITECTURE.md#L158-L158](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L158-L158)
  - [observation/documented] Tasks move through a state machine (draft, planned, approved, scheduled, running, verifying, completed/failed/blocked/cancelled); illegal transitions throw state_invalid and terminal states re-enter only via forge resume. -- evidence: [docs/ARCHITECTURE.md#L204-L206](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L204-L206), [docs/ARCHITECTURE.md#L193-L197](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L193-L197), [docs/ARCHITECTURE.md#L164-L165](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L164-L165)
- tools-permissions (2 claim(s)):
  - [observation/documented] Every tool invocation is risk-classified; low-risk reads auto-allow, medium/high risk prompts the user, sandbox violations hard-block, and critical shell commands are blocked regardless of preferences. -- evidence: [docs/ARCHITECTURE.md#L400-L401](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L400-L401), [docs/ARCHITECTURE.md#L428-L434](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L428-L434), [docs/ARCHITECTURE.md#L409-L414](https://github.com/hoangsonww/Forge-Agentic-Coding-CLI/blob/50e173d938063744014a3c5d9e7a2dd10fa748b8/docs/ARCHITECTURE.md#L409-L414)
More evidence: [full detail](forge-agentic-coding-cli.detail.md)

Metadata and full claim list: [full detail](forge-agentic-coding-cli.detail.md)
Human notes ([notes](forge-agentic-coding-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
