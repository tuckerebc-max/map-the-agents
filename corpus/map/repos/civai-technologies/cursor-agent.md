# civai-technologies/cursor-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0f5bcd94990b @ 4e70f5f0f0abf023

## Summary (orientation draft, not independently verified)

The evidence (README and constraints.md) documents a Python AI coding agent package, cursor-agent-tools, that wraps Claude, OpenAI, and Ollama models with file/search/system tools, a permission system, and an interactive mode. Development-practice guidance (linting, dev setup) appears only in a few slices. Evidence coverage: 157 of 332 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is a Python-based AI agent replicating Cursor's coding assistant capabilities, requiring Python 3.8+ and installable via pip as cursor-agent-tools. -- evidence: [README.md#L80-L82](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L80-L82), [README.md#L9-L9](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L9-L9), [README.md#L75-L76](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L75-L76)
- components (2 claim(s)):
  - [observation/documented] The repository structure includes an agent package with base, claude_agent, openai_agent, factory, permissions, and interact modules, plus tool modules for file, search, and system operations. -- evidence: [README.md#L390-L437](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L390-L437)
  - [observation/documented] Built-in tools include file operations (read_file, edit_file, delete_file, create_file, list_dir), search tools (codebase_search, grep_search, file_search, web_search, trend_search), query_images, and run_terminal_cmd. -- evidence: [README.md#L40-L45](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L40-L45), [README.md#L31-L38](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L31-L38), [README.md#L50-L51](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L50-L51), [README.md#L47-L48](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L47-L48)
- design-choices (2 claim(s)):
  - [observation/documented] Ollama models are selected by an 'ollama-' name prefix, and tool calling plus multimodal support depend on the capabilities of the specific local model chosen. -- evidence: [README.md#L166-L173](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L166-L173), [README.md#L205-L205](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L205-L205)
  - [observation/documented] edit_file supports line-range-based editing via JSON dictionaries mapping ranges like "1-5" to replacement content, in addition to whole-file replacement. -- evidence: [README.md#L744-L748](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L744-L748), [README.md#L31-L38](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L31-L38), [README.md#L753-L758](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L753-L758)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors fork and clone, install dev dependencies with pip install -e ".[dev]", set API keys in .env, submit pull requests, and must pass flake8 linting with a provided whitespace-fix script. -- evidence: [README.md#L548-L552](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L548-L552), [README.md#L556-L556](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L556-L556), [README.md#L558-L563](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L558-L563)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The public API centers on create_agent(model, temperature, system_prompt, tools) returning a BaseAgent (ClaudeAgent or OpenAIAgent), with async chat() and register_tool() methods. -- evidence: [README.md#L588-L591](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L588-L591), [README.md#L582-L586](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L582-L586), [README.md#L606-L609](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L606-L609), [README.md#L573-L580](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L573-L580), [README.md#L600-L604](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L600-L604)
- memory-state (1 claim(s)):
  - [observation/documented] The agent maintains conversation history for coherent multi-turn interactions, and chat() accepts a user_info dict with open files, cursor position, recent files, OS, and workspace path for project-aware responses. -- evidence: [README.md#L349-L355](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L349-L355), [README.md#L357-L358](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L357-L358), [README.md#L17-L25](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L17-L25)
- orchestration (1 claim(s)):
  - [observation/documented] Interactive mode (run_agent_interactive) auto-continues by default with a max_iterations cap, pauses when the model asks for input, and requests user confirmation after a threshold of tool calls (default 5), raising the limit by 5 on approval. -- evidence: [README.md#L276-L282](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L276-L282), [README.md#L329-L333](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L329-L333), [README.md#L288-L292](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L288-L292), [README.md#L269-L274](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L269-L274), [README.md#L311-L315](https://github.com/civai-technologies/cursor-agent/blob/0f5bcd94990b2325bfe9337894f97a986dc69299/README.md#L311-L315)
- tools-permissions (1 claim(s)):
More evidence: [full detail](cursor-agent.detail.md)

Metadata and full claim list: [full detail](cursor-agent.detail.md)
Human notes ([notes](cursor-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
