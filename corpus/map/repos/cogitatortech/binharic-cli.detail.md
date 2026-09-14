# cogitatortech/binharic-cli -- full detail

[Back to orientation](binharic-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cogitatortech/binharic-cli/52ccca70bdadb20742c2c3305298c5a6604e9a36/33941ff9c8c9a66d.json](../../../wiki/dossiers/cogitatortech/binharic-cli/52ccca70bdadb20742c2c3305298c5a6604e9a36/33941ff9c8c9a66d.json)

## specifications (1 claim(s))

- [observation/documented] Binharic is a terminal-based AI coding assistant with the persona of a Tech-Priest of the Adeptus Mechanicus, comparable to Codex, Gemini CLI, and Claude Code. -- evidence: [README.md#L16-L16](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L16-L16), [README.md#L22-L28](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L22-L28) (`clm_93df243fd0776a85038cecb6efd0e0e9235b2d2a96fe34e8403fceec5d96ea59`)

## components (2 claim(s))

- [observation/documented] Documented features include models from OpenAI, Google, Anthropic, and Ollama; a keyword-based RAG pipeline; built-in tools for file reading and Bash commands; and MCP-based external tools. -- evidence: [README.md#L36-L41](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L36-L41) (`clm_18c50b72d9123ea51d53be3fb79454c694eb7450885887748382c855e40195a4`)
- [observation/documented] The roadmap marks as implemented a main Tech-Priest agent plus specialized agents such as a Code Analysis Agent and a Security agent. -- evidence: [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47) (`clm_45e69ce012351ffdd9d64e6b731691b3814fff5784e9bda2ed0fb18744ce33f2`)

## design-choices (1 claim(s))

- [observation/documented] The architecture reportedly follows recommendations from Anthropic's 'building effective agents' article to a good degree. -- evidence: [README.md#L22-L28](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L22-L28) (`clm_3ec46cb45c1bcd26af6b4dc981554e100dc97fbe14ef87b1d2ee1713dd0a7879`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors need Node.js >=20, npm or yarn, GNU Make, and Python >=3.10 with pip for pre-commit; setup uses make install and make setup-hooks, with make test, make lint, and make format for tests, linting, and formatting. -- evidence: [CONTRIBUTING.md#L64-L64](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L64-L64), [CONTRIBUTING.md#L33-L36](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L33-L36), [CONTRIBUTING.md#L60-L60](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L60-L60), [CONTRIBUTING.md#L56-L56](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L56-L56), [CONTRIBUTING.md#L42-L44](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L42-L44), [CONTRIBUTING.md#L48-L52](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L48-L52) (`clm_961c61992ada0344410e800c40e28c0dba89321eb1d6f0e8647ac8668b522ca7`)
- [observation/documented] Repository development practice: pull requests should have all tests passing and a clear change description, and submission implies licensing contributions under the project's license. -- evidence: [CONTRIBUTING.md#L23-L24](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L23-L24), [CONTRIBUTING.md#L26-L27](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/CONTRIBUTING.md#L26-L27) (`clm_fa8e555c95cc622f060d8ed2a85c5b1a3671bee907b7bec601b04ff3b47da8bd`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Users install the npm package @cogitator/binharic-cli globally and launch the agent with the 'binharic' command in a terminal. -- evidence: [README.md#L70-L71](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L70-L71), [README.md#L57-L59](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L57-L59) (`clm_9fb38b8298be70b9dca5051fb4211d968b51a37d9903d76a678c4d839cf7cf14`)
- [observation/documented] Configuration is done via the ~/.config/binharic/config.json5 file, and environment variables are also supported for configuration. -- evidence: [README.md#L101-L103](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L101-L103) (`clm_0a7b6de554c258f32c18c631c3c20e806aee9f5ef28226d6a280de51b5ba2d60`)
- [observation/documented] API keys for OpenAI, Anthropic, and Google are supplied through environment variables when running the agent. -- evidence: [README.md#L65-L67](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L65-L67), [README.md#L88-L94](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L88-L94) (`clm_fa7636a79bf5f4f2d2facca4b7a82f9ab91b04e133a340938a3c476bac1b788c`)

## memory-state (1 claim(s))

- [observation/documented] Implemented context management includes token-based context window management, automatic trimming for long conversations, history preservation across sessions, and tool result summarization. -- evidence: [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47) (`clm_c828ac96ed8334853b857db406980d148e80fddd00df22b4a583de951da18e1a`)

## orchestration (1 claim(s))

- [observation/documented] The roadmap lists implemented multi-step tool calling with retry logic, transient error handling with exponential backoff, tool execution confirmation, and error/completion-based stopping conditions. -- evidence: [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47) (`clm_578c93f78aea6f58fdd729694d388e67f2459d6ff52a46083c6438c916979085`)

## tools-permissions (1 claim(s))

- [observation/documented] The roadmap lists a tool execution confirmation flow and tool execution timeout protection (10 seconds for autofix) as implemented, while sandboxed tool execution remains unchecked. -- evidence: [ROADMAP.md#L275-L286](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L275-L286), [ROADMAP.md#L11-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L11-L47), [ROADMAP.md#L146-L177](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L146-L177) (`clm_4ee0adc5b15e2d4d619cd077ef57337933da2ce88d4e53792154f30a91e594f4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project is written in TypeScript and uses the AI SDK framework for much of its agentic logic such as tool calling and workflow management. -- evidence: [README.md#L22-L28](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L22-L28) (`clm_8cd44cb541843f568717e5cff92150ffbeded0639e94da8c6af4c99ff7e97b3b`)
- [observation/documented] A Docker image is published to GitHub Container Registry with multi-arch builds (linux/amd64 and linux/arm64), and the agent can be run in a container mounting the working directory at /workspace. -- evidence: [ROADMAP.md#L222-L241](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L222-L241), [README.md#L88-L94](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L88-L94) (`clm_b45b67a03f6146c5c26ee10da5261417333507217ddfc0780cac5837812b2ae4`)

## limitations (2 claim(s))

- [observation/documented] The README states Binharic is in early development, so bugs and breaking changes are expected. -- evidence: [README.md#L45-L47](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L45-L47) (`clm_532165133fb109047382f4333d8581b2b904206d7f352374f0530bf4dc611ec0`)
- [observation/documented] The roadmap marks sandboxed tool execution, encrypted configuration files, rate limiting, and audit logging as not yet implemented. -- evidence: [ROADMAP.md#L275-L286](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/ROADMAP.md#L275-L286) (`clm_016b43cca18f3d98c016d24052c5cb12c699927d5f17f0f66b8de299241c6335`)

## relevance (1 claim(s))

- [observation/documented] The project is MIT-licensed, published on npm, and positions itself as a general-purpose coding agent able to analyze projects, run tests, find bugs, and perform code review. -- evidence: [README.md#L119-L119](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L119-L119), [README.md#L30-L32](https://github.com/CogitatorTech/binharic-cli/blob/52ccca70bdadb20742c2c3305298c5a6604e9a36/README.md#L30-L32) (`clm_2cc10d005820d402676175a8ba9fcb9644c521314f5c3f30c96efbefcefda56b`)

