# edantoledo/stoix -- full detail

[Back to orientation](stoix.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/edantoledo/stoix/8fff19c94a478c1e1ff75fbf10396d488aa25d70/1747bcbd8c5bbd73.json](../../../wiki/dossiers/edantoledo/stoix/8fff19c94a478c1e1ff75fbf10396d488aa25d70/1747bcbd8c5bbd73.json)

## specifications (1 claim(s))

- [observation/documented] Stoix is a distributed single-agent reinforcement learning library implemented end-to-end in JAX, aimed at fast iteration on RL research ideas. -- evidence: [README.md#L23-L25](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L23-L25), [README.md#L35-L35](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L35-L35) (`clm_b664691a890a2ebc1de5ee364bbbfb72163ba38ce5c88064326627cb3abff707`)

## components (5 claim(s))

- [observation/documented] The repository provides single-file implementations of many popular RL algorithms, including DQN variants, Rainbow, R2D2, DDPG family, TD3, SAC, PPO, DPO, and MPO. -- evidence: [README.md#L69-L93](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L69-L93), [README.md#L57-L57](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L57-L57) (`clm_4a812e86ebe9ba196d3b3d016ea96420b250f0aa86d210aafff1e5f79d308b6d`)
- [observation/documented] Stoix includes wrappers for JAX environments such as Gymnax, Jumanji, Brax, XMinigrid, Craftax, POPJym, Navix and JaxARC, plus non-JAX environments Envpool and Gymnasium. -- evidence: [README.md#L98-L99](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L98-L99), [README.md#L96-L96](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L96-L96) (`clm_8c1225d3c20ef9c94434fab1b642d13c61aee0ac8ee567100732a9118126dcbb`)
- [observation/documented] A SLURM launcher built on Hydra and submitit automatically submits a separate job per algorithm/environment/seed combination, with configurable resources like partition, time, nodes, and GPUs. -- evidence: [README.md#L187-L189](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L187-L189), [README.md#L173-L173](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L173-L173), [README.md#L177-L179](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L177-L179) (`clm_9a47d3ce9d49bb9e528626eb027b4a444d3017be965e21dd7600dd3c7b87f3df`)
- [observation/documented] All implementations include checkpointing to save and resume parameters and training runs, and training can be vectorized with vmap on one device or distributed with pmap across devices. -- evidence: [README.md#L57-L57](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L57-L57) (`clm_6d8730257a673a97941c703f11ad383c3d54d352fba3971556aea31ffb7f4466`)
- [observation/documented] JaxARC environment integration exposes four ARC datasets (Mini, AGI1, AGI2, ConceptARC), three action modes (point, bbox, mask), and domain metrics like best_similarity and solved via an ExtendedMetrics wrapper. -- evidence: [docs/envs/jaxarc.md#L36-L39](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/envs/jaxarc.md#L36-L39), [docs/envs/jaxarc.md#L23-L28](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/envs/jaxarc.md#L23-L28), [docs/envs/jaxarc.md#L82-L82](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/envs/jaxarc.md#L82-L82), [docs/envs/jaxarc.md#L55-L57](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/envs/jaxarc.md#L55-L57), [docs/envs/jaxarc.md#L74-L80](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/envs/jaxarc.md#L74-L80) (`clm_238efcf62959fe6a02f80350898e78bb05baac66149716872c4a09057fcd5e9c`)

## design-choices (2 claim(s))

- [observation/documented] Stoix offers two system paradigms: Anakin, fully compiled end-to-end with JAX jit/pmap for native JAX environments, and Sebulba, which separates acting and learning devices and supports non-JAX environments. -- evidence: [README.md#L42-L42](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L42-L42), [README.md#L44-L44](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L44-L44), [README.md#L46-L46](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L46-L46) (`clm_a7c783cf93a8a0ccb289eae9cf5ba9efc354592dc6daeee28dcc688c9905e6da`)
- [observation/documented] Stoix is intentionally not a modular importable library; it follows a CleanRL/PureJaxRL-style philosophy allowing code duplication for readability, with abstraction used for networks, environments, logging, and evaluation. -- evidence: [README.md#L122-L122](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L122-L122), [README.md#L52-L52](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L52-L52) (`clm_439a9f8ce5eb284dae42d79c7babeaacdd3293c6e77d5c52052200d0bc569339`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors must sign a Contributor License Agreement, use prefixed hyphen-delimited branch names, follow conventional commits, install pre-commit hooks, and submit all changes via GitHub pull request review. -- evidence: [docs/CONTRIBUTING.md#L30-L38](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L30-L38), [docs/CONTRIBUTING.md#L8-L12](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L8-L12), [docs/CONTRIBUTING.md#L44-L44](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L44-L44), [docs/CONTRIBUTING.md#L48-L51](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L48-L51), [docs/CONTRIBUTING.md#L42-L42](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L42-L42) (`clm_3ef53f9cc74098873b3d5cbb5ca09a62d2db7e3f3deacd3c20ad8fee960eecea`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Systems are run as Python scripts with Hydra configuration; hyperparameters, environments, and networks can be overridden from the command line, e.g. env=gymnax/cartpole with system-level overrides. -- evidence: [README.md#L153-L153](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L153-L153), [README.md#L143-L145](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L143-L145), [README.md#L155-L157](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L155-L157) (`clm_d7191d29a24ede4452d83a652f3b90df8611a57d7843048b85cbb88d45d62b10`)
- [observation/documented] Some algorithm variants are selected purely via network architecture config, e.g. Dueling DQN or dueling C51 by passing network=mlp_dueling_dqn or mlp_dueling_c51 to the base DQN/C51 scripts. -- evidence: [README.md#L167-L169](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L167-L169), [README.md#L159-L159](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L159-L159), [README.md#L161-L163](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L161-L163) (`clm_8bb24a521188826aab2a446c388007d3ee752b75196261629cb9f59ca7b6fa6b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Stoix natively logs experiment results to JSON files following the Gorsane et al. (2022) standard, enabling downstream aggregation and RLiable-style statistical comparison via the MARL-eval tooling. -- evidence: [README.md#L63-L63](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L63-L63), [README.md#L102-L102](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L102-L102) (`clm_0b42df519803bb0dedb5ae68f26fe173e06cfe899131f9973119e852493f2b26`)

## dependencies (1 claim(s))

- [observation/documented] Stoix targets Python 3.10, is installed by cloning and syncing with UV, and users are advised to install the JAX version matching their hardware accelerator. -- evidence: [README.md#L134-L135](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L134-L135), [README.md#L126-L132](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L126-L132), [README.md#L124-L124](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L124-L124) (`clm_b568ab29f3171f66754f054300593dae3311687a1df4e09f89b4f328686c3001`)

## limitations (2 claim(s))

- [observation/documented] Default hyperparameters and networks are not tuned for any specific environment, and the README notes actual timesteps run may be less than the requested budget unless divisibility conditions are met. -- evidence: [README.md#L118-L118](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L118-L118), [README.md#L199-L199](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L199-L199), [README.md#L35-L35](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L35-L35) (`clm_ac6d09c45b713415c41539dc56e9c8e706d8cee58052a01ffe2a88aa5455638b`)
- [observation/documented] In environments without a timestep limit or terminating mechanic, evaluation can appear to hang indefinitely while an episode never finishes; adding a step limit or action masking is suggested. -- evidence: [README.md#L197-L197](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L197-L197) (`clm_dfb57a3e5085c89830e6d9afb318514243b01527433cc447da87668ea2695cdd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

