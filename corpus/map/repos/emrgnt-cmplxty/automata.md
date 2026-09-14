# emrgnt-cmplxty/automata

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 316386a2ea5b @ 6d638d97876f6283

## Summary (orientation draft, not independently verified)

The snapshot is README and generated docs for Automata, a Python framework combining LLMs with a vector database and SCIP-based code search to build self-coding agents. Evidence covers setup/CLI usage, agent configuration classes, and embedding classes, but no code internals.

## Source coverage

Source coverage (partial): 6 of 329 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The system combines large language models such as GPT-4 with a vector database to document, search, and write code, forming the basis of its self-coding potential. -- evidence: [README.md#L138-L138](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L138-L138)
  - [observation/documented] AgentConfig encodes agent behavior defaults including model, stream, verbosity, max_iterations, and temperature, and defaults to the OPENAI provider. -- evidence: [docs/config/base/config.rst#L18-L24](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L18-L24), [docs/config/base/config.rst#L9-L10](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L9-L10), [docs/config/base/config.rst#L4-L7](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L4-L7)
- design-choices (1 claim(s)):
  - [observation/documented] Automata's stated goal is to become a fully autonomous, self-programming AI system, based on the idea that code is a form of memory that lets AI evolve real-time capabilities. -- evidence: [README.md#L19-L19](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L19-L19)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves cloning, initializing git submodules, installing via poetry, and running automata configure; Docker installation is also documented, and Windows users may need C++ build tools and gcc-11/g++-11. -- evidence: [README.md#L49-L49](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L49-L49), [README.md#L61-L64](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L61-L64), [README.md#L82-L82](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L82-L82), [README.md#L58-L59](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L58-L59), [README.md#L52-L52](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L52-L52), [README.md#L55-L55](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L55-L55), [README.md#L84-L84](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L84-L84)
  - [observation/documented] Repository development practice: contributors are directed to review CONTRIBUTING.md and a code of conduct, with GitHub issues for bugs and Discussions for general questions. -- evidence: [README.md#L220-L223](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L220-L223), [README.md#L225-L228](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L225-L228)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a CLI via poetry, including commands like automata configure, install-indexing, run-code-embedding, run-doc-embedding, and run-agent with an --instructions flag. -- evidence: [README.md#L108-L109](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L108-L109), [README.md#L115-L115](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L115-L115), [README.md#L58-L59](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L58-L59), [README.md#L118-L119](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L118-L119), [README.md#L128-L128](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L128-L128)
  - [observation/documented] A Python API lets users build an OpenAIAutomataAgent from a named config (e.g. 'automata-main'), attach factory-built tools, and run it with instructions via agent.run(). -- evidence: [README.md#L148-L152](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L148-L152), [README.md#L158-L159](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L158-L159), [README.md#L162-L162](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L162-L162), [README.md#L173-L176](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L173-L176), [README.md#L165-L170](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L165-L170)
- memory-state (1 claim(s)):
  - [observation/documented] Symbol embeddings are represented by classes such as SymbolCodeEmbedding (code-related) and SymbolDocEmbedding (documentation-related), storing a symbol plus a high-dimensional vector. -- evidence: [README.md#L183-L185](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L183-L185), [README.md#L181-L181](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L181-L181)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Automata Search requires SCIP indices, which build a code graph relating symbols by dependencies; new indices are generated periodically and users may need to generate them manually for local development. -- evidence: [README.md#L104-L104](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L104-L104)
- limitations (2 claim(s)):
More evidence: [full detail](automata.detail.md)

Metadata and full claim list: [full detail](automata.detail.md)
Human notes ([notes](automata.notes.md), never overwritten by build)

[Back to map index](../../index.md)
