# microsoft/amplifier -- full detail

[Back to orientation](amplifier.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/microsoft/amplifier/28588b93886dd4b134f131294ca98e944d71cbfd/4ae0b5b7a1d69299.json](../../../wiki/dossiers/microsoft/amplifier/28588b93886dd4b134f131294ca98e944d71cbfd/4ae0b5b7a1d69299.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Bundles are composable configuration packages defining tools, providers, agents, and behaviors; the default 'foundation' bundle includes filesystem, bash, web, search, and task-delegation tools plus 14 specialized agents. -- evidence: [README.md#L258-L258](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L258-L258), [README.md#L242-L242](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L242-L242), [README.md#L260-L262](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L260-L262) (`clm_a26993efb185ee35ced6adbddb41155da058d46c48382d1e514300c4bc200c94`)
- [observation/documented] The architecture distinguishes a provider module (a vendor-protocol adapter) from configured provider instances, so one module can back multiple instances with unique IDs, accounts, models, and priorities. -- evidence: [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L62-L64](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L62-L64), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L72-L76](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L72-L76), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L68-L70](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L68-L70) (`clm_dd0b22ed9f0d7ab2c083cd5146fc9df32524619e98c6b7e4397e831b45158a1f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Amplifier is a command-line AI assistant with a modular, extensible architecture; the CLI is described as just one reference interface for the underlying modular platform. -- evidence: [README.md#L15-L15](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L15-L15), [README.md#L17-L17](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L17-L17) (`clm_d5560c1df3035c0971e1a927de12d61acbb413349ee2fccb3e24ae8cf52713dc`)
- [observation/documented] Chat mode persists context across messages and offers slash commands (/help, /tools, /agents, /status, /config) plus /think and /do to toggle plan mode; single-shot use is via 'amplifier run'. -- evidence: [README.md#L221-L225](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L221-L225), [README.md#L231-L231](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L231-L231) (`clm_feafbfee899df31c306b17cb804cd51a9f235c122792c03ee0ff551bfe567138`)
- [observation/documented] Providers are switched with commands like 'amplifier provider use openai' or explicit flags such as --model and --deployment; bundles are added and activated with 'amplifier bundle add' and 'amplifier bundle use'. -- evidence: [README.md#L59-L60](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L59-L60), [README.md#L196-L196](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L196-L196), [README.md#L63-L64](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L63-L64), [README.md#L199-L201](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L199-L201) (`clm_5f23cd0a1d1cc5075c6b7f5409d2ff64849371e5a57f4c56bc2b863ad3580245`)

## memory-state (1 claim(s))

- [observation/documented] Every interaction is automatically saved and sessions are project-scoped; users can list sessions for the current project or across all projects with 'amplifier session list' and its --all-projects flag. -- evidence: [README.md#L291-L291](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L291-L291), [README.md#L316-L316](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L316-L316), [README.md#L301-L301](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L301-L301), [README.md#L304-L304](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L304-L304) (`clm_d99c7d6b39df0f0d2203b1679d7f215aae5e97f3991ef53793cbe136a09d03df`)

## orchestration (2 claim(s))

- [observation/documented] Delegated child sessions resolve their provider by spawn-time precedence: caller provider_preferences, then agent overlay preferences (possibly written from model_role by a routing hook), then parent mount-plan defaults. -- evidence: [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L109-L110](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L109-L110), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L112-L116](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L112-L116) (`clm_34b07f73b02a43578c752819348d39c44dc33ad06275e6004bf563c83c46b3e0`)
- [observation/documented] Routing matrices map semantic model roles to ordered provider/model candidates, but routing applies only when the composed bundle mounts a routing strategy such as the routing-matrix hook. -- evidence: [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L91-L94](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L91-L94), [docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L96-L100](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/docs/BUNDLES_PROVIDERS_ROUTING_PROJECTS.md#L96-L100) (`clm_d764a6d731b7050577da4e9535a392caad46ed70569d61df72c0fe49b643b2d6`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project builds on separate ecosystem repos: amplifier-core, a roughly 2,600-line kernel providing module protocols, session lifecycle, and hooks, and amplifier-foundation, a bundle composition library plus the default foundation bundle. -- evidence: [README.md#L401-L402](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L401-L402) (`clm_826e6306bbdac5ac13e2013ae1369de1c5a011ac42d60cea392ddc8e46e0da39`)
- [observation/documented] Supported AI providers include Anthropic Claude (recommended and most tested), OpenAI, Azure OpenAI with managed identity support, and Ollama for local free use; other providers are acknowledged as needing more testing. -- evidence: [README.md#L187-L190](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L187-L190), [README.md#L203-L203](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L203-L203), [README.md#L456-L459](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L456-L459) (`clm_cab973f079ba450cab067414c89d55ea3da7b9bb45dad0be19eed1dd998e408e`)

## limitations (1 claim(s))

- [observation/documented] The project is an early research demonstrator with safety systems not yet built in; APIs may change, some features are experimental, and native Windows shells have known issues with WSL recommended instead. -- evidence: [README.md#L23-L24](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L23-L24), [README.md#L5-L6](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L5-L6), [README.md#L441-L444](https://github.com/microsoft/amplifier/blob/28588b93886dd4b134f131294ca98e944d71cbfd/README.md#L441-L444) (`clm_f2759e7fb0653255324577daf8f08b5de9fe5a0f1806202ae13680385d6d1d50`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

