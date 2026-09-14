---
access: public
aliases: []
claim_ids:
- clm_0ee5aab3308f4b7c541935a0e0bd551e1c83eaec4f64943a411fdc3adcb069b8
- clm_347e818d022ca924c2e4f460408d60de8993eea6e1198e30412e127efa54bd0f
- clm_4025e2ff96479edc96fdbf8634a50bb5078542b248b3f25a7a9cc622bf4450d0
- clm_48ba97847fc9570ecccf2e99e6a1e68313a59f13059ef244e300720d8c59c8b3
- clm_72bab8cb2be86b2d6bc9436e12a7d76c88549c9135d96232501c2a910715a907
- clm_85e7512abb6858f0001a716b6591d767f9be01d4c7a2979ac6f8d8dfe7ae5f69
- clm_8e3dd30f22df69a287584913406984bdf0602f86fc77d9c87ba80dff20d3fa95
- clm_d316800e0d3027abc6413e5fdb6a8da8f4b3e4186e68182b4898be9322f2330c
- clm_d7f7ac577f2025c35d3806958bf28488b6ba0e54e1f87af8ff17db63965ac328
- clm_ff2be5fd26603e1cbd8f7316ec1fdf0221493770a7b830700609c66c977d3610
maturity: draft
page_id: pg_b7d834b68a6a561e8a2655271fee0f89
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4cbc9ae05e835d6393cb9188010708ba
title: yzyydev/claude_code_sub_agents/README.md @ 7597ed864ce2
updated_at: '2026-09-14T04:32:33Z'
---

# yzyydev/claude_code_sub_agents/README.md @ 7597ed864ce2

<!-- rcw:begin owner=source:src_4cbc9ae05e835d6393cb9188010708ba block=evidence -->
- The design uses wave-based agent deployment to manage context limits, fresh agent instances per wave, progressive summarization of completed iterations, and lightweight state tracking in the main orchestrator. [@claim:clm_0ee5aab3308f4b7c541935a0e0bd551e1c83eaec4f64943a411fdc3adcb069b8]
- The /solve command takes a legal analysis spec, an input directory of scenario files, and an output directory, e.g. /solve specs/law_example.md example_input/ example_output/. [@claim:clm_347e818d022ca924c2e4f460408d60de8993eea6e1198e30412e127efa54bd0f]
- Sub-agents receive structured task prompts specifying the iteration number, full spec analysis, a summary of existing outputs, and an assigned creative direction, with requirements to ensure uniqueness and follow the spec format. [@claim:clm_4025e2ff96479edc96fdbf8634a50bb5078542b248b3f25a7a9cc622bf4450d0]
- The system is organized around three command modules in .claude/commands/: start.md (iterative loop orchestrator), solve.md (parallel case processor), and prime.md (context management utilities). [@claim:clm_48ba97847fc9570ecccf2e99e6a1e68313a59f13059ef244e300720d8c59c8b3]
- The project depends on Claude Code's command system and sub-agent infrastructure, and includes a .claude/settings.local.json configuration file. [@claim:clm_72bab8cb2be86b2d6bc9436e12a7d76c88549c9135d96232501c2a910715a907]
- The README acknowledges context-capacity boundaries, noting wave-based deployment, progressive sophistication strategies, and graceful conclusion planning are used when approaching context limits. [@claim:clm_85e7512abb6858f0001a716b6591d767f9be01d4c7a2979ac6f8d8dfe7ae5f69]
- A bundled legal education example provides 10 civilian-law scenario files, a law_example.md specification, student instructions, and 10 generated IRAC-format analyses. [@claim:clm_8e3dd30f22df69a287584913406984bdf0602f86fc77d9c87ba80dff20d3fa95]
- The /prime command lists project files for context awareness, pre-loads documentation, and manages memory efficiency across agent waves. [@claim:clm_d316800e0d3027abc6413e5fdb6a8da8f4b3e4186e68182b4898be9322f2330c]
- The /start command takes a spec file, an output directory, and a count that may be a number or the literal 'infinite', e.g. /start specs/content_spec.md output/ 5. [@claim:clm_d7f7ac577f2025c35d3806958bf28488b6ba0e54e1f87af8ff17db63965ac328]
- The README self-reports tested scenarios including 10 parallel legal analyses, infinite-mode generation with maintained quality, and cross-agent deduplication; these are author claims, not an independent benchmark harness. [@claim:clm_ff2be5fd26603e1cbd8f7316ec1fdf0221493770a7b830700609c66c977d3610]
<!-- rcw:end owner=source:src_4cbc9ae05e835d6393cb9188010708ba block=evidence -->

## Researcher notes

