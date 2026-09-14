---
access: public
aliases: []
claim_ids:
- clm_35454948309d6e8a93ea6dc8c844098d21097f1fad274250449c8ba6d1494ba1
- clm_368005b66b4e53e89a1e2acb5fb5bae43c3caa9a9bd21f6f7d9624e785e51087
- clm_3a4916dd5bc6963ea37cea113cedaea187e167d96cc4442d78b02b4b00ba984a
- clm_3e6c402bbfa9db0f736dea9ecf2172bb812f08ea2fbc3343c7a1335856e05adb
- clm_5bf6237f880c0d6a1295194e977d94214dd8e35c65a7c44740c298725007698f
- clm_9c833ae391b9e0006427e8438706b0d699baaec5f1fe3e0bce087b4678115cb7
- clm_b10e31b6d60b0c5864dbe169525dc05ca1da7088b10f4057f5ca5ea610642038
- clm_ddc9a086391a35f3908fbb8272286a6c758c3c2a6afdfe7ea210073e34b17302
- clm_e5220aead22c812ec249be6580763989d48953c8f8b1e0a192f13dceb35e99ed
maturity: draft
page_id: pg_f873f668e6865304a6d0e4dbefe04782
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5ca61327d48553cfb2e260e324106a8f
title: whut09/opencode-plusplus/docs/concepts/architecture.md @ 598767170bb7
updated_at: '2026-09-14T04:31:25Z'
---

# whut09/opencode-plusplus/docs/concepts/architecture.md @ 598767170bb7

<!-- rcw:begin owner=source:src_5ca61327d48553cfb2e260e324106a8f block=evidence -->
- The Command Guard represents repository semantics: it can defer operations as approval-required or hard-stop policy-blocked destructive commands, protected paths, unknown project commands, or evidence tampering; native auto approval cannot override the latter. [@claim:clm_35454948309d6e8a93ea6dc8c844098d21097f1fad274250449c8ba6d1494ba1]
- A harness-led developer mode, opencode-plusplus orchestrate, runs a bounded loop (task, prepare, execute, collect, evaluate, decide, persist) around an explicitly configured executor, reporting finalize, repair, repack, block, rollback, or human-review. [@claim:clm_368005b66b4e53e89a1e2acb5fb5bae43c3caa9a9bd21f6f7d9624e785e51087]
- The architecture is described as Guard modules around coding agents: Context, Hallucination, Boundary, Regression, Evidence, Impact, and Loop Guards, plus an Executor Adapter and Trace Normalizer. [@claim:clm_3a4916dd5bc6963ea37cea113cedaea187e167d96cc4442d78b02b4b00ba984a]
- The v2 architecture has five responsibilities: Repo Scanner, Context Planner, Context Pack Composer, Agent Harness Layer, and an Integration Layer exposing CLI, stdio MCP server, and retriever adapters. [@claim:clm_3e6c402bbfa9db0f736dea9ecf2172bb812f08ea2fbc3343c7a1335856e05adb]
- Indexing uses the TypeScript Compiler API for TS/JS, optional Tree-sitter for Python with stdlib AST and regex fallback, and generic metadata for other files; real tokenizer modes use js-tiktoken with a chars_approx fallback. [@claim:clm_5bf6237f880c0d6a1295194e977d94214dd8e35c65a7c44740c298725007698f]
- The loop state file records state, previousState, repository/context/diff hashes, lastAction, blocking nextAction, allowedActions, satisfiedEvidence, and missingEvidence for resumable runs. [@claim:clm_9c833ae391b9e0006427e8438706b0d699baaec5f1fe3e0bce087b4678115cb7]
- The project targets helping coding agents safely complete concrete changes, distinguishing itself from repo summarizers, README generators, and raw RAG loaders. [@claim:clm_b10e31b6d60b0c5864dbe169525dc05ca1da7088b10f4057f5ca5ea610642038]
- The loop controller decides next steps such as start-agent, rebuild-context, replan, expand-context, repair-contracts, add-or-update-tests, run-tests, or ready-for-review, each with a confidence score and blocking flag. [@claim:clm_ddc9a086391a35f3908fbb8272286a6c758c3c2a6afdfe7ea210073e34b17302]
- Documented MCP tools include opencode_plusplus_build, plan, pack, retrieve, tests, impact, verify, and explain, plus experimental runtime loop tools for start/evaluate/repair/finalize flows. [@claim:clm_e5220aead22c812ec249be6580763989d48953c8f8b1e0a192f13dceb35e99ed]
<!-- rcw:end owner=source:src_5ca61327d48553cfb2e260e324106a8f block=evidence -->

## Researcher notes

