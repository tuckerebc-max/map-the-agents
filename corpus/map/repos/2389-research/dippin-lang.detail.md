# 2389-research/dippin-lang -- full detail

[Back to orientation](dippin-lang.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/dippin-lang/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/5334cb5b7378dda0.json](../../../wiki/dossiers/2389-research/dippin-lang/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/5334cb5b7378dda0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The architecture centers on an ir.Workflow intermediate representation consumed by parser, validator, formatter, exporter, migrator, simulator, cost/coverage/doctor/optimize, diff, testrunner, and LSP packages. -- evidence: [README.md#L525-L546](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L525-L546), [README.md#L505-L521](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L505-L521), [README.md#L523-L523](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L523-L523) (`clm_cb399fc7273ec0c62fe6fff511c2325cded2d1e0ea1713c941be628e1d518df6`)
- [observation/documented] The validator performs 10 structural checks (DIP001–DIP010) and 46 semantic lint rules (DIP101–DIP162 range), with diagnostics styled after the Rust compiler including codes, locations, and suggested fixes. -- evidence: [README.md#L525-L546](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L525-L546), [README.md#L382-L392](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L382-L392), [README.md#L371-L371](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L371-L371), [README.md#L396-L426](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L396-L426) (`clm_1b493f7e2ed84cd3013990460aea386dce25513eb4e1666ce12c85ebe6eca08d`)

## design-choices (2 claim(s))

- [observation/documented] Dippin is positioned as an authoring format replacing Graphviz DOT for AI pipelines, keeping DOT as the visualization target via export-dot while giving prompts, shell scripts, model config, and branching first-class syntax. -- evidence: [README.md#L9-L9](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L9-L9), [README.md#L5-L5](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L5-L5), [README.md#L37-L37](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L37-L37) (`clm_fbc8b9125ff814dbf9f6d64671b7a945e0d397deb6e1029b36f3504e4d687ebc`)
- [observation/documented] The language uses explicit node keywords (agent, tool, human, parallel, fan_in, subgraph, manager_loop) instead of DOT shape overloading, and indented multiline blocks preserve content verbatim without escaping. -- evidence: [README.md#L268-L268](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L268-L268), [README.md#L310-L310](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L310-L310), [README.md#L275-L275](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L275-L275), [README.md#L261-L261](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L261-L261), [README.md#L27-L35](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L27-L35) (`clm_8f053df3f7a5eac6dd5834a8722931ea7e32ecc5d7b8553ef2713983eee715c8`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: a pre-commit hook (installed via 'just setup-hooks') enforces gocyclo ≤5, gocognit ≤7, gofmt formatting, go test with -race, and validation of all example .dip files; 'just check' runs the full suite. -- evidence: [README.md#L566-L566](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L566-L566), [README.md#L568-L574](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L568-L574), [README.md#L556-L562](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L556-L562) (`clm_f59a745b2b4ca2979d1af1dbbe57081c1824ce4f81a4fedf71a52f5fe743f5a7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The dippin CLI offers authoring commands (parse, validate, lint, check, fmt, new, export-dot, migrate, validate-migration) plus analysis, bundle, and editor tooling subcommands. -- evidence: [README.md#L144-L156](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L144-L156), [README.md#L160-L165](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L160-L165), [README.md#L169-L174](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L169-L174), [README.md#L130-L140](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L130-L140) (`clm_6bb33b63cf9b1c1c2457844d0a071742ab3ae46e41b85665bdd0a07c3b37621b`)
- [observation/documented] Analysis commands exit 0/1/2 for ok/errors/usage, while bundle commands use a finer ladder including integrity error (2), I/O error (3), and cancelled (4). -- evidence: [README.md#L176-L176](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L176-L176) (`clm_62867df5d4072db37887b93d48a6ad108768b607392b896142d3b1e431a2fcb9`)
- [observation/documented] Any command accepts --format json for machine-readable JSON diagnostics on stderr, and dippin lsp starts a stdio Language Server Protocol server with diagnostics, hover, go-to-definition, autocomplete, and document symbols. -- evidence: [README.md#L458-L463](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L458-L463), [README.md#L178-L178](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L178-L178) (`clm_967d86354209ba0efb3a6d2014cd33c2f4cc9808098179f6e904a8820ca9cadf`)
- [observation/documented] A .dipx bundle is a deterministic, content-addressed ZIP verified by SHA-256; pack, unpack (atomic via staging plus rename), and inspect commands manage bundles, and all analysis commands accept a .dipx transparently. -- evidence: [README.md#L124-L124](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L124-L124), [README.md#L118-L122](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L118-L122), [README.md#L116-L116](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L116-L116) (`clm_c5935b88418ca5883274e1e47feadcf3f9b16c2254122fca233c0d0c0a8b34f3`)
- [observation/documented] A VS Code extension in editors/vscode/ provides .dip syntax highlighting, comment toggling, indentation-based folding, and auto-indent after colons. -- evidence: [README.md#L469-L473](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L469-L473) (`clm_52cc5cbb06b7e166833cbb3c72126acfc384e48b775dae8e6604e31f259bb771`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The product includes a scenario test runner (dippin test) that executes .test.json suites against the simulator, and simulate supports --scenario and --all-paths to exercise workflow execution paths without real LLM calls. -- evidence: [README.md#L444-L446](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L444-L446), [README.md#L144-L156](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L144-L156), [README.md#L450-L452](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L450-L452), [README.md#L430-L430](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L430-L430) (`clm_0ced0c1f6cf2123d4de9b5705d81d29e3f5b28df9c38dec9e90eaa93325422ab`)

## dependencies (1 claim(s))

- [observation/documented] Core packages claim zero external dependencies; the LSP server uses go.lsp.dev libraries, watch uses fsnotify, and coverage's shell parsing uses mvdan.cc/sh/v3/syntax. Go 1.21+ is required to build. -- evidence: [docs/analysis.md#L114-L117](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/docs/analysis.md#L114-L117), [README.md#L43-L43](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L43-L43), [README.md#L550-L550](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/README.md#L550-L550) (`clm_4274e78171743da678b3d32640846ea07df07c051046342ff395ddcfcd5c66bd`)

## limitations (1 claim(s))

- [observation/documented] The cost command does not cross-reference parsed budget ceilings such as max_cost_cents, so no warning is emitted when estimated cost exceeds the budget. -- evidence: [docs/analysis.md#L55-L61](https://github.com/2389-research/dippin-lang/blob/1ef50f81ba75e7cb92e470f34c07c743d2b07c4c/docs/analysis.md#L55-L61) (`clm_e86cc8898161ba8baa81915ac9ea64c2167326920c745401a0c4603f641eb977`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

