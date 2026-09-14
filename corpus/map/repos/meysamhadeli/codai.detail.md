# meysamhadeli/codai -- full detail

[Back to orientation](codai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/meysamhadeli/codai/4949b5ccfab7312d0527235ceb4b45ca39d437df/afc03d192cf149bb.json](../../../wiki/dossiers/meysamhadeli/codai/4949b5ccfab7312d0527235ceb4b45ca39d437df/afc03d192cf149bb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The README states codai summarizes full project context using Tree-sitter. -- evidence: [README.md#L21-L21](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L21-L21) (`clm_136f5959512b0b1b3b47a040f9fbe09485f16c53af82f2c84b50a6143134ed98`)

## design-choices (2 claim(s))

- [observation/documented] A .codai-gitignore file in the working directory root lets users specify files codai should ignore. -- evidence: [README.md#L101-L101](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L101-L101), [README.md#L103-L105](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L103-L105) (`clm_e855b8712a0a9872c789a642884dd3cedfb61cea464cc4fe31f6be8cb1d6fe01`)
- [observation/documented] The README claims context-aware code completions and per-session maintenance of conversational and code context. -- evidence: [README.md#L17-L17](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L17-L17), [README.md#L19-L19](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L19-L19) (`clm_c2cf56ce38fb284e25d0a636aa8ce7f29d12f2593321324ade2fa5bb3c73de58`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Advertised coding capabilities include adding features or tests, refactoring, describing and suggesting bug fixes, code review assistance, applying AI-generated changes, and generating documentation. -- evidence: [README.md#L25-L25](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L25-L25), [README.md#L29-L29](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L29-L29), [README.md#L31-L31](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L31-L31), [README.md#L27-L27](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L27-L27), [README.md#L23-L23](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L23-L23), [README.md#L33-L33](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L33-L33) (`clm_bd293867aa018a52465bad51d9e4d0fa75c9d2172e804131e37a116b6a1f152e`)

## interfaces (5 claim(s))

- [observation/documented] Codai is described as an AI coding agent that runs in the terminal, invoked with the command 'codai code' from a working directory. -- evidence: [README.md#L8-L8](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L8-L8), [README.md#L110-L113](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L110-L113), [README.md#L108-L108](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L108-L108) (`clm_b9100d79b6269b6ade9da5aea61367409065c0e7222473ccf49aeea67bb83e86`)
- [observation/documented] Users select an LLM provider with a '--provider' flag and a model with '--model'; OpenAI is stated as the default provider, with listed providers including Ollama, Azure OpenAI, Anthropic, Gemini, Mistral, Grok, Qwen, DeepSeek, and OpenRouter. -- evidence: [README.md#L58-L69](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L58-L69) (`clm_75840d18cec57e0bd8531d0ebfbeb2ee28f2bb455e782e2e9560c1c5c3fa7bc9`)
- [observation/documented] Configuration can come from a codai-config.yml in the working directory root, from environment variables, or via CLI flags such as --config, --provider, --temperature, and --api_key; defaults apply when no config file is present. -- evidence: [README.md#L90-L98](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L90-L98), [README.md#L88-L88](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L88-L88), [README.md#L72-L72](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L72-L72) (`clm_fee646cc0f110e72d051eb5fba9962812a6a6e507441b331524ca8babe6736c8`)
- [observation/documented] The config file supports provider, base_url, model, optional api_version, temperature, and reasoning_effort fields, plus a theme setting; themes come from the Chroma style gallery. -- evidence: [README.md#L76-L86](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L76-L86), [README.md#L103-L105](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L103-L105) (`clm_f505377e1017a89616602a33dedbc65d55d62dd622f44cb9a3ed8cb202ca73eb`)
- [observation/documented] The README claims codai can modify several files at once and tracks and displays token consumption for each request. -- evidence: [README.md#L39-L39](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L39-L39), [README.md#L41-L41](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L41-L41) (`clm_69caefed51c7f3d1bc147cad55f4725f707d3757499f11421f6b0eb0a11a6cc7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project is written in Go, with a badge indicating a required Go version of at least 1.23. -- evidence: [README.md#L1-L4](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L1-L4) (`clm_26ea4b8e4c96bb4befa91c80c196032521164a30da2b4dd579d2876f78b190e5`)
- [observation/documented] Codai can be installed globally via 'go install github.com/meysamhadeli/codai@latest'. -- evidence: [README.md#L46-L48](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L46-L48), [README.md#L44-L44](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L44-L44) (`clm_1c24b8dc5bbd7045ef5daad7ecc91586c5ec125bdf6122babc2b6ee3f3b5972f`)

## limitations (1 claim(s))

- [observation/documented] The README notes the project is a work in progress with new features to be added over time. -- evidence: [README.md#L116-L116](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L116-L116) (`clm_4af639c9eed63220200c112e982f2dff31a53644741a2dacf1d3b05c163d2073`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

