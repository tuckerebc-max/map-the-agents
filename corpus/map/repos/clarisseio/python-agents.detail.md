# clarisseio/python-agents -- full detail

[Back to orientation](python-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/clarisseio/python-agents/84c3bdc93ecd2dd172539412148f1e475ab7bf88/45d89dabc1a851af.json](../../../wiki/dossiers/clarisseio/python-agents/84c3bdc93ecd2dd172539412148f1e475ab7bf88/45d89dabc1a851af.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The framework ships modules for agents, LLMs, prompt templating (Mustache-based), memory, tools, cache, errors, adapters, and logger, with agents and LLMs described as base classes defining common interfaces. -- evidence: [README.md#L92-L106](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L92-L106) (`clm_1e1d0808139d05dba3864b86d25529872625311a4effe2d41a99e60192c16b84`)
- [observation/documented] An Emitter observability component lets code emit and match events by name, wildcard patterns, filter functions (e.g. creator instanceof BaseLLM), or regex, and supports piping events between emitters. -- evidence: [docs/emitter.md#L103-L107](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L103-L107), [docs/emitter.md#L100-L101](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L100-L101), [docs/emitter.md#L97-L98](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L97-L98), [docs/emitter.md#L109-L111](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L109-L111), [docs/emitter.md#L94-L95](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L94-L95), [docs/emitter.md#L141-L142](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L141-L142) (`clm_e7e602b45d064b2a5569a86a027686ed51a26a0ad69d97c89f1d5fa88aa6a55e`)

## design-choices (2 claim(s))

- [observation/documented] Cache keys are produced by serializing function parameters with key order irrelevant; the default decorator key function is ObjectHashKeyFn, and SingletonCacheKeyFn yields a single shared key regardless of arguments. -- evidence: [docs/cache.md#L97-L99](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L97-L99), [docs/cache.md#L291-L294](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L291-L294), [docs/cache.md#L287-L289](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L287-L289) (`clm_913dc7f704cc758ef9f4483e202bf62f82d35cb37c2e3ad7dfc780f94e846dd7`)
- [observation/documented] The framework is designed to perform robustly with IBM Granite and Llama 3.x models, with optimization for other popular LLMs stated as ongoing work. -- evidence: [README.md#L14-L14](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L14-L14) (`clm_a8de7343144be5b87745fe02e08557bee254684a2e777138baec5ccf4c9f557a`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: local setup involves cloning, yarn install --immutable && yarn prepare, creating .env from .env.template, and running examples via yarn start with a file path; contributions follow CONTRIBUTING.md. -- evidence: [README.md#L79-L82](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L79-L82), [README.md#L86-L86](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L86-L86), [README.md#L121-L121](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L121-L121) (`clm_f04908d4897156bb7710f69f1b00a1f1d173ef83a828ad73d94ebf0ca2c01ec2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Agents are constructed with an LLM, memory, and tools, and run via an awaited run({prompt}) call whose result exposes response.result.text. -- evidence: [README.md#L61-L67](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L61-L67), [README.md#L55-L59](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L55-L59), [README.md#L69-L70](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L69-L70) (`clm_dde7c03a70959a2e0be462959b04513032da6fa5df74c4f487b3c7f017da1258`)
- [observation/documented] The run method supports an observe callback exposing an emitter where listeners can subscribe to events such as 'update' during execution; observe is also supported on tools and LLMs. -- evidence: [docs/emitter.md#L192-L194](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L192-L194), [docs/emitter.md#L178-L188](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L178-L188), [README.md#L61-L67](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L61-L67) (`clm_9c4e6d06d460d4142badf7aa52e19bce7e1bccf67582aff4296e4ed4dc407e4e`)
- [observation/documented] Caches expose async set/get/has/delete/clear/size operations, and custom caches are created by extending BaseCache, whose example also includes createSnapshot and loadSnapshot methods. -- evidence: [docs/cache.md#L39-L42](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L39-L42), [docs/cache.md#L20-L22](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L20-L22), [docs/cache.md#L24-L26](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L24-L26), [docs/cache.md#L35-L37](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L35-L37), [docs/cache.md#L331-L331](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L331-L331), [docs/cache.md#L28-L33](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L28-L33), [docs/cache.md#L368-L372](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L368-L372), [docs/cache.md#L364-L366](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L364-L366) (`clm_66b7a4cfb127b60833caf7c04e8539168c4f11e21546b810314e7ddcf9469ead`)

## memory-state (1 claim(s))

- [observation/documented] Memory classes such as UnconstrainedMemory store BaseMessage objects with add/addMany, expose messages, isEmpty, asReadOnly, and reset, and can be passed to LLM generate calls. -- evidence: [docs/memory.md#L29-L33](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L29-L33), [docs/memory.md#L61-L64](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L61-L64), [docs/memory.md#L21-L27](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L21-L27), [docs/memory.md#L35-L39](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L35-L39), [docs/memory.md#L19-L19](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L19-L19) (`clm_8d53a7077166165c222faeffffa1630d57fb4c192fa056703e754080a92e1e81`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package installs via npm or yarn as 'Clarisse-agent-framework', and examples use an Ollama chat LLM adapter defaulting to llama3.1 (8B) with the 70B model recommended. -- evidence: [README.md#L40-L42](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L40-L42), [README.md#L53-L53](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L53-L53), [README.md#L34-L36](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L34-L36) (`clm_e323144efd2cd4e2b3eed95db1b65ff5f592b13cb7d11b6738292f13d1cc45e7`)

## limitations (1 claim(s))

- [observation/documented] The legal notice states the code is an IBM open-source project, not an IBM product, with no obligation to provide enhancements, updates, support, or ongoing maintenance. -- evidence: [README.md#L126-L126](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L126-L126) (`clm_e0f554009905401c66358f2863bc660907310f45ee2d059481676b150e47bcbf`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

