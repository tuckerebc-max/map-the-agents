# pirua-game/ai_game_base_analysis_cli_mcp_tool

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 736979b30879 @ 68f8ae5cfc92e112

## Summary (orientation draft, not independently verified)

The evidence consists of README documentation (English, Japanese, Korean) for gdep, a game-codebase analysis CLI with an MCP server, web UI, and C# parser DLL. Claims below are documentation-based product descriptions. Evidence coverage: 170 of 349 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] gdep includes a browser-based web UI with dependency graphs, call-flow visualization, a class browser with impact analysis and lint, an AI chat agent with tool-calling, and engine-specific explorers (GAS, Blueprint mapping, Animator, BehaviorTree, StateTree). -- evidence: [README.md#L204-L208](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L204-L208)
  - [observation/documented] A C# parser ships as a single OS-agnostic DLL (gdep.dll), located via the $GDEP_DLL env var, then publish_dll/gdep.dll, publish/gdep.dll, and a legacy binary path. -- evidence: [README.md#L394-L394](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L394-L394), [README.md#L400-L400](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L400-L400)
- design-choices (2 claim(s)):
  - [observation/documented] UE5 analysis responses (analyze_ue5_gas, analyze_ue5_blueprint_mapping) begin with a transparency header reporting analysis method, a HIGH/MEDIUM/LOW confidence tier, asset coverage, and validated UE version. -- evidence: [README.md#L129-L134](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L129-L134), [README.md#L127-L127](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L127-L127)
  - [observation/documented] gdep init generates a .gdep/AGENTS.md file instructing AI agents how to treat results by confidence tier (HIGH trust fully, MEDIUM reliable, LOW verify source). -- evidence: [README.md#L136-L136](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L136-L136)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] gdep provides a CLI with commands including detect, scan, describe, flow, impact, method-impact, path, test-scope, watch, lint, advise, graph, diff, init, context, hints, and config. -- evidence: [README.md#L218-L236](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L218-L236)
  - [observation/documented] The product ships an MCP server exposing 30 game-engine-aware tools (e.g. get_project_context, wiki_search, analyze_impact_and_risk, trace_gameplay_flow) for Claude Desktop, Cursor, and other MCP-compatible agents. -- evidence: [README.md#L43-L43](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L43-L43), [README.md#L75-L106](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L75-L106), [README.md#L64-L64](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L64-L64)
- memory-state (1 claim(s)):
  - [observation/documented] Analysis results are cached in .gdep/wiki/ and indexed in SQLite with FTS5 full-text search (BM25 ranking, CamelCase-aware), with staleness detection flagging nodes whose source files changed since analysis. -- evidence: [README.md#L119-L123](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L119-L123), [README.md#L110-L111](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L110-L111)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Documented benchmarks report UE5 warm scan 0.46s on a 2,800+ asset project, Unity warm scan 0.49s on 900+ classes, 28.5 MB peak memory, and 5/5 (100%) MCP accuracy on code-based facts. -- evidence: [README.md#L30-L35](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L30-L35)
- dependencies (1 claim(s)):
More evidence: [full detail](ai_game_base_analysis_cli_mcp_tool.detail.md)

Metadata and full claim list: [full detail](ai_game_base_analysis_cli_mcp_tool.detail.md)
Human notes ([notes](ai_game_base_analysis_cli_mcp_tool.notes.md), never overwritten by build)

[Back to map index](../../index.md)
