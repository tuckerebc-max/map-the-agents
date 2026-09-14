# bhouston/mycoder -- full detail

[Back to orientation](mycoder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bhouston/mycoder/774e068e5daefab9c18bac898521d238dd12c794/3e0884f69cea3872.json](../../../wiki/dossiers/bhouston/mycoder/774e068e5daefab9c18bac898521d238dd12c794/3e0884f69cea3872.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is a monorepo with packages for the CLI (mycoder), the agent module (mycoder-agent), and a documentation website (mycoder-docs). -- evidence: [README.md#L181-L183](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L181-L183) (`clm_5315fed80e403e031415a87be7d61065f669cdd77f6b123459b8e3d1e044358e`)

## design-choices (1 claim(s))

- [observation/documented] A system browser detection feature lets MyCoder use installed Chrome, Edge, Firefox and other browsers on Windows, macOS, and Linux, falling back to Playwright's bundled browsers when none is found. -- evidence: [README.md#L230-L233](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L230-L233), [README.md#L226-L226](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L226-L226) (`clm_eb8936d9ebfd494ca25f96b9b5b51bf201eec1762595c9c87890db0d1f92d7ec`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run pnpm install/build/test/commit, and releases follow Conventional Commits with an automated CI/CD pipeline that versions, generates a changelog, creates a GitHub Release, tags, and publishes to NPM after PR review and merge to main. -- evidence: [README.md#L207-L207](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L207-L207), [README.md#L199-L199](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L199-L199), [README.md#L196-L196](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L196-L196), [README.md#L209-L216](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L209-L216), [README.md#L189-L190](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L189-L190), [README.md#L193-L193](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L193-L193), [README.md#L202-L203](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L202-L203) (`clm_7dbd129df1bbcaccdda3283960c665d4fb75adcc50e55ffb18ec1923991db512`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] MyCoder is a command-line interface for AI-powered coding tasks, installable globally via npm. -- evidence: [README.md#L3-L3](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L3-L3), [README.md#L21-L23](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L21-L23) (`clm_13727861b09edf775d51e1eeed662317e425bd2f693da1590234cbb99a45e2b0`)
- [observation/documented] The CLI supports interactive mode (-i), prompt arguments, prompt files (-f), an --interactive correction mode, and flags like --userPrompt false and --upgradeCheck false for automated runs. -- evidence: [README.md#L37-L37](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L37-L37), [README.md#L34-L34](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L34-L34), [README.md#L43-L43](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L43-L43), [README.md#L31-L31](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L31-L31), [README.md#L46-L47](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L46-L47), [README.md#L40-L40](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L40-L40) (`clm_8fe42009510d3705d71eabb048e566865ff15528ab82f674c9c1c9f7ede94c0b`)
- [observation/documented] Configuration is resolved from multiple locations in precedence order (project-root mycoder.config.js variants, .mycoder.rc, package.json 'mycoder' field, XDG user config) and supports many file formats; CLI arguments override config-file settings. -- evidence: [README.md#L65-L65](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L65-L65), [README.md#L51-L51](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L51-L51), [README.md#L57-L63](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L57-L63), [README.md#L131-L131](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L131-L131) (`clm_147e89f771065bcc89af4309e8e6c133022464e0e817f742b562d29e6e2bbf6f`)
- [observation/documented] Users can define custom CLI commands in mycoder.config.js with description, args, and an execute function returning a prompt string; execute may be asynchronous, and custom commands cannot override built-ins. -- evidence: [docs/custom-commands.md#L42-L48](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/docs/custom-commands.md#L42-L48), [docs/custom-commands.md#L92-L93](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/docs/custom-commands.md#L92-L93), [docs/custom-commands.md#L3-L3](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/docs/custom-commands.md#L3-L3), [docs/custom-commands.md#L14-L22](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/docs/custom-commands.md#L14-L22), [docs/custom-commands.md#L67-L67](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/docs/custom-commands.md#L67-L67) (`clm_811cf508b2c3e73d3cce56d7d48563df557bc2aecbb3f626831628140d6d4194`)
- [observation/documented] MyCoder supports Model Context Protocol (MCP) server configuration with named servers, bearer auth, default resources, and default tools, plus a GitHub mode for working with issues and PRs including /mycoder comment commands. -- evidence: [README.md#L7-L15](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L7-L15), [README.md#L165-L165](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L165-L165), [README.md#L113-L129](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L113-L129), [README.md#L167-L169](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L167-L169) (`clm_b21356fc24fb5c7571891599b88c9be6e6559adc28e51fbfafcacf4de4c3f53f`)
- [observation/documented] With --interactive, users can press Ctrl+M during execution to send corrections to the running agent, which incorporates them into its decision-making; this can also be enabled via an 'interactive: true' config option. -- evidence: [README.md#L145-L147](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L145-L147), [README.md#L135-L135](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L135-L135), [README.md#L155-L161](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L155-L161), [README.md#L149-L149](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L149-L149) (`clm_fc9ecd126a7b8c1590632529267490703f00ea2de01aa20141f8960d264b2723`)

## memory-state (1 claim(s))

- [observation/documented] Status updates are sent every 5 interactions and when token usage exceeds 50%, and above 70% usage the agent is reminded to use the compactHistory tool, which summarizes all but a configurable number of recent messages. -- evidence: [example-status-update.md#L36-L36](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L36-L36), [example-status-update.md#L50-L50](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L50-L50), [example-status-update.md#L42-L48](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L42-L48), [example-status-update.md#L28-L28](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L28-L28) (`clm_ecf349c0bd1940a90fbc41b5f8c43b29846c156987b03855a328e2adb04fecae`)

## orchestration (1 claim(s))

- [observation/documented] MyCoder can spawn sub-agents for concurrent task processing, and status updates report active sub-agents, shell processes, and browser sessions. -- evidence: [example-status-update.md#L30-L34](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L30-L34), [README.md#L7-L15](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L7-L15), [example-status-update.md#L10-L12](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L10-L12), [example-status-update.md#L19-L20](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L19-L20), [example-status-update.md#L14-L17](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L14-L17) (`clm_bf5de17e4dedac00ffd37fe9c375666165e1cc9882790d81103535113734962e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The agent leverages Anthropic's Claude, OpenAI models, and Ollama, and uses Playwright for browser automation, which normally requires separate browser installation. -- evidence: [README.md#L7-L15](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L7-L15), [README.md#L222-L222](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L222-L222) (`clm_8d4a16d014f6a851e63fb00ead2cbe9f5c82a76b88cbef174bf913669e57d5db`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

