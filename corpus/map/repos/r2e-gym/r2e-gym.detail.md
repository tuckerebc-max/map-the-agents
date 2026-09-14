# r2e-gym/r2e-gym -- full detail

[Back to orientation](r2e-gym.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/r2e-gym/r2e-gym/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/ea915f385f175d1e.json](../../../wiki/dossiers/r2e-gym/r2e-gym/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/ea915f385f175d1e.json)

## specifications (1 claim(s))

- [observation/documented] R2E-Gym is presented as a procedurally curated gym environment for training real-world SWE agents, with over 8.1K problems across 13 repos including executable environments, unit tests, and natural-language task descriptions. -- evidence: [README.md#L56-L56](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L56-L56) (`clm_0038e0d1f4aca2898132cc91cacf76cd27e62c1f7fdc5edcbf87b2b7754d2f54`)

## components (1 claim(s))

- [observation/documented] Precollected SFT trajectories are provided for three agent types: a general-purpose code editing agent, an execution-based testing agent generating targeted unit tests, and an execution-free verifier agent for training-free patch reranking. -- evidence: [README.md#L196-L199](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L196-L199) (`clm_b92fc9d3d0712fa090da61ecf9b50f9119ac19d177b37020dc00cac42e888b02`)

## design-choices (2 claim(s))

- [observation/documented] The SWE-GEN recipe curates executable training environments from commits rather than human-written pull requests or unit tests, which the authors say enables more scalable data curation and agent training. -- evidence: [README.md#L68-L68](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L68-L68) (`clm_2a78f6b2e2fa5cb4ae62e73bb23d1a27088055b133737c559a680e54e8eff004`)
- [observation/documented] Hybrid Test-time Scaling combines execution-based and execution-free verifiers, described as having complementary strengths and weaknesses, to achieve better performance when scaling test-time compute. -- evidence: [README.md#L79-L79](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L79-L79), [README.md#L45-L48](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L45-L48) (`clm_b3079e72100b30c8ceb09f7c23b92046eaea0c0a4963d7065a915b2a2e2524e7`)

## workflows (2 claim(s))

- [observation/documented] Agent training is done with LLaMA-Factory using provided config files (e.g., llamafactory-cli train train/train_r2egym_32B_agent.yaml), with optional faster-training dependencies like flashattention2, deepspeed, liger-kernel, and unsloth. -- evidence: [README.md#L231-L234](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L231-L234), [README.md#L226-L229](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L226-L229), [README.md#L218-L219](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L218-L219), [README.md#L208-L209](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L208-L209) (`clm_27965e66a0f070d8bacf7a2014c3a18f4fe657305378424f1f5211f39ef7041c`)
- [observation/documented] Environment generation follows a documented pipeline: register the repo in constants and a RepoName enum with a test command, add it as a git submodule, collect and filter commits (bug-fix, test-matching, test-entity edits), then validate with Docker-based installation and test execution. -- evidence: [docs/ENV_GENERATION.md#L87-L97](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L87-L97), [docs/ENV_GENERATION.md#L107-L119](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L107-L119), [docs/ENV_GENERATION.md#L121-L125](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L121-L125), [docs/ENV_GENERATION.md#L42-L49](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L42-L49), [docs/ENV_GENERATION.md#L22-L31](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L22-L31), [docs/ENV_GENERATION.md#L34-L40](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L34-L40), [docs/ENV_GENERATION.md#L60-L61](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L60-L61), [docs/ENV_GENERATION.md#L99-L104](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L99-L104) (`clm_22c6037214ff8457abe117e18e2f6c1e400b0746b230638c66fe6b6006e38d5a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The Python API exposes EnvArgs and RepoEnv from r2egym.agenthub.environment.env and AgentArgs/Agent from r2egym.agenthub.agent.agent; an agent is run via agent.run(env, max_steps=40, use_fn_calling=True). -- evidence: [README.md#L115-L117](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L115-L117), [README.md#L126-L127](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L126-L127), [README.md#L103-L108](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L103-L108), [README.md#L122-L123](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L122-L123) (`clm_fd9de2c267f06d54ee8715e61b9df43b676325b52834ba688c121d3acb4b5ffd`)
- [observation/documented] Environments support automated reward calculation via env.runtime._calculate_reward() using unit tests, plus helpers such as apply_patch, get_gt_commit, and reverse_patch, and env.get_stats() for per-environment metadata. -- evidence: [README.md#L132-L133](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L132-L133), [README.md#L135-L136](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L135-L136), [README.md#L138-L139](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L138-L139), [README.md#L144-L145](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L144-L145), [README.md#L141-L142](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L141-L142) (`clm_691ef8969fad957caf6b3d9c62b23d5e4b0f3351d3ab55df03035f9ddd372ea6`)
- [observation/documented] Agent runs return a Trajectory object containing the full agent trajectory, problem statement, max execution time, exit reason, and output patch. -- evidence: [README.md#L129-L130](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L129-L130) (`clm_b04ee9d2bc1f1174733a7f39f90ff344b5c0dadbacd4ed583aab58f8269effe2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Trajectory collection and evaluation support parallelized inference via runagent_multiple with --max_workers (e.g., 54 workers), and each gym instance uses a Docker image of roughly 300-500MB. -- evidence: [README.md#L157-L173](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L157-L173) (`clm_7109bf6fe3a687b1da02d2a3436cd0d52ea85ffc014e625c6ba30c60f79054e7`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The README reports benchmark results: 51% pass@1 on SWE-Bench Verified with hybrid test-time scaling and 34.4% pass@1 for the commit-based curation approach, both claimed as state-of-the-art for open-weight SWE agents. -- evidence: [README.md#L79-L79](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L79-L79), [README.md#L68-L68](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L68-L68), [README.md#L42-L43](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L42-L43) (`clm_320a8ee4b12b7adff5a77e9936d6d8d08aeca0c003309ed56bf699883cc534a7`)
- [observation/documented] The repo's own evaluation command only produces output trajectories and patches; final SWE-Bench scores are obtained with the official SWE-Bench evaluation harness. -- evidence: [README.md#L191-L192](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L191-L192) (`clm_6492ad663eb6d55b551f021a0cef2fdba426c9eaf4fb8b5fc967e8bcbc57da54`)

## dependencies (1 claim(s))

- [observation/documented] The project uses uv for environment management (venv creation and sync), and agent runs can target LLMs including claude-3-5-sonnet-20241022, gpt-4o, or a vLLM-served R2EGym-32B-Agent model. -- evidence: [README.md#L175-L189](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L175-L189), [README.md#L122-L123](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L122-L123), [README.md#L157-L173](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L157-L173), [README.md#L97-L100](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L97-L100) (`clm_d71cf33803093d7e55fe61adfd646e9b3e60ff7e0abf26ecadb1c01991200f52`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

