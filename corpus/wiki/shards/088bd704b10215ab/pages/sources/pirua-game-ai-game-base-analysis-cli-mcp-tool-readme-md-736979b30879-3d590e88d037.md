---
access: public
aliases: []
claim_ids:
- clm_1625aa059738f74368ab929e843399c63fceda0261bb2aa3021d5bb43803291c
- clm_349169a5a1bf50c133ca4b35b4a9204b6a7479206587a4425ab1640129ee2ac3
- clm_3ce0e47dd862de0b30ddf198015a13caa174810e790a46bd91fa163a5835fd99
- clm_3d440b3068c552f2947e47b3daf49dbafe85144989ebc57635c01e3be3aa00fd
- clm_4a99e8228e5c5222026bc9a8770a0f2c75f732b34f78d9ee242b698c845bfc70
- clm_86a648a1935ef2e5f4a1318fdae49dd7bf680a28f5a913d249cde6e17651c44b
- clm_926e0a626ff0cd1a10fb611e2d210041a84e74a4337a71f8c7871a7f87a3fa3c
- clm_92f5c67975dd037e56aed2b4ebd8d7dd6072a38c61c27db991ee15c8f949cd41
- clm_a3755f418d1dc114ccb868cbdb82891dfa00f19ed110f5c3ec1759fcb6320c42
- clm_b69057892fbbf24ae67feca5d2d0b6cd197ff38c55ea54623d3de3cafe053b2e
- clm_c1fe6bb464e9faa697b294f48e04b1f6f3f21f7db86fb433852fa3d91e185471
- clm_e27565b53f7a6f28de366569de8f7030f1c31eef70dce44e58c05597c25048ea
- clm_f55457fc6be982865885ccbecaee358ae6cc17304dec73c7fd13953746a10011
maturity: draft
page_id: pg_b3bc563c93935c71bb513d590e88d037
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_320a23ce2cfa599bb2774acb1d91378c
title: pirua-game/ai_game_base_analysis_cli_mcp_tool/README.md @ 736979b30879
updated_at: '2026-09-14T04:16:16Z'
---

# pirua-game/ai_game_base_analysis_cli_mcp_tool/README.md @ 736979b30879

<!-- rcw:begin owner=source:src_320a23ce2cfa599bb2774acb1d91378c block=evidence -->
- The lint command implements 19 game-engine anti-pattern rules across Unity, UE5, Axmol, and common architecture checks; --fix is a dry-run that suggests fixes without changing files. [@claim:clm_1625aa059738f74368ab929e843399c63fceda0261bb2aa3021d5bb43803291c]
- Analysis results are cached in .gdep/wiki/ and indexed in SQLite with FTS5 full-text search (BM25 ranking, CamelCase-aware), with staleness detection flagging nodes whose source files changed since analysis. [@claim:clm_349169a5a1bf50c133ca4b35b4a9204b6a7479206587a4425ab1640129ee2ac3]
- Documented benchmarks report UE5 warm scan 0.46s on a 2,800+ asset project, Unity warm scan 0.49s on 900+ classes, 28.5 MB peak memory, and 5/5 (100%) MCP accuracy on code-based facts. [@claim:clm_3ce0e47dd862de0b30ddf198015a13caa174810e790a46bd91fa163a5835fd99]
- The find_call_path MCP tool (shortest call path between two methods) is documented as C#/Unity only, and Axmol analysis uses Tree-sitter with no back-reference support. [@claim:clm_3d440b3068c552f2947e47b3daf49dbafe85144989ebc57635c01e3be3aa00fd]
- gdep provides a CLI with commands including detect, scan, describe, flow, impact, method-impact, path, test-scope, watch, lint, advise, graph, diff, init, context, hints, and config. [@claim:clm_4a99e8228e5c5222026bc9a8770a0f2c75f732b34f78d9ee242b698c845bfc70]
- A C# parser ships as a single OS-agnostic DLL (gdep.dll), located via the $GDEP_DLL env var, then publish_dll/gdep.dll, publish/gdep.dll, and a legacy binary path. [@claim:clm_86a648a1935ef2e5f4a1318fdae49dd7bf680a28f5a913d249cde6e17651c44b]
- Prerequisites are Python 3.11+ for the CLI and MCP server, and .NET Runtime 8.0+ for C#/Unity project analysis. [@claim:clm_926e0a626ff0cd1a10fb611e2d210041a84e74a4337a71f8c7871a7f87a3fa3c]
- UE5 analysis responses (analyze_ue5_gas, analyze_ue5_blueprint_mapping) begin with a transparency header reporting analysis method, a HIGH/MEDIUM/LOW confidence tier, asset coverage, and validated UE version. [@claim:clm_92f5c67975dd037e56aed2b4ebd8d7dd6072a38c61c27db991ee15c8f949cd41]
- gdep init generates a .gdep/AGENTS.md file instructing AI agents how to treat results by confidence tier (HIGH trust fully, MEDIUM reliable, LOW verify source). [@claim:clm_a3755f418d1dc114ccb868cbdb82891dfa00f19ed110f5c3ec1759fcb6320c42]
- The web UI supports only English and Korean, supports Ollama as local LLM, and is described as a non-commercial tool whose features may not be perfect. [@claim:clm_b69057892fbbf24ae67feca5d2d0b6cd197ff38c55ea54623d3de3cafe053b2e]
- gdep includes a browser-based web UI with dependency graphs, call-flow visualization, a class browser with impact analysis and lint, an AI chat agent with tool-calling, and engine-specific explorers (GAS, Blueprint mapping, Animator, BehaviorTree, StateTree). [@claim:clm_c1fe6bb464e9faa697b294f48e04b1f6f3f21f7db86fb433852fa3d91e185471]
- The product ships an MCP server exposing 30 game-engine-aware tools (e.g. get_project_context, wiki_search, analyze_impact_and_risk, trace_gameplay_flow) for Claude Desktop, Cursor, and other MCP-compatible agents. [@claim:clm_e27565b53f7a6f28de366569de8f7030f1c31eef70dce44e58c05597c25048ea]
- The MCP server is configured via an mcpServers JSON entry running the gdep-mcp command with a PYTHONUTF8=1 environment variable. [@claim:clm_f55457fc6be982865885ccbecaee358ae6cc17304dec73c7fd13953746a10011]
<!-- rcw:end owner=source:src_320a23ce2cfa599bb2774acb1d91378c block=evidence -->

## Researcher notes

