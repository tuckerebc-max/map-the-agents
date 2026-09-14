# samholt/l2mac

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 105e74afdc67 @ 3bdf23d1d7da66dc

## Summary (orientation draft, not independently verified)

L2MAC is documented as an LLM-based multi-agent framework that executes self-generated prompt programs via a control unit and persistent file store to produce large outputs (codebases, books) from a single prompt, with a CLI and Python API, YAML-based LLM configuration, and reported benchmark results.

## Source coverage

Source coverage (partial): 6 of 38 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Each prompt-program instruction step is loaded into a new LLM agent whose context is managed by a control unit and given tools to read and write a persistent file-store holding final and intermediate outputs. -- evidence: [README.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L28-L29)
- design-choices (3 claim(s)):
  - [observation/documented] L2MAC is described as an LLM-based multi-agent system implementing a stored-program von Neumann-style architecture for extensive, consistent output generation. -- evidence: [README.md#L4-L6](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L4-L6), [README.md#L8-L10](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L8-L10)
  - [observation/documented] The prompt-program is a sequence of instruction-step prompts; unless explicitly given, it is self-generated (bootstrapped) and then executed. -- evidence: [README.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L28-L29)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors join the dev team by submitting a PR, with ongoing tasks listed on the roadmap; a rotating Chief Evangelist community role is recruited via email. -- evidence: [docs/guide/faq.md#L31-L31](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L31-L31), [docs/guide/faq.md#L16-L17](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L16-L17), [docs/guide/faq.md#L21-L21](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L21-L21), [docs/guide/faq.md#L36-L39](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/faq.md#L36-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] L2MAC offers a CLI (e.g. `l2mac "..."` creating a codebase repo in ./workspace) and a Python library API including generate_codebase and run_l2mac, plus helper functions for book and custom domains. -- evidence: [docs/guide/api.md#L28-L29](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L28-L29), [docs/guide/api.md#L42-L42](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L42-L42), [README.md#L77-L81](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L77-L81), [docs/guide/api.md#L46-L46](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L46-L46), [README.md#L71-L73](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L71-L73), [docs/guide/api.md#L38-L38](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L38-L38)
  - [observation/documented] The main generation API accepts parameters including prompt_task, domain ('codebase' or 'book', default 'codebase'), run_tests (default False), steps (default 10), prompt_program, prompts_file_path, tools_enabled, debugging_level, and init_config. -- evidence: [docs/guide/api.md#L9-L18](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L9-L18)
- memory-state (1 claim(s)):
  - [observation/documented] L2MAC reads and updates existing code files created many instruction steps earlier, and generates unit tests used as an error checker to fix code that fails after updates. -- evidence: [README.md#L162-L165](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L162-L165), [README.md#L176-L176](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L176-L176)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The tools_enabled parameter controls which functions agents can use, defaulting to all available tools; for codebase generation, tools include syntax-error checking and running unit tests. -- evidence: [docs/guide/api.md#L9-L18](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/docs/guide/api.md#L9-L18), [README.md#L31-L32](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L31-L32)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports benchmark results: the highest percentage of implemented user-specified features on system design tasks (averaged over 10 random seeds) and a claimed 90.2% Pass@1 on HumanEval. -- evidence: [README.md#L135-L136](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L135-L136), [README.md#L138-L140](https://github.com/samholt/L2MAC/blob/105e74afdc6721e4d530c65862a32b97b5434e61/README.md#L138-L140)
- dependencies (2 claim(s)):
More evidence: [full detail](l2mac.detail.md)

Metadata and full claim list: [full detail](l2mac.detail.md)
Human notes ([notes](l2mac.notes.md), never overwritten by build)

[Back to map index](../../index.md)
