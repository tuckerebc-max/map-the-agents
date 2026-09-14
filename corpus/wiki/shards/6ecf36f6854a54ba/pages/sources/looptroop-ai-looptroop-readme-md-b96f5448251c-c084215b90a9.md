---
access: public
aliases: []
claim_ids:
- clm_033d8e8301d3f6e3cb58b3f2a2fb44a08ba5a7b6a8d31fbaf9bc012720704d9c
- clm_2abe9024f33cbd37a0d4709f08deab2d872cdc0379d9b3a20488cef244401e56
- clm_470e331903969e540e10930219b7073fb196f926befaa3de9e163cf79ff031f0
- clm_69e7b28e17c7c9cd3cb62f6703a31855cef9ef7c7de36dfb200688a37ec3842f
- clm_79e8d01bb7cca8c65d5e547819fb6446a45c092360becd077008e0137c17d57b
- clm_7d72436a35c6911703a34bc27f83f0608d467a48771687b442901d14fabc07a4
- clm_9ab483c3e8ba2c80a49d5d377d7be79d1c03b30e24c1c0bccbecbcc55fa9273b
- clm_b00207897340c2e07835c964b9903801cb62727d88e67234867ff03b7c4abfa9
- clm_c4cd945265732b7bb583c43f88fd873886f55696f36a2fd3be84af724c406f56
- clm_ccbe11c3fcb65bc48edc088b700798cf7c05da855c8c14a1f98e4125da75fadd
- clm_d69ba7a1fdb830462d2306c75adc875e445ffdf868adc47da1a8ef361a24c6ed
- clm_da2552b636d8ce46930655b064a0ebe0d27af4dc6b37c9759ac5210b5f4f26b9
- clm_efe666d19a18be7b48c5b911e171840a73774f754f6de7d2d3e4b63a099841df
maturity: draft
page_id: pg_acd96c5325195545a6b3c084215b90a9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bf994b4b089651d099914dc939c3245b
title: looptroop-ai/LoopTroop/README.md @ b96f5448251c
updated_at: '2026-09-14T02:13:33Z'
---

# looptroop-ai/LoopTroop/README.md @ b96f5448251c

<!-- rcw:begin owner=source:src_bf994b4b089651d099914dc939c3245b block=evidence -->
- The ticket pipeline flows from codebase discovery through council planning, an approval gate, isolated bead execution, final tests, optional manual QA, and integration/PR review, with QA failures spawning fix beads. [@claim:clm_033d8e8301d3f6e3cb58b3f2a2fb44a08ba5a7b6a8d31fbaf9bc012720704d9c]
- The product converts a ticket into a PRD with Epics and User Stories plus decomposed implementation steps, stored as a durable artifact for later bead execution. [@claim:clm_2abe9024f33cbd37a0d4709f08deab2d872cdc0379d9b3a20488cef244401e56]
- In alpha, LLM Councils support 2–10 distinct models including the main implementer, and each project allows only one active ticket in the execution band at a time. [@claim:clm_470e331903969e540e10930219b7073fb196f926befaa3de9e163cf79ff031f0]
- A CLI is provided: `looptroop open` starts the app in the background if not running, and `looptroop start` runs the service without a browser. [@claim:clm_69e7b28e17c7c9cd3cb62f6703a31855cef9ef7c7de36dfb200688a37ec3842f]
- Execution runs each bead via OpenCode in isolated Git worktrees; on failure a Ralph-style loop logs the trace, resets the worktree, discards the session, and retries fresh until tests pass or limits are hit. [@claim:clm_79e8d01bb7cca8c65d5e547819fb6446a45c092360becd077008e0137c17d57b]
- A local GUI dashboard lets users manage attached repositories, configure implementer and council models, answer interview questions, and track ticket, bead, and execution-log state. [@claim:clm_7d72436a35c6911703a34bc27f83f0608d467a48771687b442901d14fabc07a4]
- The product requires git and authenticated `gh` for the PR step, plus OpenCode with at least one configured model provider; it can start OpenCode if installed but will not install it. [@claim:clm_9ab483c3e8ba2c80a49d5d377d7be79d1c03b30e24c1c0bccbecbcc55fa9273b]
- The tool is unsuited to urgent quick fixes or trivial tasks due to orchestration overhead and high API token usage from multi-model councils and long retry loops. [@claim:clm_b00207897340c2e07835c964b9903801cb62727d88e67234867ff03b7c4abfa9]
- The orchestrator runs OpenCode in dangerously-skip-permissions (YOLO) mode, giving the agent full local execution rights without confirmation prompts; worktrees isolate code but not command execution. [@claim:clm_c4cd945265732b7bb583c43f88fd873886f55696f36a2fd3be84af724c406f56]
- npm/bun/pnpm/Yarn installs need Node 24.18.1+ and git and gh; Homebrew and Scoop ship locked bundles pulling in node@24, git, and gh; Docker images include Node, git, and gh but need an external OpenCode server and a mounted project. [@claim:clm_ccbe11c3fcb65bc48edc088b700798cf7c05da855c8c14a1f98e4125da75fadd]
- Context engineering feeds the agent only minimal per-status context (active bead, target file, test file) instead of full transcripts, to avoid context rot. [@claim:clm_d69ba7a1fdb830462d2306c75adc875e445ffdf868adc47da1a8ef361a24c6ed]
- Work is decomposed into 'beads' — small independently implementable units with purpose, acceptance criteria, dependencies, target files, and validation steps. [@claim:clm_da2552b636d8ce46930655b064a0ebe0d27af4dc6b37c9759ac5210b5f4f26b9]
- Planning uses an LLM Council where multiple model instances draft plans, score each other with a weighted rubric, vote, and the winner refines and verifies coverage. [@claim:clm_efe666d19a18be7b48c5b911e171840a73774f754f6de7d2d3e4b63a099841df]
<!-- rcw:end owner=source:src_bf994b4b089651d099914dc939c3245b block=evidence -->

## Researcher notes

