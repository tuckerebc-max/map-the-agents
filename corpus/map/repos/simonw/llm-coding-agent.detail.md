# simonw/llm-coding-agent -- full detail

[Back to orientation](llm-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/simonw/llm-coding-agent/01dbde5897fcfe2841ecf7882203d8cf6e099b59/0a77211a52823127.json](../../../wiki/dossiers/simonw/llm-coding-agent/01dbde5897fcfe2841ecf7882203d8cf6e099b59/0a77211a52823127.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] CodingTools is an llm.Toolbox confined to a root directory providing read_file, write_file, edit_file, list_files, search_files, and execute_command tools. -- evidence: [README.md#L111-L113](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L111-L113), [README.md#L102-L105](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L102-L105), [README.md#L86-L86](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L86-L86), [README.md#L91-L96](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L91-L96) (`clm_77c31256546cc921ba24364dc1db10558798a76b2e05b6d3f52701f826c9df48`)

## design-choices (3 claim(s))

- [observation/documented] edit_file performs exact string replacement requiring old_string to appear exactly once unless replace_all is set, and returns a unified diff so the model can verify its edit. -- evidence: [README.md#L98-L98](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L98-L98), [spec.md#L125-L130](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L125-L130) (`clm_2c1c5848689dbe4f5688bfedf3b1342d78ee8fd27a944634004f90efa1827a65`)
- [observation/documented] All file access is confined to the session root: paths escaping via '..', absolute paths, or symlinks return an 'Error:' string instead of content, letting the model self-correct. -- evidence: [spec.md#L99-L103](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L99-L103), [README.md#L117-L117](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L117-L117) (`clm_01e602b4a3b3c60f70407054fd9b8dbfb7f0bc9c6a149bd07577933ebe8e0ac9`)
- [inference/documented] search_files appears to use ripgrep when installed with a pure-Python fallback producing identical output; list_files reportedly respects .gitignore, delegating to git ls-files when available. -- evidence: [README.md#L107-L107](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L107-L107), [spec.md#L134-L138](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L134-L138), [spec.md#L142-L144](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L142-L144) (`clm_d5646bd937c74811f9b3f8697396fc75138c43621b9eb60ac2686a896068a30f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors create a virtualenv, install with `python -m pip install -e '.[test]'`, and run tests via `python -m pytest`. -- evidence: [README.md#L121-L134](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L121-L134) (`clm_933b7538f182d389a8a6f45f7f4832787bb3819eb9e261eda01d65ce6550c0ee`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Installing the package as an LLM plugin adds an `llm code` command that starts an interactive coding agent session in the current directory with any tool-capable model LLM supports. -- evidence: [README.md#L30-L30](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L30-L30) (`clm_05a130e5c22ae8f56894e63c7adbc40240b8c70ecb7926309e1f96f2b2008b3c`)
- [observation/documented] The `llm code` CLI accepts options including an initial prompt, -m/--model, -s/--system, -d/--directory, --yolo, repeatable --allow glob patterns, --no-tool, -c/--continue, --cid, -o model options, and --chain-limit. -- evidence: [spec.md#L56-L68](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L56-L68), [README.md#L32-L38](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L32-L38) (`clm_3b973c5f241e60d897fa48bc5fceb0613d81ffe76c19e9fa6ef59c839a042462`)
- [observation/documented] A Python API exposes CodingAgent with model, root, approve, and chain_limit parameters; run() returns final text plus tool call/result pairs, and subsequent run() calls continue the same conversation. -- evidence: [README.md#L73-L74](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L73-L74), [spec.md#L223-L233](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L223-L233), [README.md#L63-L71](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L63-L71) (`clm_ead4edc1fbfe73e19563b5d0b12b3892066e45adec7c08ece3fb294e4f3d1ccb`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are logged to LLM's SQLite database like `llm chat`, so `llm logs` shows full transcripts including tool calls, and conversations can be resumed via -c or --cid. -- evidence: [spec.md#L87-L88](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L87-L88), [README.md#L42-L42](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L42-L42), [README.md#L44-L48](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L44-L48) (`clm_32ed866bcd5a9f97c53a291aabbd26ec1f96a6bc3e8608f9f366cd3b7c11ced8`)

## orchestration (1 claim(s))

- [observation/documented] The agent loop uses conversation.chain with a chain_limit (default 25) bounding tool-execution rounds per run; hitting the limit sets result.hit_limit and returns control to the user. -- evidence: [README.md#L82-L82](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L82-L82), [spec.md#L209-L216](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L209-L216) (`clm_ba6ecd1deaba4c0493baada9920faa08f560a8dba835e9484a48deda377495b2`)

## tools-permissions (2 claim(s))

- [observation/documented] Read-only tools run freely, while writes, edits, and shell commands require approval; 'y' approves once, 'a' approves similar actions for the session, and denial is reported back to the model. -- evidence: [spec.md#L173-L183](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L173-L183), [README.md#L40-L40](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L40-L40) (`clm_37698841144f6e248c0570549c1451204410ec42d3e5e15ea26e0dcbea3b680c`)
- [observation/documented] The permission system is implemented as a before_call callback on the chain (raising llm.CancelToolCall on denial), with --allow patterns and --yolo skipping prompts; approvals are session-scoped and not persisted. -- evidence: [spec.md#L161-L161](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L161-L161), [spec.md#L173-L183](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L173-L183) (`clm_00e53cc6633f6bddee4cade1ed3598f8dc6cd73854e7f8671bd2dded45883172`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package requires Python 3.10+ and pins llm>=0.32a3, needing pip install --pre until LLM 0.32 is stable; it has no other runtime dependencies beyond what llm brings. -- evidence: [spec.md#L30-L37](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L30-L37), [spec.md#L39-L43](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L39-L43), [README.md#L22-L25](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/README.md#L22-L25) (`clm_70a40b8d7668a1e5e247e0904d1dbb2ba96dfcd85cde3b714f0ad26761eaff98`)

## limitations (1 claim(s))

- [observation/documented] The spec lists non-goals for the initial release: no sandboxing or containerization (safety comes from the approval flow), no MCP, sub-agents, git or IDE integration, and no Windows-specific shell handling. -- evidence: [spec.md#L21-L26](https://github.com/simonw/llm-coding-agent/blob/01dbde5897fcfe2841ecf7882203d8cf6e099b59/spec.md#L21-L26) (`clm_a7de350f2d97856f6fd0b7302d524d57ba3d6ed9b52bfc97373fa184b6958693`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

