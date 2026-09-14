---
access: public
aliases: []
claim_ids:
- clm_2fc9b17bed586322835bcb9bdf657c2f8c5aaf7619f0688efb20fa61613beb45
- clm_47d39bf281f7ca2b2974edc9c444ad8a8ff419bf7b1f43d338accdd579ba7e1e
- clm_4b6398ea7b85f7fd6db0078ef902ec5386ebefdb45a73371fc27c4735383562d
- clm_5b0bc25f3b0251a99ef16f7fa64e86956f39e98e5a91941f9ac368bb3951f240
- clm_716ab2adabeb919dc9483619000965697ff6dc00e886ecbe2686abf9c3798a9a
- clm_931b97a69340244055563191084f2dfb9146850278c486e72a1e654d326a3df3
- clm_96ec5e1d914a0dba3b89a09aecc1647b96b21822254bc27e289fa8ad83de9ce6
- clm_a90b0f48bed624f65ef5a249f595fc35737052abf2f246cbbaa0dd536dd36738
- clm_be389fa9c74b794bfb6e7ce9493e5d4d0d4179324b58927ff6dcad4edbff1aeb
- clm_df7d65bc8dedda12804ed92477e82444a70f2be2ec779cef45ec8f7873b937d8
maturity: draft
page_id: pg_3a37f52cc8b75f70bcbf7daaa7529fab
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1d1060d0f50055639eb096c6c30c5e28
title: SmythOS/sre/README.md @ 5c382a1ec07a
updated_at: '2026-09-14T02:41:13Z'
---

# SmythOS/sre/README.md @ 5c382a1ec07a

<!-- rcw:begin owner=source:src_1d1060d0f50055639eb096c6c30c5e28 block=evidence -->
- The SDK is distributed as the npm package @smythos/sdk, with a separate @smythos/cli package recommended for creating new projects. [@claim:clm_2fc9b17bed586322835bcb9bdf657c2f8c5aaf7619f0688efb20fa61613beb45]
- Documented supported connectors include storage (Local, S3, Google Cloud, Azure), LLMs (OpenAI, Anthropic, Google AI, AWS Bedrock, Groq, Perplexity), VectorDBs (Pinecone, Milvus, RAMVec), caches (RAM, Redis), and vaults (JSON file, AWS Secrets Manager, HashiCorp). [@claim:clm_47d39bf281f7ca2b2974edc9c444ad8a8ff419bf7b1f43d338accdd579ba7e1e]
- SRE ships 40+ production-ready components (e.g. GenAILLM, APICall, WebSearch, Classifier, ForEach, S3, ECMAScript) invocable programmatically or via the .smyth workflow format. [@claim:clm_4b6398ea7b85f7fd6db0078ef902ec5386ebefdb45a73371fc27c4735383562d]
- The SDK exposes Agent.import to load .smyth agent files, agent.prompt for one-shot queries with a .stream() event mode, and agent.chat() for conversations that remember prior turns. [@claim:clm_5b0bc25f3b0251a99ef16f7fa64e86956f39e98e5a91941f9ac368bb3951f240]
- Agents can be defined in code with new Agent({name, model, behavior}) and extended via agent.addSkill, whose process function can access agent-scoped LLM, VectorDB, and storage connectors. [@claim:clm_716ab2adabeb919dc9483619000965697ff6dc00e886ecbe2686abf9c3798a9a]
- The project targets builders of production AI agents, positioning itself as an OS-like kernel layer managing AI resources with agent orchestration and lifecycle management. [@claim:clm_931b97a69340244055563191084f2dfb9146850278c486e72a1e654d326a3df3]
- The repo is a monorepo with three packages: the SRE core runtime (packages/core), the SDK (packages/sdk), and a CLI (packages/cli) for scaffolding and project management. [@claim:clm_96ec5e1d914a0dba3b89a09aecc1647b96b21822254bc27e289fa8ad83de9ce6]
- Every operation requires authorization through a Candidate/ACL system so agents only access resources they are permitted to; access is obtained via AccessCandidate.agent(agentId) passed to a connector. [@claim:clm_a90b0f48bed624f65ef5a249f595fc35737052abf2f246cbbaa0dd536dd36738]
- SRE is implicitly initialized with default connectors (RAM cache, local storage, console log) when the SDK is used, and can be explicitly re-initialized with built-in or custom connectors for production setups. [@claim:clm_be389fa9c74b794bfb6e7ce9493e5d4d0d4179324b58927ff6dcad4edbff1aeb]
- SRE provides a unified abstraction layer so all providers of a given resource type (storage, VectorDB, cache, LLM) expose the same API, letting providers be swapped without changing business logic. [@claim:clm_df7d65bc8dedda12804ed92477e82444a70f2be2ec779cef45ec8f7873b937d8]
<!-- rcw:end owner=source:src_1d1060d0f50055639eb096c6c30c5e28 block=evidence -->

## Researcher notes

