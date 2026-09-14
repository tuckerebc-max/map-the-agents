---
access: public
aliases: []
claim_ids:
- clm_00653a1b3c00132caeae35cfac4b7d5792c44044eaf116ea5a6bf552424bea7d
- clm_02aa47e3613ad22b1d6ca8cd72f6363cf9367bc16c6e8d8138488fc19c1b1295
- clm_0acfa49b0bd88396a9b621ab725f2943a7a55a2d83685f76f7d0c3ffd52204b3
- clm_208fd78d53f2f3422bb3381a68eb5b1d88de69c2fbe91b5e417310d9f64f1c27
- clm_2f014212af75a9cadb059ebea58098da837e3b697fff680b27c768d436886288
- clm_2f0e78da1fc0bfc41ed1620976549fe283a7d788ec79775052d263b8140456a4
- clm_572249c81f94a4a534489e23ea2c816840df19ec8c406752f051eb060cd4571d
- clm_5d938e80747f10f9652a61c96c58e43f2202b09ef821f23d4e3110cd61509d20
- clm_69ccefc9b543fd9ad05673960e50d3124e920fd39a1306278275642cd46c9991
- clm_6ede4fe863ae2deef43e9d0cced88c516de3ff4596a9508056c12ea6876dc19d
- clm_8b8f808790a1442b03d1aa98d38db6147fa7a3d048eb6a0dcf78f1c43571b8c3
- clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46
- clm_d2749f1e3e19ac4df142a4651e444d318f2bb4f3e27339876e84b5c61ed59442
maturity: draft
page_id: pg_c15326d414785424b26a760d75082ded
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_af48ddd846c15f26bb9af44635475d94
title: stippi/code-assistant/README.md @ ba818a46c472
updated_at: '2026-09-14T02:43:45Z'
---

# stippi/code-assistant/README.md @ ba818a46c472

<!-- rcw:begin owner=source:src_af48ddd846c15f26bb9af44635475d94 block=evidence -->
- Repository development practice: building from source requires the Rust toolchain via rustup, specific Linux system libraries for gpui, the Metal toolchain on macOS, and 'cargo build --release'; browser-agency work followed a TDD/checkpoint style where each step compiles, is tested, and is committable on its own. [@claim:clm_00653a1b3c00132caeae35cfac4b7d5792c44044eaf116ea5a6bf552424bea7d]
- The agent supports reusable, task-specific skills (playbooks) loadable on demand, and auto-loads AGENTS.md or CLAUDE.md from the project root as repo-specific guidance. [@claim:clm_02aa47e3613ad22b1d6ca8cd72f6363cf9367bc16c6e8d8138488fc19c1b1295]
- The product includes permission tiers and a command sandbox; --sandbox-mode offers danger-full-access (the default), read-only, and workspace-write, with --sandbox-network allowing outbound network access in workspace-write mode. [@claim:clm_0acfa49b0bd88396a9b621ab725f2943a7a55a2d83685f76f7d0c3ffd52204b3]
- Any mode can accept an initial task via a --task flag, e.g. asking it to explain the codebase. [@claim:clm_208fd78d53f2f3422bb3381a68eb5b1d88de69c2fbe91b5e417310d9f64f1c27]
- Multiple LLM providers are supported, including Anthropic, OpenAI, Google Vertex AI, Ollama, OpenRouter, SAP AI Core, Groq, Cerebras, and Mistral, configured via providers.json and models.json with example files for each. [@claim:clm_2f014212af75a9cadb059ebea58098da837e3b697fff680b27c768d436886288]
- The project is an open-source Rust AI coding agent that runs an autonomous agent loop over a codebase — reading, searching, editing files, and running commands — while keeping the user informed of what it is doing. [@claim:clm_2f0e78da1fc0bfc41ed1620976549fe283a7d788ec79775052d263b8140456a4]
- File handling preserves each file's stored encoding, BOM, and CRLF/LF line endings, giving the model clean text while writing the file back in its original form. [@claim:clm_572249c81f94a4a534489e23ea2c816840df19ec8c406752f051eb060cd4571d]
- Sessions are per project with branching and persistent state; each chat session is permanently tied to its initial project/folder and tool syntax, which cannot be changed later. [@claim:clm_5d938e80747f10f9652a61c96c58e43f2202b09ef821f23d4e3110cd61509d20]
- Tool-invocation syntax is adaptive per session: native function calling, XML tags, or triple-caret blocks, selectable via --tool-syntax native|xml|caret. [@claim:clm_69ccefc9b543fd9ad05673960e50d3124e920fd39a1306278275642cd46c9991]
- Zed integration registers the binary as an agent_servers entry with 'acp' args and an API key env var; Claude Desktop integration uses the 'server' subcommand in an mcpServers entry. [@claim:clm_6ede4fe863ae2deef43e9d0cced88c516de3ff4596a9508056c12ea6876dc19d]
- The binary offers four interface modes: a native GUI by default, a terminal mode via --tui, an ACP agent via 'acp' for editors like Zed, and a headless MCP server via 'server'. [@claim:clm_8b8f808790a1442b03d1aa98d38db6147fa7a3d048eb6a0dcf78f1c43571b8c3]
- The GUI is built on Zed's GPUI framework; the codebase is organized into crates including llm, code_assistant, and web, with the web crate already owning chromiumoxide for browser automation. [@claim:clm_9c35d3a491edeef165698ba1bc5dfd4f11f7b866fb56c9f03a7bf86d66e92c46]
- Format-on-save runs project formatters after the assistant modifies matching files and updates tool parameters to reflect formatted content, keeping the model's view in sync without re-reading files; mappings pair glob patterns with shell commands. [@claim:clm_d2749f1e3e19ac4df142a4651e444d318f2bb4f3e27339876e84b5c61ed59442]
<!-- rcw:end owner=source:src_af48ddd846c15f26bb9af44635475d94 block=evidence -->

## Researcher notes

