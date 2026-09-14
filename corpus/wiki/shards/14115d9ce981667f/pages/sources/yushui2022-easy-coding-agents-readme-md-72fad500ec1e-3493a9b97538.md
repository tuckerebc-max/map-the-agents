---
access: public
aliases: []
claim_ids:
- clm_0c8eab665bdd47ac89de026a5120d4294f81156c86177e3ff2e111dfb7cfcfe8
- clm_32c61942c7b7f9ce407e4dcf7e70eaace648d1b5e102959a0cb29f3ac42d4dcc
- clm_53e76b533dd7cf160bf24f6e1a199daadda836c5bcbc143f1f7184a4c5126737
- clm_6330d333c86292bbf8e4231cfb79979bc5af44f24198294056819bbf933c97ab
- clm_643598215c175a689f4e71944392fe1caaad3b3474504fc901feecb906cfc159
- clm_661dec3ba4969c2bd4c8a2b146c0a93b79a9fdda7729c6a6cc696f6bdcbd0c3d
- clm_70eda541be796d8e6cc82028fb52639752ade0361a1fd547e53c86500f37efc7
- clm_adf4990862a0c1fb7b65a35ecafaff2eef6df10281d54ccbec8b3f18fe1712a3
- clm_b5dda14ff871449e5396bc37648bb045de52b2733c0ecb0ff15536288e04b9de
- clm_be4597f148decf72d8985d6558fd5d6db5587ad04311d5689ae930338e431b85
- clm_d432652a1b14bd4230a5a565b52defd13a0541554e6a6719f0a9c39ee8b42012
maturity: draft
page_id: pg_bdb778059f7955ac93b03493a9b97538
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_56dec4ff10e459069a6f6fe4c201fc65
title: yushui2022/easy-coding-agents/README.md @ 72fad500ec1e
updated_at: '2026-09-14T03:26:07Z'
---

# yushui2022/easy-coding-agents/README.md @ 72fad500ec1e

<!-- rcw:begin owner=source:src_56dec4ff10e459069a6f6fe4c201fc65 block=evidence -->
- The CLI exposes slash commands for custom-agent management (/agent create, list, use, preview, edit, delete) and lets users invoke a specialist agent inline via @AgentName syntax. [@claim:clm_0c8eab665bdd47ac89de026a5120d4294f81156c86177e3ff2e111dfb7cfcfe8]
- A SWE-bench-format memory probe checks whether issue context, failing-test evidence, task state, and false-DONE prevention survive memory reconstruction; it explicitly does not measure patch correctness, which requires the official SWE-bench Docker harness. [@claim:clm_32c61942c7b7f9ce407e4dcf7e70eaace648d1b5e102959a0cb29f3ac42d4dcc]
- The engine uses a double-buffered async queue (input_queue -> processing_queue -> AgentEngine._run_autonomous_loop) to separate user events from execution tasks and keep the CLI responsive during streaming and tool runs. [@claim:clm_53e76b533dd7cf160bf24f6e1a199daadda836c5bcbc143f1f7184a4c5126737]
- Repository development practice: contributors install requirements.txt and requirements-dev.txt, run tests with 'python -m pytest tests -q', and can run fixture benchmarks via benchmark/memory_eval/run.py and benchmark/coding_memory/run.py commands. [@claim:clm_6330d333c86292bbf8e4231cfb79979bc5af44f24198294056819bbf933c97ab]
- The README itself lists unsupported claims: official LongMemEval/LoCoMo leaderboard accuracy, SWE-bench patch resolved rate, general superiority over vector RAG or long-context baselines, and full production sandboxing or enterprise permission control. [@claim:clm_643598215c175a689f4e71944392fe1caaad3b3474504fc901feecb906cfc159]
- Built-in tools include read (line-numbered, offset/limit), write, edit (unique-string replacement), smart_search (ripgrep-style with tree-sitter), glob, grep, bash, todo tools, ask_user/ask_selection, and agent management tools. [@claim:clm_661dec3ba4969c2bd4c8a2b146c0a93b79a9fdda7729c6a6cc696f6bdcbd0c3d]
- Memory is packaged as agent_memory_core, storing events, large tool outputs under refs/*.md, task nodes, claims with support status, and coding entities in SQLite, with quality gates requiring evidence for file-content claims, error explanations, and DONE transitions. [@claim:clm_70eda541be796d8e6cc82028fb52639752ade0361a1fd547e53c86500f37efc7]
- The project is a Python coding-agent runtime whose main.py provides a prompt_toolkit CLI, with core.engine.AgentEngine running an autonomous task-driven loop and core.task.TaskManager tracking pending, in-progress, completed, and skipped tasks. [@claim:clm_adf4990862a0c1fb7b65a35ecafaff2eef6df10281d54ccbec8b3f18fe1712a3]
- The agent has three runtime modes: Plan (analyze without writing code until approval), Code (default autonomous implementation), and Chat (Q&A avoiding file changes); Shift+Tab cycles modes without restarting. [@claim:clm_b5dda14ff871449e5396bc37648bb045de52b2733c0ecb0ff15536288e04b9de]
- A benchmark harness compares six memory baselines (no_memory, summary, long-context, keyword FTS, vector RAG, evidence-gated) on LongMemEval-S, LoCoMo10, and BEAM-lite, scoring retrieval/term recall, evidence source coverage, tokens, latency, and false-fact rate after a context wipe. [@claim:clm_be4597f148decf72d8985d6558fd5d6db5587ad04311d5689ae930338e431b85]
- The README reports evidence-gated memory at 0.40 retrieval recall and 0.87 evidence coverage on LongMemEval-S (100 cases), and the docs note LoCoMo10 answer-term recall remains low and is described as a current weakness. [@claim:clm_d432652a1b14bd4230a5a565b52defd13a0541554e6a6719f0a9c39ee8b42012]
<!-- rcw:end owner=source:src_56dec4ff10e459069a6f6fe4c201fc65 block=evidence -->

## Researcher notes

