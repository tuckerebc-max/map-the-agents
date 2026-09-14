# legorobotdude/privatecode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b7d665774224 @ b0511418ecab4e43

## Summary (orientation draft, not independently verified)

A terminal-based coding assistant that runs local LLMs via Ollama, offering file-context queries, web search, file editing/creation, command execution with confirmation, and a plan/vibecode step executor. All product behavior claims below come from the README; no repository-name or development-practice claims are retained.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is a terminal coding assistant using local LLMs via Ollama for coding help, web search, file editing, and command execution with user confirmation. -- evidence: [README.md#L5-L5](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Thinking blocks let the model include reasoning in responses, hidden by default, with thinking:on/off and thinking:length N commands controlling display and length. -- evidence: [README.md#L184-L184](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L184-L184), [README.md#L188-L190](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L188-L190)
  - [observation/documented] Defaults are configurable in code_assistant.py, including DEFAULT_MODEL, MAX_SEARCH_RESULTS (5), MAX_URL_CONTENT_LENGTH (10000), SHOW_THINKING (False), and DEFAULT_TIMEOUT (500 seconds). -- evidence: [README.md#L283-L290](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L283-L290), [README.md#L281-L281](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L281-L281)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (7 claim(s)):
  - [observation/documented] Users include file context by placing file paths in square brackets in queries, and multiple files can be included in one question. -- evidence: [README.md#L69-L72](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L69-L72), [README.md#L62-L62](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L62-L62)
  - [observation/documented] Partial file reading supports line-range syntax [file:start-end], [file:start-], [file:-end], and [file:line], with 1-indexed line numbers. -- evidence: [README.md#L233-L233](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L233-L233), [README.md#L228-L231](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L228-L231)
- memory-state (1 claim(s)):
  - [observation/documented] Conversation history is maintained for context during a session but is not saved between sessions. -- evidence: [README.md#L294-L302](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L294-L302)
- orchestration (1 claim(s)):
  - [observation/documented] The plan:/vibecode: feature has the LLM break a request into JSON-formatted executable steps (file creation, code writing, edits, commands, output verification), each confirmed interactively and optionally saved to a JSON file. -- evidence: [README.md#L444-L444](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L444-L444), [README.md#L437-L442](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L437-L442), [README.md#L451-L454](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L451-L454)
- tools-permissions (2 claim(s)):
  - [observation/documented] Commands are checked against a list of safe prefixes, dangerous commands trigger extra warnings, and every command requires explicit user confirmation before execution. -- evidence: [README.md#L271-L277](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L271-L277), [README.md#L418-L422](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L418-L422)
  - [observation/documented] File edits always require user confirmation, and a .bak backup is created before modifying any file. -- evidence: [README.md#L271-L277](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L271-L277)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project requires Python 3.6+, a locally running Ollama instance with a pulled code LLM (e.g., codellama, llama2, mixtral), and optionally an internet connection for web search. -- evidence: [README.md#L26-L29](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L26-L29)
  - [observation/documented] requirements.txt lists requests, beautifulsoup4, lxml, colorama, pytest, pytest-mock, and chardet at minimum versions. -- evidence: [requirements.txt#L1-L7](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/requirements.txt#L1-L7)
More evidence: [full detail](privatecode.detail.md)

Metadata and full claim list: [full detail](privatecode.detail.md)
Human notes ([notes](privatecode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
