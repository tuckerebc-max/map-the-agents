---
access: public
aliases: []
claim_ids:
- clm_1b217440dacbc54f25b051a141bd391269c41f509d78b4502ada01f572d74bb9
- clm_1d95211fe73d3f9ae2202c7c28deade8371c39ef89bc2d6a6134b252e8df1ad3
- clm_4b1b553bd054c3723d0a9cdf15704557f32817f992f35c5189cc3b58b9ab8a36
- clm_61e3202353768dad80642486389778d3d02f0fe28bc34ad4ece26f2726632657
- clm_7d7c5d511c5d89b5ec67a6a441bfb9a7f2151e17212c1079239ba57b6a01cd22
- clm_901eb3f779301a802238c7b77de033a873d1a965e4abe481d16c5c32142f2892
- clm_991f99ad189dc73fce08739833b4136501cf3146af09b80fe527abc4c144ca68
- clm_99a7222cf8ffba50f9169124e4bd36934b5325f2c5731dd47b2eb17b887a0fd4
- clm_f7c7f04d5d3c938471198771e8587a033e2ed2c87604f5cbcb8f5389d84465f7
maturity: draft
page_id: pg_50f7020866bd53c5ac3ed32fb7fe2264
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8e463dd36db05cdf955758c0b8807a08
title: ismorphism/DeepGame/README.md @ 88e6f8927f9c
updated_at: '2026-09-14T03:59:19Z'
---

# ismorphism/DeepGame/README.md @ 88e6f8927f9c

<!-- rcw:begin owner=source:src_8e463dd36db05cdf955758c0b8807a08 block=evidence -->
- Installation involves cloning rllab at a specific commit and pip-installing packages such as joblib, theano, keras, tensorflow, gym, tensorflow_probability, and maci. [@claim:clm_1b217440dacbc54f25b051a141bd391269c41f509d78b4502ada01f572d74bb9]
- The README states the repository is not really active due to limited development time, and that breaking changes may occur. [@claim:clm_1d95211fe73d3f9ae2202c7c28deade8371c39ef89bc2d6a6134b252e8df1ad3]
- The project requires Python 3.6+, Numpy, Nashpy, and Matplotlib, and additionally depends on the mapr2 module from a separate GitHub repository. [@claim:clm_4b1b553bd054c3723d0a9cdf15704557f32817f992f35c5189cc3b58b9ab8a36]
- Default parameter values include grid size 3, gamma 0.95, epsilon 0.5, 1000 iterations, learning rate 0.9, and method 'Q'. [@claim:clm_61e3202353768dad80642486389778d3d02f0fe28bc34ad4ece26f2726632657]
- The program is stated to be checked only for the case of two agents (n_agents=2). [@claim:clm_7d7c5d511c5d89b5ec67a6a441bfb9a7f2151e17212c1079239ba57b6a01cd22]
- DeepGame implements single- and multi-agent learning algorithms, including vanilla Q-learning where each agent behaves optimally per Q-values, and Nash Q-learning aiming for Nash equilibrium. [@claim:clm_901eb3f779301a802238c7b77de033a873d1a965e4abe481d16c5c32142f2892]
- The learning_rate argument is described as applying to the Q-learning method, and the method argument selects between Q-learning and Nash-Q. [@claim:clm_991f99ad189dc73fce08739833b4136501cf3146af09b80fe527abc4c144ca68]
- The program is run via run_grid_game.py, configurable through CLI arguments including grid size, gamma, epsilon, iterations, learning rate, and method selection. [@claim:clm_99a7222cf8ffba50f9169124e4bd36934b5325f2c5731dd47b2eb17b887a0fd4]
- Repository development practice: the README instructs users to run the program with 'python run_grid_game.py' using default parameters, and to adjust hyperparameters via its command-line arguments. [@claim:clm_f7c7f04d5d3c938471198771e8587a033e2ed2c87604f5cbcb8f5389d84465f7]
<!-- rcw:end owner=source:src_8e463dd36db05cdf955758c0b8807a08 block=evidence -->

## Researcher notes

