---
access: public
aliases: []
claim_ids:
- clm_149adf6e2b18fb414afd4d1dc814d3cfb5a53954580811415e4cda1b36e350af
- clm_2a53c31d2925de4221f9f297d52bb62bca1a25aa6720e25839d0d9b36571589d
- clm_2e79f6cbc445267e043fc325c57984bccf8c193287c97134b3e4b9c18052ced9
- clm_3576d03ca23a9ca7bdc0abee2d0a7cb17fa1b93cdb689155e55da1ac03ed52d5
- clm_48ba8b306d91ee5b2d38650cd784466fc0e617e55754d4961b0e87a5912f7321
- clm_4ac2a362fa3af9474cb702bd6f65d30d415aa5000881f91e77d93cd0867669a2
- clm_564419e94a8ee8d48902fe6a4f50b05b0c12f52b2c4116c10130e8e60cad44a8
- clm_612402e8c8d146e9c5a8673d4b6a7d2d8a0970ba9f32ee1044ed1d4279e145ae
- clm_769193f44278cef171e83166d0cc0fc6c4ed8a29d0241e461ad90c8e978efafb
- clm_9f09e96cd9af30f094c300cef6398c3c551203087faf24c716f6ef1d43d46a95
- clm_a38fc0c3f7be31d02d4a7d7f4b0b7782dc77e9f7b624a8bbd4a7c1628216ae77
- clm_a44717dbddbadf2b1f5ad6eb79c3d44d385d3fdab98a5d35331e82c15392cd89
- clm_d4c4d2868c3b0afdb628b0aa96067462dfc7d7f3fff2ae8ed5284dac86893d31
- clm_ea3d0bb4e9fa30f07c0f2f6a9c2f1d677bae9e9892e403233566d989f00940c4
- clm_f8b13a279b9a761d3ec1eda3fb2aad88901a66a0b2bf6ca7d4ef56fe846c992c
maturity: draft
page_id: pg_6d2e8440fb7c5903b3c6919e8f645f4b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_281df9e0d30a5dfa88293103989dd807
title: akashgit/remote-factory/README.md @ 4262d361ebbf
updated_at: '2026-09-14T01:32:34Z'
---

# akashgit/remote-factory/README.md @ 4262d361ebbf

<!-- rcw:begin owner=source:src_281df9e0d30a5dfa88293103989dd807 block=evidence -->
- In create mode, prefixing `--focus` with a mode name and colon (e.g. "improve: ...") updates an existing registered workflow, while a focus without a colon always creates a new mode. [@claim:clm_149adf6e2b18fb414afd4d1dc814d3cfb5a53954580811415e4cda1b36e350af]
- The eval system scores each change with a weighted composite across Hygiene (6 dimensions), Growth (5 dimensions), and user-defined Project tiers; `factory discover` auto-detects language and framework to generate the eval profile. [@claim:clm_2a53c31d2925de4221f9f297d52bb62bca1a25aa6720e25839d0d9b36571589d]
- Repository development practice: contributors install dev deps with `uv sync --all-groups`, run `pytest -v`, lint with `ruff check .`, and type-check with `mypy factory/`; a contributing guide covers dev setup, code style, testing, and PR workflow. [@claim:clm_2e79f6cbc445267e043fc325c57984bccf8c193287c97134b3e4b9c18052ced9]
- The system is described as four layers: a Python CLI, a workflow graph engine of Pydantic DAGs with typed nodes (AgentNode, FnNode, GateNode, ForkNode, JoinNode), a CEO orchestrator agent, and specialist Claude Code subprocess agents. [@claim:clm_3576d03ca23a9ca7bdc0abee2d0a7cb17fa1b93cdb689155e55da1ac03ed52d5]
- Shipped workflows include frontend-design, parallel-improve, deep-research, design-v2, deep-qa, and study, plus community-contributed benchmark workflows (swebench, featurebench, legacybench, devopsgym, terminalbench, and others) following a study→solver→gate→merge pattern. [@claim:clm_48ba8b306d91ee5b2d38650cd784466fc0e617e55754d4961b0e87a5912f7321]
- The primary CLI is `factory ceo <path> --mode <mode>` with modes including design, design-v2, create, meta, and outer-loop (run headless), plus `--focus` to target a backlog item, GitHub issue, or topic. [@claim:clm_4ac2a362fa3af9474cb702bd6f65d30d415aa5000881f91e77d93cd0867669a2]
- The CEO agent detects project state, reads SKILL.md playbooks, spawns specialist agents via `factory agent <role>`, and makes keep/revert decisions based on eval scores. [@claim:clm_564419e94a8ee8d48902fe6a4f50b05b0c12f52b2c4116c10130e8e60cad44a8]
- An outer loop evolves workflow DAGs against benchmarks via MAP-Elites: it mutates workflow structure, evaluates candidates on a real benchmark instance, and selects for higher test pass rates. [@claim:clm_612402e8c8d146e9c5a8673d4b6a7d2d8a0970ba9f32ee1044ed1d4279e145ae]
- Workflow graphs are exported to SKILL.md prose playbooks through a verified pipeline (templatize, review agent, guard, split) producing SKILL.md plus SKILL.annotations.yaml, with a CI regression test guarding drift between definitions and exported skills. [@claim:clm_769193f44278cef171e83166d0cc0fc6c4ed8a29d0241e461ad90c8e978efafb]
- Design-v2 replaces hardcoded researchers and a single strategist with three Director agents that dynamically size N (3-7) research directions, M (2-5) strategy perspectives, and K (2-5) QA testers, following parallel generation, synthesis, then gating. [@claim:clm_9f09e96cd9af30f094c300cef6398c3c551203087faf24c716f6ef1d43d46a95]
- Prerequisites are Python 3.11+, the uv package manager, and an installed, authenticated Claude Code; LangFuse tracing additionally requires Docker or Podman with a compose tool. [@claim:clm_a38fc0c3f7be31d02d4a7d7f4b0b7782dc77e9f7b624a8bbd4a7c1628216ae77]
- Repository development practice: after editing a workflow graph in `factory/workflow/definitions.py`, contributors re-export skills via `factory workflow export-skills` and test with `pytest tests/test_workflow.py -v`. [@claim:clm_a44717dbddbadf2b1f5ad6eb79c3d44d385d3fdab98a5d35331e82c15392cd89]
- re:factory is also distributed as a Claude Code plugin exposing a `/factory:implement` slash command, namespaced subagents like `factory:ceo`, and bundled skills; the plugin still shells out to the globally installed `factory` CLI. [@claim:clm_d4c4d2868c3b0afdb628b0aa96067462dfc7d7f3fff2ae8ed5284dac86893d31]
- Additional CLI surface includes `factory outer-loop calibrate`, `factory run --loop --interval`, `factory tmux --loop`, `factory discover`, `factory ace`, `factory install`, and `factory workflow export-skills`. [@claim:clm_ea3d0bb4e9fa30f07c0f2f6a9c2f1d677bae9e9892e403233566d989f00940c4]
- All state is local: per-project state lives in `.factory/` (recommended for .gitignore) and global state in `~/.factory/`, including a registry at `~/.factory/registry.json` and evolved playbooks under `~/.factory/playbooks/`. [@claim:clm_f8b13a279b9a761d3ec1eda3fb2aad88901a66a0b2bf6ca7d4ef56fe846c992c]
<!-- rcw:end owner=source:src_281df9e0d30a5dfa88293103989dd807 block=evidence -->

## Researcher notes

