---
access: public
aliases: []
claim_ids:
- clm_2ef94f1e8e2bf38ea4a947bde31bcfcbe57f9bc2e72ecb8ecd9b5f827c177097
- clm_4ee3552cabf3d003d5cb8de21ac92cd55e1ec9d8e062d648a6fa604c96074a4f
- clm_535cc2e71452127661a850cf1d1640dc9e05efa99bff640b950eccdeea584422
- clm_5cc5bd7684040e0404a8d624779ad5eab4c72aea4e9ca65dd2152bc8929384e4
- clm_8510a54d07b2349ffc1fe40f3282abf07e56717b6c23fa9d0d8a6ef3d3b5f3e7
- clm_956863e8798b597f03be73e3bd7b460f80139047798925c3b9fda64bab6c0558
- clm_9c4deee429f5663cb829ff592f10d4f4dfc7b16fbca63e1d292acfba05a4fba9
- clm_b464f1fa2c3cfd05d47aa83b4ef7468398022a3f92de310aaf1fbf6ef944c089
- clm_b7aab3587b646437cde5f4be0b80fd71e435546d136c3a230d4cc0ce8a00f289
- clm_e66f5f68793b89610129a948533260bc1b98c74d809600f6f1f5286618c4f804
- clm_ee5d1dae846d121ade6a9953a13457815c6a3846eed3aaefdc1896e624667c57
maturity: draft
page_id: pg_240e4a1476925321bd13d5fdf723f828
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8f54cdd3da7d546fad63f58a04a112f2
title: ZhuLinsen/MiniAgent/README.md @ 657909f0237b
updated_at: '2026-09-14T04:41:41Z'
---

# ZhuLinsen/MiniAgent/README.md @ 657909f0237b

<!-- rcw:begin owner=source:src_8f54cdd3da7d546fad63f58a04a112f2 block=evidence -->
- The CLI is launched via 'miniagent' or 'python -m miniagent', and configuration is done through a .env file with variables such as LLM_API_KEY, LLM_MODEL, and LLM_API_BASE; Gemini is supported via Google's OpenAI-compatible endpoint. [@claim:clm_2ef94f1e8e2bf38ea4a947bde31bcfcbe57f9bc2e72ecb8ecd9b5f827c177097]
- The framework exposes MCP protocol support via load_mcp_tools, allowing tools from any MCP server (e.g. the filesystem server) to be added to an agent with agent.add_tool. [@claim:clm_4ee3552cabf3d003d5cb8de21ac92cd55e1ec9d8e062d648a6fa604c96074a4f]
- A Skill system provides reusable agent configurations combining prompt, tool whitelist, and parameters, with four built-in roles (coder, researcher, reviewer, tester) and a register_skill API for custom skills. [@claim:clm_535cc2e71452127661a850cf1d1640dc9e05efa99bff640b950eccdeea584422]
- A built-in Orchestrator decomposes complex tasks and assigns them to specialized workers driven by the Skill system, e.g. planning researcher → coder → tester for a research-and-code task. [@claim:clm_5cc5bd7684040e0404a8d624779ad5eab4c72aea4e9ca65dd2152bc8929384e4]
- requirements.txt lists seven runtime dependencies: openai, requests, python-dotenv, tenacity, psutil, distro, and rich; python-docx is an optional extra for Word document support. [@claim:clm_8510a54d07b2349ffc1fe40f3282abf07e56717b6c23fa9d0d8a6ef3d3b5f3e7]
- The product supports two tool-calling modes: a default text-parsing mode where the LLM emits structured text like 'TOOL: bash / ARGS: {...}', and a native OpenAI function-calling mode enabled via mode="native" that supports parallel tool calls. [@claim:clm_956863e8798b597f03be73e3bd7b460f80139047798925c3b9fda64bab6c0558]
- Documented built-in tools include code tools (read, write, edit, grep, glob, bash with timeout), OS tools (open_browser, open_app, create_docx, clipboard), system tools (system_info, process_list, env_get/set), and misc tools (calculator with AST-safe evaluation, web_search, http_request). [@claim:clm_9c4deee429f5663cb829ff592f10d4f4dfc7b16fbca63e1d292acfba05a4fba9]
- The product includes lightweight session memory stored at ~/.miniagent/memory.json (path configurable via MINIAGENT_HOME) and auto-compresses conversation history beyond a configurable message limit. [@claim:clm_b464f1fa2c3cfd05d47aa83b4ef7468398022a3f92de310aaf1fbf6ef944c089]
- The runtime includes a safety guard that auto-detects dangerous bash commands and requires confirmation before execution, controlled by a CONFIRM_DANGEROUS setting documented as defaulting to true. [@claim:clm_b7aab3587b646437cde5f4be0b80fd71e435546d136c3a230d4cc0ce8a00f289]
- The documented project layout includes agent.py (LLM loop, tool calling, context management), cli.py (Rich streaming CLI), tools/ (code_tools.py, basic_tools.py), extensions/ (mcp_client.py, orchestrator.py), skills.py, config.py, memory.py, and utils/. [@claim:clm_e66f5f68793b89610129a948533260bc1b98c74d809600f6f1f5286618c4f804]
- MiniAgent is documented as a minimalist, transparent CLI agent framework whose core engine is a single agent.py file, positioned as an educational 'AI Agent textbook'. [@claim:clm_ee5d1dae846d121ade6a9953a13457815c6a3846eed3aaefdc1896e624667c57]
<!-- rcw:end owner=source:src_8f54cdd3da7d546fad63f58a04a112f2 block=evidence -->

## Researcher notes

