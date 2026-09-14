# doriandarko/deepseek-engineer -- full detail

[Back to orientation](deepseek-engineer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/doriandarko/deepseek-engineer/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/2653c09f24d1c2cb.json](../../../wiki/dossiers/doriandarko/deepseek-engineer/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/2653c09f24d1c2cb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [inference/documented] The rich and prompt_toolkit dependencies suggest the color-coded, streaming terminal UI described in the README is likely built on those libraries. -- evidence: [README.md#L67-L70](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L67-L70), [requirements.txt#L1-L5](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/requirements.txt#L1-L5) (`clm_71d27dbda41d22032771baf9f574d618039ffae7ce5e285eb3e22374d4fc1cdb`)

## design-choices (2 claim(s))

- [observation/documented] Version 2.0 replaced structured JSON output with native function calling, citing natural conversation, automatic file operations, visible chain-of-thought reasoning, and better error handling. -- evidence: [README.md#L9-L13](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L9-L13) (`clm_8d719611548e97507af863eb63b7345df2535ce2844445e091bc489b84fc8f8e`)
- [observation/documented] The architecture streams three channels (reasoning, content, tool_calls), executes tools in real time during streaming, and automatically follows up after tool completion. -- evidence: [README.md#L181-L184](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L181-L184) (`clm_f69c99bfb54e2748ec1d192cd6938fed6f98d631fc92a2a01db1261118dae131`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup is via git clone, uv venv/uv sync (or pip install -r requirements.txt), and running deepseek-eng.py with uv run or python3. -- evidence: [README.md#L258-L263](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L258-L263), [README.md#L248-L253](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L248-L253), [README.md#L106-L110](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L106-L110), [README.md#L100-L104](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L100-L104), [README.md#L86-L90](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L86-L90) (`clm_cc8356b39eeaca8bbde504b8228cd4e5bb38b69b9701a28f98dbbe0f25aa9c9d`)
- [observation/documented] Repository development practice: the project is described as experimental, showcasing DeepSeek reasoning model capabilities, with contributions welcome. -- evidence: [README.md#L269-L269](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L269-L269), [README.md#L245-L245](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L245-L245) (`clm_1ef55058eaa5af441283f0aa7ce56f72037b415fee3605f5f858efeb0e0bdfeb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is an interactive terminal coding assistant integrating DeepSeek reasoning models, offering file operations, code analysis, and assistance via natural conversation and function calling. -- evidence: [README.md#L5-L5](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L5-L5) (`clm_9018ebaf615f3d694de988564c4036e3d225d0747f5ee6edab34e9ad5ee4df2d`)
- [observation/documented] An /add command lets users preload a single file or an entire directory (with smart filtering) into conversation context, complementing the AI's automatic file reading. -- evidence: [README.md#L64-L64](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L64-L64), [README.md#L60-L62](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L60-L62) (`clm_ebeef8cb079b3e5094b22e8563fe21bbce0e7e2d0f87f1ac74c0036b9e03e320`)

## memory-state (1 claim(s))

- [observation/documented] Context management includes automatic file detection from user messages, conversation cleanup to prevent token overflow, and file content preservation across history. -- evidence: [README.md#L189-L192](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L189-L192) (`clm_dc45547fad417bdf6267a9bfe966031549c2ad51c5e6eb3a05227b051f309765`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt lists openai, pydantic, python-dotenv, rich, and prompt_toolkit; the README states Python 3.11+ is required for optimal performance. -- evidence: [requirements.txt#L1-L5](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/requirements.txt#L1-L5), [README.md#L81-L82](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L81-L82) (`clm_eecabb6f369aa66ce410267c0bc161692dcdde771473aa18ac54c99cb7237ae7`)
- [observation/documented] The tool requires a DeepSeek API key, configured via a DEEPSEEK_API_KEY entry in a .env file. -- evidence: [README.md#L230-L231](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L230-L231), [README.md#L81-L82](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L81-L82), [README.md#L92-L96](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L92-L96) (`clm_124900f3f00d2970d83b13989bd7708f49f0ac731879f2417617b915d0cd354a`)

## limitations (1 claim(s))

- [observation/documented] Documented safety constraints include path normalization and validation, directory traversal protection, a 5MB per-file size limit, and binary file detection and exclusion. -- evidence: [README.md#L73-L76](https://github.com/Doriandarko/deepseek-engineer/blob/9aa7a2d3611b1af42b4cde20a00a50df25001fbb/README.md#L73-L76) (`clm_43536b8aa7915a83c820323539f577462ae87d81b00d35f279ef3cfd4dcb35fa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

