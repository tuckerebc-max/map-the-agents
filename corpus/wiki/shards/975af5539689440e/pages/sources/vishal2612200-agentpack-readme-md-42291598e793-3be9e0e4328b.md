---
access: public
aliases: []
claim_ids:
- clm_0bdf4f3040b7671bd019b1c10e5795b1a2163a87e14e7ac912a9840f661661df
- clm_0f7881a93d0fc238ab33b2f78842149641b32db3f969e72c357b08826dbc8afa
- clm_538d094a33ced44031b6f7bc86ad50456583165c8f72c2c43019ceafa6fc1561
- clm_5c1e44a62b1b69e6ddb4799ccd52eeefaca51b6108527df4250a2a87e547f5b2
- clm_86ffd3cc21d7e346af668407533985f08d124640693d211af44f8ce51a352949
- clm_aff41bb1d6529d50d5190d8d90b9b0584821ec7ed771c914a8c4b9a8a87b9acc
- clm_c386e4c0b6f7208262b31272dd45150c13701af213e8c4566bc1a532bc5c7cb8
- clm_da3f65b49be34024cb8985e4ff3cc8f592bf39b4f8ce20e8217a648dac44bcc2
maturity: draft
page_id: pg_6dd772f0bf8b5ce1870b3be9e0e4328b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ca158ac32066586290f25ae7b5027533
title: vishal2612200/agentpack/README.md @ 42291598e793
updated_at: '2026-09-14T04:30:29Z'
---

# vishal2612200/agentpack/README.md @ 42291598e793

<!-- rcw:begin owner=source:src_ca158ac32066586290f25ae7b5027533 block=evidence -->
- AgentPack is advisory: it does not edit source code, assign people, enforce policy, approve changes, or provide hard multi-agent locks, and it is not a coding agent, hosted index, or correctness oracle. [@claim:clm_0bdf4f3040b7671bd019b1c10e5795b1a2163a87e14e7ac912a9840f661661df]
- Core scan, route, pack, stats, explain, and benchmark operations run without hosted indexing, embeddings, or model API calls; network use is limited to explicit GitHub operations, optional enrichment, and external-agent workflows. [@claim:clm_0f7881a93d0fc238ab33b2f78842149641b32db3f969e72c357b08826dbc8afa]
- The public benchmark measures file selection against files changed in historical public commits: 107 cases with 67.2% average recall and 50.6% average token precision, per the published results artifact. [@claim:clm_538d094a33ced44031b6f7bc86ad50456583165c8f72c2c43019ceafa6fc1561]
- The CLI requires Python 3.10+ and is installable via pipx (recommended) or pip; the npm wrapper @vishal2612200/agentpack installs the Python CLI and requires Node.js 18+. [@claim:clm_5c1e44a62b1b69e6ddb4799ccd52eeefaca51b6108527df4250a2a87e547f5b2]
- Generated context, receipts, task state, snapshots, and memory are stored locally under .agentpack/, and summary caches are keyed by file hash so only changed files are re-summarized. [@claim:clm_86ffd3cc21d7e346af668407533985f08d124640693d211af44f8ce51a352949]
- The product exposes a CLI four-command loop: agentpack work, learn --json, finish, and doctor, where work prepares task context, finish records validation and task memory, and doctor checks installation and integration. [@claim:clm_aff41bb1d6529d50d5190d8d90b9b0584821ec7ed771c914a8c4b9a8a87b9acc]
- The project is at alpha version 0.4.4, licensed AGPL v3, with APIs that may change before 1.0 and platform targets of macOS, Linux, and Windows PowerShell with Git for Windows. [@claim:clm_c386e4c0b6f7208262b31272dd45150c13701af213e8c4566bc1a532bc5c7cb8]
- The benchmark authors state it only supports claims about ranked file-selection quality, not reduced tool calls, cost, completion time, or task success; no public end-to-end A/B outcome report is published yet. [@claim:clm_da3f65b49be34024cb8985e4ff3cc8f592bf39b4f8ce20e8217a648dac44bcc2]
<!-- rcw:end owner=source:src_ca158ac32066586290f25ae7b5027533 block=evidence -->

## Researcher notes

