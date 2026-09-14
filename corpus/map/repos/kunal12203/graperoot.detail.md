# kunal12203/graperoot -- full detail

[Back to orientation](graperoot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kunal12203/graperoot/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/657d207f0df5b456.json](../../../wiki/dossiers/kunal12203/graperoot/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/657d207f0df5b456.json)

## specifications (1 claim(s))

- [observation/documented] GrapeRoot is described as an open-source launcher that sits between the user and an AI coding assistant, building a semantic graph of files, symbols, imports, and call chains to pre-load relevant code into each prompt. -- evidence: [README.md#L36-L36](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L36-L36) (`clm_0667d9c48fc227f8ac7df1cb0680ec75cee55027ee0a1f772be35bd7d282819e`)

## components (1 claim(s))

- [observation/documented] Project data lives in `<project>/.dual-graph/` (info_graph.json for the semantic graph, chat_action_graph.json for session memory, context-store.json for persistent decisions/tasks/facts), with a global install at `~/.dual-graph/`. -- evidence: [README.md#L287-L291](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L287-L291), [README.md#L279-L283](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L279-L283), [README.md#L285-L285](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L285-L285), [README.md#L277-L277](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L277-L277) (`clm_a2465bfe59d6e087aba968d090d7b07ad72c731ccfc3520f2dc0f82e2ff1278b`)

## design-choices (1 claim(s))

- [observation/documented] All processing is stated to be local with no code leaving the machine, and telemetry is limited to anonymous crash reports (error type, failed step, OS/Python version, product version), explicitly excluding code, file paths, project names, prompts, and personal data. -- evidence: [README.md#L338-L338](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L338-L338), [README.md#L334-L336](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L334-L336), [README.md#L332-L332](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L332-L332), [README.md#L271-L271](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L271-L271) (`clm_b544584cbf1b437c88efedc91d45b9fed5d5a8e1dfcafe8a3c07aa0209f9988f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's contributing section invites PRs for bug fixes, new AI assistant support, install improvements, and docs for the open-source launcher scripts. -- evidence: [README.md#L368-L368](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L368-L368) (`clm_3678470c1677ce8c2ac2d9b3cd86c02900da89c61819814fd7e323b1c86dd2ad`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes launcher commands: `dgc` for Claude Code, `dg` for Codex CLI, `dgo` for OpenCode, and `graperoot . --<tool>` flags for Cursor, Gemini CLI, Copilot, OpenClaw, Kilocode, MiMo Code, Antigravity, Kiro CLI, and Command Code. -- evidence: [README.md#L127-L140](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L127-L140), [README.md#L240-L251](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L240-L251), [README.md#L179-L183](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L179-L183), [README.md#L187-L191](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L187-L191), [README.md#L232-L236](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L232-L236) (`clm_472679bcff213673743544cc72c7076c2d7c32eeb7ac2f5d201fe69018740b28`)
- [observation/documented] The `graperoot` CLI supports an interactive picker, `--version`, `--update`, `--no-auto-update`, `--auto-update`, and `--no-telemetry`/`--telemetry` flags per the README usage sections. -- evidence: [README.md#L321-L324](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L321-L324), [README.md#L223-L228](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L223-L228), [README.md#L311-L314](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L311-L314), [README.md#L316-L319](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L316-L319), [README.md#L340-L344](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L340-L344) (`clm_93cd3ae6d87b222eb6a4a51d3efd2191dcf7c5d0e0ea12d668a01d500e1e1223`)

## memory-state (1 claim(s))

- [observation/documented] The README describes session memory: files that were read, edited, or queried are weighted higher in future turns, so context compounds across a session. -- evidence: [README.md#L52-L52](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L52-L52), [README.md#L266-L269](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L266-L269) (`clm_5c077b75da2b64a399993a6f592f42d8ecfd16ca4f157e3f96d95ff951cf6d44`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The AI assistant can call graph-aware MCP tools (`graph_read`, `graph_retrieve`, `graph_neighbors`) to explore further, and read budgets are hard-capped per turn via environment variables like DG_HARD_MAX_READ_CHARS (default 4000) and DG_TURN_READ_BUDGET_CHARS (default 18000). -- evidence: [README.md#L299-L305](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L299-L305), [README.md#L266-L269](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L266-L269) (`clm_96b6e692a00eeb3497137124f1eed4769aa8d3ae5a973da78a60fb3251625030`)

## evaluation (1 claim(s))

- [observation/documented] The README reports benchmarks over real-world codebases (7,700+ files) and 50+ prompts, claiming cost per prompt dropping from $0.49 to $0.27, average turns from 11.7 to 3.5, and quality scores from 76.6 to 86.6 out of 100, with full methodology at graperoot.dev/benchmarks. -- evidence: [README.md#L99-L105](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L99-L105), [README.md#L121-L121](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L121-L121), [README.md#L97-L97](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L97-L97) (`clm_6fc75c51afdd856b301b29649d70d932f64a94ad88b9389877bf7cb0129efba8`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The graph engine (`graperoot` pip package) is proprietary; only the launcher scripts in `bin/` are open source under Apache 2.0, per the licensing and contributing sections. -- evidence: [README.md#L396-L396](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L396-L396), [README.md#L368-L368](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L368-L368), [README.md#L398-L398](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L398-L398), [README.md#L38-L38](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L38-L38), [README.md#L370-L370](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L370-L370) (`clm_35ac8f7234e4b70bdb6ca027e019249cae7e83deb9df9f908406e593d6407f90`)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers using AI coding assistants on TypeScript, JavaScript, Python, Go, Swift, Rust, Java, Kotlin, Scala, C#, Ruby, and PHP codebases, on macOS, Linux, or Windows. -- evidence: [README.md#L13-L17](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L13-L17), [README.md#L146-L146](https://github.com/kunal12203/GrapeRoot/blob/e21c5b9cd3e3a1392c1861d4e98a7c434fb5fbdb/README.md#L146-L146) (`clm_87b802a21e8db6e32ae3c9f15dfb124050e28325f6b04a1bcc624f1d1c3f59de`)

