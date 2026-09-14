# r2e-gym/r2e-gym

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0d94c4eb9431 @ ea915f385f175d1e

## Summary (orientation draft, not independently verified)

R2E-Gym is a documented framework for procedurally generating executable SWE environments, running SWE agents against them, collecting trajectories, and training/evaluating agents and verifiers; all evidence is documentation (README and ENV_GENERATION.md), no source code slices.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] R2E-Gym is presented as a procedurally curated gym environment for training real-world SWE agents, with over 8.1K problems across 13 repos including executable environments, unit tests, and natural-language task descriptions. -- evidence: [README.md#L56-L56](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L56-L56)
- components (1 claim(s)):
  - [observation/documented] Precollected SFT trajectories are provided for three agent types: a general-purpose code editing agent, an execution-based testing agent generating targeted unit tests, and an execution-free verifier agent for training-free patch reranking. -- evidence: [README.md#L196-L199](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L196-L199)
- design-choices (2 claim(s)):
  - [observation/documented] The SWE-GEN recipe curates executable training environments from commits rather than human-written pull requests or unit tests, which the authors say enables more scalable data curation and agent training. -- evidence: [README.md#L68-L68](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L68-L68)
  - [observation/documented] Hybrid Test-time Scaling combines execution-based and execution-free verifiers, described as having complementary strengths and weaknesses, to achieve better performance when scaling test-time compute. -- evidence: [README.md#L79-L79](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L79-L79), [README.md#L45-L48](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L45-L48)
- workflows (2 claim(s)):
  - [observation/documented] Agent training is done with LLaMA-Factory using provided config files (e.g., llamafactory-cli train train/train_r2egym_32B_agent.yaml), with optional faster-training dependencies like flashattention2, deepspeed, liger-kernel, and unsloth. -- evidence: [README.md#L231-L234](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L231-L234), [README.md#L226-L229](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L226-L229), [README.md#L218-L219](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L218-L219), [README.md#L208-L209](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L208-L209)
  - [observation/documented] Environment generation follows a documented pipeline: register the repo in constants and a RepoName enum with a test command, add it as a git submodule, collect and filter commits (bug-fix, test-matching, test-entity edits), then validate with Docker-based installation and test execution. -- evidence: [docs/ENV_GENERATION.md#L87-L97](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L87-L97), [docs/ENV_GENERATION.md#L107-L119](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L107-L119), [docs/ENV_GENERATION.md#L121-L125](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L121-L125), [docs/ENV_GENERATION.md#L42-L49](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L42-L49), [docs/ENV_GENERATION.md#L22-L31](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L22-L31), [docs/ENV_GENERATION.md#L34-L40](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L34-L40), [docs/ENV_GENERATION.md#L60-L61](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L60-L61), [docs/ENV_GENERATION.md#L99-L104](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/docs/ENV_GENERATION.md#L99-L104)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The Python API exposes EnvArgs and RepoEnv from r2egym.agenthub.environment.env and AgentArgs/Agent from r2egym.agenthub.agent.agent; an agent is run via agent.run(env, max_steps=40, use_fn_calling=True). -- evidence: [README.md#L115-L117](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L115-L117), [README.md#L126-L127](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L126-L127), [README.md#L103-L108](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L103-L108), [README.md#L122-L123](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L122-L123)
  - [observation/documented] Environments support automated reward calculation via env.runtime._calculate_reward() using unit tests, plus helpers such as apply_patch, get_gt_commit, and reverse_patch, and env.get_stats() for per-environment metadata. -- evidence: [README.md#L132-L133](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L132-L133), [README.md#L135-L136](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L135-L136), [README.md#L138-L139](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L138-L139), [README.md#L144-L145](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L144-L145), [README.md#L141-L142](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L141-L142)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Trajectory collection and evaluation support parallelized inference via runagent_multiple with --max_workers (e.g., 54 workers), and each gym instance uses a Docker image of roughly 300-500MB. -- evidence: [README.md#L157-L173](https://github.com/R2E-Gym/R2E-Gym/blob/0d94c4eb9431cd195c55a7ea3abd54006c9a1735/README.md#L157-L173)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
More evidence: [full detail](r2e-gym.detail.md)

Metadata and full claim list: [full detail](r2e-gym.detail.md)
Human notes ([notes](r2e-gym.notes.md), never overwritten by build)

[Back to map index](../../index.md)
