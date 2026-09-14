# aurasgit/public-agent-framwork -- full detail

[Back to orientation](public-agent-framwork.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aurasgit/public-agent-framwork/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/e342f0b1feb8ac41.json](../../../wiki/dossiers/aurasgit/public-agent-framwork/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/e342f0b1feb8ac41.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The framework ships modules including agents, llms, template (Mustache-based prompt templating), memory, tools, cache, errors, and adapters for different environments. -- evidence: [README.md#L92-L106](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L92-L106) (`clm_8c80167e586d2e5227097dd9f204d893934dbbf1852539d1792c743d660e280d`)
- [observation/documented] An Emitter system provides observability, supporting typed events, wildcard and regex matching, filter functions, namespaces, and piping events between emitters. -- evidence: [docs/emitter.md#L141-L142](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L141-L142), [docs/emitter.md#L5-L5](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L5-L5), [docs/emitter.md#L100-L101](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L100-L101), [docs/emitter.md#L97-L98](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L97-L98), [docs/emitter.md#L109-L111](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L109-L111), [docs/emitter.md#L103-L107](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L103-L107), [docs/emitter.md#L21-L23](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L21-L23), [docs/emitter.md#L48-L55](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L48-L55) (`clm_1304e3d5fa0059933a0148e844ef87ef4a705a77900b1005bd4a1660c4609230`)
- [observation/documented] The memory module offers UnconstrainedMemory storing BaseMessage objects with add, addMany, reset, asReadOnly, and isEmpty operations. -- evidence: [docs/memory.md#L35-L39](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/memory.md#L35-L39), [docs/memory.md#L21-L27](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/memory.md#L21-L27), [docs/memory.md#L15-L17](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/memory.md#L15-L17), [docs/memory.md#L29-L33](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/memory.md#L29-L33) (`clm_92f1fdcb1e5d344e90b93dbeb00e1a386f53dabeb77c97d091451753a3375933`)

## design-choices (2 claim(s))

- [observation/documented] Tool and LLM caching keys are created by serializing function parameters, with object key order not mattering; identical inputs are served from cache. -- evidence: [docs/cache.md#L89-L93](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L89-L93), [docs/cache.md#L121-L127](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L121-L127), [docs/cache.md#L97-L99](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L97-L99) (`clm_c2d3c71a6b36fc0829c12dd768cde8d54a846dedccf7684b563c4e1a5d72316d`)
- [observation/documented] The framework is designed to perform robustly with IBM Granite and Llama 3.x models, with optimization for other LLMs in progress. -- evidence: [README.md#L14-L14](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L14-L14) (`clm_5366a4a13191dc83de1becc51c4a41ed544186f2a4060b0135f9198aa0c75489`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Agents are constructed with an LLM, memory, and tools, and executed via an async run method taking a prompt. -- evidence: [README.md#L61-L67](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L61-L67), [README.md#L55-L59](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L55-L59) (`clm_685300f577cc0943a7cea70792fb0bce36a7bc23c841dc22928f742f0200c116`)
- [observation/documented] Agent runs expose an observe method whose callback receives an emitter for streaming per-update events during execution. -- evidence: [README.md#L61-L67](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L61-L67), [docs/emitter.md#L178-L188](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L178-L188) (`clm_578356617ec97a0d348c676410cb8e1332b8e53cbd3264af94b5f58fb8855bcc`)
- [observation/documented] Custom cache providers implement a BaseCache class with set, get, has, delete, clear, size, and snapshot methods. -- evidence: [docs/cache.md#L352-L354](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L352-L354), [docs/cache.md#L344-L346](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L344-L346), [docs/cache.md#L331-L331](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L331-L331), [docs/cache.md#L360-L362](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L360-L362), [docs/cache.md#L348-L350](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L348-L350), [docs/cache.md#L356-L358](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L356-L358), [docs/cache.md#L339-L342](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L339-L342) (`clm_c56b90f92aa0978e189f9e3590f538c141f5fabaa805547a97a2a4b4e2c0b564`)
- [observation/documented] LLM adapters include OllamaChatLLM, configurable with modelId, generation parameters, and an optional cache. -- evidence: [README.md#L53-L53](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L53-L53), [docs/cache.md#L110-L119](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L110-L119) (`clm_aa12aa208a1ff22974cc318ae010668b8baf0dd422496c20ded7a076a57e66f6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The framework is distributed as the npm package Auralia-agent-framework, installable with npm or yarn. -- evidence: [README.md#L34-L36](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L34-L36), [README.md#L40-L42](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L40-L42) (`clm_65886b7a0b7ca92aaa7c3b9e783ee3791441b0643b4b04c3965a11504b16dc78`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

