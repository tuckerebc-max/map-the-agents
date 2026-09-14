# qwenlm/qwen-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 31a4d36d1236 @ 7bb51c83562efe20

## Summary (orientation draft, not independently verified)

Qwen-Agent is a documented framework for building LLM applications on Qwen models, with atomic LLM/Tool components, an Assistant agent, Docker-based code interpreter, MCP support, and a BrowserQwen Chrome-extension example application. Evidence covers product architecture, configuration interfaces, dependencies, and a released DeepPlanning evaluation benchmark.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Qwen-Agent is a framework for developing LLM applications leveraging Qwen's instruction following, tool usage, planning, and memory capabilities, and it serves as the backend of Qwen Chat. -- evidence: [README.md#L32-L35](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L32-L35)
- components (2 claim(s)):
  - [observation/documented] The framework provides atomic components — LLMs inheriting from BaseChatModel and Tools inheriting from BaseTool — plus higher-level Agents derived from class Agent. -- evidence: [README.md#L87-L88](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L87-L88)
  - [observation/documented] BrowserQwen is an example Chrome extension built on Qwen-Agent offering webpage/PDF discussion, browsing-history recording, and Code Interpreter integration, backed by a locally deployed server on port 7864. -- evidence: [browser_qwen.md#L19-L20](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L19-L20), [browser_qwen.md#L104-L105](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L104-L105), [browser_qwen.md#L107-L107](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L107-L107), [browser_qwen.md#L95-L96](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L95-L96), [browser_qwen.md#L22-L25](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L22-L25), [browser_qwen.md#L84-L85](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/browser_qwen.md#L84-L85)
- design-choices (2 claim(s)):
  - [observation/documented] The default tool-calling template natively supports parallel function calls, and agent classes such as FnCallAgent and ReActChat are built on the function calling capability. -- evidence: [README.md#L239-L239](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L239-L239), [README.md#L237-L237](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L237-L237)
  - [observation/documented] LLM config options include thought_in_content (affecting tool-call parsing), fncall_prompt_type (default 'nous', recommended for qwen3), max_input_tokens truncation, and use_raw_api for the API's native tool call interface. -- evidence: [README.md#L256-L261](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L256-L261), [README.md#L266-L267](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L266-L267), [README.md#L263-L264](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L263-L264), [README.md#L272-L276](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L272-L276)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Agents are configured via an llm_cfg dict with keys such as model, model_type, model_server, api_key, and generate_cfg; both DashScope and OpenAI-compatible services (e.g. vLLM, Ollama) are supported. -- evidence: [README.md#L125-L130](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L125-L130), [README.md#L251-L254](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L251-L254), [README.md#L132-L135](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L132-L135), [README.md#L242-L249](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L242-L249)
  - [observation/documented] The Assistant agent accepts llm, system_message, function_list, and files arguments, and agents run via bot.run(messages=...) as a generator yielding streaming responses. -- evidence: [README.md#L144-L154](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L144-L154), [README.md#L157-L171](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L157-L171)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The built-in code interpreter tool executes agent-written code inside local Docker containers with basic sandbox isolation, mounting only the specified working directory; Docker must be installed and running beforehand. -- evidence: [README.md#L189-L189](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L189-L189), [README.md#L292-L292](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L292-L292), [README.md#L187-L187](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L187-L187)
  - [observation/documented] MCP servers are configured through an mcpServers JSON structure specifying command and args, e.g. npx-based memory and filesystem servers or a uvx sqlite server. -- evidence: [README.md#L196-L219](https://github.com/QwenLM/Qwen-Agent/blob/31a4d36d123688581a9e9744427272b33ce940e0/README.md#L196-L219)
- evaluation (1 claim(s)):
More evidence: [full detail](qwen-agent.detail.md)

Metadata and full claim list: [full detail](qwen-agent.detail.md)
Human notes ([notes](qwen-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
