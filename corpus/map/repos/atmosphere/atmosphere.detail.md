# atmosphere/atmosphere -- full detail

[Back to orientation](atmosphere.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/atmosphere/atmosphere/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/0d4003c8c705d782.json](../../../wiki/dossiers/atmosphere/atmosphere/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/0d4003c8c705d782.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The atmosphere-ai module ships an AgentRuntime SPI with a built-in OpenAI-compatible adapter; eleven more adapters live in separate modules, two of which (Anthropic, Cohere) are native HTTP+SSE clients. -- evidence: [README.md#L158-L158](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L158-L158) (`clm_9495451c2824285e4cdf93b4cf5acbadfd3df68688b1febe8f9c0a066640d41b`)
- [observation/documented] Governance controls include GovernancePolicy/PolicyRing with allow/deny lists and rate limits, @AgentScope purpose enforcement, tool approval policies, and a plan-and-verify verifier module. -- evidence: [README.md#L185-L197](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L185-L197) (`clm_866dbf102562ab740b8c8ed962d16fcd651a2a2ca03d871ac77d80fc8d80b761`)

## design-choices (1 claim(s))

- [observation/documented] Runtime adapter capabilities are pinned by AbstractAgentRuntimeContractTest.expectedCapabilities(), so a runtime cannot drift from its declared feature set without breaking tests. -- evidence: [README.md#L162-L162](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L162-L162) (`clm_6bcef9d731bbe2026b8a197c2d7cfb552b7356f3a7787bafcc153e10c2271495`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the project uses Maven with the wrapper; contributors run ./mvnw install/test, per-module builds, checkstyle and PMD checks, and must run a full compile with zero warnings before committing. -- evidence: [AGENTS.md#L6-L15](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L6-L15), [AGENTS.md#L150-L155](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L150-L155), [AGENTS.md#L3-L3](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L3-L3) (`clm_ad3f148d318f8c6a8c547eec161986c6edbe137402cbdf14d4cb9f9fb2570f6b`)
- [observation/documented] Repository development practice: git hooks must be enabled via core.hooksPath .githooks each session; they enforce copyright headers, no unused imports, commit format, and no AI-generated commit trailers, and --no-verify is forbidden. -- evidence: [AGENTS.md#L60-L65](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L60-L65), [AGENTS.md#L33-L37](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L33-L37), [AGENTS.md#L39-L44](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L39-L44) (`clm_4bd65132a66b7da93119254b1974d747dc1adb365c6872079484679e86bba8d3`)

## skills-patterns (1 claim(s))

- [observation/documented] The CLI can import agent skill files, e.g. atmosphere import of an Anthropic SKILL.md URL, and a companion atmosphere-skills repository offers curated skill files. -- evidence: [README.md#L329-L332](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L329-L332), [README.md#L87-L91](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L87-L91) (`clm_59e1042ef9426e125d9916612293db078e2cb6e1258ba03a124b50767486c5c8`)

## interfaces (3 claim(s))

- [observation/documented] A single @Agent annotation declares an agent, with @Prompt for streaming messages, @Command for slash commands (including confirmation prompts), and @AiTool for tool methods. -- evidence: [README.md#L111-L115](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L111-L115), [README.md#L101-L104](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L101-L104), [README.md#L95-L95](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L95-L95), [README.md#L117-L122](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L117-L122), [README.md#L106-L109](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L106-L109), [README.md#L97-L99](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L97-L99) (`clm_fb6713b36ffa426fdcdb8eda2035d0323e5d3e8314d5858e62985d1fde7743fb`)
- [observation/documented] Classpath modules register endpoints: browser endpoint at /atmosphere/agent/my-agent, MCP at .../mcp, A2A at .../a2a, AG-UI at .../agui, plus an admin dashboard and console UI. -- evidence: [README.md#L124-L132](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L124-L132) (`clm_ba10976b125261eb4662d9e32927cc3641c68a9993b7d1677164a87c7d833aa6`)
- [observation/documented] Governance policy can be declared in YAML (deny-list phrases, cost ceilings) or via annotations such as @AgentScope with purpose, forbiddenTopics, and breach behavior. -- evidence: [README.md#L216-L223](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L216-L223), [README.md#L201-L212](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L201-L212) (`clm_dcbd1dfe153dd5b16dd19e6fa54acf0eaac04d057dd760a6929b6e103c28a90a`)

## memory-state (1 claim(s))

- [observation/documented] Memory is provided as AiConversationMemory per-conversation history and LongTermMemory per-user facts, in-memory or durable via SQLite/Redis modules, with a SemanticRecallInterceptor for vector recall. -- evidence: [README.md#L40-L49](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L40-L49) (`clm_f8ae665ea548119f524007c1f61b5ff38a134d5f727d987a48c53adb0c5521b8`)

## orchestration (1 claim(s))

- [observation/documented] Multi-agent orchestration uses @Coordinator and AgentFleet with handoffs, conditional routing, an event-sourced coordination journal, and durable hibernating Workflow<S> over a CheckpointStore (optionally Temporal-backed). -- evidence: [README.md#L40-L49](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L40-L49) (`clm_1e5262574ae80babe3f511539e5876c8a6270d2afb102599dd2f1d5ac4318e3f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Java 21+, Spring Boot 4.1.0 or 3.5 via the -Pspring-boot3 profile, and Quarkus 3.36.3+; artifacts are published to Maven Central and atmosphere.js to npm. -- evidence: [README.md#L307-L307](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L307-L307), [README.md#L11-L17](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L11-L17) (`clm_1d8a5d6574f48abd25d811da533c4341eefd473c537d96def482da856dd7a66b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

