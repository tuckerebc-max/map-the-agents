# blushyes/coro-code -- full detail

[Back to orientation](coro-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/blushyes/coro-code/679c57af5376166538867a0aaf0fd877067821e3/d60a9546779f7cea.json](../../../wiki/dossiers/blushyes/coro-code/679c57af5376166538867a0aaf0fd877067821e3/d60a9546779f7cea.json)

## specifications (1 claim(s))

- [observation/documented] Coro Code is described as a high-performance AI coding agent written in Rust with a rich terminal UI, formerly named Trae Agent Rust and kept compatible with the original tool spec. -- evidence: [README.md#L18-L18](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L18-L18) (`clm_6b2bbe199eda7e43e3192109650caa6134868244fe9a1875d3416af6a324589f`)

## components (1 claim(s))

- [observation/documented] The Chinese README lists built-in tools including bash, edit, json_edit, thinking, task_done, ckg, and mcp, plus Git-aware file search using @path syntax. -- evidence: [README_zh.md#L22-L26](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README_zh.md#L22-L26) (`clm_8ae7d19b5dcc47fc7fb6c523825502a51ab6182d7bf1fecabf67369fd8cddd1d`)

## design-choices (1 claim(s))

- [observation/documented] Config loading follows a unified priority of CLI arguments over environment variables over JSON file, marked completed in the roadmap; token compression (intelligent context compression with adaptive context windows) is also marked completed. -- evidence: [README.md#L159-L164](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L159-L164), [README.md#L136-L140](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L136-L140) (`clm_c912fb44b30d2435db819d5d54c2e0adab406608ee85ac55888f4fcab53c2b1f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are strongly recommended to install pre-commit hooks via platform-specific scripts; the hooks run cargo fmt --check, cargo clippy, and cargo test before each commit, and the contribution flow is fork, branch, change, test, PR. -- evidence: [README.md#L246-L251](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L246-L251), [README.md#L221-L221](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L221-L221), [README.md#L238-L240](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L238-L240), [README.md#L227-L227](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L227-L227) (`clm_299bcb4871abf4771455bd883ffbd2fc56e4118d300e1ca82c97dabb44a175dc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI binary is named `coro`; it can run in interactive mode or accept a single task as a direct argument, and supports a `--config` flag pointing to a custom JSON config file. -- evidence: [README.md#L98-L99](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L98-L99), [README.md#L49-L50](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L49-L50), [README.md#L46-L46](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L46-L46) (`clm_2bf0de4578b961a7d9080147bebb0561775bdc1f45f6a3352b93678b555ade3b`)
- [observation/documented] Configuration can be supplied via environment variables (OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL, and generic CORO_BASE_URL/CORO_MODEL overrides) or a `coro.json` file specifying protocol, base_url, api_key, model, and sampling params such as max_tokens, temperature, and top_p. -- evidence: [README.md#L58-L59](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L58-L59), [README.md#L74-L86](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L74-L86), [README.md#L72-L72](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L72-L72), [README.md#L66-L68](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L66-L68), [README.md#L62-L63](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L62-L63) (`clm_9556d28f055dbb68eb513c67ac54ecd299e619901ede627f5e45fa05d951b44a`)

## memory-state (2 claim(s))

- [observation/documented] The core library supports exporting conversation and execution context to JSON (as a string, a file such as .coro/context.json, or a structured snapshot) and restoring it later via agent APIs like export_context_json and restore_context_from_file, exposed through coro_core::agent. -- evidence: [README.md#L206-L211](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L206-L211), [README.md#L198-L200](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L198-L200), [README.md#L195-L196](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L195-L196), [README.md#L193-L193](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L193-L193), [README.md#L202-L204](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L202-L204) (`clm_0f116f8b5d9380e50baa0615aa1d61b658932cce2261651b1cb711c007107da5`)
- [observation/documented] The persistence snapshot contains conversation_history, AgentExecutionContext, and optional AgentConfig; on restore the saved config is applied, unpaired tool results are handled automatically, and system prompts are re-injected by the agent as needed. -- evidence: [README.md#L215-L217](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L215-L217) (`clm_420a3d43d798aa7969f8186ffea262c5ab3bd41ee42e5e2a00cda3239737d957`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] A tool-call permission system (tool/command/directory whitelists, interactive confirmation, sensitive-operation warnings) appears only as a planned roadmap item, not as a shipped capability. -- evidence: [README.md#L136-L140](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L136-L140) (`clm_06225f693747db933d7f3136a0f65b449f8d374b452d1e86ebd72186503c2520`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] Installation is via `cargo install --git https://github.com/Blushyes/coro-code --bin coro`; prerequisites are Rust stable 1.70+ and an API key, with OpenAI recommended and Anthropic/Google noted as coming soon. -- evidence: [README.md#L38-L40](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L38-L40), [README.md#L33-L34](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L33-L34) (`clm_2f711fbe0e5285214b5d14384f3dc2a0c4c3b5c9e3a221706edebbaa9d95db18`)
- [observation/documented] Only OpenAI (gpt-4o, gpt-4o-mini) is listed as ready; Anthropic claude-3.5 and Google gemini-1.5 support are marked as coming, though env vars for those providers and Azure OpenAI are documented. -- evidence: [README.md#L111-L127](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L111-L127), [README.md#L103-L107](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L103-L107) (`clm_2a3c2c4b2f8c94a65c35ec5d90604f76d1f282c34cff9f412414967faebee801`)
- [observation/documented] The project is dual licensed under MIT and Apache-2.0, and credits Trae Agent (original Python implementation and spec), the iocraft terminal UI framework, and model APIs from OpenAI, Anthropic, and Google. -- evidence: [README.md#L262-L265](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L262-L265), [README.md#L257-L258](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L257-L258), [README.md#L255-L255](https://github.com/Blushyes/coro-code/blob/679c57af5376166538867a0aaf0fd877067821e3/README.md#L255-L255) (`clm_f124beb60ff6aae401d9d3922073e0ecaa34d8b4c177492d1ee4b36b0a82b757`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

