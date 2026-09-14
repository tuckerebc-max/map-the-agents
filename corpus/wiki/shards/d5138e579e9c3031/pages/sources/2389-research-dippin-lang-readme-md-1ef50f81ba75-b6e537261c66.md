---
access: public
aliases: []
claim_ids:
- clm_0ced0c1f6cf2123d4de9b5705d81d29e3f5b28df9c38dec9e90eaa93325422ab
- clm_1b493f7e2ed84cd3013990460aea386dce25513eb4e1666ce12c85ebe6eca08d
- clm_4274e78171743da678b3d32640846ea07df07c051046342ff395ddcfcd5c66bd
- clm_52cc5cbb06b7e166833cbb3c72126acfc384e48b775dae8e6604e31f259bb771
- clm_62867df5d4072db37887b93d48a6ad108768b607392b896142d3b1e431a2fcb9
- clm_6bb33b63cf9b1c1c2457844d0a071742ab3ae46e41b85665bdd0a07c3b37621b
- clm_8f053df3f7a5eac6dd5834a8722931ea7e32ecc5d7b8553ef2713983eee715c8
- clm_967d86354209ba0efb3a6d2014cd33c2f4cc9808098179f6e904a8820ca9cadf
- clm_c5935b88418ca5883274e1e47feadcf3f9b16c2254122fca233c0d0c0a8b34f3
- clm_cb399fc7273ec0c62fe6fff511c2325cded2d1e0ea1713c941be628e1d518df6
- clm_f59a745b2b4ca2979d1af1dbbe57081c1824ce4f81a4fedf71a52f5fe743f5a7
- clm_fbc8b9125ff814dbf9f6d64671b7a945e0d397deb6e1029b36f3504e4d687ebc
maturity: draft
page_id: pg_0387c3140d8957a480e8b6e537261c66
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_71bb9ff210a554a0ab1f0226e6a6e026
title: 2389-research/dippin-lang/README.md @ 1ef50f81ba75
updated_at: '2026-09-14T01:26:01Z'
---

# 2389-research/dippin-lang/README.md @ 1ef50f81ba75

<!-- rcw:begin owner=source:src_71bb9ff210a554a0ab1f0226e6a6e026 block=evidence -->
- The product includes a scenario test runner (dippin test) that executes .test.json suites against the simulator, and simulate supports --scenario and --all-paths to exercise workflow execution paths without real LLM calls. [@claim:clm_0ced0c1f6cf2123d4de9b5705d81d29e3f5b28df9c38dec9e90eaa93325422ab]
- The validator performs 10 structural checks (DIP001–DIP010) and 46 semantic lint rules (DIP101–DIP162 range), with diagnostics styled after the Rust compiler including codes, locations, and suggested fixes. [@claim:clm_1b493f7e2ed84cd3013990460aea386dce25513eb4e1666ce12c85ebe6eca08d]
- Core packages claim zero external dependencies; the LSP server uses go.lsp.dev libraries, watch uses fsnotify, and coverage's shell parsing uses mvdan.cc/sh/v3/syntax. Go 1.21+ is required to build. [@claim:clm_4274e78171743da678b3d32640846ea07df07c051046342ff395ddcfcd5c66bd]
- A VS Code extension in editors/vscode/ provides .dip syntax highlighting, comment toggling, indentation-based folding, and auto-indent after colons. [@claim:clm_52cc5cbb06b7e166833cbb3c72126acfc384e48b775dae8e6604e31f259bb771]
- Analysis commands exit 0/1/2 for ok/errors/usage, while bundle commands use a finer ladder including integrity error (2), I/O error (3), and cancelled (4). [@claim:clm_62867df5d4072db37887b93d48a6ad108768b607392b896142d3b1e431a2fcb9]
- The dippin CLI offers authoring commands (parse, validate, lint, check, fmt, new, export-dot, migrate, validate-migration) plus analysis, bundle, and editor tooling subcommands. [@claim:clm_6bb33b63cf9b1c1c2457844d0a071742ab3ae46e41b85665bdd0a07c3b37621b]
- The language uses explicit node keywords (agent, tool, human, parallel, fan_in, subgraph, manager_loop) instead of DOT shape overloading, and indented multiline blocks preserve content verbatim without escaping. [@claim:clm_8f053df3f7a5eac6dd5834a8722931ea7e32ecc5d7b8553ef2713983eee715c8]
- Any command accepts --format json for machine-readable JSON diagnostics on stderr, and dippin lsp starts a stdio Language Server Protocol server with diagnostics, hover, go-to-definition, autocomplete, and document symbols. [@claim:clm_967d86354209ba0efb3a6d2014cd33c2f4cc9808098179f6e904a8820ca9cadf]
- A .dipx bundle is a deterministic, content-addressed ZIP verified by SHA-256; pack, unpack (atomic via staging plus rename), and inspect commands manage bundles, and all analysis commands accept a .dipx transparently. [@claim:clm_c5935b88418ca5883274e1e47feadcf3f9b16c2254122fca233c0d0c0a8b34f3]
- The architecture centers on an ir.Workflow intermediate representation consumed by parser, validator, formatter, exporter, migrator, simulator, cost/coverage/doctor/optimize, diff, testrunner, and LSP packages. [@claim:clm_cb399fc7273ec0c62fe6fff511c2325cded2d1e0ea1713c941be628e1d518df6]
- Repository development practice: a pre-commit hook (installed via 'just setup-hooks') enforces gocyclo ≤5, gocognit ≤7, gofmt formatting, go test with -race, and validation of all example .dip files; 'just check' runs the full suite. [@claim:clm_f59a745b2b4ca2979d1af1dbbe57081c1824ce4f81a4fedf71a52f5fe743f5a7]
- Dippin is positioned as an authoring format replacing Graphviz DOT for AI pipelines, keeping DOT as the visualization target via export-dot while giving prompts, shell scripts, model config, and branching first-class syntax. [@claim:clm_fbc8b9125ff814dbf9f6d64671b7a945e0d397deb6e1029b36f3504e4d687ebc]
<!-- rcw:end owner=source:src_71bb9ff210a554a0ab1f0226e6a6e026 block=evidence -->

## Researcher notes

