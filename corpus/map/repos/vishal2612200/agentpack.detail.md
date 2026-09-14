# vishal2612200/agentpack -- full detail

[Back to orientation](agentpack.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vishal2612200/agentpack/42291598e79344feae3a9dfdfd0778df9e7dd578/fa61ecf8e3ff9329.json](../../../wiki/dossiers/vishal2612200/agentpack/42291598e79344feae3a9dfdfd0778df9e7dd578/fa61ecf8e3ff9329.json)

## specifications (1 claim(s))

- [observation/documented] The project is at alpha version 0.4.4, licensed AGPL v3, with APIs that may change before 1.0 and platform targets of macOS, Linux, and Windows PowerShell with Git for Windows. -- evidence: [README.md#L422-L422](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L422-L422), [README.md#L398-L398](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L398-L398), [README.md#L400-L402](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L400-L402) (`clm_c386e4c0b6f7208262b31272dd45150c13701af213e8c4566bc1a532bc5c7cb8`)

## components (2 claim(s))

- [observation/documented] The architecture is a local pipeline: scan with .agentignore, build offline summaries and a Tree-sitter semantic graph, score files for the task, select by value per token, redact secrets at materialization, and cache a pack registry with block IDs. -- evidence: [docs/architecture.md#L3-L3](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L3-L3), [docs/architecture.md#L66-L86](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L66-L86) (`clm_d116c0cf96861979462133c2f4327d28977f0d3c53fd629c4727657b85bb339d`)
- [observation/documented] Adapters render agent-specific context files (Claude, Cursor, Windsurf, Codex, Antigravity, generic), while separate installers configure each tool's repo files such as CLAUDE.md, .cursorrules, and AGENTS.md. -- evidence: [docs/architecture.md#L269-L277](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L269-L277), [docs/architecture.md#L279-L284](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L279-L284) (`clm_4a0658aa6790e099b39e55a1973d2d0082225b27bf4bdaffb309fb0fe08ee30e`)

## design-choices (1 claim(s))

- [observation/documented] Core scan, route, pack, stats, explain, and benchmark operations run without hosted indexing, embeddings, or model API calls; network use is limited to explicit GitHub operations, optional enrichment, and external-agent workflows. -- evidence: [README.md#L264-L267](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L264-L267), [README.md#L276-L280](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L276-L280) (`clm_0f7881a93d0fc238ab33b2f78842149641b32db3f969e72c357b08826dbc8afa`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a CLI four-command loop: agentpack work, learn --json, finish, and doctor, where work prepares task context, finish records validation and task memory, and doctor checks installation and integration. -- evidence: [README.md#L88-L93](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L88-L93), [README.md#L362-L366](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L362-L366) (`clm_aff41bb1d6529d50d5190d8d90b9b0584821ec7ed771c914a8c4b9a8a87b9acc`)
- [observation/documented] The MCP server exposes tools including start_task, pack_context, get_context, explain, related, stats, and delta, per the package layout documentation. -- evidence: [docs/architecture.md#L304-L304](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L304-L304) (`clm_fbe419f399197dcb2bf30310a246f3c4f107f3b0e4b7b47405025bae25d03ec4`)

## memory-state (2 claim(s))

- [observation/documented] Generated context, receipts, task state, snapshots, and memory are stored locally under .agentpack/, and summary caches are keyed by file hash so only changed files are re-summarized. -- evidence: [README.md#L264-L267](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L264-L267), [docs/architecture.md#L386-L386](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L386-L386) (`clm_86ffd3cc21d7e346af668407533985f08d124640693d211af44f8ce51a352949`)
- [observation/documented] Sessions are thread-scoped by default: when host session/thread environment variables are present, commands and MCP tools use isolated state under .agentpack/threads/<id>/, with --thread global as a legacy opt-out. -- evidence: [docs/architecture.md#L343-L368](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L343-L368) (`clm_31a43498fcc175add0626d3b0ef99e249e6a755dd4dd2caeb270755320d7adc5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The public benchmark measures file selection against files changed in historical public commits: 107 cases with 67.2% average recall and 50.6% average token precision, per the published results artifact. -- evidence: [README.md#L309-L310](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L309-L310), [README.md#L303-L307](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L303-L307), [README.md#L295-L298](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L295-L298) (`clm_538d094a33ced44031b6f7bc86ad50456583165c8f72c2c43019ceafa6fc1561`)
- [observation/documented] The benchmark authors state it only supports claims about ranked file-selection quality, not reduced tool calls, cost, completion time, or task success; no public end-to-end A/B outcome report is published yet. -- evidence: [README.md#L321-L324](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L321-L324), [README.md#L300-L301](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L300-L301) (`clm_da3f65b49be34024cb8985e4ff3cc8f592bf39b4f8ce20e8217a648dac44bcc2`)

## dependencies (1 claim(s))

- [observation/documented] The CLI requires Python 3.10+ and is installable via pipx (recommended) or pip; the npm wrapper @vishal2612200/agentpack installs the Python CLI and requires Node.js 18+. -- evidence: [README.md#L334-L337](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L334-L337), [README.md#L328-L330](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L328-L330), [README.md#L348-L351](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L348-L351) (`clm_5c1e44a62b1b69e6ddb4799ccd52eeefaca51b6108527df4250a2a87e547f5b2`)

## limitations (1 claim(s))

- [observation/documented] AgentPack is advisory: it does not edit source code, assign people, enforce policy, approve changes, or provide hard multi-agent locks, and it is not a coding agent, hosted index, or correctness oracle. -- evidence: [README.md#L73-L77](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L73-L77), [README.md#L206-L208](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L206-L208), [README.md#L162-L165](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L162-L165) (`clm_0bdf4f3040b7671bd019b1c10e5795b1a2163a87e14e7ac912a9840f661661df`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

