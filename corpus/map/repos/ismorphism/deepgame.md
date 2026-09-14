# ismorphism/deepgame

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 88e6f8927f9c @ 80ed664568fffc29

## Summary (orientation draft, not independently verified)

The snapshot contains only README and LICENSE files describing DeepGame, a Python project implementing Q-learning and Nash Q-learning for grid-world games, with installation and CLI usage instructions. No source code is present in the evidence.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] DeepGame implements single- and multi-agent learning algorithms, including vanilla Q-learning where each agent behaves optimally per Q-values, and Nash Q-learning aiming for Nash equilibrium. -- evidence: [README.md#L7-L9](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L7-L9)
  - [observation/documented] The project is MIT licensed, copyright 2023 Boris Piakillia (Pyakillya), with the standard permission and no-warranty terms. -- evidence: [LICENSE.md#L1-L1](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L1-L1), [LICENSE.md#L5-L10](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L5-L10), [LICENSE.md#L3-L3](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L3-L3), [LICENSE.md#L15-L21](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L15-L21)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The learning_rate argument is described as applying to the Q-learning method, and the method argument selects between Q-learning and Nash-Q. -- evidence: [README.md#L52-L57](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L52-L57)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README instructs users to run the program with 'python run_grid_game.py' using default parameters, and to adjust hyperparameters via its command-line arguments. -- evidence: [README.md#L45-L48](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L45-L48), [README.md#L50-L50](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L50-L50)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The program is run via run_grid_game.py, configurable through CLI arguments including grid size, gamma, epsilon, iterations, learning rate, and method selection. -- evidence: [README.md#L45-L48](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L45-L48), [README.md#L52-L57](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L52-L57), [README.md#L50-L50](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L50-L50)
  - [observation/documented] Default parameter values include grid size 3, gamma 0.95, epsilon 0.5, 1000 iterations, learning rate 0.9, and method 'Q'. -- evidence: [README.md#L52-L57](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L52-L57)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project requires Python 3.6+, Numpy, Nashpy, and Matplotlib, and additionally depends on the mapr2 module from a separate GitHub repository. -- evidence: [README.md#L13-L16](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L13-L16), [README.md#L18-L18](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L18-L18)
  - [observation/documented] Installation involves cloning rllab at a specific commit and pip-installing packages such as joblib, theano, keras, tensorflow, gym, tensorflow_probability, and maci. -- evidence: [README.md#L36-L36](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L36-L36), [README.md#L22-L28](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L22-L28), [README.md#L32-L34](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L32-L34), [README.md#L38-L41](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L38-L41)
- limitations (2 claim(s)):
  - [observation/documented] The README states the repository is not really active due to limited development time, and that breaking changes may occur. -- evidence: [README.md#L3-L3](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L3-L3)
  - [observation/documented] The program is stated to be checked only for the case of two agents (n_agents=2). -- evidence: [README.md#L3-L3](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](deepgame.detail.md).

Metadata and full claim list: [full detail](deepgame.detail.md)
Human notes ([notes](deepgame.notes.md), never overwritten by build)

[Back to map index](../../index.md)
