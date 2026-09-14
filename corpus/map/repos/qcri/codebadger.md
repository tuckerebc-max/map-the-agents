# qcri/codebadger

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: lekssays/codebadger (github id 1067656065).
Latest snapshot: commit 857adcabe386 @ 4467dca7c5129a6c

## Summary (orientation draft, not independently verified)

Selected evidence records: codebadger is a containerized MCP server giving AI agents queryable access to codebase structure and data flow via Joern Code Property Graphs. It accepts a Git repository, local path, or pasted snippet, builds a CPG, and exposes it over MCP for CPGQL queries, taint tracing, slicing, and vulnerability hunting.

## Source coverage

Source coverage (partial): 6 of 16 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] codebadger is a containerized MCP server giving AI agents queryable access to codebase structure and data flow via Joern Code Property Graphs. -- evidence: [README.md#L3-L5](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/README.md#L3-L5)
- components (1 claim(s)):
  - [observation/documented] Vulnerability detectors cover use-after-free, double free, null deref (CWE-476), heap/stack overflow, uninitialized reads, integer overflow, format strings, TOCTOU, and command injection. -- evidence: [docs/available-tools.md#L106-L109](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L106-L109), [docs/available-tools.md#L95-L102](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L95-L102), [docs/available-tools.md#L113-L116](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L113-L116)
- design-choices (1 claim(s)):
  - [observation/documented] The product analyzes only the CPG, not files on disk: source is discarded after the build, so there are no file-reading tools and users must grep their own checkout. -- evidence: [docs/available-tools.md#L19-L22](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L19-L22), [docs/available-tools.md#L34-L38](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L34-L38)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: docs/contributing.md covers dev setup, tests, and guidelines, and tests/ contains unit and integration suites per the repository layout. -- evidence: [docs/architecture.md#L154-L165](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L154-L165), [README.md#L30-L42](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/README.md#L30-L42)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] It accepts a Git repository, local path, or pasted snippet, builds a CPG, and exposes it over MCP for CPGQL queries, taint tracing, slicing, and vulnerability hunting. -- evidence: [README.md#L7-L11](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/README.md#L7-L11)
  - [observation/documented] Documented tools include generate_cpg, get_cpg_status, remove_cpg, list_methods, get_call_graph, get_cfg, run_cpgql_query, find_taint_flows, get_program_slice, and get_variable_flow. -- evidence: [docs/available-tools.md#L77-L83](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L77-L83), [docs/available-tools.md#L48-L53](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L48-L53), [docs/available-tools.md#L62-L68](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L62-L68), [docs/available-tools.md#L34-L38](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/available-tools.md#L34-L38)
- memory-state (2 claim(s)):
  - [observation/documented] Admission is governed by a memory budget rather than a fixed server count: heap tiers derive from CPG size, with LRU eviction, an RSS backstop, and an idle-TTL reaper (default 600s). -- evidence: [docs/architecture.md#L88-L89](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L88-L89), [docs/architecture.md#L102-L112](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L102-L112)
  - [observation/documented] CPGs are disk-cached by content hash; sleeping servers cost no RAM and wake by re-importing the cached .bin on the next query. -- evidence: [docs/architecture.md#L83-L84](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L83-L84)
- orchestration (2 claim(s)):
  - [observation/documented] Joern runs out-of-process in Docker; a Python FastMCP server orchestrates CPG generation, a memory-aware query-server pool, caching, and a durable job queue. -- evidence: [docs/architecture.md#L3-L5](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L3-L5), [docs/architecture.md#L9-L11](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L9-L11)
  - [observation/documented] Postgres stores catalog, tool cache, findings, and the durable job queue; Redis holds cross-process query locks and the pool ledger, and the server refuses to boot if either is unreachable. -- evidence: [docs/architecture.md#L33-L42](https://github.com/qcri/codebadger/blob/857adcabe38677c53d068b310ab4f6ca51828c61/docs/architecture.md#L33-L42)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](codebadger.detail.md)

Metadata and full claim list: [full detail](codebadger.detail.md)
Human notes ([notes](codebadger.notes.md), never overwritten by build)

[Back to map index](../../index.md)
