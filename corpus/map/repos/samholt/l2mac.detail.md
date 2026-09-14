# samholt/l2mac -- full detail

[Back to orientation](l2mac.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/samholt/l2mac/105e74afdc6721e4d530c65862a32b97b5434e61/3bdf23d1d7da66dc.json](../../../wiki/dossiers/samholt/l2mac/105e74afdc6721e4d530c65862a32b97b5434e61/3bdf23d1d7da66dc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Each prompt-program instruction step is loaded into a new LLM agent whose context is managed by a control unit and given tools to read and write a persistent file-store holding final and intermediate outputs. -- evidence: [README.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L28-L29) (`clm_6e34f0918824d10bbc18e4c655bb9a8208177c37650d5d8786fc358697c5f903`)

## design-choices (3 claim(s))

- [observation/documented] L2MAC is described as an LLM-based multi-agent system implementing a stored-program von Neumann-style architecture for extensive, consistent output generation. -- evidence: [README.md#L4-L6](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L4-L6), [README.md#L8-L10](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L8-L10) (`clm_a04e8c4b1684de0695edef34e3e9c971362ac1e985cbd39229659a81c88738c6`)
- [observation/documented] The prompt-program is a sequence of instruction-step prompts; unless explicitly given, it is self-generated (bootstrapped) and then executed. -- evidence: [README.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L28-L29) (`clm_9898baa4293b785f998b047fd9e75ac557663249290b5c00743af2b494cdeb29`)
- [observation/documented] The framework aims to produce outputs unbounded by the underlying LLM's fixed context window by persisting outputs to a file store. -- evidence: [README.md#L184-L184](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L184-L184), [README.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L28-L29) (`clm_d750e279a85365211b4d8f2c3bd325f1ce1a2be42ccb7267d5260fd70db0f13a`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors join the dev team by submitting a PR, with ongoing tasks listed on the roadmap; a rotating Chief Evangelist community role is recruited via email. -- evidence: [docs/guide/faq.md#L31-L31](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L31-L31), [docs/guide/faq.md#L16-L17](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L16-L17), [docs/guide/faq.md#L21-L21](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L21-L21), [docs/guide/faq.md#L36-L39](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L36-L39) (`clm_8d4640ef4d158be0a6db3a7228998a3d82993e21701395b55e21bda0e0e0b5cf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] L2MAC offers a CLI (e.g. `l2mac "..."` creating a codebase repo in ./workspace) and a Python library API including generate_codebase and run_l2mac, plus helper functions for book and custom domains. -- evidence: [docs/guide/api.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L28-L29), [docs/guide/api.md#L42-L42](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L42-L42), [README.md#L77-L81](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L77-L81), [docs/guide/api.md#L46-L46](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L46-L46), [README.md#L71-L73](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L71-L73), [docs/guide/api.md#L38-L38](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L38-L38) (`clm_a3587c5c5ca174845d6e4cafea96026f314e4869f60627c583f8ac65ba34533d`)
- [observation/documented] The main generation API accepts parameters including prompt_task, domain ('codebase' or 'book', default 'codebase'), run_tests (default False), steps (default 10), prompt_program, prompts_file_path, tools_enabled, debugging_level, and init_config. -- evidence: [docs/guide/api.md#L9-L18](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L9-L18) (`clm_186cf25acdbeb3437e66b2eafd1c73c71344e4eab4bc446e9c7fc923b19b1c21`)

## memory-state (1 claim(s))

- [observation/documented] L2MAC reads and updates existing code files created many instruction steps earlier, and generates unit tests used as an error checker to fix code that fails after updates. -- evidence: [README.md#L162-L165](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L162-L165), [README.md#L176-L176](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L176-L176) (`clm_4f6790d79109c2af1a8e29c7601bd75a44033d73a294658db5e635ad3c6277d3`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The tools_enabled parameter controls which functions agents can use, defaulting to all available tools; for codebase generation, tools include syntax-error checking and running unit tests. -- evidence: [docs/guide/api.md#L9-L18](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L9-L18), [README.md#L31-L32](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L31-L32) (`clm_38802e992c323b0c3772365c82c4d3c5228e8cd06ee342b87af5f840288c35e3`)

## evaluation (1 claim(s))

- [observation/documented] The README reports benchmark results: the highest percentage of implemented user-specified features on system design tasks (averaged over 10 random seeds) and a claimed 90.2% Pass@1 on HumanEval. -- evidence: [README.md#L135-L136](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L135-L136), [README.md#L138-L140](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L138-L140) (`clm_892b17f9d243d77fbdda0a3b6d2293d1a1a02a44f375bb4b550d21a41e0ecb6c`)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt lists pyyaml, pydantic, typer>=0.9.0, numpy, openai, tiktoken, timeout-decorator, and pygame==2.1.2; the README states Python 3.7+ is needed. -- evidence: [README.md#L38-L39](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L38-L39), [requirements.txt#L1-L8](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/requirements.txt#L1-L8) (`clm_edd71fb9fc6c8aaf4c6e591bb5ca20930f2faf275be81c0a8ef9f7045a006c50`)
- [observation/documented] Configuration uses an LLM API with api_type (e.g. openai or azure), model (example gpt-4o), base_url, and api_key, set in ~/.l2mac/config.yaml or initialized via `l2mac --init-config`. -- evidence: [README.md#L51-L52](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L51-L52), [README.md#L59-L65](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L59-L65), [README.md#L54-L55](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L54-L55) (`clm_c05feff024bc3d2c437852991ede8b9984b4c6fdcb23a233fda5af8e4249f7d1`)

## limitations (1 claim(s))

- [observation/documented] The FAQ notes that any package an LLM agent tries to use must already be installed in the running virtualenv; self-created per-generation virtualenvs are planned on the roadmap. -- evidence: [docs/guide/faq.md#L36-L39](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L36-L39) (`clm_607a9dbacfcca7a49dcae274c51d1466c5b54980d70adbe6f84bcd5c5bfb4eba`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

