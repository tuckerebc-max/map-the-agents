# jondot/picocode -- full detail

[Back to orientation](picocode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jondot/picocode/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/850b47d6cc5a3e69.json](../../../wiki/dossiers/jondot/picocode/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/850b47d6cc5a3e69.json)

## specifications (1 claim(s))

- [observation/documented] picocode is described as a minimal, high-performance coding agent written in Rust, shipped as a single compact binary. -- evidence: [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44), [README.md#L10-L10](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L10-L10) (`clm_a5c5965e9cab445f0f34d1af726a622b4877421aad113580c00ea30293b7a0da`)

## components (1 claim(s))

- [observation/documented] The agent exposes filesystem tools (read/write/edit/list/make/remove/move/copy), grep_text, glob_files, a bash tool, and an optional agent_browser for web automation. -- evidence: [README.md#L115-L118](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L115-L118) (`clm_ccbff68f23d69cb924e9c2661ef1d47b1ad94efea05c2799241e888ad5b0ede0`)

## design-choices (2 claim(s))

- [observation/documented] Users can switch expert personas (e.g., architect, security, zen) via --persona to change how the agent thinks and speaks. -- evidence: [README.md#L50-L64](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L50-L64), [README.md#L48-L48](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L48-L48), [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44) (`clm_85b57fc66a9f15f3cffbe78022bf4a393fc52ac1691966376af82f4addeadc08`)
- [observation/documented] A local AGENTS.md file can supply the agent with custom codebase-specific instructions. -- evidence: [README.md#L66-L67](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L66-L67) (`clm_ac74669940cd19dc0fe52b71e454f476efa55f547458bcd81f84d77eaca4b4b4`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: hacking on picocode requires Rust (latest stable) and a provider API key; new tools are added in src/tools.rs with #[rig_tool] and registered in src/agent.rs's build_rig_agent. -- evidence: [README.md#L126-L127](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L126-L127), [README.md#L142-L144](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L142-L144), [README.md#L122-L122](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L122-L122) (`clm_339d94fddef2798179b7138dac787df0f71c0bd853e7a20c14aec774c7d069e6`)
- [observation/documented] Repository development practice: local development uses git clone followed by cargo run to build and execute the agent. -- evidence: [README.md#L137-L138](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L137-L138), [README.md#L133-L134](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L133-L134) (`clm_08a480bc2930b2bacc5f48274268e8d41191e6f71dbb6395f12a4bd76888f3c9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI offers interactive chat (default), single-prompt mode, and a recipe subcommand that runs named tasks from picocode.yaml. -- evidence: [README.md#L98-L100](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L98-L100), [README.md#L71-L71](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L71-L71) (`clm_ff4b68fea7d08de4c3dbe45305fd54160235a4d74249f488c3e5b373a6dc3b5b`)
- [observation/documented] Flags include --provider, --model, --yolo to disable confirmations, --quiet for piping, --persona, and --tool-call-limit with a default of 50. -- evidence: [README.md#L104-L109](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L104-L109) (`clm_ea3725fcde65690257189cc63760e826c55b9130447ef9fd300a87e89b01e48f`)
- [observation/documented] Recipes defined in picocode.yaml support inline prompts or prompt files, and can pin a persona and model per recipe. -- evidence: [README.md#L75-L79](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L75-L79), [README.md#L81-L84](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L81-L84), [README.md#L88-L90](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L88-L90) (`clm_0e735734f6479d252b30488b3007fa0a1c0b7d751afcf8c10b3b4e5bcdb2ec7e`)
- [observation/documented] The crate is structured as a library plus binary; library users call create_agent with an AgentConfig specifying provider, model, output, yolo, and tool_call_limit. -- evidence: [README.md#L159-L161](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L159-L161), [README.md#L167-L178](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L167-L178), [README.md#L155-L155](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L155-L155) (`clm_cf4ccd84e5b8029ef451eea565288dbdd3f5538911aa5175799dff445ec5da41`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Destructive actions such as deleting files or running shell commands require manual confirmation by default; --yolo disables all confirmation prompts. -- evidence: [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44), [README.md#L104-L109](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L104-L109) (`clm_18badee181a23da5e332ec19866d246bd71de86391e684ed570e54de5c23ae22`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Multi-provider LLM support (Anthropic, OpenAI, DeepSeek, Google, Ollama, and others) is provided via the Rig library. -- evidence: [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44), [README.md#L122-L122](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L122-L122) (`clm_4cebaceae44e5ebbfa28efaa6ec0feb6e0c486656b60527d47542cc9d3730792`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

