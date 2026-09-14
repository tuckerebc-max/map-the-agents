---
access: public
aliases: []
claim_ids:
- clm_1d57dcc7d3c0acc23dd46e1a7cbc70352c24b0eda74deec655337016955093c0
- clm_20e24f06a0c4e72163e81c6327f59e640e68a8aa53d801a78838ce84b8529497
- clm_34bf24e120dc7f0549c6077e12267dd135a1d69b0fc7d66da1b2b35cd55d2d18
- clm_3a5f6427ae410dc49efd65eecbe5d3a2903c060e330fb19dbd728850d8a939de
- clm_5e55f3ee68c05787ef0368a9169f7df34aade2cdbd50369082d28d476404f066
- clm_fc57dc33369d45c5a0700ddf421df8311cd3c2c25b630888c303049e9d973ec1
maturity: draft
page_id: pg_fa369b75021d5db8be520c2619d3cf89
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_82fe263f2e53561986010018f5d325a9
title: earendil-works/pi/README.md @ 71dca871bc80
updated_at: '2026-09-14T01:47:27Z'
---

# earendil-works/pi/README.md @ 71dca871bc80

<!-- rcw:begin owner=source:src_82fe263f2e53561986010018f5d325a9 block=evidence -->
- Repository development practice: development uses npm install --ignore-scripts, npm run build/check, ./test.sh (skipping LLM-dependent tests without API keys), and ./pi-test.sh to run pi from sources. [@claim:clm_1d57dcc7d3c0acc23dd46e1a7cbc70352c24b0eda74deec655337016955093c0]
- Repository development practice: new contributors' issues and PRs are auto-closed by default and reviewed daily by maintainers, per CONTRIBUTING.md. [@claim:clm_20e24f06a0c4e72163e81c6327f59e640e68a8aa53d801a78838ce84b8529497]
- The repository is a monorepo whose packages include a coding-agent CLI, an agent runtime with tool calling and state management, a multi-provider LLM API, a TUI library, a telemetry package, and a chord application-composition runtime. [@claim:clm_34bf24e120dc7f0549c6077e12267dd135a1d69b0fc7d66da1b2b35cd55d2d18]
- Direct external dependencies are pinned to exact versions, .npmrc sets save-exact and min-release-age=2, and the published CLI package carries a shrinkwrap file pinning transitive dependencies. [@claim:clm_3a5f6427ae410dc49efd65eecbe5d3a2903c060e330fb19dbd728850d8a939de]
- Pi ships without a built-in permission system for filesystem, process, network, or credential access; by default it runs with the permissions of the launching user and process. [@claim:clm_5e55f3ee68c05787ef0368a9169f7df34aade2cdbd50369082d28d476404f066]
- Repository development practice: npm dependency changes are treated as reviewed code changes, with CI installing via npm ci --ignore-scripts and a scheduled workflow running npm audit and signature checks. [@claim:clm_fc57dc33369d45c5a0700ddf421df8311cd3c2c25b630888c303049e9d973ec1]
<!-- rcw:end owner=source:src_82fe263f2e53561986010018f5d325a9 block=evidence -->

## Researcher notes

