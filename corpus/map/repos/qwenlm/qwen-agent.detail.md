# qwenlm/qwen-agent -- full detail

[Back to orientation](qwen-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/qwenlm/qwen-agent/31a4d36d123688581a9e9744427272b33ce940e0/7bb51c83562efe20.json](../../../wiki/dossiers/qwenlm/qwen-agent/31a4d36d123688581a9e9744427272b33ce940e0/7bb51c83562efe20.json)

## specifications (1 claim(s))

- [observation/documented] Qwen-Agent is a framework for developing LLM applications leveraging Qwen's instruction following, tool usage, planning, and memory capabilities, and it serves as the backend of Qwen Chat. -- evidence: [README.md#L32-L35](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L32-L35) (`clm_4fe0340659d2bfaa557d28db862f0e366f56fb7723ac60155707b6e523d07323`)

## components (2 claim(s))

- [observation/documented] The framework provides atomic components — LLMs inheriting from BaseChatModel and Tools inheriting from BaseTool — plus higher-level Agents derived from class Agent. -- evidence: [README.md#L87-L88](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L87-L88) (`clm_a8a8e2091af5f22234d07ce2148f66bcd85567404f32d21232d36e6879be51c3`)
- [observation/documented] BrowserQwen is an example Chrome extension built on Qwen-Agent offering webpage/PDF discussion, browsing-history recording, and Code Interpreter integration, backed by a locally deployed server on port 7864. -- evidence: [browser_qwen.md#L19-L20](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L19-L20), [browser_qwen.md#L104-L105](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L104-L105), [browser_qwen.md#L107-L107](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L107-L107), [browser_qwen.md#L95-L96](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L95-L96), [browser_qwen.md#L22-L25](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L22-L25), [browser_qwen.md#L84-L85](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L84-L85) (`clm_e998ace10df8f97cd12c4dc753b1b8fcb5024b4bb98503108a81b449a2a0f712`)

## design-choices (2 claim(s))

- [observation/documented] The default tool-calling template natively supports parallel function calls, and agent classes such as FnCallAgent and ReActChat are built on the function calling capability. -- evidence: [README.md#L239-L239](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L239-L239), [README.md#L237-L237](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L237-L237) (`clm_10d3ae5c94869fb6987477a1f4db977efd9dca8e1eb6f5ac5dbe4da88f14593a`)
- [observation/documented] LLM config options include thought_in_content (affecting tool-call parsing), fncall_prompt_type (default 'nous', recommended for qwen3), max_input_tokens truncation, and use_raw_api for the API's native tool call interface. -- evidence: [README.md#L256-L261](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L256-L261), [README.md#L266-L267](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L266-L267), [README.md#L263-L264](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L263-L264), [README.md#L272-L276](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L272-L276) (`clm_e72f95e00dd1825f15db9d7ac8d0a309472fc5a348d4ef88355126aa5c000659`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Agents are configured via an llm_cfg dict with keys such as model, model_type, model_server, api_key, and generate_cfg; both DashScope and OpenAI-compatible services (e.g. vLLM, Ollama) are supported. -- evidence: [README.md#L125-L130](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L125-L130), [README.md#L251-L254](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L251-L254), [README.md#L132-L135](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L132-L135), [README.md#L242-L249](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L242-L249) (`clm_8685ead407712b0b4785cc14f9cd31635c292e5e00e072ffcdfbaf888ac42371`)
- [observation/documented] The Assistant agent accepts llm, system_message, function_list, and files arguments, and agents run via bot.run(messages=...) as a generator yielding streaming responses. -- evidence: [README.md#L144-L154](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L144-L154), [README.md#L157-L171](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L157-L171) (`clm_c293aebf2a893059b8891ff980550c58ad1df936ec2c795140ba4fb773a239be`)
- [observation/documented] Custom tools are registered with a @register_tool decorator, defining a description, a parameters schema, and a call() method that parses LLM-generated arguments. -- evidence: [README.md#L103-L113](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L103-L113), [README.md#L115-L121](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L115-L121) (`clm_9dff9aaf949c5a2c01dd7d7d6bea0d802d4ee5889fbf0e9c11466c7ea5c9d941`)
- [observation/documented] A Gradio-based WebUI (qwen_agent.gui.WebUI) enables rapid deployment of chat interfaces for agents; per the Gradio 5 upgrade note, the GUI requires Python 3.10 or higher. -- evidence: [README.md#L38-L46](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L38-L46), [README.md#L178-L182](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L178-L182), [README.md#L175-L176](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L175-L176) (`clm_cb5b056f5baa9a35d81f8d482d2162cdc3d6af41a77f4f6bc195011e4eb6e3cd`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The built-in code interpreter tool executes agent-written code inside local Docker containers with basic sandbox isolation, mounting only the specified working directory; Docker must be installed and running beforehand. -- evidence: [README.md#L189-L189](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L189-L189), [README.md#L292-L292](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L292-L292), [README.md#L187-L187](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L187-L187) (`clm_cfde5686ce7eb6fa325d045be8b7169150472158ce5aa131ccd4b7d42d967098`)
- [observation/documented] MCP servers are configured through an mcpServers JSON structure specifying command and args, e.g. npx-based memory and filesystem servers or a uvx sqlite server. -- evidence: [README.md#L196-L219](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L196-L219) (`clm_5055cd059ff7009563a7b881c90866936bdd11bfefdf1a9f26ab32bf5f99e164`)

## evaluation (1 claim(s))

- [observation/documented] The project released the DeepPlanning agent evaluation benchmark (Jan 2026) and links a benchmark page in its README. -- evidence: [README.md#L38-L46](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L38-L46), [README.md#L27-L29](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L27-L29) (`clm_55d9bc175bb42f30328da7645454bbf48fa02c3e7c0ef6a021ce831cc3066069`)

## dependencies (1 claim(s))

- [observation/documented] The package installs from PyPI as qwen-agent with optional extras [gui,rag,code_interpreter,mcp], or editable from source; MCP examples additionally require uv, git, and sqlite3. -- evidence: [README.md#L63-L67](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L63-L67), [README.md#L52-L54](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L52-L54), [README.md#L232-L234](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L232-L234), [README.md#L229-L229](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L229-L229) (`clm_07ab85a9f1f1bf766913f005ed2ae66429422fa03553b37967cf2e9f44d11c29`)

## limitations (1 claim(s))

- [observation/documented] The Docker-based code interpreter implements only basic sandbox isolation and mounts only the specified working directory, so the docs advise caution when using it in production environments. -- evidence: [README.md#L292-L292](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L292-L292) (`clm_6d2b941b6fa2bae7b1942b43199b5b45d74eee970de019555dbcab8478bc526c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

