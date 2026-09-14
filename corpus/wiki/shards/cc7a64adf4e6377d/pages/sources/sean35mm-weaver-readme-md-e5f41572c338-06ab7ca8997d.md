---
access: public
aliases: []
claim_ids:
- clm_2f886137322c968ff06bdae0f53712257db1ed8b7a884c8feee04995700b3bf7
- clm_4f167678b215908ecd09ffc520142bdf74c0c4a12438bf081b94bc18944bb28c
- clm_5470496c16381c00da9f4e1a1e4117470f26ca8555a7a3147e27236d0d4c3a55
- clm_57a4b6731a8f14e357541188dd6fa769bb9fa1540c48bd60f2b1f64ad97ec3bc
- clm_61b171794e50af4426f16980e6c5292f69f962efafcc85fe5e8929cc7c5354aa
- clm_73e7cdb88e75296202af70f403b799f451e874f4c5f6ac3e799a0f00491e6068
- clm_8418c0ab7953e285b5cc16510a2b493aa0a851a23d27afc7374613c42d5d3595
- clm_8f8801ef03dd66024c5b3eec22051d56413b3aa7dba68620ae27c6b291cc81b5
- clm_b86c7a3a42e7f0968cb408ad731d76a3734209fec33e6c1431013648f560a94a
- clm_d488d60cf0d9212bb0f3d245d22a2082cbcfdff6a7051842fee8f51aad88acfc
- clm_df5f37479e54adc8e9ff5573202bad5481d3630b5b002defafb70c7ce6628c6b
- clm_fee3c2c3de339a8678f4c312be7cd48b0092e511b69e47d06b9863ed41f0b43d
maturity: draft
page_id: pg_cdf76e0146ab5685bb6f06ab7ca8997d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_07648eff57c85f7db581a954b4ae1299
title: sean35mm/weaver/README.md @ e5f41572c338
updated_at: '2026-09-14T02:39:04Z'
---

# sean35mm/weaver/README.md @ e5f41572c338

<!-- rcw:begin owner=source:src_07648eff57c85f7db581a954b4ae1299 block=evidence -->
- Weaver is a CLI over a local SQLite store with no cloud account, remote sync, coordination daemon, or MCP server; Git stays authoritative for code and the CLI for coordination. [@claim:clm_2f886137322c968ff06bdae0f53712257db1ed8b7a884c8feee04995700b3bf7]
- There is no individual permanent-purge command for scratchpads; pads move through active→archived or trash with restore/recover operations. [@claim:clm_4f167678b215908ecd09ffc520142bdf74c0c4a12438bf081b94bc18944bb28c]
- The OpenCode plugin (installed via init --hooks) provides fixed-operation tools such as weaver_scratchpad_* and weaver_fact_* that invoke the CLI contract, with stdin Markdown, JSON reads, and explicit revisions for mutations. [@claim:clm_5470496c16381c00da9f4e1a1e4117470f26ca8555a7a3147e27236d0d4c3a55]
- The generated OpenCode plugin file has no dependency on the Weaver npm package, suggesting the installed integration is self-contained. [@claim:clm_57a4b6731a8f14e357541188dd6fa769bb9fa1540c48bd60f2b1f64ad97ec3bc]
- Claims are advisory and TTL-bound; a claim exit code 1 means the claim was recorded with an overlap found, and different-worktree overlaps are informational because files are isolated. [@claim:clm_61b171794e50af4426f16980e6c5292f69f962efafcc85fe5e8929cc7c5354aa]
- The CLI exposes scratchpad commands (list/create/read/use/edit-section/archive/trash/recover), coordination commands (status, task, claim, preflight, done, fact/forget), and setup commands (init, disable, deinit, upgrade, uninstall). [@claim:clm_73e7cdb88e75296202af70f403b799f451e874f4c5f6ac3e799a0f00491e6068]
- The product provides a status→task→claim→done coordination loop, live sessions, advisory file claims, recent activity, optional Markdown scratchpads, and durable Repository Facts. [@claim:clm_8418c0ab7953e285b5cc16510a2b493aa0a851a23d27afc7374613c42d5d3595]
- Stores live under ~/.weaver/ with one SQLite database per repository identity; scratchpads, facts, intents, and reasons are plaintext local data, and there is no telemetry. [@claim:clm_8f8801ef03dd66024c5b3eec22051d56413b3aa7dba68620ae27c6b291cc81b5]
- Every scratchpad mutation creates a revision, and passing --revision prevents a stale writer from replacing a newer edit. [@claim:clm_b86c7a3a42e7f0968cb408ad731d76a3734209fec33e6c1431013648f560a94a]
- The self-contained binary supports macOS and Linux on arm64/x64 (WSL2 on Windows), installs to ~/.local/bin/weaver, and requires no Node, npm, server, or account. [@claim:clm_d488d60cf0d9212bb0f3d245d22a2082cbcfdff6a7051842fee8f51aad88acfc]
- The first scratchpads invocation owns a foreground server per project store and OS user; later invocations reuse it, and worktrees sharing repo identity and WEAVER_HOME share the instance. [@claim:clm_df5f37479e54adc8e9ff5573202bad5481d3630b5b002defafb70c7ce6628c6b]
- The scratchpads web UI supports WYSIWYG and Markdown source modes, autosave with revision conflict handling, search, revision history, and shows sessions, claims, activity, and Facts; it binds only to loopback with an unguessable launch capability. [@claim:clm_fee3c2c3de339a8678f4c312be7cd48b0092e511b69e47d06b9863ed41f0b43d]
<!-- rcw:end owner=source:src_07648eff57c85f7db581a954b4ae1299 block=evidence -->

## Researcher notes

