# qcri/codebadger -- full detail

[Back to orientation](codebadger.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/qcri/codebadger/857adcabe38677c53d068b310ab4f6ca51828c61/4467dca7c5129a6c.json](../../../wiki/dossiers/qcri/codebadger/857adcabe38677c53d068b310ab4f6ca51828c61/4467dca7c5129a6c.json)

## specifications (1 claim(s))

- [observation/documented] codebadger is a containerized MCP server giving AI agents queryable access to codebase structure and data flow via Joern Code Property Graphs. -- evidence: [README.md#L3-L5](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/README.md#L3-L5) (`clm_a3414dc7335b049bfb74f9de522a114993622259c9159041b5874cb060cfa8d1`)

## components (1 claim(s))

- [observation/documented] Vulnerability detectors cover use-after-free, double free, null deref (CWE-476), heap/stack overflow, uninitialized reads, integer overflow, format strings, TOCTOU, and command injection. -- evidence: [docs/available-tools.md#L106-L109](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L106-L109), [docs/available-tools.md#L95-L102](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L95-L102), [docs/available-tools.md#L113-L116](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L113-L116) (`clm_7534fb0d5e43f58e61709c4528f73172cb7da6bd32456dcbbbe0bb6e00ca247d`)

## design-choices (1 claim(s))

- [observation/documented] The product analyzes only the CPG, not files on disk: source is discarded after the build, so there are no file-reading tools and users must grep their own checkout. -- evidence: [docs/available-tools.md#L19-L22](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L19-L22), [docs/available-tools.md#L34-L38](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L34-L38) (`clm_1c8b043b57ca5a887e56505d7952db69de53c1927c10b4a5e224c0946d12cd51`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: docs/contributing.md covers dev setup, tests, and guidelines, and tests/ contains unit and integration suites per the repository layout. -- evidence: [docs/architecture.md#L154-L165](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L154-L165), [README.md#L30-L42](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/README.md#L30-L42) (`clm_eddbab0b459a32ee1bbd15d57e34d03969dc32e68f2862158c49eb5082a139de`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] It accepts a Git repository, local path, or pasted snippet, builds a CPG, and exposes it over MCP for CPGQL queries, taint tracing, slicing, and vulnerability hunting. -- evidence: [README.md#L7-L11](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/README.md#L7-L11) (`clm_afb163250a804e714901a4165b99e9bac622ef5881646d1fa92407fc0cfe2389`)
- [observation/documented] Documented tools include generate_cpg, get_cpg_status, remove_cpg, list_methods, get_call_graph, get_cfg, run_cpgql_query, find_taint_flows, get_program_slice, and get_variable_flow. -- evidence: [docs/available-tools.md#L77-L83](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L77-L83), [docs/available-tools.md#L48-L53](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L48-L53), [docs/available-tools.md#L62-L68](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L62-L68), [docs/available-tools.md#L34-L38](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L34-L38) (`clm_991f98a2b40e90c9654cb89e216e7022e85f6c567e396e913c27706fa929fe9a`)
- [observation/documented] A GET /health endpoint probes joern, postgres, redis, docker, and cpg_queue concurrently, returning up/partial/down with HTTP 200/503 for orchestrators. -- evidence: [docs/architecture.md#L133-L135](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L133-L135), [docs/architecture.md#L137-L146](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L137-L146) (`clm_cad58bb0f79f261bb375a9cf2b3748f801aa7ed68c4451b0a78201a56c2e41a1`)

## memory-state (2 claim(s))

- [observation/documented] Admission is governed by a memory budget rather than a fixed server count: heap tiers derive from CPG size, with LRU eviction, an RSS backstop, and an idle-TTL reaper (default 600s). -- evidence: [docs/architecture.md#L88-L89](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L88-L89), [docs/architecture.md#L102-L112](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L102-L112) (`clm_d5b7cab0ede4e71c693091319690d6b5c4a003541a2e1dd4a0d40724360426a9`)
- [observation/documented] CPGs are disk-cached by content hash; sleeping servers cost no RAM and wake by re-importing the cached .bin on the next query. -- evidence: [docs/architecture.md#L83-L84](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L83-L84) (`clm_c4d3ec1a1eff10baba78763332f400021c9f4b3d26516b39a80d40ffed4cf37f`)

## orchestration (2 claim(s))

- [observation/documented] Joern runs out-of-process in Docker; a Python FastMCP server orchestrates CPG generation, a memory-aware query-server pool, caching, and a durable job queue. -- evidence: [docs/architecture.md#L3-L5](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L3-L5), [docs/architecture.md#L9-L11](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L9-L11) (`clm_525758f066a3868907d88ac5d23d4fc4ce4477bbc18dbd70acfdf856a9c23095`)
- [observation/documented] Postgres stores catalog, tool cache, findings, and the durable job queue; Redis holds cross-process query locks and the pool ledger, and the server refuses to boot if either is unreachable. -- evidence: [docs/architecture.md#L33-L42](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L33-L42) (`clm_b70b2702076dc089762bdc197e643d4e093417d6d2ed28ad5e42295b64c90b97`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Configuration comes from config.yaml overlaid by env vars only where ${VAR:default} placeholders exist; memory settings default to 0 for auto-derivation from host RAM. -- evidence: [docs/configuration.md#L3-L7](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/configuration.md#L3-L7), [docs/configuration.md#L35-L37](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/configuration.md#L35-L37) (`clm_3480f2b93dc74583b8dcaf3484e4e42abbc5b88f2cd4eaf38322ee79746522ea`)

## limitations (1 claim(s))

- [observation/documented] Git-history reconnaissance is not a built-in tool because only the CPG is kept, not the source .git; such mining must be run in a separate checkout. -- evidence: [docs/available-tools.md#L125-L127](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L125-L127) (`clm_325c6474998977cfd0ee302e4824ee1ca1d7837b574e492a70e6b8ffed77c449`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

