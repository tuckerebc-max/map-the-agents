# bytedance/trae-agent -- full detail

[Back to orientation](trae-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bytedance/trae-agent/e839e559ac61bdd0e057c375dd1dee391fee797d/aac655fead22ca30.json](../../../wiki/dossiers/bytedance/trae-agent/e839e559ac61bdd0e057c375dd1dee391fee797d/aac655fead22ca30.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Trae Agent supports multiple LLM providers (OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Google Gemini), and the trajectory docs reference a dedicated client module for each of these providers. -- evidence: [docs/TRAJECTORY_RECORDING.md#L86-L86](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L86-L86), [docs/TRAJECTORY_RECORDING.md#L100-L100](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L100-L100), [docs/TRAJECTORY_RECORDING.md#L30-L30](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L30-L30), [docs/TRAJECTORY_RECORDING.md#L72-L72](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L72-L72), [docs/TRAJECTORY_RECORDING.md#L58-L58](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L58-L58), [docs/TRAJECTORY_RECORDING.md#L44-L44](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L44-L44), [README.md#L19-L25](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L19-L25), [docs/TRAJECTORY_RECORDING.md#L114-L114](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L114-L114) (`clm_f44b4c51de4deb55a9aac3e6e970147178370bc2f6cb47411d791cd4edff3fae`)
- [observation/documented] The bash tool runs commands in a persistent shared session with a 120-second per-command timeout, session restart, and background process support. -- evidence: [docs/tools.md#L24-L28](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/tools.md#L24-L28) (`clm_2df7bf3c3ed690c509643939fa767b95b0a0924c496b60bb0429e0a062edb71a`)

## design-choices (2 claim(s))

- [observation/documented] Configuration is YAML-based (JSON is deprecated legacy), with priority order: command-line arguments > config file > environment variables > defaults; base_url overrides are supported. -- evidence: [docs/legacy_config.md#L3-L3](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/legacy_config.md#L3-L3), [README.md#L123-L123](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L123-L123), [README.md#L84-L84](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L84-L84), [docs/legacy_config.md#L30-L33](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/legacy_config.md#L30-L33) (`clm_7e215360a0f8501095e3442584814ada2d5210f20dbb44f5f834fc596642c8f0`)
- [observation/documented] The example YAML config enables Lakeview step summarization, sets max_steps (e.g. 200), and selects tools such as bash, str_replace_based_edit_tool, sequentialthinking, and task_done. -- evidence: [README.md#L53-L63](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L53-L63) (`clm_315cd9521dd2c6c9451354643db30468aeceae472210d97cc83e7f8aed617aaf`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the repo runs pre-commit and unit-test GitHub Actions workflows, and contributors are directed to CONTRIBUTING.md and docs/roadmap.md. -- evidence: [README.md#L13-L13](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L13-L13), [README.md#L240-L240](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L240-L240), [README.md#L3-L7](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L3-L7) (`clm_df4d90838ec52f5314868ac18a482200b4650e3375b05a8e16c542d70154cb11`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Trae Agent provides a CLI (trae-cli) that accepts natural-language task instructions and runs software engineering workflows, with 'run' and 'interactive' subcommands. -- evidence: [README.md#L133-L133](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L133-L133), [README.md#L9-L9](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L9-L9), [README.md#L139-L140](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L139-L140) (`clm_f39b61fedd65ad044dc0b7bf6aefdd90db70bb13d1c9a703fceb6ce178b59368`)
- [observation/documented] Interactive mode supports typed task descriptions plus commands: status, help, clear, and exit/quit. -- evidence: [README.md#L208-L213](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L208-L213) (`clm_eb247ec09709d329a23be035d2983ddc4b67b035123a2f218d23dde3d5ee2cea`)
- [observation/documented] CLI options include --provider/--model, --working-dir, --trajectory-file, --must-patch, and --max-steps for interactive mode. -- evidence: [README.md#L175-L175](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L175-L175), [README.md#L172-L172](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L172-L172), [README.md#L169-L169](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L169-L169), [README.md#L178-L179](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L178-L179), [README.md#L146-L146](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L146-L146) (`clm_8d9ff2c67a48ee2a2c3b4a821249a2bbb6eed4ff32372fa96ea5ca31a47cdf1a`)
- [inference/documented] A programmatic SDK with headless API access appears to be planned but not yet shipped, since it is described in the roadmap as future work. -- evidence: [docs/roadmap.md#L8-L8](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/roadmap.md#L8-L8), [docs/roadmap.md#L11-L12](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/roadmap.md#L11-L12) (`clm_aca77c8bcde55ea598c9f2f18a5093bf3fb321e960373f910eaec13071b99673`)

## memory-state (1 claim(s))

- [observation/documented] Trajectory recording captures LLM interactions, agent steps, tool usage, and metadata into JSON files, saved continuously during execution with auto-generated or custom filenames. -- evidence: [docs/TRAJECTORY_RECORDING.md#L160-L161](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L160-L161), [docs/TRAJECTORY_RECORDING.md#L320-L324](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L320-L324), [docs/TRAJECTORY_RECORDING.md#L3-L3](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L3-L3), [README.md#L234-L234](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L234-L234), [docs/TRAJECTORY_RECORDING.md#L9-L11](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L9-L11) (`clm_09ada320ed13dd01fc2804f81599c947be57293b75ae911202cf134863e3cd45`)

## orchestration (1 claim(s))

- [observation/documented] Tasks can execute inside Docker: via an image, an existing container ID, a Dockerfile path, or a local tar image file, with an option to keep or remove the container afterward; Docker must be configured in the environment. -- evidence: [README.md#L200-L200](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L200-L200), [README.md#L183-L183](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L183-L183), [README.md#L188-L188](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L188-L188), [README.md#L197-L197](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L197-L197), [README.md#L203-L204](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L203-L204), [README.md#L194-L194](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L194-L194) (`clm_86c140ba7873adb0ac6a36f922803eb3960d54f520556769c4adabc65631bf25`)

## tools-permissions (1 claim(s))

- [observation/documented] Optional MCP services can be enabled via an mcp_servers config section, e.g. launching a Playwright MCP server through npx. -- evidence: [README.md#L113-L113](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L113-L113), [README.md#L115-L121](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L115-L121) (`clm_d7eb1a524c542c93c47858311d242af219b64d3e5a806b9a2bdc230205ce3b66`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project requires Python 3.12+ and UV, and setup uses 'uv sync --all-extras' with a virtualenv; an API key for the chosen provider is also needed. -- evidence: [README.md#L30-L31](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L30-L31), [README.md#L35-L40](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L35-L40), [README.md#L3-L7](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L3-L7) (`clm_5f4ea45a578e90e98c1c9e8b44a9e9618eacb5e3f31fe248a94104c48be1b214`)

## limitations (1 claim(s))

- [observation/documented] The str_replace_based_edit_tool requires absolute paths and exact unique string matches, and its create operation fails if the file already exists. -- evidence: [docs/tools.md#L15-L18](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/tools.md#L15-L18), [docs/tools.md#L9-L13](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/tools.md#L9-L13) (`clm_1a589295bf7fb3a60afe98d632eedd5d7bdec54d280c3b7d08888a9d15ff4ca0`)

## relevance (1 claim(s))

- [observation/documented] The project positions itself as a research-friendly, modular agent platform aimed at studying agent architectures, ablation studies, and novel agent capabilities. -- evidence: [README.md#L15-L15](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L15-L15) (`clm_4c1c0ed4bfeb22f77eba3e07d6269683a6455300477ad669d76b989484861497`)

