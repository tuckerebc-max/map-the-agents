# edantoledo/stoix

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8fff19c94a47 @ 1747bcbd8c5bbd73

## Summary (orientation draft, not independently verified)

Stoix is a JAX-based distributed single-agent reinforcement learning research codebase offering Anakin and Sebulba system paradigms, many algorithm implementations, Hydra configuration, and JSON-based evaluation logging; contributor guidelines cover CLA, pre-commit, and PR review.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Stoix is a distributed single-agent reinforcement learning library implemented end-to-end in JAX, aimed at fast iteration on RL research ideas. -- evidence: [README.md#L23-L25](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L23-L25), [README.md#L35-L35](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L35-L35)
- components (5 claim(s)):
  - [observation/documented] The repository provides single-file implementations of many popular RL algorithms, including DQN variants, Rainbow, R2D2, DDPG family, TD3, SAC, PPO, DPO, and MPO. -- evidence: [README.md#L69-L93](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L69-L93), [README.md#L57-L57](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L57-L57)
  - [observation/documented] Stoix includes wrappers for JAX environments such as Gymnax, Jumanji, Brax, XMinigrid, Craftax, POPJym, Navix and JaxARC, plus non-JAX environments Envpool and Gymnasium. -- evidence: [README.md#L98-L99](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L98-L99), [README.md#L96-L96](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L96-L96)
- design-choices (2 claim(s)):
  - [observation/documented] Stoix offers two system paradigms: Anakin, fully compiled end-to-end with JAX jit/pmap for native JAX environments, and Sebulba, which separates acting and learning devices and supports non-JAX environments. -- evidence: [README.md#L42-L42](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L42-L42), [README.md#L44-L44](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L44-L44), [README.md#L46-L46](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L46-L46)
  - [observation/documented] Stoix is intentionally not a modular importable library; it follows a CleanRL/PureJaxRL-style philosophy allowing code duplication for readability, with abstraction used for networks, environments, logging, and evaluation. -- evidence: [README.md#L122-L122](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L122-L122), [README.md#L52-L52](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L52-L52)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors must sign a Contributor License Agreement, use prefixed hyphen-delimited branch names, follow conventional commits, install pre-commit hooks, and submit all changes via GitHub pull request review. -- evidence: [docs/CONTRIBUTING.md#L30-L38](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L30-L38), [docs/CONTRIBUTING.md#L8-L12](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L8-L12), [docs/CONTRIBUTING.md#L44-L44](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L44-L44), [docs/CONTRIBUTING.md#L48-L51](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L48-L51), [docs/CONTRIBUTING.md#L42-L42](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/docs/CONTRIBUTING.md#L42-L42)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Systems are run as Python scripts with Hydra configuration; hyperparameters, environments, and networks can be overridden from the command line, e.g. env=gymnax/cartpole with system-level overrides. -- evidence: [README.md#L153-L153](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L153-L153), [README.md#L143-L145](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L143-L145), [README.md#L155-L157](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L155-L157)
  - [observation/documented] Some algorithm variants are selected purely via network architecture config, e.g. Dueling DQN or dueling C51 by passing network=mlp_dueling_dqn or mlp_dueling_c51 to the base DQN/C51 scripts. -- evidence: [README.md#L167-L169](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L167-L169), [README.md#L159-L159](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L159-L159), [README.md#L161-L163](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L161-L163)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Stoix natively logs experiment results to JSON files following the Gorsane et al. (2022) standard, enabling downstream aggregation and RLiable-style statistical comparison via the MARL-eval tooling. -- evidence: [README.md#L63-L63](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L63-L63), [README.md#L102-L102](https://github.com/EdanToledo/Stoix/blob/8fff19c94a478c1e1ff75fbf10396d488aa25d70/README.md#L102-L102)
- dependencies (1 claim(s)):
More evidence: [full detail](stoix.detail.md)

Metadata and full claim list: [full detail](stoix.detail.md)
Human notes ([notes](stoix.notes.md), never overwritten by build)

[Back to map index](../../index.md)
