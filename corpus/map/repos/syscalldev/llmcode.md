# syscalldev/llmcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 81eda39f03db @ 147d5407e0ca0bb7

## Summary (orientation draft, not independently verified)

LLM Code is a terminal-based agentic coding tool that understands the codebase and accepts natural-language commands, inspired by Claude Code but open-source and customizable. The product exposes slash commands including /help, /exit, /pwd, /ls, /tree, /cat, /write, /append, /cd, /mkdir, /config, and /context (or /#) for workspace context.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] LLM Code is a terminal-based agentic coding tool that understands the codebase and accepts natural-language commands, inspired by Claude Code but open-source and customizable. -- evidence: [README.md#L7-L7](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L7-L7), [README.md#L9-L9](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L9-L9)
- components (1 claim(s)):
  - [observation/documented] Documented features include an interactive AI coding assistant, file and directory operations, file editing/appending, codebase context understanding, configurable settings, and colored terminal output. -- evidence: [README.md#L17-L22](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L17-L22)
- design-choices (1 claim(s)):
  - [observation/documented] The tool defaults to the OpenAI API endpoint (https://api.openai.com/v1) as its base URL, with the model configurable by the user. -- evidence: [README.md#L80-L83](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L80-L83)
- workflows (1 claim(s)):
  - [observation/documented] Recommended usage pattern: provide context first via /context, /#, or /tree before requesting code modifications, using /context <file> for specific files. -- evidence: [README.md#L136-L139](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L136-L139)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes slash commands including /help, /exit, /pwd, /ls, /tree, /cat, /write, /append, /cd, /mkdir, /config, and /context (or /#) for workspace context. -- evidence: [README.md#L68-L71](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L68-L71), [README.md#L52-L55](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L52-L55), [README.md#L57-L62](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L57-L62), [README.md#L64-L66](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L64-L66), [README.md#L73-L74](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L73-L74)
  - [observation/documented] The application is started by running 'python main.py', and the API key is set interactively via '/config set apiKey YOUR_API_KEY'. -- evidence: [README.md#L45-L48](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L45-L48), [README.md#L37-L41](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L37-L41)
- memory-state (1 claim(s)):
  - [observation/documented] Configuration is persisted in a JSON file at ~/.llm_code_config.json with keys apiKey, baseUrl (default https://api.openai.com/v1), model, and debug. -- evidence: [README.md#L80-L83](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L80-L83), [README.md#L78-L78](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L78-L78)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] The project is described as under active development and in its early stages, with the README noting that LLM Code is being used to build itself. -- evidence: [README.md#L3-L3](https://github.com/syscalldev/LLMCode/blob/81eda39f03db80cfb4eb7f57338985804115ca0c/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](llmcode.detail.md).

Metadata and full claim list: [full detail](llmcode.detail.md)
Human notes ([notes](llmcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
