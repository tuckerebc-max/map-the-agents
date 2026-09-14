# holasoymalva/deepseek-cli -- full detail

[Back to orientation](deepseek-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/holasoymalva/deepseek-cli/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/482743830e15d71f.json](../../../wiki/dossiers/holasoymalva/deepseek-cli/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/482743830e15d71f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The setup command checks for Ollama, starts the service if needed, downloads the specified model, and verifies the installation. -- evidence: [README.md#L254-L258](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L254-L258) (`clm_54dc8ead1474aa04af021fab0527ebd6e3ffd3478aa20820cb261f510bcf471d`)
- [observation/documented] Interactive mode is described as a REPL with syntax highlighting, session history, automatic file-context inclusion, and multi-turn conversations. -- evidence: [README.md#L264-L268](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L264-L268), [README.md#L262-L262](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L262-L262) (`clm_d9b9c25e69d44e022c6ac93bc017953783a158987342ec87fd19ba537e58b69f`)

## design-choices (1 claim(s))

- [observation/documented] Local Ollama mode is the default (DEEPSEEK_USE_LOCAL defaults to true), with cloud API mode available when an API key is configured. -- evidence: [README.md#L210-L212](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L210-L212), [README.md#L189-L194](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L189-L194) (`clm_0b49e44eae0d6f75000740e730fd9bb0c31499e52951f11f4a3172b43ff0a457`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors fork and clone, run npm install, npm test, and npm run dev; building from source uses npm run build and npm run package. -- evidence: [README.md#L314-L320](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L314-L320), [README.md#L334-L337](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L334-L337), [README.md#L341-L344](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L341-L344) (`clm_285caf2684ad69c68f08dd3bf292f5e471e5a4e54de134aa96a10d34849672f0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands including interactive mode (deepseek), single-prompt mode (deepseek chat), setup, --local, --model, --help, and --version. -- evidence: [README.md#L236-L244](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L236-L244) (`clm_9e3ca3eb82627843c6e15e661055d3f76d90d809f79d54b19c967792f01bc761`)
- [observation/documented] Repository context can be controlled via flags such as --include-all for the whole repo and --include with specific files or directories. -- evidence: [README.md#L282-L284](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L282-L284), [README.md#L278-L279](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L278-L279) (`clm_9d59647431191d78e427360bbdb7cbdae2094d0d0f7131fb9b6dd4fc66beddc1`)
- [observation/documented] A --ollama-host flag lets users point the CLI at a custom Ollama server URL, e.g. a remote host on the LAN. -- evidence: [LOCAL-SETUP.md#L125-L126](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/LOCAL-SETUP.md#L125-L126) (`clm_dcc7e99694ef5f102d29380e020b52d19d47e78e9a8bfe9411026ef58579466a`)

## memory-state (1 claim(s))

- [observation/documented] The CLI maintains context across interactions in multi-turn conversations and automatically includes relevant project files as context. -- evidence: [README.md#L274-L274](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L274-L274), [README.md#L264-L268](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L264-L268) (`clm_62fcda64728896ed31da080e7c2e724c24c8bf511400a65fc2d66ebc779f6061`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool requires Node.js 18 or higher and Ollama for local operation; the npm package is run-deepseek-cli installed globally. -- evidence: [README.md#L23-L25](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L23-L25), [README.md#L38-L41](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L38-L41) (`clm_8e8c81f1842663578b7239f0dccdf34ef0585f5afd2988aec1a945aa647a96ce`)
- [observation/documented] It uses DeepSeek Coder models in 1.3B, 6.7B, and 33B sizes, with documented RAM needs of 2GB, 8GB, and 32GB respectively. -- evidence: [LOCAL-SETUP.md#L15-L20](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/LOCAL-SETUP.md#L15-L20), [README.md#L198-L202](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L198-L202), [README.md#L366-L368](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L366-L368) (`clm_3709556df144f9e03e1d826f757a93068fb82e85577181c9d2b036acdae5969c`)

## limitations (1 claim(s))

- [observation/documented] Documented model context windows are 16K tokens for the 1.3b, 6.7b, and 33b instruct variants, and the 33b model is noted as slower. -- evidence: [README.md#L356-L360](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L356-L360) (`clm_ed3777558493ccb1fbf7d1877f1d1fb0383571cad9e1ab4c254a48311be1056c`)

## relevance (1 claim(s))

- [observation/documented] The project is a command-line AI coding assistant for code generation, refactoring, debugging, review, and scaffolding, built on Gemini CLI's foundation and DeepSeek Coder models. -- evidence: [README.md#L8-L8](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L8-L8), [README.md#L12-L17](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L12-L17), [README.md#L432-L434](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L432-L434) (`clm_23a99ad150f103d31f45d2502bc2a64c40907e9686cf88b1ec1cb1dad0732cf7`)

