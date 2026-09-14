# smythos/sre -- full detail

[Back to orientation](sre.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/smythos/sre/5c382a1ec07accc75947c3e4fa24841532ae7c88/de590e843dd1e761.json](../../../wiki/dossiers/smythos/sre/5c382a1ec07accc75947c3e4fa24841532ae7c88/de590e843dd1e761.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The repo is a monorepo with three packages: the SRE core runtime (packages/core), the SDK (packages/sdk), and a CLI (packages/cli) for scaffolding and project management. -- evidence: [README.md#L145-L145](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L145-L145), [README.md#L114-L114](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L114-L114), [README.md#L134-L134](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L134-L134), [README.md#L110-L110](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L110-L110) (`clm_96ec5e1d914a0dba3b89a09aecc1647b96b21822254bc27e289fa8ad83de9ce6`)
- [observation/documented] SRE ships 40+ production-ready components (e.g. GenAILLM, APICall, WebSearch, Classifier, ForEach, S3, ECMAScript) invocable programmatically or via the .smyth workflow format. -- evidence: [README.md#L351-L356](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L351-L356), [README.md#L348-L349](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L348-L349) (`clm_4b6398ea7b85f7fd6db0078ef902ec5386ebefdb45a73371fc27c4735383562d`)

## design-choices (2 claim(s))

- [observation/documented] SRE provides a unified abstraction layer so all providers of a given resource type (storage, VectorDB, cache, LLM) expose the same API, letting providers be swapped without changing business logic. -- evidence: [README.md#L67-L67](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L67-L67), [README.md#L65-L65](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L65-L65), [README.md#L63-L63](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L63-L63) (`clm_df7d65bc8dedda12804ed92477e82444a70f2be2ec779cef45ec8f7873b937d8`)
- [observation/documented] SRE is implicitly initialized with default connectors (RAM cache, local storage, console log) when the SDK is used, and can be explicitly re-initialized with built-in or custom connectors for production setups. -- evidence: [README.md#L325-L333](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L325-L333), [README.md#L314-L315](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L314-L315), [README.md#L296-L303](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L296-L303), [README.md#L290-L291](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L290-L291) (`clm_be389fa9c74b794bfb6e7ce9493e5d4d0d4179324b58927ff6dcad4edbff1aeb`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors fork the repo, install dependencies with pnpm, create a .smyth (or ~/.smyth) directory with a vault.json of provider API keys, then build with pnpm build and test with pnpm test. -- evidence: [docs/core/media/CONTRIBUTING.md#L71-L73](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L71-L73), [docs/core/media/CONTRIBUTING.md#L30-L32](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L30-L32), [docs/core/media/CONTRIBUTING.md#L52-L65](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L52-L65), [docs/core/media/CONTRIBUTING.md#L34-L36](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L34-L36), [docs/core/media/CONTRIBUTING.md#L77-L79](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L77-L79), [docs/core/media/CONTRIBUTING.md#L21-L21](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L21-L21) (`clm_0fffe65a383326c6bd3040b23694aedd1333af166c6ed73aaeaafad2e58af0bd`)
- [observation/documented] Repository development practice: contributions must follow a fork-branch-PR workflow with DCO sign-off (git commit -s), clear commit messages, passing tests, and linting/formatting before submission. -- evidence: [docs/core/media/CONTRIBUTING.md#L175-L180](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L175-L180), [docs/core/media/CONTRIBUTING.md#L165-L169](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L165-L169), [docs/core/media/CONTRIBUTING.md#L156-L159](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L156-L159), [docs/core/media/CONTRIBUTING.md#L141-L144](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L141-L144), [docs/core/media/CONTRIBUTING.md#L153-L154](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L153-L154) (`clm_b445a62b5dc42ec52aadfc5827421fa9bc86b9fc1f6819763072ba7952679337`)
- [observation/documented] Repository development practice: security vulnerabilities must be reported privately by email to security@smythos.com rather than opened as public GitHub issues. -- evidence: [SECURITY.md#L12-L12](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/SECURITY.md#L12-L12), [docs/core/media/CONTRIBUTING.md#L118-L125](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/docs/core/media/CONTRIBUTING.md#L118-L125), [SECURITY.md#L14-L14](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/SECURITY.md#L14-L14) (`clm_c3c6dada5c4db197fcba661722dab2bdc317900573393f29b3da788184068e98`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The SDK exposes Agent.import to load .smyth agent files, agent.prompt for one-shot queries with a .stream() event mode, and agent.chat() for conversations that remember prior turns. -- evidence: [README.md#L208-L209](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L208-L209), [README.md#L181-L185](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L181-L185), [README.md#L158-L161](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L158-L161), [README.md#L175-L179](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L175-L179), [README.md#L196-L197](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L196-L197), [README.md#L163-L164](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L163-L164) (`clm_5b0bc25f3b0251a99ef16f7fa64e86956f39e98e5a91941f9ac368bb3951f240`)
- [observation/documented] Agents can be defined in code with new Agent({name, model, behavior}) and extended via agent.addSkill, whose process function can access agent-scoped LLM, VectorDB, and storage connectors. -- evidence: [README.md#L255-L259](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L255-L259), [README.md#L251-L253](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L251-L253), [README.md#L231-L243](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L231-L243), [README.md#L223-L229](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L223-L229) (`clm_716ab2adabeb919dc9483619000965697ff6dc00e886ecbe2686abf9c3798a9a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Every operation requires authorization through a Candidate/ACL system so agents only access resources they are permitted to; access is obtained via AccessCandidate.agent(agentId) passed to a connector. -- evidence: [README.md#L282-L286](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L282-L286), [README.md#L279-L280](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L279-L280) (`clm_a90b0f48bed624f65ef5a249f595fc35737052abf2f246cbbaa0dd536dd36738`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Documented supported connectors include storage (Local, S3, Google Cloud, Azure), LLMs (OpenAI, Anthropic, Google AI, AWS Bedrock, Groq, Perplexity), VectorDBs (Pinecone, Milvus, RAMVec), caches (RAM, Redis), and vaults (JSON file, AWS Secrets Manager, HashiCorp). -- evidence: [README.md#L126-L130](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L126-L130) (`clm_47d39bf281f7ca2b2974edc9c444ad8a8ff419bf7b1f43d338accdd579ba7e1e`)
- [observation/documented] The SDK is distributed as the npm package @smythos/sdk, with a separate @smythos/cli package recommended for creating new projects. -- evidence: [README.md#L87-L90](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L87-L90), [README.md#L98-L100](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L98-L100) (`clm_2fc9b17bed586322835bcb9bdf657c2f8c5aaf7619f0688efb20fa61613beb45`)

## limitations (1 claim(s))

- [inference/documented] Some SmythOS modules are proprietary and kept in private repositories under commercial terms, so this public repo likely does not contain the complete product codebase. -- evidence: [NOTICE.md#L8-L9](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/NOTICE.md#L8-L9) (`clm_953d2b597fac799a6d03d718a184cb0ac4e3240656be969ca3da3a3ac1d8be04`)

## relevance (1 claim(s))

- [observation/documented] The project targets builders of production AI agents, positioning itself as an OS-like kernel layer managing AI resources with agent orchestration and lifecycle management. -- evidence: [README.md#L28-L28](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L28-L28), [README.md#L23-L24](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L23-L24), [README.md#L57-L57](https://github.com/SmythOS/sre/blob/5c382a1ec07accc75947c3e4fa24841532ae7c88/README.md#L57-L57) (`clm_931b97a69340244055563191084f2dfb9146850278c486e72a1e654d326a3df3`)

