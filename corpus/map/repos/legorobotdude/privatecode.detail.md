# legorobotdude/privatecode -- full detail

[Back to orientation](privatecode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/legorobotdude/privatecode/b7d6657742249b610ef85b9b168b3be75462d045/b0511418ecab4e43.json](../../../wiki/dossiers/legorobotdude/privatecode/b7d6657742249b610ef85b9b168b3be75462d045/b0511418ecab4e43.json)

## specifications (1 claim(s))

- [observation/documented] The product is a terminal coding assistant using local LLMs via Ollama for coding help, web search, file editing, and command execution with user confirmation. -- evidence: [README.md#L5-L5](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L5-L5) (`clm_0ee0b3505e206d9e8594b6ff74894fe1608d6bd77fb57d42aef12c08d36042c2`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Thinking blocks let the model include reasoning in responses, hidden by default, with thinking:on/off and thinking:length N commands controlling display and length. -- evidence: [README.md#L184-L184](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L184-L184), [README.md#L188-L190](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L188-L190) (`clm_1aa3064b6c5a8d0ab28891fff901ba6d203e7b79cc787d8a1951a54a3653f1c6`)
- [observation/documented] Defaults are configurable in code_assistant.py, including DEFAULT_MODEL, MAX_SEARCH_RESULTS (5), MAX_URL_CONTENT_LENGTH (10000), SHOW_THINKING (False), and DEFAULT_TIMEOUT (500 seconds). -- evidence: [README.md#L283-L290](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L283-L290), [README.md#L281-L281](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L281-L281) (`clm_5be491f29429e4b078e517657dcb78565eb9b4b8a4d515f7fcde9a65579d91e8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (7 claim(s))

- [observation/documented] Users include file context by placing file paths in square brackets in queries, and multiple files can be included in one question. -- evidence: [README.md#L69-L72](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L69-L72), [README.md#L62-L62](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L62-L62) (`clm_74000dd14bfee9a144ffe8030077dfacbd4376a9e048db9817b172fc2431031c`)
- [observation/documented] Partial file reading supports line-range syntax [file:start-end], [file:start-], [file:-end], and [file:line], with 1-indexed line numbers. -- evidence: [README.md#L233-L233](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L233-L233), [README.md#L228-L231](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L228-L231) (`clm_69221903dc71a12bf3242c8a1a0bdb1344446579c4006795d559871c70772896`)
- [observation/documented] Queries prefixed with search: perform web searches, and URLs in square brackets are fetched for reference content; search can be combined with file context. -- evidence: [README.md#L94-L97](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L94-L97), [README.md#L89-L92](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L89-L92), [README.md#L83-L87](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L83-L87) (`clm_1faa8ee252ea242c6df1ca7778b4198e7e68eb812926eba3571d137153babe38`)
- [observation/documented] The edit: prefix requests file edits; the assistant shows a diff of proposed changes and asks for confirmation before saving. -- evidence: [README.md#L99-L104](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L99-L104) (`clm_95ca6ddd9542e680f564169bbca1ee0fdb45ec3e4931b540210793a5ba2fc396`)
- [observation/documented] The create: prefix makes new empty files with confirmation, supports multiple files at once, auto-creates missing directories, and prompts before overwriting existing files. -- evidence: [README.md#L358-L360](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L358-L360), [README.md#L356-L356](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L356-L356), [README.md#L112-L118](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L112-L118), [README.md#L348-L348](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L348-L348) (`clm_0ef5444d3de449ce87a39657254757fd527bfaa1ed0706c5f57dcf72625475af`)
- [observation/documented] Editing a nonexistent file prompts to create it, allowing file creation and editing in a single step. -- evidence: [README.md#L372-L372](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L372-L372), [README.md#L106-L110](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L106-L110), [README.md#L364-L364](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L364-L364) (`clm_64597b60f8efe53f351ca63ab3613b5e86b38a194392d4fa05e18cbf35b423fd`)
- [observation/documented] The model: prefix switches the active Ollama model at runtime, and timeout:N adjusts the LLM operation timeout. -- evidence: [README.md#L143-L147](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L143-L147), [README.md#L156-L162](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L156-L162) (`clm_0a8f2ed8d91143e3862b012d60017f63e61219e7ce9a59100337d38f64372551`)

## memory-state (1 claim(s))

- [observation/documented] Conversation history is maintained for context during a session but is not saved between sessions. -- evidence: [README.md#L294-L302](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L294-L302) (`clm_96765caec6bd0b77b087ca5ff83348a3b05312b251ae5912458580cc8bf52175`)

## orchestration (1 claim(s))

- [observation/documented] The plan:/vibecode: feature has the LLM break a request into JSON-formatted executable steps (file creation, code writing, edits, commands, output verification), each confirmed interactively and optionally saved to a JSON file. -- evidence: [README.md#L444-L444](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L444-L444), [README.md#L437-L442](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L437-L442), [README.md#L451-L454](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L451-L454) (`clm_2d901df74540148a0e3fc66e1f77a465a38d55f28e23e4ace3d0e8877ba662a6`)

## tools-permissions (2 claim(s))

- [observation/documented] Commands are checked against a list of safe prefixes, dangerous commands trigger extra warnings, and every command requires explicit user confirmation before execution. -- evidence: [README.md#L271-L277](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L271-L277), [README.md#L418-L422](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L418-L422) (`clm_cf1df6c63239e22ced3a71c067ea8eff848867adb141fedca4998616869dabff`)
- [observation/documented] File edits always require user confirmation, and a .bak backup is created before modifying any file. -- evidence: [README.md#L271-L277](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L271-L277) (`clm_18c28a839b5b8ccec163d0d2bed44c0c11e38a7b2225a494755ad193793bb01b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project requires Python 3.6+, a locally running Ollama instance with a pulled code LLM (e.g., codellama, llama2, mixtral), and optionally an internet connection for web search. -- evidence: [README.md#L26-L29](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/README.md#L26-L29) (`clm_e493b12851c8cfa896f657a81bf1edf8fee99d43aa80d73b53adaa087982b1af`)
- [observation/documented] requirements.txt lists requests, beautifulsoup4, lxml, colorama, pytest, pytest-mock, and chardet at minimum versions. -- evidence: [requirements.txt#L1-L7](https://github.com/Legorobotdude/PrivateCode/blob/b7d6657742249b610ef85b9b168b3be75462d045/requirements.txt#L1-L7) (`clm_eac6b3928ca076cace88ec72634609e4267ab579dcaa5091182cbbb4a7f0f858`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

