# pirua-game/ai_game_base_analysis_cli_mcp_tool -- full detail

[Back to orientation](ai_game_base_analysis_cli_mcp_tool.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/088bd704/b10215ab/736979b30879d4c4442262aa951fdf6b53cd001c/68f8ae5cfc92e112.json](../../../wiki/dossiers/088bd704/b10215ab/736979b30879d4c4442262aa951fdf6b53cd001c/68f8ae5cfc92e112.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] gdep includes a browser-based web UI with dependency graphs, call-flow visualization, a class browser with impact analysis and lint, an AI chat agent with tool-calling, and engine-specific explorers (GAS, Blueprint mapping, Animator, BehaviorTree, StateTree). -- evidence: [README.md#L204-L208](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L204-L208) (`clm_c1fe6bb464e9faa697b294f48e04b1f6f3f21f7db86fb433852fa3d91e185471`)
- [observation/documented] A C# parser ships as a single OS-agnostic DLL (gdep.dll), located via the $GDEP_DLL env var, then publish_dll/gdep.dll, publish/gdep.dll, and a legacy binary path. -- evidence: [README.md#L394-L394](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L394-L394), [README.md#L400-L400](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L400-L400) (`clm_86a648a1935ef2e5f4a1318fdae49dd7bf680a28f5a913d249cde6e17651c44b`)

## design-choices (2 claim(s))

- [observation/documented] UE5 analysis responses (analyze_ue5_gas, analyze_ue5_blueprint_mapping) begin with a transparency header reporting analysis method, a HIGH/MEDIUM/LOW confidence tier, asset coverage, and validated UE version. -- evidence: [README.md#L129-L134](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L129-L134), [README.md#L127-L127](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L127-L127) (`clm_92f5c67975dd037e56aed2b4ebd8d7dd6072a38c61c27db991ee15c8f949cd41`)
- [observation/documented] gdep init generates a .gdep/AGENTS.md file instructing AI agents how to treat results by confidence tier (HIGH trust fully, MEDIUM reliable, LOW verify source). -- evidence: [README.md#L136-L136](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L136-L136) (`clm_a3755f418d1dc114ccb868cbdb82891dfa00f19ed110f5c3ec1759fcb6320c42`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] gdep provides a CLI with commands including detect, scan, describe, flow, impact, method-impact, path, test-scope, watch, lint, advise, graph, diff, init, context, hints, and config. -- evidence: [README.md#L218-L236](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L218-L236) (`clm_4a99e8228e5c5222026bc9a8770a0f2c75f732b34f78d9ee242b698c845bfc70`)
- [observation/documented] The product ships an MCP server exposing 30 game-engine-aware tools (e.g. get_project_context, wiki_search, analyze_impact_and_risk, trace_gameplay_flow) for Claude Desktop, Cursor, and other MCP-compatible agents. -- evidence: [README.md#L43-L43](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L43-L43), [README.md#L75-L106](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L75-L106), [README.md#L64-L64](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L64-L64) (`clm_e27565b53f7a6f28de366569de8f7030f1c31eef70dce44e58c05597c25048ea`)
- [observation/documented] The MCP server is configured via an mcpServers JSON entry running the gdep-mcp command with a PYTHONUTF8=1 environment variable. -- evidence: [README.md#L53-L62](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L53-L62) (`clm_f55457fc6be982865885ccbecaee358ae6cc17304dec73c7fd13953746a10011`)
- [observation/documented] The find_call_path MCP tool (shortest call path between two methods) is documented as C#/Unity only, and Axmol analysis uses Tree-sitter with no back-reference support. -- evidence: [README.md#L331-L337](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L331-L337), [README_JA.md#L73-L104](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README_JA.md#L73-L104) (`clm_3d440b3068c552f2947e47b3daf49dbafe85144989ebc57635c01e3be3aa00fd`)

## memory-state (1 claim(s))

- [observation/documented] Analysis results are cached in .gdep/wiki/ and indexed in SQLite with FTS5 full-text search (BM25 ranking, CamelCase-aware), with staleness detection flagging nodes whose source files changed since analysis. -- evidence: [README.md#L119-L123](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L119-L123), [README.md#L110-L111](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L110-L111) (`clm_349169a5a1bf50c133ca4b35b4a9204b6a7479206587a4425ab1640129ee2ac3`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Documented benchmarks report UE5 warm scan 0.46s on a 2,800+ asset project, Unity warm scan 0.49s on 900+ classes, 28.5 MB peak memory, and 5/5 (100%) MCP accuracy on code-based facts. -- evidence: [README.md#L30-L35](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L30-L35) (`clm_3ce0e47dd862de0b30ddf198015a13caa174810e790a46bd91fa163a5835fd99`)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Python 3.11+ for the CLI and MCP server, and .NET Runtime 8.0+ for C#/Unity project analysis. -- evidence: [README.md#L146-L149](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L146-L149) (`clm_926e0a626ff0cd1a10fb611e2d210041a84e74a4337a71f8c7871a7f87a3fa3c`)

## limitations (2 claim(s))

- [observation/documented] The web UI supports only English and Korean, supports Ollama as local LLM, and is described as a non-commercial tool whose features may not be perfect. -- evidence: [README.md#L210-L210](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L210-L210) (`clm_b69057892fbbf24ae67feca5d2d0b6cd197ff38c55ea54623d3de3cafe053b2e`)
- [observation/documented] The lint command implements 19 game-engine anti-pattern rules across Unity, UE5, Axmol, and common architecture checks; --fix is a dry-run that suggests fixes without changing files. -- evidence: [README.md#L305-L325](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L305-L325), [README.md#L300-L303](https://github.com/pirua-game/ai_game_base_analysis_cli_mcp_tool/blob/736979b30879d4c4442262aa951fdf6b53cd001c/README.md#L300-L303) (`clm_1625aa059738f74368ab929e843399c63fceda0261bb2aa3021d5bb43803291c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

