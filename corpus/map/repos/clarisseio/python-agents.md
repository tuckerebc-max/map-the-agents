# clarisseio/python-agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 84c3bdc93ecd @ 45d89dabc1a851af

## Summary (orientation draft, not independently verified)

Selected evidence records: The framework ships modules for agents, LLMs, prompt templating (Mustache-based), memory, tools, cache, errors, adapters, and logger, with agents and LLMs described as base classes defining common interfaces. Agents are constructed with an LLM, memory, and tools, and run via an awaited run({prompt}) call whose result exposes response.result.text.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The framework ships modules for agents, LLMs, prompt templating (Mustache-based), memory, tools, cache, errors, adapters, and logger, with agents and LLMs described as base classes defining common interfaces. -- evidence: [README.md#L92-L106](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L92-L106)
  - [observation/documented] An Emitter observability component lets code emit and match events by name, wildcard patterns, filter functions (e.g. creator instanceof BaseLLM), or regex, and supports piping events between emitters. -- evidence: [docs/emitter.md#L103-L107](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L103-L107), [docs/emitter.md#L100-L101](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L100-L101), [docs/emitter.md#L97-L98](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L97-L98), [docs/emitter.md#L109-L111](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L109-L111), [docs/emitter.md#L94-L95](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L94-L95), [docs/emitter.md#L141-L142](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L141-L142)
- design-choices (2 claim(s)):
  - [observation/documented] Cache keys are produced by serializing function parameters with key order irrelevant; the default decorator key function is ObjectHashKeyFn, and SingletonCacheKeyFn yields a single shared key regardless of arguments. -- evidence: [docs/cache.md#L97-L99](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L97-L99), [docs/cache.md#L291-L294](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L291-L294), [docs/cache.md#L287-L289](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/cache.md#L287-L289)
  - [observation/documented] The framework is designed to perform robustly with IBM Granite and Llama 3.x models, with optimization for other popular LLMs stated as ongoing work. -- evidence: [README.md#L14-L14](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L14-L14)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: local setup involves cloning, yarn install --immutable && yarn prepare, creating .env from .env.template, and running examples via yarn start with a file path; contributions follow CONTRIBUTING.md. -- evidence: [README.md#L79-L82](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L79-L82), [README.md#L86-L86](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L86-L86), [README.md#L121-L121](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L121-L121)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Agents are constructed with an LLM, memory, and tools, and run via an awaited run({prompt}) call whose result exposes response.result.text. -- evidence: [README.md#L61-L67](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L61-L67), [README.md#L55-L59](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L55-L59), [README.md#L69-L70](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L69-L70)
  - [observation/documented] The run method supports an observe callback exposing an emitter where listeners can subscribe to events such as 'update' during execution; observe is also supported on tools and LLMs. -- evidence: [docs/emitter.md#L192-L194](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L192-L194), [docs/emitter.md#L178-L188](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/emitter.md#L178-L188), [README.md#L61-L67](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/README.md#L61-L67)
- memory-state (1 claim(s)):
  - [observation/documented] Memory classes such as UnconstrainedMemory store BaseMessage objects with add/addMany, expose messages, isEmpty, asReadOnly, and reset, and can be passed to LLM generate calls. -- evidence: [docs/memory.md#L29-L33](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L29-L33), [docs/memory.md#L61-L64](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L61-L64), [docs/memory.md#L21-L27](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L21-L27), [docs/memory.md#L35-L39](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L35-L39), [docs/memory.md#L19-L19](https://github.com/clarisseIO/python-agents/blob/84c3bdc93ecd2dd172539412148f1e475ab7bf88/docs/memory.md#L19-L19)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](python-agents.detail.md)

Metadata and full claim list: [full detail](python-agents.detail.md)
Human notes ([notes](python-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
