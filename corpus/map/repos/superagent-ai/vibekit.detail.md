# superagent-ai/vibekit -- full detail

[Back to orientation](vibekit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/superagent-ai/vibekit/c670afd2e332037cd591209b7df1ff48ab7162ee/0959511238b49f06.json](../../../wiki/dossiers/superagent-ai/vibekit/c670afd2e332037cd591209b7df1ff48ab7162ee/0959511238b49f06.json)

## specifications (2 claim(s))

- [observation/documented] VibeKit is described as a TypeScript SDK for running AI coding agents (Claude, Codex, Gemini, OpenCode) in secure sandboxes with GitHub integration. -- evidence: [LLM.md#L4-L4](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L4-L4) (`clm_69578c6cef61e07b6ae58db8535d69a7faece0a88d01872ac8df0344f2bf4f01`)
- [observation/documented] The core package is @vibe-kit/vibekit at version 0.0.43 with main entry dist/index.js. -- evidence: [LLM.md#L6-L8](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L6-L8) (`clm_06bb76789dfc3e916b0109c921b13b6eb23f90a16f7f92d1488d4dee025098de`)

## components (1 claim(s))

- [observation/documented] The README advertises related packages installable as @vibe-kit/sdk (run coding agents in secure sandboxes) and @vibe-kit/auth (handle authentication flows for VibeKit-powered applications). -- evidence: [README.md#L48-L48](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L48-L48), [README.md#L50-L52](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L50-L52), [README.md#L59-L61](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L59-L61), [README.md#L63-L63](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L63-L63), [README.md#L57-L57](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L57-L57) (`clm_6aa1bc9760bd5f3025e1ca6853338fa824fd31283901a480bb54f2347d0f4f59`)

## design-choices (2 claim(s))

- [observation/documented] The CLI positions itself as a safety layer: it runs agent output in isolated Docker containers locally, auto-redacts secrets and API keys, and provides observability via real-time logs, traces, and metrics. -- evidence: [README.md#L32-L32](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L32-L32), [README.md#L36-L36](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L36-L36), [README.md#L34-L34](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L34-L34) (`clm_4d8ade6f032e585ff1b1867a0830685d98e720922af745138e0939760ba18cf6`)
- [observation/documented] The CLI claims to work entirely offline and locally with no cloud dependencies, and to support Claude Code, Gemini CLI, Grok CLI, Codex CLI, OpenCode, and more. -- evidence: [README.md#L40-L40](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L40-L40), [README.md#L38-L38](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L38-L38) (`clm_854517df0732636e175bcfcb5e1642a2907a480af35a3cb61fbc533cfd395f31`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The SDK uses a builder pattern: new VibeKit() configured via withAgent (type, provider, apiKey, model), withSandbox, withGithub, withSecrets, and withWorkingDirectory. -- evidence: [LLM.md#L263-L274](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L263-L274), [LLM.md#L40-L52](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L40-L52), [LLM.md#L94-L107](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L94-L107) (`clm_1a03d8f7ebe2fd511a51c2b51785c7078dc7761c1aa4d92dc0ae29b4b84cced9`)
- [observation/documented] Documented SDK methods include generateCode(prompt, mode) with 'code' or 'ask' modes, executeCommand, getHost(port), pause, resume, createPullRequest, and kill. -- evidence: [LLM.md#L113-L117](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L113-L117), [LLM.md#L291-L293](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L291-L293), [LLM.md#L286-L289](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L286-L289), [LLM.md#L279-L280](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L279-L280), [LLM.md#L63-L67](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L63-L67), [LLM.md#L119-L126](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L119-L126), [LLM.md#L282-L284](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L282-L284) (`clm_657aa16d28ceeacc66b5e731fad36e26a1e856498ff0af666df1ec2715583279`)
- [observation/documented] The SDK exposes event listeners via .on('update') and .on('error') for streaming progress and errors. -- evidence: [LLM.md#L276-L277](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L276-L277), [LLM.md#L54-L57](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L54-L57), [LLM.md#L59-L61](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L59-L61), [LLM.md#L109-L111](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L109-L111) (`clm_0e9f065cdf2484fe05d6b3b70664c9a3b0b93767e7f9425889f11527a1449b93`)
- [observation/documented] The SDK is documented as fully typed with TypeScript definitions, exporting types such as VibeKit, AgentResponse, AgentType, ModelProvider, and per-provider config types. -- evidence: [LLM.md#L573-L575](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L573-L575), [LLM.md#L585-L588](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L585-L588), [LLM.md#L581-L583](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L581-L583), [LLM.md#L569-L571](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L569-L571), [LLM.md#L559-L559](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L559-L559), [LLM.md#L561-L567](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L561-L567), [LLM.md#L577-L579](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L577-L579) (`clm_f75c71fdbafcf0cd881c6b47ec33712830ef9b89af499a6ccf7306ca5c0066a2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Sandbox providers are separate packages: @vibe-kit/e2b, @vibe-kit/daytona, @vibe-kit/northflank, @vibe-kit/cloudflare (Workers only), and @vibe-kit/modal. -- evidence: [LLM.md#L22-L27](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L22-L27), [LLM.md#L10-L15](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L10-L15) (`clm_2d356680516396ac4bd74b9fa23af0464fac7f7bb24a977270aba83a8876a183`)
- [observation/documented] Common environment variables include OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, E2B_API_KEY, DAYTONA_API_KEY, NORTHFLANK_API_KEY, and GITHUB_TOKEN. -- evidence: [LLM.md#L546-L553](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L546-L553) (`clm_13ca6cdd1bebbe1eb04971d6171499b0bf4e64ab2be3562bbf571eef5fa22d3d`)

## limitations (1 claim(s))

- [observation/documented] Cloudflare sandboxes only work inside Cloudflare Workers and cannot be used in regular Node.js applications or other environments; they use Durable Object bindings instead of API keys. -- evidence: [LLM.md#L297-L297](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L297-L297), [LLM.md#L502-L508](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L502-L508), [LLM.md#L555-L555](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L555-L555) (`clm_e3930ee3d6991f6f0073ce384a48e199b5e2ae7b6cae66b1cc93d16496d1b4aa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

