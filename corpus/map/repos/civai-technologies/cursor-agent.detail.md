# civai-technologies/cursor-agent -- full detail

[Back to orientation](cursor-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/civai-technologies/cursor-agent/0f5bcd94990b2325bfe9337894f97a986dc69299/4e70f5f0f0abf023.json](../../../wiki/dossiers/civai-technologies/cursor-agent/0f5bcd94990b2325bfe9337894f97a986dc69299/4e70f5f0f0abf023.json)

## specifications (1 claim(s))

- [observation/documented] The project is a Python-based AI agent replicating Cursor's coding assistant capabilities, requiring Python 3.8+ and installable via pip as cursor-agent-tools. -- evidence: [README.md#L80-L82](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L80-L82), [README.md#L9-L9](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L9-L9), [README.md#L75-L76](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L75-L76) (`clm_4df247ad20c1bc8937905bf2a2cf03aa75c9e515bb692b6a9a7e7abcec08df4d`)

## components (2 claim(s))

- [observation/documented] The repository structure includes an agent package with base, claude_agent, openai_agent, factory, permissions, and interact modules, plus tool modules for file, search, and system operations. -- evidence: [README.md#L390-L437](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L390-L437) (`clm_b07a1ea50e3fff8dd8b3b86bf2a588b41e9c50bfac4201b3c6f90a87fb3a24be`)
- [observation/documented] Built-in tools include file operations (read_file, edit_file, delete_file, create_file, list_dir), search tools (codebase_search, grep_search, file_search, web_search, trend_search), query_images, and run_terminal_cmd. -- evidence: [README.md#L40-L45](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L40-L45), [README.md#L31-L38](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L31-L38), [README.md#L50-L51](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L50-L51), [README.md#L47-L48](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L47-L48) (`clm_1c5c018174b5d4889f53dd4c32603cb5101591c2b4ef4a3acf44216bfb0b479f`)

## design-choices (2 claim(s))

- [observation/documented] Ollama models are selected by an 'ollama-' name prefix, and tool calling plus multimodal support depend on the capabilities of the specific local model chosen. -- evidence: [README.md#L166-L173](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L166-L173), [README.md#L205-L205](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L205-L205) (`clm_52cd3f5f30a6bd59f7aecebb933b0ef8b5bdaef258c5a7a964ce84e8df7bda0e`)
- [observation/documented] edit_file supports line-range-based editing via JSON dictionaries mapping ranges like "1-5" to replacement content, in addition to whole-file replacement. -- evidence: [README.md#L744-L748](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L744-L748), [README.md#L31-L38](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L31-L38), [README.md#L753-L758](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L753-L758) (`clm_6e2f3b19aa81653267f7dfcd2c38a48d86f6997d8653ccff95c36ff960630b83`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors fork and clone, install dev dependencies with pip install -e ".[dev]", set API keys in .env, submit pull requests, and must pass flake8 linting with a provided whitespace-fix script. -- evidence: [README.md#L548-L552](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L548-L552), [README.md#L556-L556](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L556-L556), [README.md#L558-L563](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L558-L563) (`clm_bffb2f24afcce619548870364582bc19d02929c210816977211a1febdb189caa`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The public API centers on create_agent(model, temperature, system_prompt, tools) returning a BaseAgent (ClaudeAgent or OpenAIAgent), with async chat() and register_tool() methods. -- evidence: [README.md#L588-L591](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L588-L591), [README.md#L582-L586](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L582-L586), [README.md#L606-L609](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L606-L609), [README.md#L573-L580](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L573-L580), [README.md#L600-L604](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L600-L604) (`clm_e11e70f9d237a87a7666ac072919f26374309d9809b72fe85a389be28eca2687`)

## memory-state (1 claim(s))

- [observation/documented] The agent maintains conversation history for coherent multi-turn interactions, and chat() accepts a user_info dict with open files, cursor position, recent files, OS, and workspace path for project-aware responses. -- evidence: [README.md#L349-L355](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L349-L355), [README.md#L357-L358](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L357-L358), [README.md#L17-L25](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L17-L25) (`clm_a159b40e8c98e5fc157b81f2016faf6b524978c2f7188ead9360a56cfef40704`)

## orchestration (1 claim(s))

- [observation/documented] Interactive mode (run_agent_interactive) auto-continues by default with a max_iterations cap, pauses when the model asks for input, and requests user confirmation after a threshold of tool calls (default 5), raising the limit by 5 on approval. -- evidence: [README.md#L276-L282](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L276-L282), [README.md#L329-L333](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L329-L333), [README.md#L288-L292](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L288-L292), [README.md#L269-L274](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L269-L274), [README.md#L311-L315](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L311-L315) (`clm_9fd5f34f9cae13ed17376cc276e16c6e5ce6740e45742d043dab35684f85c918`)

## tools-permissions (1 claim(s))

- [observation/documented] The agent ships a permission system: file modifications and command executions require approval by default, with an optional YOLO auto-approval mode, command allow/denylists, file-deletion protection, and customizable permission handlers. -- evidence: [README.md#L480-L480](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L480-L480), [README.md#L523-L526](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L523-L526), [README.md#L529-L532](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L529-L532), [README.md#L462-L467](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L462-L467), [README.md#L484-L488](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L484-L488) (`clm_d0ad9b23cde59eb301ce2660fc4cfb0a87dc7598d6669d4fbbebc036aaaebef6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The agent depends on Anthropic and/or OpenAI API keys, optionally uses a Google Search API for web_search, and can use locally hosted Ollama models at a configurable host (default localhost:11434). -- evidence: [README.md#L118-L119](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L118-L119), [README.md#L114-L115](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L114-L115), [README.md#L17-L25](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L17-L25), [README.md#L75-L76](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L75-L76) (`clm_bc6134b23206b61319343fd756b07d2a3d8e64369c57a5a86862de02042c2edc`)

## limitations (1 claim(s))

- [observation/documented] Documented constraints include provider context-window limits (e.g., up to 200K tokens for Claude 3 Opus, 16K-128K for OpenAI models), API rate limits, token-based costs, and tool execution running code on the user's system. -- evidence: [constraints.md#L8-L9](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/constraints.md#L8-L9), [constraints.md#L19-L20](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/constraints.md#L19-L20), [constraints.md#L15-L16](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/constraints.md#L15-L16), [README.md#L792-L796](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L792-L796) (`clm_81931ce69bb84aba01a0a0fe0b71ae4764b751e783930485304caffc8919b708`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

