---
access: public
aliases: []
claim_ids:
- clm_1c5c018174b5d4889f53dd4c32603cb5101591c2b4ef4a3acf44216bfb0b479f
- clm_4df247ad20c1bc8937905bf2a2cf03aa75c9e515bb692b6a9a7e7abcec08df4d
- clm_52cd3f5f30a6bd59f7aecebb933b0ef8b5bdaef258c5a7a964ce84e8df7bda0e
- clm_6e2f3b19aa81653267f7dfcd2c38a48d86f6997d8653ccff95c36ff960630b83
- clm_81931ce69bb84aba01a0a0fe0b71ae4764b751e783930485304caffc8919b708
- clm_9fd5f34f9cae13ed17376cc276e16c6e5ce6740e45742d043dab35684f85c918
- clm_a159b40e8c98e5fc157b81f2016faf6b524978c2f7188ead9360a56cfef40704
- clm_b07a1ea50e3fff8dd8b3b86bf2a588b41e9c50bfac4201b3c6f90a87fb3a24be
- clm_bc6134b23206b61319343fd756b07d2a3d8e64369c57a5a86862de02042c2edc
- clm_bffb2f24afcce619548870364582bc19d02929c210816977211a1febdb189caa
- clm_d0ad9b23cde59eb301ce2660fc4cfb0a87dc7598d6669d4fbbebc036aaaebef6
- clm_e11e70f9d237a87a7666ac072919f26374309d9809b72fe85a389be28eca2687
maturity: draft
page_id: pg_e6d1f4e1af1d50929b6b37baa9021904
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c4cbd3a7ed345fe3aa322a898341de5f
title: civai-technologies/cursor-agent/README.md @ 0f5bcd94990b
updated_at: '2026-09-14T01:40:45Z'
---

# civai-technologies/cursor-agent/README.md @ 0f5bcd94990b

<!-- rcw:begin owner=source:src_c4cbd3a7ed345fe3aa322a898341de5f block=evidence -->
- Built-in tools include file operations (read_file, edit_file, delete_file, create_file, list_dir), search tools (codebase_search, grep_search, file_search, web_search, trend_search), query_images, and run_terminal_cmd. [@claim:clm_1c5c018174b5d4889f53dd4c32603cb5101591c2b4ef4a3acf44216bfb0b479f]
- The project is a Python-based AI agent replicating Cursor's coding assistant capabilities, requiring Python 3.8+ and installable via pip as cursor-agent-tools. [@claim:clm_4df247ad20c1bc8937905bf2a2cf03aa75c9e515bb692b6a9a7e7abcec08df4d]
- Ollama models are selected by an 'ollama-' name prefix, and tool calling plus multimodal support depend on the capabilities of the specific local model chosen. [@claim:clm_52cd3f5f30a6bd59f7aecebb933b0ef8b5bdaef258c5a7a964ce84e8df7bda0e]
- edit_file supports line-range-based editing via JSON dictionaries mapping ranges like "1-5" to replacement content, in addition to whole-file replacement. [@claim:clm_6e2f3b19aa81653267f7dfcd2c38a48d86f6997d8653ccff95c36ff960630b83]
- Documented constraints include provider context-window limits (e.g., up to 200K tokens for Claude 3 Opus, 16K-128K for OpenAI models), API rate limits, token-based costs, and tool execution running code on the user's system. [@claim:clm_81931ce69bb84aba01a0a0fe0b71ae4764b751e783930485304caffc8919b708]
- Interactive mode (run_agent_interactive) auto-continues by default with a max_iterations cap, pauses when the model asks for input, and requests user confirmation after a threshold of tool calls (default 5), raising the limit by 5 on approval. [@claim:clm_9fd5f34f9cae13ed17376cc276e16c6e5ce6740e45742d043dab35684f85c918]
- The agent maintains conversation history for coherent multi-turn interactions, and chat() accepts a user_info dict with open files, cursor position, recent files, OS, and workspace path for project-aware responses. [@claim:clm_a159b40e8c98e5fc157b81f2016faf6b524978c2f7188ead9360a56cfef40704]
- The repository structure includes an agent package with base, claude_agent, openai_agent, factory, permissions, and interact modules, plus tool modules for file, search, and system operations. [@claim:clm_b07a1ea50e3fff8dd8b3b86bf2a588b41e9c50bfac4201b3c6f90a87fb3a24be]
- The agent depends on Anthropic and/or OpenAI API keys, optionally uses a Google Search API for web_search, and can use locally hosted Ollama models at a configurable host (default localhost:11434). [@claim:clm_bc6134b23206b61319343fd756b07d2a3d8e64369c57a5a86862de02042c2edc]
- Repository development practice: contributors fork and clone, install dev dependencies with pip install -e ".[dev]", set API keys in .env, submit pull requests, and must pass flake8 linting with a provided whitespace-fix script. [@claim:clm_bffb2f24afcce619548870364582bc19d02929c210816977211a1febdb189caa]
- The agent ships a permission system: file modifications and command executions require approval by default, with an optional YOLO auto-approval mode, command allow/denylists, file-deletion protection, and customizable permission handlers. [@claim:clm_d0ad9b23cde59eb301ce2660fc4cfb0a87dc7598d6669d4fbbebc036aaaebef6]
- The public API centers on create_agent(model, temperature, system_prompt, tools) returning a BaseAgent (ClaudeAgent or OpenAIAgent), with async chat() and register_tool() methods. [@claim:clm_e11e70f9d237a87a7666ac072919f26374309d9809b72fe85a389be28eca2687]
<!-- rcw:end owner=source:src_c4cbd3a7ed345fe3aa322a898341de5f block=evidence -->

## Researcher notes

