---
access: public
aliases: []
claim_ids:
- clm_0bee21d4c1a943d8e5fbcc5658fdd0212ac01c21488daaef1438c899e02730bd
- clm_16b7239792ace71aa86a18151a929db30e7d4d535451977ce169a695f8e9ed24
- clm_2312944799fde20b13aa5b6a7c2a71b47f08b3d266fb2c738423f29da5581db6
- clm_4243351e15a8bc1abd623b66bd802be5cd708309686b2b476efb2b4504546421
- clm_743324725155d54211d041a10efa7cf7cc762b3c8be84eb83ccb89002e0cd93d
- clm_dcdab43fcde10abb8bf3cd76130e0661d64ff11dca3dadd60949e56a23bd5485
- clm_ebb4dc71f53b8b459f5faeaa027884ba31bddbc8ac15120f32e0320ff6946f32
- clm_efa85ec34864250470d8d2f8e636b36df18f26f59a9004c4181caa744991f45d
maturity: draft
page_id: pg_5f5e36566f695416af3fb26027890514
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_127e18e155e755048424147744df9f07
title: FerroxLabs/agents-md/AGENTS.md @ 90c7198cfa97
updated_at: '2026-09-14T03:50:05Z'
---

# FerroxLabs/agents-md/AGENTS.md @ 90c7198cfa97

<!-- rcw:begin owner=source:src_127e18e155e755048424147744df9f07 block=evidence -->
- The file is deliberately kept tight (about 200 lines per the README, with under 300 suggested as a ceiling) so rules stay loaded, and sections 0-9 are meant to be left untouched by users. [@claim:clm_0bee21d4c1a943d8e5fbcc5658fdd0212ac01c21488daaef1438c899e02730bd]
- Repository development practice: agents are told to define verifiable success criteria, write and run verification (tests, scripts, benchmarks) before claiming success, and fix causes rather than tests when verification fails. [@claim:clm_16b7239792ace71aa86a18151a929db30e7d4d535451977ce169a695f8e9ed24]
- Repository development practice: section 10 (Project context) is a per-project template with TODO placeholders for stack, build/test/lint commands, layout, and forbidden areas, to be filled only with what can be verified from the codebase. [@claim:clm_2312944799fde20b13aa5b6a7c2a71b47f08b3d266fb2c738423f29da5581db6]
- The template synthesizes Karpathy's four principles on LLM coding failure modes, Boris Cherny's Claude Code workflow with reactive pruning, Anthropic's Claude Code best practices, community anti-sycophancy patterns, and the AGENTS.md standard. [@claim:clm_4243351e15a8bc1abd623b66bd802be5cd708309686b2b476efb2b4504546421]
- Repository development practice: the file includes a self-improvement loop instructing agents to diagnose mistakes as missing versus ignored rules, add or tighten rules accordingly, and prune lines every few weeks. [@claim:clm_743324725155d54211d041a10efa7cf7cc762b3c8be84eb83ccb89002e0cd93d]
- Repository development practice: the file's non-negotiables instruct agents to skip flattery, disagree with false premises, never fabricate facts, ask when a task has two plausible interpretations, and touch only lines traceable to the request. [@claim:clm_dcdab43fcde10abb8bf3cd76130e0661d64ff11dca3dadd60949e56a23bd5485]
- Repository development practice: section 11 (Project Learnings) starts empty and the agent is instructed to append one concrete rule each time the user corrects its approach, tightening or removing lines as issues disappear. [@claim:clm_ebb4dc71f53b8b459f5faeaa027884ba31bddbc8ac15120f32e0320ff6946f32]
- Repository development practice: the file directs agents to run existing test suites, linters, and type checkers rather than guessing, and to prefer CLI tools like gh, aws, gcloud, and kubectl when available. [@claim:clm_efa85ec34864250470d8d2f8e636b36df18f26f59a9004c4181caa744991f45d]
<!-- rcw:end owner=source:src_127e18e155e755048424147744df9f07 block=evidence -->

## Researcher notes

