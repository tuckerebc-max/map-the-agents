# gabrielmaialva33/winx-code-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a48e7a9f7e86 @ 3dc3feafd9c47b9c

## Summary (orientation draft, not independently verified)

Winx is a Rust MCP runtime (MCP 2026-07-28) offering durable PTY shell sessions, guarded file editing, and repository navigation over Streamable HTTP and stdio, with a Unix daemon architecture (winxd + per-session winx-guardian). Evidence is README-only documentation. Evidence coverage: 133 of 339 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] On Unix, the MCP adapter is separated from PTY-owning processes: winxd manages the control plane and one winx-guardian per session keeps shells alive across disconnects and adapter upgrades. -- evidence: [README.md#L40-L44](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L40-L44), [README.md#L325-L328](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L325-L328)
- design-choices (1 claim(s)):
  - [observation/documented] The SEARCH/REPLACE matcher tolerates model mistakes: indentation adjustment, smart-quote normalization, line-number stripping, neighbor-block disambiguation, and one retry on over-escaped quotes, while refusing heavily fuzzy matches. -- evidence: [README.md#L300-L314](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L300-L314)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Winx is a remote-first MCP runtime exposing a Streamable HTTP endpoint at /mcp (default 127.0.0.1:8000) plus a stdio transport for local clients like Claude Code, Cursor, and VS Code. -- evidence: [README.md#L100-L103](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L100-L103), [README.md#L35-L38](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L35-L38), [README.md#L692-L693](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L692-L693)
  - [observation/documented] The single mutation tool EditFiles supports replace, SEARCH/REPLACE, revision-bound line patches, atomic batches, verification, and undo, with legacy edit names kept as hidden compatibility aliases. -- evidence: [README.md#L234-L239](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L234-L239), [README.md#L195-L197](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L195-L197), [README.md#L82-L96](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L82-L96)
- memory-state (1 claim(s)):
  - [observation/documented] Durable sessions survive HTTP disconnects: guardians are capped at 32 by default with tiered idle retention (30 minutes never-used, 24 hours used), and active commands are never evicted. -- evidence: [README.md#L643-L647](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L643-L647)
- orchestration (1 claim(s)):
  - [observation/documented] MCP Tasks on BashCommand are capability-driven: adaptive promotes only after runtime state is running, until_complete creates a Task immediately, and return_early never does; cancellation is generation-bound with a fail-closed fallback. -- evidence: [README.md#L268-L280](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L268-L280)
- tools-permissions (3 claim(s)):
  - [observation/documented] Workspaces have three modes: wcgw (full access), architect (read-only), and code_writer (command allowlist plus write globs), with the allowlist parsed via tree-sitter to check every command including pipelines and substitutions. -- evidence: [README.md#L137-L191](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L137-L191)
  - [observation/documented] Tool catalogs are profiled as terminal (2 tools), read-only (4), coding (5), and full (7), or an exact per-principal allowlist; policy is enforced at both discovery and dispatch. -- evidence: [README.md#L219-L220](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L219-L220), [README.md#L204-L209](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L204-L209), [README.md#L199-L202](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L199-L202)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](winx-code-agent.detail.md)

Metadata and full claim list: [full detail](winx-code-agent.detail.md)
Human notes ([notes](winx-code-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
