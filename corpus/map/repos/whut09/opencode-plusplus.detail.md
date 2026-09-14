# whut09/opencode-plusplus -- full detail

[Back to orientation](opencode-plusplus.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/whut09/opencode-plusplus/598767170bb73e869293c6a91526bcb852b696c0/009551e19bce206c.json](../../../wiki/dossiers/whut09/opencode-plusplus/598767170bb73e869293c6a91526bcb852b696c0/009551e19bce206c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The architecture is described as Guard modules around coding agents: Context, Hallucination, Boundary, Regression, Evidence, Impact, and Loop Guards, plus an Executor Adapter and Trace Normalizer. -- evidence: [docs/concepts/architecture.md#L61-L68](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L61-L68) (`clm_3a4916dd5bc6963ea37cea113cedaea187e167d96cc4442d78b02b4b00ba984a`)
- [observation/documented] The v2 architecture has five responsibilities: Repo Scanner, Context Planner, Context Pack Composer, Agent Harness Layer, and an Integration Layer exposing CLI, stdio MCP server, and retriever adapters. -- evidence: [docs/concepts/architecture.md#L145-L149](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L145-L149) (`clm_3e6c402bbfa9db0f736dea9ecf2172bb812f08ea2fbc3343c7a1335856e05adb`)

## design-choices (2 claim(s))

- [observation/documented] By default the plugin works offline: it does not fetch remote Context sources or call a second model; remote sources or feedback transports must be explicitly enabled. -- evidence: [README.md#L48-L48](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L48-L48) (`clm_49cecca808c9b69673572d73ea82b182f6e3a8e3c3be5d181df0dacadcff8d49`)
- [observation/documented] The plugin runs in-process inside OpenCode Desktop, does not start a second model or CLI process, and does not expose hidden model chain-of-thought. -- evidence: [README.md#L44-L44](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L44-L44), [README.md#L92-L92](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L92-L92) (`clm_c91721ef053953c0cf728c2c5a45f19c6b2ee4630c8f8ce774bcb08a8bc23505`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors fork, read AGENTS.md, add deterministic tests before behavior changes, keep runtime artifacts out of commits, and run npm run check, lint, format:check, docs:bilingual:check, and npm test. -- evidence: [README.md#L125-L131](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L125-L131) (`clm_af975098dfe5e6c90cec3cae92ed1a0547cd6f25c6568b6208cd03c8b5487095`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The Windows installer adds a selectable OpenCode primary mode named OpenCode++ chosen from the mode picker, with no Slash Commands to remember. -- evidence: [README.md#L40-L40](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L40-L40) (`clm_86b1491f8552eb44bc3212aaebcbd24ef94d8229cb18d0c44eeddaf1d11405e9`)
- [observation/documented] Documented MCP tools include opencode_plusplus_build, plan, pack, retrieve, tests, impact, verify, and explain, plus experimental runtime loop tools for start/evaluate/repair/finalize flows. -- evidence: [docs/concepts/architecture.md#L145-L149](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L145-L149) (`clm_e5220aead22c812ec249be6580763989d48953c8f8b1e0a192f13dceb35e99ed`)
- [observation/documented] Desktop results default to a compact Verified, Repair required, or Human review status, with structured JSON containing an actionSummary of observed, prevented, requested, repaired, verified, and unresolved items. -- evidence: [README.md#L90-L90](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L90-L90) (`clm_cf859cfb002088c1cde2700bca96d733a8a447f98c2847a294417de7fb108001`)

## memory-state (2 claim(s))

- [observation/documented] Runtime artifacts are local per repository: traces, runs, loops, sidecar latest.md and visualization.json, plus cache, context-registry usage/feedback, annotations, and interventions directories under .agent-context/. -- evidence: [README.md#L80-L84](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L80-L84), [README.md#L104-L104](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L104-L104) (`clm_2497cb3e3c24a6c42b4703774043b26d17a6b3ffa14d90290dabd285faf69196`)
- [observation/documented] The loop state file records state, previousState, repository/context/diff hashes, lastAction, blocking nextAction, allowedActions, satisfiedEvidence, and missingEvidence for resumable runs. -- evidence: [docs/concepts/architecture.md#L334-L334](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L334-L334) (`clm_9c833ae391b9e0006427e8438706b0d699baaec5f1fe3e0bce087b4678115cb7`)

## orchestration (2 claim(s))

- [observation/documented] A harness-led developer mode, opencode-plusplus orchestrate, runs a bounded loop (task, prepare, execute, collect, evaluate, decide, persist) around an explicitly configured executor, reporting finalize, repair, repack, block, rollback, or human-review. -- evidence: [docs/concepts/architecture.md#L155-L157](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L155-L157) (`clm_368005b66b4e53e89a1e2acb5fb5bae43c3caa9a9bd21f6f7d9624e785e51087`)
- [observation/documented] The loop controller decides next steps such as start-agent, rebuild-context, replan, expand-context, repair-contracts, add-or-update-tests, run-tests, or ready-for-review, each with a confidence score and blocking flag. -- evidence: [docs/concepts/architecture.md#L330-L330](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L330-L330), [docs/concepts/architecture.md#L321-L328](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L321-L328) (`clm_ddc9a086391a35f3908fbb8272286a6c758c3c2a6afdfe7ea210073e34b17302`)

## tools-permissions (2 claim(s))

- [observation/documented] The Command Guard represents repository semantics: it can defer operations as approval-required or hard-stop policy-blocked destructive commands, protected paths, unknown project commands, or evidence tampering; native auto approval cannot override the latter. -- evidence: [docs/concepts/architecture.md#L46-L46](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L46-L46) (`clm_35454948309d6e8a93ea6dc8c844098d21097f1fad274250449c8ba6d1494ba1`)
- [observation/documented] The plugin explicitly is not an operating-system sandbox; it cannot stop another application from editing a file or prove business semantics from an exit code. -- evidence: [README.md#L86-L86](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L86-L86) (`clm_6db76b511b4e0757606e6e78946f762eea12f230874571947b7f8e5cf7eb718e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Indexing uses the TypeScript Compiler API for TS/JS, optional Tree-sitter for Python with stdlib AST and regex fallback, and generic metadata for other files; real tokenizer modes use js-tiktoken with a chars_approx fallback. -- evidence: [docs/concepts/architecture.md#L271-L271](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L271-L271), [docs/concepts/architecture.md#L194-L196](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L194-L196) (`clm_5bf6237f880c0d6a1295194e977d94214dd8e35c65a7c44740c298725007698f`)

## limitations (1 claim(s))

- [observation/documented] A passing command alone is evidence, not a correctness proof; verified fixes require fresh command or CI evidence matched to the current working tree, and blocking results require repair or human review. -- evidence: [README.md#L86-L86](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L86-L86), [README.md#L96-L100](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L96-L100), [README.md#L28-L34](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L28-L34) (`clm_dfedc3d12440d425f2ce8f6881281c57b133753d9b037201982221e7b52afa56`)

## relevance (1 claim(s))

- [observation/documented] The project targets helping coding agents safely complete concrete changes, distinguishing itself from repo summarizers, README generators, and raw RAG loaders. -- evidence: [docs/concepts/architecture.md#L159-L159](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L159-L159) (`clm_b10e31b6d60b0c5864dbe169525dc05ca1da7088b10f4057f5ca5ea610642038`)

