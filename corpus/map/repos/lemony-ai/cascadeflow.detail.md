# lemony-ai/cascadeflow -- full detail

[Back to orientation](cascadeflow.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lemony-ai/cascadeflow/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/75606ca846a6a60c.json](../../../wiki/dossiers/lemony-ai/cascadeflow/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/75606ca846a6a60c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The core mechanism is speculative execution with quality validation: run a cheap drafter first, validate responses against configurable thresholds, and escalate to a larger model only when validation fails. -- evidence: [docs/ARCHITECTURE.md#L23-L25](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L23-L25), [README.md#L94-L94](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L94-L94), [README.md#L96-L99](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L96-L99) (`clm_e6a7c744c8bae06c0de0284053194c022af1f65f2bed1cfc23ac739f5200a839`)
- [observation/documented] CascadeAgent (agent.py) is the main orchestrator and entry point for all queries, exposing run, run_streaming, and stream_events and coordinating routing, cost calculation, metrics, and callbacks. -- evidence: [docs/ARCHITECTURE.md#L193-L196](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L193-L196), [docs/ARCHITECTURE.md#L191-L191](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L191-L191), [docs/ARCHITECTURE.md#L198-L203](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L198-L203) (`clm_a749448530b64115cb7a22d572bf71f69a51f234046be065a86a8f7b8532d7a9`)
- [observation/documented] WholeResponseCascade is described as the core cascade execution engine, with an execute(query, drafter, verifier) method that runs the speculative cascade. -- evidence: [docs/ARCHITECTURE.md#L215-L216](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L215-L216), [docs/ARCHITECTURE.md#L213-L213](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L213-L213) (`clm_dd4f84a04013e3473b26f875b20b99b9520b69335ed1142f69b8ca6c882299e1`)
- [observation/documented] The repository is a pnpm/Turborepo monorepo with a Python package and a TypeScript packages/core library; the TypeScript library is described as an MVP supporting only the OpenAI provider. -- evidence: [docs/ARCHITECTURE.md#L142-L142](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L142-L142), [docs/ARCHITECTURE.md#L168-L172](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L168-L172), [docs/ARCHITECTURE.md#L33-L33](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L33-L33) (`clm_59db4708848d5fae7af17a22cb1146fba3f487cdb1ca2146967a7ee43ff2afa8`)

## design-choices (1 claim(s))

- [observation/documented] cascadeflow is positioned as an in-process intelligence layer operating inside the agent execution loop rather than at the HTTP request boundary like external proxies. -- evidence: [README.md#L38-L38](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L38-L38), [README.md#L61-L68](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L61-L68) (`clm_ac723b9c4e4dbb6552dde2862cc9d1013bf6ce726fe9214be03f9524f730f63f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The harness API offers three tiers: cascadeflow.init(mode="observe") for zero-change tracking, cascadeflow.run(budget=..., max_tool_calls=...) sessions with summary() and trace(), and a @cascadeflow.agent decorator accepting budget, compliance, and KPI weights. -- evidence: [README.md#L168-L171](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L168-L171), [README.md#L175-L181](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L175-L181), [README.md#L183-L188](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L183-L188) (`clm_1e1d1698d9b25d73fec4a6cd5cdb1cc13948cbf4bd3b41cd829227e10d5996d4`)
- [observation/documented] A drop-in gateway for existing OpenAI/Anthropic clients can be started with 'python -m cascadeflow.server --mode auto --port 8084'. -- evidence: [README.md#L392-L392](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L392-L392), [README.md#L394-L396](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L394-L396) (`clm_d21b758dfb2ab084ea5668c40b8111cae9360a3e726c0cf1d78d8197bf184aa2`)
- [observation/documented] The Hermes integration exposes HermesDelegationRouter and HermesDelegationRequest, returning a structured routing decision (reason, confidence, domain, complexity, model) before Hermes spawns a subagent, while Hermes keeps credentials, base URLs, and fallback chains. -- evidence: [README.md#L452-L452](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L452-L452), [README.md#L456-L460](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L456-L460), [README.md#L489-L497](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L489-L497) (`clm_75614c2ff2fd8bcd4b4b1aca27120f9d8809b95a9f9c29763473896fcb64b32b`)
- [observation/documented] The n8n integration provides two community nodes: a CascadeFlow (Model) sub-node drop-in for Chain/LLM nodes and a standalone CascadeFlow Agent node supporting tool calling, memory, and multi-step reasoning. -- evidence: [README.md#L416-L419](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L416-L419), [README.md#L437-L441](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L437-L441) (`clm_ed6f8462c639ef3299732d00dbe13fb75379e32d87313b344511a0d45a778ee3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] At runtime the harness can enforce decisions with four actions: allow, switch_model, deny_tool, and stop, based on current context and policy state. -- evidence: [README.md#L75-L84](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L75-L84) (`clm_650e40919bad9bc58ecb009b7e7abec0cf7b6bd1c3ff193cbd986c41e8cfae46`)

## evaluation (1 claim(s))

- [observation/documented] The README reports benchmark-based cost savings of 69% on MT-Bench, 93% on GSM8K, 52% on MMLU, and 80% on TruthfulQA while retaining 96% GPT-5 quality. -- evidence: [README.md#L28-L28](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L28-L28) (`clm_329a04d23f32e682d8a5bb4fe175a0a49de9f90baf8ac4b92fafd9a4b3fe54d4`)

## dependencies (1 claim(s))

- [observation/documented] ML-based semantic quality validation is optional: Python via cascadeflow[semantic] (FastEmbed, ~80MB model) and TypeScript via @cascadeflow/ml with @huggingface/transformers (BGE-small-en-v1.5 embeddings, auto-downloaded). -- evidence: [README.md#L340-L346](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L340-L346), [README.md#L296-L298](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L296-L298), [README.md#L224-L226](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L224-L226) (`clm_e79390dea62e5dc89e2dd661c9209b7e88afff7ff5de9e4ea2a6d65031ce9a30`)

## limitations (1 claim(s))

- [observation/documented] GPT-5 streaming requires OpenAI organization verification, while non-streaming GPT-5 works for all users; basic examples work without verification since GPT-5 is only called when needed. -- evidence: [README.md#L260-L260](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L260-L260) (`clm_231d49f38fa674438b63ed81870c72d683bbaeb8a244a74cc71e880751107f4f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

