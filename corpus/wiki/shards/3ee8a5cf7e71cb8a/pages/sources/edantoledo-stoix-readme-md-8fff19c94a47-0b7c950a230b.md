---
access: public
aliases: []
claim_ids:
- clm_0b42df519803bb0dedb5ae68f26fe173e06cfe899131f9973119e852493f2b26
- clm_439a9f8ce5eb284dae42d79c7babeaacdd3293c6e77d5c52052200d0bc569339
- clm_4a812e86ebe9ba196d3b3d016ea96420b250f0aa86d210aafff1e5f79d308b6d
- clm_6d8730257a673a97941c703f11ad383c3d54d352fba3971556aea31ffb7f4466
- clm_8bb24a521188826aab2a446c388007d3ee752b75196261629cb9f59ca7b6fa6b
- clm_8c1225d3c20ef9c94434fab1b642d13c61aee0ac8ee567100732a9118126dcbb
- clm_9a47d3ce9d49bb9e528626eb027b4a444d3017be965e21dd7600dd3c7b87f3df
- clm_a7c783cf93a8a0ccb289eae9cf5ba9efc354592dc6daeee28dcc688c9905e6da
- clm_ac6d09c45b713415c41539dc56e9c8e706d8cee58052a01ffe2a88aa5455638b
- clm_b568ab29f3171f66754f054300593dae3311687a1df4e09f89b4f328686c3001
- clm_b664691a890a2ebc1de5ee364bbbfb72163ba38ce5c88064326627cb3abff707
- clm_d7191d29a24ede4452d83a652f3b90df8611a57d7843048b85cbb88d45d62b10
- clm_dfb57a3e5085c89830e6d9afb318514243b01527433cc447da87668ea2695cdd
maturity: draft
page_id: pg_11b0d634e3ea503d97b10b7c950a230b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2c2ae8d2667356cf88e06a02262b58fc
title: EdanToledo/Stoix/README.md @ 8fff19c94a47
updated_at: '2026-09-14T03:49:05Z'
---

# EdanToledo/Stoix/README.md @ 8fff19c94a47

<!-- rcw:begin owner=source:src_2c2ae8d2667356cf88e06a02262b58fc block=evidence -->
- Stoix natively logs experiment results to JSON files following the Gorsane et al. (2022) standard, enabling downstream aggregation and RLiable-style statistical comparison via the MARL-eval tooling. [@claim:clm_0b42df519803bb0dedb5ae68f26fe173e06cfe899131f9973119e852493f2b26]
- Stoix is intentionally not a modular importable library; it follows a CleanRL/PureJaxRL-style philosophy allowing code duplication for readability, with abstraction used for networks, environments, logging, and evaluation. [@claim:clm_439a9f8ce5eb284dae42d79c7babeaacdd3293c6e77d5c52052200d0bc569339]
- The repository provides single-file implementations of many popular RL algorithms, including DQN variants, Rainbow, R2D2, DDPG family, TD3, SAC, PPO, DPO, and MPO. [@claim:clm_4a812e86ebe9ba196d3b3d016ea96420b250f0aa86d210aafff1e5f79d308b6d]
- All implementations include checkpointing to save and resume parameters and training runs, and training can be vectorized with vmap on one device or distributed with pmap across devices. [@claim:clm_6d8730257a673a97941c703f11ad383c3d54d352fba3971556aea31ffb7f4466]
- Some algorithm variants are selected purely via network architecture config, e.g. Dueling DQN or dueling C51 by passing network=mlp_dueling_dqn or mlp_dueling_c51 to the base DQN/C51 scripts. [@claim:clm_8bb24a521188826aab2a446c388007d3ee752b75196261629cb9f59ca7b6fa6b]
- Stoix includes wrappers for JAX environments such as Gymnax, Jumanji, Brax, XMinigrid, Craftax, POPJym, Navix and JaxARC, plus non-JAX environments Envpool and Gymnasium. [@claim:clm_8c1225d3c20ef9c94434fab1b642d13c61aee0ac8ee567100732a9118126dcbb]
- A SLURM launcher built on Hydra and submitit automatically submits a separate job per algorithm/environment/seed combination, with configurable resources like partition, time, nodes, and GPUs. [@claim:clm_9a47d3ce9d49bb9e528626eb027b4a444d3017be965e21dd7600dd3c7b87f3df]
- Stoix offers two system paradigms: Anakin, fully compiled end-to-end with JAX jit/pmap for native JAX environments, and Sebulba, which separates acting and learning devices and supports non-JAX environments. [@claim:clm_a7c783cf93a8a0ccb289eae9cf5ba9efc354592dc6daeee28dcc688c9905e6da]
- Default hyperparameters and networks are not tuned for any specific environment, and the README notes actual timesteps run may be less than the requested budget unless divisibility conditions are met. [@claim:clm_ac6d09c45b713415c41539dc56e9c8e706d8cee58052a01ffe2a88aa5455638b]
- Stoix targets Python 3.10, is installed by cloning and syncing with UV, and users are advised to install the JAX version matching their hardware accelerator. [@claim:clm_b568ab29f3171f66754f054300593dae3311687a1df4e09f89b4f328686c3001]
- Stoix is a distributed single-agent reinforcement learning library implemented end-to-end in JAX, aimed at fast iteration on RL research ideas. [@claim:clm_b664691a890a2ebc1de5ee364bbbfb72163ba38ce5c88064326627cb3abff707]
- Systems are run as Python scripts with Hydra configuration; hyperparameters, environments, and networks can be overridden from the command line, e.g. env=gymnax/cartpole with system-level overrides. [@claim:clm_d7191d29a24ede4452d83a652f3b90df8611a57d7843048b85cbb88d45d62b10]
- In environments without a timestep limit or terminating mechanic, evaluation can appear to hang indefinitely while an episode never finishes; adding a step limit or action masking is suggested. [@claim:clm_dfb57a3e5085c89830e6d9afb318514243b01527433cc447da87668ea2695cdd]
<!-- rcw:end owner=source:src_2c2ae8d2667356cf88e06a02262b58fc block=evidence -->

## Researcher notes

