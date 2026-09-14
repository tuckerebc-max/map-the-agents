# agentscope-ai/agentscope -- full detail

[Back to orientation](agentscope.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/agentscope-ai/agentscope/b82253ba1b680a67091c4de32f074477c30ba416/a07620e1b7cb9181.json](../../../wiki/dossiers/agentscope-ai/agentscope/b82253ba1b680a67091c4de32f074477c30ba416/a07620e1b7cb9181.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The SDK exposes building blocks including a ReAct reasoning-acting loop, Toolkit, Model, Context, Event System, Permission & HITL, Middleware, Memory, and Workspace/Sandbox. -- evidence: [README.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L126-L136), [README_zh.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L126-L136) (`clm_958f015877fb238170c14298d3db9399182748c226eee2396bef9e8e7bd4b9a9`)
- [observation/documented] The agent service is a FastAPI backend with a pre-built Web UI offering multi-tenancy, multi-session isolation, channels (Feishu, Discord, DingTalk), RAG service, persistence, and scheduling. -- evidence: [README.md#L75-L86](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L75-L86), [README.md#L181-L181](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L181-L181), [README.md#L183-L192](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L183-L192) (`clm_12bee3f31ba7f3645c11e95b418d3277c0bc343f628d4eec5b3fa7c3dafaa5df`)

## design-choices (1 claim(s))

- [observation/documented] The design philosophy is to leverage models' reasoning and tool-use abilities rather than constrain them with strict prompts and opinionated orchestrations. -- evidence: [README.md#L68-L70](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L68-L70), [README_zh.md#L68-L69](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L68-L69) (`clm_9bb0d76b026b7fc704616006669df783a83e00341ed41ca20669caa3aaddefe9`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors must follow Conventional Commits for commit and PR titles, with GitHub Actions validating PR titles against main and blocking non-conforming ones. -- evidence: [CONTRIBUTING_zh.md#L152-L152](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L152-L152), [CONTRIBUTING_zh.md#L127-L127](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L127-L127) (`clm_24fd25c8e9727ded58e0e2b29682e4ab4867fb8241c8b28e3fd5c78fcb2f5b5b`)
- [observation/documented] Repository development practice: optional dependencies must be lazily imported at the point of use rather than at module top, to keep 'import agentscope' lightweight; pre-commit and pytest must be run before a PR. -- evidence: [CONTRIBUTING_zh.md#L111-L111](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L111-L111), [CONTRIBUTING_zh.md#L191-L197](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L191-L197), [CONTRIBUTING_zh.md#L114-L115](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L114-L115), [CONTRIBUTING_zh.md#L93-L99](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L93-L99) (`clm_5bd272c408f91e198fbe7af6f4c06e8719c5ccea27bf0b8521b3ca1efb77c8da`)
- [observation/documented] Repository development practice: AI-assisted contributions are welcome but must be responsibly used — authors must review diffs line by line, keep PRs atomic, and avoid dumping unreviewed AI-generated changes on maintainers. -- evidence: [CONTRIBUTING_zh.md#L32-L32](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L32-L32), [CONTRIBUTING_zh.md#L34-L34](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L34-L34), [CONTRIBUTING_zh.md#L28-L28](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L28-L28), [CONTRIBUTING_zh.md#L36-L36](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L36-L36) (`clm_828d07782af495a250feb8322e7974a6fdba67ad0c73411999465960694be043`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Toolkit manages Python tools, MCP servers, and skills, and ships built-in coding tools (shell, file edit, search) plus task/plan tools. -- evidence: [README.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L126-L136) (`clm_92fe4edd0a45f7317da5dc4a2ce3931b523532d9d8e0b9347091c5cf86364b7b`)
- [observation/documented] Recent releases add A2A protocol support via an A2AAgent for chatting with remote A2A agents, and RealtimeAgent supporting DashScope, OpenAI, Gemini, and xAI realtime APIs. -- evidence: [README.md#L75-L86](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L75-L86), [docs/NEWS.md#L5-L24](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/docs/NEWS.md#L5-L24) (`clm_868ee557da0d841fffc1396f92bf9e82a2ba390c4f6be68ccc8178e68ca5ef87`)

## memory-state (1 claim(s))

- [observation/documented] The memory building block is described as agentic memory with switchable backends, naming ReMe and Mem0. -- evidence: [README_zh.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L126-L136) (`clm_287953c98da2eafd9ecb44ff58d723d777685cd50210048d81f5ebcbb486b862`)

## orchestration (1 claim(s))

- [observation/documented] The agent service offers leader-worker orchestration with built-in team tools and task planning, where a leader agent spawns and coordinates workers. -- evidence: [README.md#L183-L192](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L183-L192), [README.md#L196-L225](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L196-L225) (`clm_1095e22f83e87c0d0f81c23bf4e10d345063d96fe349612433e0e4f76718e337`)

## tools-permissions (1 claim(s))

- [observation/documented] The product includes a permission system with fine-grained control over tools and resources, confirmation flows, and a bypass mode where the agent runs without pausing for tool-call confirmations. -- evidence: [README.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L126-L136), [README.md#L196-L225](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L196-L225) (`clm_b97e74373cbfdc3da9b3d16a391d98a22805b5e97cb4bd09555f8a1007d26067`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] AgentScope requires Python 3.11 or higher and can be installed from PyPI via 'uv pip install agentscope'. -- evidence: [README.md#L106-L108](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L106-L108), [README.md#L102-L102](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L102-L102), [README_zh.md#L102-L102](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L102-L102) (`clm_30b1f905f2be6cc5abed2485ea79c148d95f7819d875987aba4b183aba9220a2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

