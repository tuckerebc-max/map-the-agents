# ismorphism/deepgame -- full detail

[Back to orientation](deepgame.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ismorphism/deepgame/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/80ed664568fffc29.json](../../../wiki/dossiers/ismorphism/deepgame/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/80ed664568fffc29.json)

## specifications (2 claim(s))

- [observation/documented] DeepGame implements single- and multi-agent learning algorithms, including vanilla Q-learning where each agent behaves optimally per Q-values, and Nash Q-learning aiming for Nash equilibrium. -- evidence: [README.md#L7-L9](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L7-L9) (`clm_901eb3f779301a802238c7b77de033a873d1a965e4abe481d16c5c32142f2892`)
- [observation/documented] The project is MIT licensed, copyright 2023 Boris Piakillia (Pyakillya), with the standard permission and no-warranty terms. -- evidence: [LICENSE.md#L1-L1](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L1-L1), [LICENSE.md#L5-L10](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L5-L10), [LICENSE.md#L3-L3](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L3-L3), [LICENSE.md#L15-L21](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/LICENSE.md#L15-L21) (`clm_38357181d1856dd0ec4461a641e738adcb727dbc4327bfe756a66df289a78c21`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The learning_rate argument is described as applying to the Q-learning method, and the method argument selects between Q-learning and Nash-Q. -- evidence: [README.md#L52-L57](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L52-L57) (`clm_991f99ad189dc73fce08739833b4136501cf3146af09b80fe527abc4c144ca68`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README instructs users to run the program with 'python run_grid_game.py' using default parameters, and to adjust hyperparameters via its command-line arguments. -- evidence: [README.md#L45-L48](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L45-L48), [README.md#L50-L50](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L50-L50) (`clm_f7c7f04d5d3c938471198771e8587a033e2ed2c87604f5cbcb8f5389d84465f7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The program is run via run_grid_game.py, configurable through CLI arguments including grid size, gamma, epsilon, iterations, learning rate, and method selection. -- evidence: [README.md#L45-L48](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L45-L48), [README.md#L52-L57](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L52-L57), [README.md#L50-L50](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L50-L50) (`clm_99a7222cf8ffba50f9169124e4bd36934b5325f2c5731dd47b2eb17b887a0fd4`)
- [observation/documented] Default parameter values include grid size 3, gamma 0.95, epsilon 0.5, 1000 iterations, learning rate 0.9, and method 'Q'. -- evidence: [README.md#L52-L57](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L52-L57) (`clm_61e3202353768dad80642486389778d3d02f0fe28bc34ad4ece26f2726632657`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project requires Python 3.6+, Numpy, Nashpy, and Matplotlib, and additionally depends on the mapr2 module from a separate GitHub repository. -- evidence: [README.md#L13-L16](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L13-L16), [README.md#L18-L18](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L18-L18) (`clm_4b1b553bd054c3723d0a9cdf15704557f32817f992f35c5189cc3b58b9ab8a36`)
- [observation/documented] Installation involves cloning rllab at a specific commit and pip-installing packages such as joblib, theano, keras, tensorflow, gym, tensorflow_probability, and maci. -- evidence: [README.md#L36-L36](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L36-L36), [README.md#L22-L28](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L22-L28), [README.md#L32-L34](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L32-L34), [README.md#L38-L41](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L38-L41) (`clm_1b217440dacbc54f25b051a141bd391269c41f509d78b4502ada01f572d74bb9`)

## limitations (2 claim(s))

- [observation/documented] The README states the repository is not really active due to limited development time, and that breaking changes may occur. -- evidence: [README.md#L3-L3](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L3-L3) (`clm_1d95211fe73d3f9ae2202c7c28deade8371c39ef89bc2d6a6134b252e8df1ad3`)
- [observation/documented] The program is stated to be checked only for the case of two agents (n_agents=2). -- evidence: [README.md#L3-L3](https://github.com/ismorphism/DeepGame/blob/88e6f8927f9ce3ed9097dc0b1b2818955db127c3/README.md#L3-L3) (`clm_7d7c5d511c5d89b5ec67a6a441bfb9a7f2151e17212c1079239ba57b6a01cd22`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

