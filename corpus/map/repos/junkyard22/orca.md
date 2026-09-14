# junkyard22/orca

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 115d36b6cf51 @ 91cfee230c8891fa

## Summary (orientation draft, not independently verified)

Selected evidence records: The runtime is organized as packages: benson-core (intent parsing), orca-core (runtime, event bus, SQLite persistence), maestro-core (role routing), pappy-core (QC verdicts), miranda-core (compliance gate), workbench-core (tool execution), and dewey-core (context store). The pipeline routes user input through Benson (intent parsing) to an Orca Runtime that orchestrates Maestro role routing, Pappy QC (PASS/WARN/FAIL), and Miranda compliance with a repair loop.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The runtime is organized as packages: benson-core (intent parsing), orca-core (runtime, event bus, SQLite persistence), maestro-core (role routing), pappy-core (QC verdicts), miranda-core (compliance gate), workbench-core (tool execution), and dewey-core (context store). -- evidence: [ARCHITECTURE.md#L32-L45](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L32-L45), [README.md#L88-L95](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L88-L95)
- design-choices (1 claim(s)):
  - [observation/documented] Roles include brain (decompose/route), strong_model, cheap_model, reviewer, narrator, planner_deep, debugger, reader, and vision; several roles are optional with documented fallbacks (e.g. planner_deep falls back to brain). -- evidence: [ARCHITECTURE.md#L11-L28](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L11-L28)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: ARCHITECTURE.md directs contributors to run a contract-check checklist before coding tasks touching orchestration, LLM paths, gates, QC, or role contracts, and mandates that agent-loop changes go only in packages/agent-loop-core. -- evidence: [ARCHITECTURE.md#L3-L7](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L3-L7), [ARCHITECTURE.md#L150-L157](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L150-L157)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] MCP servers are declared in orca-settings.json under mcpServers[] with stdio transport; by default each server's tools are namespaced with a ${id}_ prefix to avoid collisions. -- evidence: [ARCHITECTURE.md#L120-L120](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L120-L120), [ARCHITECTURE.md#L114-L116](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L114-L116), [ARCHITECTURE.md#L174-L175](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L174-L175)
  - [observation/documented] The desktop composer's Cargo tray accepts /repo, /file, /task, /connect, /context, /status commands plus @repo/@file/@task/@connector references, storing resources as typed references rather than raw contents. -- evidence: [ARCHITECTURE.md#L56-L59](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L56-L59), [README.md#L37-L42](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L37-L42), [ARCHITECTURE.md#L63-L73](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L63-L73)
- memory-state (1 claim(s)):
  - [observation/documented] Dewey persists a session-independent typed ContextManifest in ~/.orca/userContext.json storing resource locators and labels, never raw file or connector contents; raw contents load only via explicitly permitted tool calls. -- evidence: [ARCHITECTURE.md#L63-L73](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L63-L73), [ARCHITECTURE.md#L75-L77](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L75-L77)
- orchestration (1 claim(s)):
  - [observation/documented] The pipeline routes user input through Benson (intent parsing) to an Orca Runtime that orchestrates Maestro role routing, Pappy QC (PASS/WARN/FAIL), and Miranda compliance with a repair loop. -- evidence: [README.md#L7-L23](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L7-L23), [ARCHITECTURE.md#L11-L28](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L11-L28)
- tools-permissions (3 claim(s)):
  - [observation/documented] Role tool access is capability-scoped: tools resolve into named groups (filesystem-read/write, shell, github-read/write, web, documentation), and unclassifiable tool names are excluded from every role with no allow-by-default fallback. -- evidence: [ARCHITECTURE.md#L179-L182](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L179-L182), [ARCHITECTURE.md#L184-L193](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L184-L193)
More evidence: [full detail](orca.detail.md)

Metadata and full claim list: [full detail](orca.detail.md)
Human notes ([notes](orca.notes.md), never overwritten by build)

[Back to map index](../../index.md)
