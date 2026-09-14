---
access: public
aliases: []
claim_ids:
- clm_0038e0d1f4aca2898132cc91cacf76cd27e62c1f7fdc5edcbf87b2b7754d2f54
- clm_27965e66a0f070d8bacf7a2014c3a18f4fe657305378424f1f5211f39ef7041c
- clm_2a78f6b2e2fa5cb4ae62e73bb23d1a27088055b133737c559a680e54e8eff004
- clm_320a8ee4b12b7adff5a77e9936d6d8d08aeca0c003309ed56bf699883cc534a7
- clm_6492ad663eb6d55b551f021a0cef2fdba426c9eaf4fb8b5fc967e8bcbc57da54
- clm_691ef8969fad957caf6b3d9c62b23d5e4b0f3351d3ab55df03035f9ddd372ea6
- clm_7109bf6fe3a687b1da02d2a3436cd0d52ea85ffc014e625c6ba30c60f79054e7
- clm_b04ee9d2bc1f1174733a7f39f90ff344b5c0dadbacd4ed583aab58f8269effe2
- clm_b3079e72100b30c8ceb09f7c23b92046eaea0c0a4963d7065a915b2a2e2524e7
- clm_b92fc9d3d0712fa090da61ecf9b50f9119ac19d177b37020dc00cac42e888b02
- clm_d71cf33803093d7e55fe61adfd646e9b3e60ff7e0abf26ecadb1c01991200f52
- clm_fd9de2c267f06d54ee8715e61b9df43b676325b52834ba688c121d3acb4b5ffd
maturity: draft
page_id: pg_d510215ec08258938d75cc00dc0947bb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d8e2c60d433f54849c3561da377b87f5
title: R2E-Gym/R2E-Gym/README.md @ 0d94c4eb9431
updated_at: '2026-09-14T04:17:34Z'
---

# R2E-Gym/R2E-Gym/README.md @ 0d94c4eb9431

<!-- rcw:begin owner=source:src_d8e2c60d433f54849c3561da377b87f5 block=evidence -->
- R2E-Gym is presented as a procedurally curated gym environment for training real-world SWE agents, with over 8.1K problems across 13 repos including executable environments, unit tests, and natural-language task descriptions. [@claim:clm_0038e0d1f4aca2898132cc91cacf76cd27e62c1f7fdc5edcbf87b2b7754d2f54]
- Agent training is done with LLaMA-Factory using provided config files (e.g., llamafactory-cli train train/train_r2egym_32B_agent.yaml), with optional faster-training dependencies like flashattention2, deepspeed, liger-kernel, and unsloth. [@claim:clm_27965e66a0f070d8bacf7a2014c3a18f4fe657305378424f1f5211f39ef7041c]
- The SWE-GEN recipe curates executable training environments from commits rather than human-written pull requests or unit tests, which the authors say enables more scalable data curation and agent training. [@claim:clm_2a78f6b2e2fa5cb4ae62e73bb23d1a27088055b133737c559a680e54e8eff004]
- The README reports benchmark results: 51% pass@1 on SWE-Bench Verified with hybrid test-time scaling and 34.4% pass@1 for the commit-based curation approach, both claimed as state-of-the-art for open-weight SWE agents. [@claim:clm_320a8ee4b12b7adff5a77e9936d6d8d08aeca0c003309ed56bf699883cc534a7]
- The repo's own evaluation command only produces output trajectories and patches; final SWE-Bench scores are obtained with the official SWE-Bench evaluation harness. [@claim:clm_6492ad663eb6d55b551f021a0cef2fdba426c9eaf4fb8b5fc967e8bcbc57da54]
- Environments support automated reward calculation via env.runtime._calculate_reward() using unit tests, plus helpers such as apply_patch, get_gt_commit, and reverse_patch, and env.get_stats() for per-environment metadata. [@claim:clm_691ef8969fad957caf6b3d9c62b23d5e4b0f3351d3ab55df03035f9ddd372ea6]
- Trajectory collection and evaluation support parallelized inference via runagent_multiple with --max_workers (e.g., 54 workers), and each gym instance uses a Docker image of roughly 300-500MB. [@claim:clm_7109bf6fe3a687b1da02d2a3436cd0d52ea85ffc014e625c6ba30c60f79054e7]
- Agent runs return a Trajectory object containing the full agent trajectory, problem statement, max execution time, exit reason, and output patch. [@claim:clm_b04ee9d2bc1f1174733a7f39f90ff344b5c0dadbacd4ed583aab58f8269effe2]
- Hybrid Test-time Scaling combines execution-based and execution-free verifiers, described as having complementary strengths and weaknesses, to achieve better performance when scaling test-time compute. [@claim:clm_b3079e72100b30c8ceb09f7c23b92046eaea0c0a4963d7065a915b2a2e2524e7]
- Precollected SFT trajectories are provided for three agent types: a general-purpose code editing agent, an execution-based testing agent generating targeted unit tests, and an execution-free verifier agent for training-free patch reranking. [@claim:clm_b92fc9d3d0712fa090da61ecf9b50f9119ac19d177b37020dc00cac42e888b02]
- The project uses uv for environment management (venv creation and sync), and agent runs can target LLMs including claude-3-5-sonnet-20241022, gpt-4o, or a vLLM-served R2EGym-32B-Agent model. [@claim:clm_d71cf33803093d7e55fe61adfd646e9b3e60ff7e0abf26ecadb1c01991200f52]
- The Python API exposes EnvArgs and RepoEnv from r2egym.agenthub.environment.env and AgentArgs/Agent from r2egym.agenthub.agent.agent; an agent is run via agent.run(env, max_steps=40, use_fn_calling=True). [@claim:clm_fd9de2c267f06d54ee8715e61b9df43b676325b52834ba688c121d3acb4b5ffd]
<!-- rcw:end owner=source:src_d8e2c60d433f54849c3561da377b87f5 block=evidence -->

## Researcher notes

