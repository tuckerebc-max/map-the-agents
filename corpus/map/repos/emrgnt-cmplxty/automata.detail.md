# emrgnt-cmplxty/automata -- full detail

[Back to orientation](automata.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/emrgnt-cmplxty/automata/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/6d638d97876f6283.json](../../../wiki/dossiers/emrgnt-cmplxty/automata/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/6d638d97876f6283.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The system combines large language models such as GPT-4 with a vector database to document, search, and write code, forming the basis of its self-coding potential. -- evidence: [README.md#L138-L138](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L138-L138) (`clm_43e379b31b240f9e3e7bf7f40e9e0a2d6c217e8f24540ff918d6dfea559294b4`)
- [observation/documented] AgentConfig encodes agent behavior defaults including model, stream, verbosity, max_iterations, and temperature, and defaults to the OPENAI provider. -- evidence: [docs/config/base/config.rst#L18-L24](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L18-L24), [docs/config/base/config.rst#L9-L10](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L9-L10), [docs/config/base/config.rst#L4-L7](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L4-L7) (`clm_df92cbf81a40ba46bd8b860152406faa3bec644af0aad145f09f37b998a78cf8`)
- [observation/documented] OpenAIAutomataAgentConfig.Config includes a SUPPORTED_MODELS list of allowed OpenAI engine models and an arbitrary_types_allowed setting. -- evidence: [docs/config/openai_agent/config.rst#L4-L8](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/openai_agent/config.rst#L4-L8), [docs/config/openai_agent/config.rst#L17-L22](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/openai_agent/config.rst#L17-L22) (`clm_869094e77bd9233134af86f1f6ec250dec36ac483492dcf38f637fbdd8d4cf9b`)

## design-choices (1 claim(s))

- [observation/documented] Automata's stated goal is to become a fully autonomous, self-programming AI system, based on the idea that code is a form of memory that lets AI evolve real-time capabilities. -- evidence: [README.md#L19-L19](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L19-L19) (`clm_9f3f7ba7e9352de750866c46f451dc2220b6786d763b852257ee880b0587bbfe`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup involves cloning, initializing git submodules, installing via poetry, and running automata configure; Docker installation is also documented, and Windows users may need C++ build tools and gcc-11/g++-11. -- evidence: [README.md#L49-L49](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L49-L49), [README.md#L61-L64](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L61-L64), [README.md#L82-L82](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L82-L82), [README.md#L58-L59](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L58-L59), [README.md#L52-L52](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L52-L52), [README.md#L55-L55](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L55-L55), [README.md#L84-L84](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L84-L84) (`clm_6b974e0d9f4385f3780b3bbdb0d47e9644d509ed4358053da3d918be6f87cc38`)
- [observation/documented] Repository development practice: contributors are directed to review CONTRIBUTING.md and a code of conduct, with GitHub issues for bugs and Discussions for general questions. -- evidence: [README.md#L220-L223](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L220-L223), [README.md#L225-L228](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L225-L228) (`clm_53f2661cb03643611bf2ba4cac75f59f373f92de40a1d681bd146b1f3cb806de`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a CLI via poetry, including commands like automata configure, install-indexing, run-code-embedding, run-doc-embedding, and run-agent with an --instructions flag. -- evidence: [README.md#L108-L109](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L108-L109), [README.md#L115-L115](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L115-L115), [README.md#L58-L59](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L58-L59), [README.md#L118-L119](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L118-L119), [README.md#L128-L128](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L128-L128) (`clm_b22474d246151d7c9b7439b12dbf6c59b686e813a9991bcf33861ddf71cb333b`)
- [observation/documented] A Python API lets users build an OpenAIAutomataAgent from a named config (e.g. 'automata-main'), attach factory-built tools, and run it with instructions via agent.run(). -- evidence: [README.md#L148-L152](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L148-L152), [README.md#L158-L159](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L158-L159), [README.md#L162-L162](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L162-L162), [README.md#L173-L176](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L173-L176), [README.md#L165-L170](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L165-L170) (`clm_748309999bd42126656b07956940a61515bf55088a5c85d93ef72ed2de4243a2`)

## memory-state (1 claim(s))

- [observation/documented] Symbol embeddings are represented by classes such as SymbolCodeEmbedding (code-related) and SymbolDocEmbedding (documentation-related), storing a symbol plus a high-dimensional vector. -- evidence: [README.md#L183-L185](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L183-L185), [README.md#L181-L181](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L181-L181) (`clm_cd48e3de9055f3e69d33a5de85e1fec0dc54a1fccbe440873b5f0095cddc12a0`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Automata Search requires SCIP indices, which build a code graph relating symbols by dependencies; new indices are generated periodically and users may need to generate them manually for local development. -- evidence: [README.md#L104-L104](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/README.md#L104-L104) (`clm_1081b78582db481837b5c1291c68b5fbd23ab049048203e646bf065556f34a2e`)

## limitations (2 claim(s))

- [observation/documented] Per its docs, OpenAIAutomataAgentConfig.Config can only use models predefined in SUPPORTED_MODELS; using another model requires updating that attribute. -- evidence: [docs/config/openai_agent/config.rst#L52-L55](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/openai_agent/config.rst#L52-L55) (`clm_d123c07f3a199be2dbd4a9e1d11dd248880915b300535c678198888ed65fb14a`)
- [observation/documented] Docs note AgentConfig behavior strictly depends on its defined parameters, which may be inflexible when dynamic parameter adjustment is needed, and error handling for invalid configs may be challenging. -- evidence: [docs/config/base/config.rst#L73-L77](https://github.com/emrgnt-cmplxty/automata/blob/316386a2ea5b5707c6c9cb2cf36e19b5ab913993/docs/config/base/config.rst#L73-L77) (`clm_31acd56680686ee1cc289c3ad68c5b45bfbe9d000dc3b4246de62df455c11fbc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

