---
access: public
aliases: []
claim_ids:
- clm_298aa49449ca42a6869151a1e905cecbeeb70ec483dac8ea42332403613b2f2d
- clm_2fa82defceb6b657527159a20818cff13f31664cc44bc90f22bb675ac4b9c273
- clm_60f4b8e396cf16f26efef8bca8e617537b02d7e8120fe96379715a395f23400b
- clm_73b8abcfc4bcace2d4eef3909a6d42d70d53bdc8084b051ed31836579b0f9edd
- clm_847e79c694dfa5a025b03991ded40c5a58c15365f1aa79bfaa55dbb9f8ab2733
- clm_8adf95349c5360a706a6f293ca66e49b04d0ac4912b54632bc1d26daabc64700
- clm_8db05fe039abe8bf3c7748d54d0cfe1ce3968ddbd79a8bc21fddc178bee1bb3f
- clm_b246bd719e68dffb364351d2812e94dc8b77841c791738109d13dc6bc7240379
- clm_c591f429ce11725d0ecf9d96667a542347a3cbe8ff03f98460dea8b492012332
- clm_ec655c89135001641b1a84c96b750ee762cb65a7cf6d01cb2c890735a08e424b
maturity: draft
page_id: pg_1e3a872417f158ab8893092c80f26a1b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9f7165dbd30150229fafd313055e6bc0
title: exqqstar/ExAgent/README.md @ d9adbbd6f18a
updated_at: '2026-09-14T03:07:36Z'
---

# exqqstar/ExAgent/README.md @ d9adbbd6f18a

<!-- rcw:begin owner=source:src_9f7165dbd30150229fafd313055e6bc0 block=evidence -->
- The project is dual-licensed MIT OR Apache-2.0, and Rust dependency license policy is enforced via cargo deny configured in deny.toml. [@claim:clm_298aa49449ca42a6869151a1e905cecbeeb70ec483dac8ea42332403613b2f2d]
- A typed app-server boundary exposes the local Rust runtime to the desktop; the Tauri shell stays project-aware while the runtime owns thread execution, model calls, tools, state, and live events. [@claim:clm_2fa82defceb6b657527159a20818cff13f31664cc44bc90f22bb675ac4b9c273]
- The memory system supports automatic prompt recall, explicit memory tools, candidate saves, local promote/archive/forget flows, and audit state. [@claim:clm_60f4b8e396cf16f26efef8bca8e617537b02d7e8120fe96379715a395f23400b]
- Each thread runs behind an actor-backed ThreadRuntime that serializes turns while streaming snapshots, status, and events back to the GUI. [@claim:clm_73b8abcfc4bcace2d4eef3909a6d42d70d53bdc8084b051ed31836579b0f9edd]
- The project states it currently targets personal workstation use, with non-goals including production-grade sandbox isolation, hosted collaboration, and a stable public SDK. [@claim:clm_847e79c694dfa5a025b03991ded40c5a58c15365f1aa79bfaa55dbb9f8ab2733]
- Agent policy gates both tool visibility and execution; tool contracts live in src/tools while per-turn orchestration lives in src/runtime/tool. [@claim:clm_8adf95349c5360a706a6f293ca66e49b04d0ac4912b54632bc1d26daabc64700]
- Local durability is append-first: each thread has a rollout.jsonl ledger, and IndexDb stores cross-thread indexes for projects, threads, goals, memory, and review state. [@claim:clm_8db05fe039abe8bf3c7748d54d0cfe1ce3968ddbd79a8bc21fddc178bee1bb3f]
- Repository development practice: contributors run npm ci, tauri:dev, test, and build commands, plus cargo test, fmt, clippy, and cargo deny checks for verification. [@claim:clm_b246bd719e68dffb364351d2812e94dc8b77841c791738109d13dc6bc7240379]
- The model layer normalizes provider-specific APIs into internal conversation, tool-call, multimodal, reasoning, and streaming types. [@claim:clm_c591f429ce11725d0ecf9d96667a542347a3cbe8ff03f98460dea8b492012332]
- ExAgent is a desktop-first agent workbench with a Rust runtime and Tauri/React GUI, aimed at long-running coding work in local projects with resumable sessions. [@claim:clm_ec655c89135001641b1a84c96b750ee762cb65a7cf6d01cb2c890735a08e424b]
<!-- rcw:end owner=source:src_9f7165dbd30150229fafd313055e6bc0 block=evidence -->

## Researcher notes

