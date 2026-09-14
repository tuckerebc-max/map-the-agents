# amrit110/oli -- full detail

[Back to orientation](oli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/amrit110/oli/18cf418cb0ee5812761c7de664c796dca6ddfabb/9033f0017a5fdc22.json](../../../wiki/dossiers/amrit110/oli/18cf418cb0ee5812761c7de664c796dca6ddfabb/9033f0017a5fdc22.json)

## specifications (1 claim(s))

- [observation/documented] The README describes oli as an open-source coding-assistant alternative to Claude Code with a hybrid architecture, supporting cloud APIs (Anthropic, OpenAI, Google) as well as local models served through Ollama. -- evidence: [README.md#L15-L20](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/README.md#L15-L20), [README.md#L13-L13](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/README.md#L13-L13) (`clm_bc68bc1b03f789674400243839252ad23fdb3f4d89dbfaffdb92ee3f7c5b90c9`)

## components (1 claim(s))

- [observation/documented] The server exposes a JSON-RPC 2.0 API over stdio, documented to include a cancel_task method for stopping the current or a named task and a clear_conversation method for resetting conversation history. -- evidence: [docs/src/api.md#L197-L197](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L197-L197), [docs/src/api.md#L10-L11](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L10-L11), [docs/src/api.md#L233-L233](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L233-L233) (`clm_57355eea2390faede08f2688b72e0b50df89906f7c21502b884ad075fe92308f`)

## design-choices (1 claim(s))

- [observation/documented] The API docs state the server can be extended with additional JSON-RPC methods by editing main.rs and registering them, citing language-server-protocol integration or MCP support as example use cases. -- evidence: [docs/src/api.md#L602-L602](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L602-L602) (`clm_8d2e9bbfc045e4d13132539c6bce05481791cbc8e4cf66c1f532e07205886c69`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are asked to comment on an existing issue or open a new one before starting work, and to fill out the pull-request template and link it to the relevant issue. -- evidence: [CONTRIBUTING.md#L11-L12](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/CONTRIBUTING.md#L11-L12), [CONTRIBUTING.md#L5-L9](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/CONTRIBUTING.md#L5-L9) (`clm_024c245d3b55a35ca5eaf22aac44009ac35ea9a636dacbcbfe967e1ec4814cec`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The documented get_tasks method returns each task's id, description, status, tool count, and separate input and output token counts. -- evidence: [docs/src/api.md#L155-L163](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L155-L163) (`clm_f4d6ef52c761d440c13bde67502350cfdd03d2ff01b6822d842bc1d65e6c1692`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The API docs state the server has no built-in authentication and should be treated as a trusted component, recommending a sandboxed deployment and passing model API keys through environment variables. -- evidence: [docs/src/api.md#L595-L598](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L595-L598) (`clm_1ef04899217fa6667c30c97a3de62703f1d78382fa0be15dc5f95d2b6724bcb0`)

## evaluation (1 claim(s))

- [observation/documented] A documented benchmark methodology measures how efficiently each tool performs against local Ollama models using simple test cases, with the results table automatically refreshed by the CI/CD pipeline on new pull requests. -- evidence: [docs/src/benchmark.md#L8-L9](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/benchmark.md#L8-L9), [docs/src/benchmark.md#L13-L13](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/benchmark.md#L13-L13) (`clm_27430597a1d2dc7682c78899f7f77ea6da992a5c081e3f065a607c12f559efd8`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The README carries an explicit warning that the project is at a very early stage and prone to bugs and issues, asking users to report problems as they hit them. -- evidence: [README.md#L22-L22](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/README.md#L22-L22) (`clm_de7eada43deae50963ea2987d6fb52d741ec875dd7ed7505ee273d34c2f9e1cd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

