# sean35mm/weaver -- full detail

[Back to orientation](weaver.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sean35mm/weaver/e5f41572c338f41e402e9ea309088d74d10a6f68/f18b9c6d31110a99.json](../../../wiki/dossiers/sean35mm/weaver/e5f41572c338f41e402e9ea309088d74d10a6f68/f18b9c6d31110a99.json)

## specifications (1 claim(s))

- [observation/documented] Weaver is a CLI over a local SQLite store with no cloud account, remote sync, coordination daemon, or MCP server; Git stays authoritative for code and the CLI for coordination. -- evidence: [README.md#L29-L31](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L29-L31) (`clm_2f886137322c968ff06bdae0f53712257db1ed8b7a884c8feee04995700b3bf7`)

## components (1 claim(s))

- [observation/documented] The product provides a status→task→claim→done coordination loop, live sessions, advisory file claims, recent activity, optional Markdown scratchpads, and durable Repository Facts. -- evidence: [README.md#L13-L16](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L13-L16) (`clm_8418c0ab7953e285b5cc16510a2b493aa0a851a23d27afc7374613c42d5d3595`)

## design-choices (2 claim(s))

- [observation/documented] Claims are advisory and TTL-bound; a claim exit code 1 means the claim was recorded with an overlap found, and different-worktree overlaps are informational because files are isolated. -- evidence: [README.md#L172-L176](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L172-L176) (`clm_61b171794e50af4426f16980e6c5292f69f962efafcc85fe5e8929cc7c5354aa`)
- [observation/documented] Every scratchpad mutation creates a revision, and passing --revision prevents a stale writer from replacing a newer edit. -- evidence: [README.md#L92-L94](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L92-L94) (`clm_b86c7a3a42e7f0968cb408ad731d76a3734209fec33e6c1431013648f560a94a`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run tests with npm test (node --test) and npm run test:bun (bun test), both of which must pass, plus npm run typecheck and npm run build. -- evidence: [AGENTS.md#L15-L22](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L15-L22) (`clm_f684634f85579c3dce135998a0672517376d5c6341e7ce0cea1775366be85623`)
- [observation/documented] Repository development practice: Conventional Commits are mandatory and drive versioning via release-please; releases are cut by merging the release-please PR rather than hand-creating releases. -- evidence: [AGENTS.md#L38-L41](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L38-L41), [AGENTS.md#L26-L34](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L26-L34) (`clm_fdae64f4fe72ba2fca9a00ff7f238827f62f72e697e6e5aa745fd85f50b9a0e0`)
- [observation/documented] Repository development practice: tests use node:test with node:assert/strict, relative imports use explicit .ts extensions, pure logic is clock-injectable, and the core stays zero-runtime-dependency except picomatch. -- evidence: [AGENTS.md#L26-L34](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L26-L34) (`clm_c942ed358ecbf9eae68ee3ea5904c196f4269e1d945b9346186cb49dbf973bea`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes scratchpad commands (list/create/read/use/edit-section/archive/trash/recover), coordination commands (status, task, claim, preflight, done, fact/forget), and setup commands (init, disable, deinit, upgrade, uninstall). -- evidence: [README.md#L200-L204](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L200-L204), [README.md#L195-L198](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L195-L198), [README.md#L188-L193](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L188-L193) (`clm_73e7cdb88e75296202af70f403b799f451e874f4c5f6ac3e799a0f00491e6068`)
- [observation/documented] The scratchpads web UI supports WYSIWYG and Markdown source modes, autosave with revision conflict handling, search, revision history, and shows sessions, claims, activity, and Facts; it binds only to loopback with an unguessable launch capability. -- evidence: [README.md#L114-L118](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L114-L118) (`clm_fee3c2c3de339a8678f4c312be7cd48b0092e511b69e47d06b9863ed41f0b43d`)

## memory-state (2 claim(s))

- [observation/documented] Stores live under ~/.weaver/ with one SQLite database per repository identity; scratchpads, facts, intents, and reasons are plaintext local data, and there is no telemetry. -- evidence: [README.md#L210-L222](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L210-L222) (`clm_8f8801ef03dd66024c5b3eec22051d56413b3aa7dba68620ae27c6b291cc81b5`)
- [observation/documented] The first scratchpads invocation owns a foreground server per project store and OS user; later invocations reuse it, and worktrees sharing repo identity and WEAVER_HOME share the instance. -- evidence: [README.md#L120-L125](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L120-L125) (`clm_df5f37479e54adc8e9ff5573202bad5481d3630b5b002defafb70c7ce6628c6b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The OpenCode plugin (installed via init --hooks) provides fixed-operation tools such as weaver_scratchpad_* and weaver_fact_* that invoke the CLI contract, with stdin Markdown, JSON reads, and explicit revisions for mutations. -- evidence: [README.md#L29-L31](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L29-L31), [README.md#L150-L151](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L150-L151), [README.md#L164-L168](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L164-L168), [README.md#L153-L162](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L153-L162) (`clm_5470496c16381c00da9f4e1a1e4117470f26ca8555a7a3147e27236d0d4c3a55`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The self-contained binary supports macOS and Linux on arm64/x64 (WSL2 on Windows), installs to ~/.local/bin/weaver, and requires no Node, npm, server, or account. -- evidence: [README.md#L41-L42](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L41-L42) (`clm_d488d60cf0d9212bb0f3d245d22a2082cbcfdff6a7051842fee8f51aad88acfc`)
- [inference/documented] The generated OpenCode plugin file has no dependency on the Weaver npm package, suggesting the installed integration is self-contained. -- evidence: [README.md#L150-L151](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L150-L151) (`clm_57a4b6731a8f14e357541188dd6fa769bb9fa1540c48bd60f2b1f64ad97ec3bc`)

## limitations (1 claim(s))

- [observation/documented] There is no individual permanent-purge command for scratchpads; pads move through active→archived or trash with restore/recover operations. -- evidence: [README.md#L96-L99](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L96-L99) (`clm_4f167678b215908ecd09ffc520142bdf74c0c4a12438bf081b94bc18944bb28c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

