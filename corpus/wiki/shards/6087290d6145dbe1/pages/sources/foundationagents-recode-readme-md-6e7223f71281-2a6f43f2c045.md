---
access: public
aliases: []
claim_ids:
- clm_45edd50f2672648a1d4dfb2fc6024f86274fc6a17445bfb8ac58981e37078e60
- clm_61c35d4d263c6703773a944e12e1bfef2e34c95b2b9742990c524edf78045add
- clm_6eb3a3e434db03eeabec6b8c5c00994b0db0f6aff15dfba227c6dcfb732d7fab
- clm_721246fc7c765c90322b6284177c63b2a4c18e25f74fac9250694bcd33ff0be1
- clm_8a4871abab48bb47d8e6eef15a12b040b4a60235b39a18d3e11020d3bbbd1e26
- clm_95f55e37f0dd17298292ebc74421fff2e842e03f2211020afa3819da795845c3
- clm_a4dfa0ef344f5a11532515bc193774a19b966baff05da8ed4b02e9fd649c3815
- clm_cea2a64673e1fcee30bcf2a6881f8ec1146ed91798d6bdd0f32c7065e49b6cf9
- clm_cf097eab89e8611c16a8261a2d5050cca27b04c5c56e6dc7c8fcff65c64064f9
- clm_e098cece56a6f7c93277cc51090f0bfce3590d6f5e39ca1379775d691fc2e29a
- clm_ffb847cc2ddf28386453d5bb775269e8eb5e5b60b2723a82e445d3b6bb8727c7
maturity: draft
page_id: pg_a4f8ee58c5675dba80fc2a6f43f2c045
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d08cff3a535f5a548c8f645962d8cb20
title: FoundationAgents/ReCode/README.md @ 6e7223f71281
updated_at: '2026-09-14T03:51:43Z'
---

# FoundationAgents/ReCode/README.md @ 6e7223f71281

<!-- rcw:begin owner=source:src_d08cff3a535f5a548c8f645962d8cb20 block=evidence -->
- The repository includes run.py as CLI entry point, agents/recode/ implementation, envs/ wrappers for alfworld, webshop, and sciworld, configs/, and utils/ with an async OpenAI wrapper and constrained executor. [@claim:clm_45edd50f2672648a1d4dfb2fc6024f86274fc6a17445bfb8ac58981e37078e60]
- LLM access is configured via named profiles in configs/profiles.yaml selected with --profile; OPENAI_API_KEY serves as a fallback, and cost tracking loads configs/prices.json with a track_costs toggle. [@claim:clm_61c35d4d263c6703773a944e12e1bfef2e34c95b2b9742990c524edf78045add]
- A constrained Python executor maintains environment variables, validates code blocks, and exposes the toolset available to the agent. [@claim:clm_6eb3a3e434db03eeabec6b8c5c00994b0db0f6aff15dfba227c6dcfb732d7fab]
- Partial programs are organized in a tree where each node captures one sub-task and records its execution trace. [@claim:clm_721246fc7c765c90322b6284177c63b2a4c18e25f74fac9250694bcd33ff0be1]
- A dynamic execution loop executes each node immediately, with fresh observations deciding whether to expand further, retry, or finish. [@claim:clm_8a4871abab48bb47d8e6eef15a12b040b4a60235b39a18d3e11020d3bbbd1e26]
- run.py exposes flags including -a/--agent, -e/--env, -n/--instances, -c/--concurrent, --split, --seed, --max-depth, --profile, and -C/--config for YAML-based flag overrides. [@claim:clm_95f55e37f0dd17298292ebc74421fff2e842e03f2211020afa3819da795845c3]
- The README reports SFT experiments with Qwen2.5-7B-Instruct giving ReCode+SFT an average of 70.4% versus ReAct+SFT (67.6%) and CodeAct+SFT (55.8%). [@claim:clm_a4dfa0ef344f5a11532515bc193774a19b966baff05da8ed4b02e9fd649c3815]
- New environments implement a base Env contract with reset, _run, is_done, is_success, and report, plus per-environment prompts and few-shot files under agents/recode/resources/. [@claim:clm_cea2a64673e1fcee30bcf2a6881f8ec1146ed91798d6bdd0f32c7065e49b6cf9]
- Repository development practice: setup requires a conda environment with Python 3.10 or newer, and the README suggests configuring the three benchmark environments separately since dependency conflicts are unconfirmed. [@claim:clm_cf097eab89e8611c16a8261a2d5050cca27b04c5c56e6dc7c8fcff65c64064f9]
- The README reports inference comparisons against ReAct, CodeAct, AdaPlanner, and ADaPT, claiming an average score of 60.8 (10.5 above the best baseline) and a perfect 100 in ALFWorld with claude-4-sonnet. [@claim:clm_e098cece56a6f7c93277cc51090f0bfce3590d6f5e39ca1379775d691fc2e29a]
- ReCode unifies plan and action into a single code representation, treating high-level plans as placeholder functions that recursively decompose into executable primitives. [@claim:clm_ffb847cc2ddf28386453d5bb775269e8eb5e5b60b2723a82e445d3b6bb8727c7]
<!-- rcw:end owner=source:src_d08cff3a535f5a548c8f645962d8cb20 block=evidence -->

## Researcher notes

