# cogitatortech/binharic-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 52ccca70bdad @ 33941ff9c8c9a66d

## Summary (orientation draft, not independently verified)

Binharic is a TypeScript terminal-based AI coding agent with a Tech-Priest persona, built on the AI SDK, supporting multiple LLM providers, built-in tools, MCP, and a RAG pipeline; evidence is mostly README and roadmap documentation plus contributor guidelines.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Binharic is a terminal-based AI coding assistant with the persona of a Tech-Priest of the Adeptus Mechanicus, comparable to Codex, Gemini CLI, and Claude Code. -- evidence: [README.md#L16-L16](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L16-L16), [README.md#L22-L28](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L22-L28)
- components (2 claim(s)):
  - [observation/documented] Documented features include models from OpenAI, Google, Anthropic, and Ollama; a keyword-based RAG pipeline; built-in tools for file reading and Bash commands; and MCP-based external tools. -- evidence: [README.md#L36-L41](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L36-L41)
  - [observation/documented] The roadmap marks as implemented a main Tech-Priest agent plus specialized agents such as a Code Analysis Agent and a Security agent. -- evidence: [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture reportedly follows recommendations from Anthropic's 'building effective agents' article to a good degree. -- evidence: [README.md#L22-L28](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L22-L28)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors need Node.js >=20, npm or yarn, GNU Make, and Python >=3.10 with pip for pre-commit; setup uses make install and make setup-hooks, with make test, make lint, and make format for tests, linting, and formatting. -- evidence: [CONTRIBUTING.md#L64-L64](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L64-L64), [CONTRIBUTING.md#L33-L36](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L33-L36), [CONTRIBUTING.md#L60-L60](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L60-L60), [CONTRIBUTING.md#L56-L56](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L56-L56), [CONTRIBUTING.md#L42-L44](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L42-L44), [CONTRIBUTING.md#L48-L52](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L48-L52)
  - [observation/documented] Repository development practice: pull requests should have all tests passing and a clear change description, and submission implies licensing contributions under the project's license. -- evidence: [CONTRIBUTING.md#L23-L24](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L23-L24), [CONTRIBUTING.md#L26-L27](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L26-L27)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Users install the npm package @cogitator/binharic-cli globally and launch the agent with the 'binharic' command in a terminal. -- evidence: [README.md#L70-L71](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L70-L71), [README.md#L57-L59](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L57-L59)
  - [observation/documented] Configuration is done via the ~/.config/binharic/config.json5 file, and environment variables are also supported for configuration. -- evidence: [README.md#L101-L103](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L101-L103)
- memory-state (1 claim(s)):
  - [observation/documented] Implemented context management includes token-based context window management, automatic trimming for long conversations, history preservation across sessions, and tool result summarization. -- evidence: [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47)
- orchestration (1 claim(s)):
  - [observation/documented] The roadmap lists implemented multi-step tool calling with retry logic, transient error handling with exponential backoff, tool execution confirmation, and error/completion-based stopping conditions. -- evidence: [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47)
- tools-permissions (1 claim(s)):
  - [observation/documented] The roadmap lists a tool execution confirmation flow and tool execution timeout protection (10 seconds for autofix) as implemented, while sandboxed tool execution remains unchecked. -- evidence: [ROADMAP.md#L275-L286](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L275-L286), [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47), [ROADMAP.md#L146-L177](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L146-L177)
More evidence: [full detail](binharic-cli.detail.md)

Metadata and full claim list: [full detail](binharic-cli.detail.md)
Human notes ([notes](binharic-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
