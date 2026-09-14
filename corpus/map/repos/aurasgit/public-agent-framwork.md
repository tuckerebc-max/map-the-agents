# aurasgit/public-agent-framwork

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f3f27582c6a2 @ e342f0b1feb8ac41

## Summary (orientation draft, not independently verified)

Selected evidence records: The framework ships modules including agents, llms, template (Mustache-based prompt templating), memory, tools, cache, errors, and adapters for different environments. Agents are constructed with an LLM, memory, and tools, and executed via an async run method taking a prompt.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The framework ships modules including agents, llms, template (Mustache-based prompt templating), memory, tools, cache, errors, and adapters for different environments. -- evidence: [README.md#L92-L106](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L92-L106)
  - [observation/documented] An Emitter system provides observability, supporting typed events, wildcard and regex matching, filter functions, namespaces, and piping events between emitters. -- evidence: [docs/emitter.md#L141-L142](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L141-L142), [docs/emitter.md#L5-L5](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L5-L5), [docs/emitter.md#L100-L101](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L100-L101), [docs/emitter.md#L97-L98](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L97-L98), [docs/emitter.md#L109-L111](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L109-L111), [docs/emitter.md#L103-L107](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L103-L107), [docs/emitter.md#L21-L23](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L21-L23), [docs/emitter.md#L48-L55](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L48-L55)
- design-choices (2 claim(s)):
  - [observation/documented] Tool and LLM caching keys are created by serializing function parameters, with object key order not mattering; identical inputs are served from cache. -- evidence: [docs/cache.md#L89-L93](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L89-L93), [docs/cache.md#L121-L127](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L121-L127), [docs/cache.md#L97-L99](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/cache.md#L97-L99)
  - [observation/documented] The framework is designed to perform robustly with IBM Granite and Llama 3.x models, with optimization for other LLMs in progress. -- evidence: [README.md#L14-L14](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L14-L14)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Agents are constructed with an LLM, memory, and tools, and executed via an async run method taking a prompt. -- evidence: [README.md#L61-L67](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L61-L67), [README.md#L55-L59](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L55-L59)
  - [observation/documented] Agent runs expose an observe method whose callback receives an emitter for streaming per-update events during execution. -- evidence: [README.md#L61-L67](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L61-L67), [docs/emitter.md#L178-L188](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/docs/emitter.md#L178-L188)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The framework is distributed as the npm package Auralia-agent-framework, installable with npm or yarn. -- evidence: [README.md#L34-L36](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L34-L36), [README.md#L40-L42](https://github.com/aurasgit/public-agent-framwork/blob/f3f27582c6a2cc6d18c9856e8c0348c5418b3636/README.md#L40-L42)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](public-agent-framwork.detail.md) for every claim.)

Metadata and full claim list: [full detail](public-agent-framwork.detail.md)
Human notes ([notes](public-agent-framwork.notes.md), never overwritten by build)

[Back to map index](../../index.md)
