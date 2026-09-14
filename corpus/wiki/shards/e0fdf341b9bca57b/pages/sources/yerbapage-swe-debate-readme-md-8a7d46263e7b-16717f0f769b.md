---
access: public
aliases: []
claim_ids:
- clm_17091cf4874fbaa403f699dfbf47b791be7c412338b90a295486e329a1e40704
- clm_4dde719c4211c3530e92467b9bca3ff5c51956f87e983a6408cbe24d08c06255
- clm_5d9d2a83c5ab7d890160aee287c445b3e23036c6ec21d136c884b69cad8d89b0
- clm_6620062f79d27f9edbb7fa2391588145c8dbaff3e912e97f2fe6515c9408efc8
- clm_69bc5ec94c149224c341c6834c49dbea67906714df56c83a66e6806acc9bdff0
- clm_6aee5d31a8ed678a7ea6e77c7146f3032dfba56f3fefd32ac8f530a4ecf31185
- clm_8035ea9deabf7ce2557cf6d84d427458fda970e6a06f90baf0cf9e89290425ba
- clm_8996364c8eadf65410f6ada7d2ed5afbe39d4464b1184f7f7a688669de4995d4
- clm_cf75ef3889b0913764634c28bba112c8d81cf7ff6851ba075f50c4004f84dceb
- clm_d37382d2995290346c0126a641ec7da8b6a7c3f58311b893f995f4970659d40a
- clm_e9105be3010d31a2f0f55e06335070133fbddaf3b44be1a834602e2cff3c544e
maturity: draft
page_id: pg_fac70561c8125d9dae5516717f0f769b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_befae1d8e55f5e9f9c115f1095ce15ed
title: YerbaPage/SWE-Debate/README.md @ 8a7d46263e7b
updated_at: '2026-09-14T03:26:05Z'
---

# YerbaPage/SWE-Debate/README.md @ 8a7d46263e7b

<!-- rcw:begin owner=source:src_befae1d8e55f5e9f9c115f1095ce15ed block=evidence -->
- Installation involves pip installing requirements from localization/requirements.txt plus the moatless-tree-search package. [@claim:clm_17091cf4874fbaa403f699dfbf47b791be7c412338b90a295486e329a1e40704]
- The EntityLocalizationPipeline is configured with a model name and max_depth, and run via run_pipeline taking instance data, a file context, and max_initial_entities. [@claim:clm_4dde719c4211c3530e92467b9bca3ff5c51956f87e983a6408cbe24d08c06255]
- Setup workflow: clone the project, install dependencies, then copy .env.example to .env and set OPENAI_API_KEY and optionally OPENAI_BASE_URL. [@claim:clm_5d9d2a83c5ab7d890160aee287c445b3e23036c6ec21d136c884b69cad8d89b0]
- The example uses four deepseek-chat completion models with distinct temperatures (0.7, 0.7, 1, 0.2) for ReAct, discriminator, and value roles, all set to REACT response format. [@claim:clm_6620062f79d27f9edbb7fa2391588145c8dbaff3e912e97f2fe6515c9408efc8]
- SWE-Debate is described as a competitive multi-agent debate framework for software issue resolution that uses graph-guided localization and structured debate. [@claim:clm_69bc5ec94c149224c341c6834c49dbea67906714df56c83a66e6806acc9bdff0]
- The project includes an Entity Localization Pipeline built on the Moatless framework. [@claim:clm_6aee5d31a8ed678a7ea6e77c7146f3032dfba56f3fefd32ac8f530a4ecf31185]
- Documented features include entity extraction from issue descriptions, graph-driven search over code dependencies, localization chain generation, multi-agent debate, and automated solution-plan generation. [@claim:clm_8035ea9deabf7ce2557cf6d84d427458fda970e6a06f90baf0cf9e89290425ba]
- Search trajectories are persisted to a per-instance JSON file under a trajectory directory keyed by instance ID and date. [@claim:clm_8996364c8eadf65410f6ada7d2ed5afbe39d4464b1184f7f7a688669de4995d4]
- The example MCTS flow uses a SearchTree with a CodingAgent, ValueFunction, AgentDiscriminator (5 agents, 3 rounds), and a FeedbackAgent, with limits on depth, iterations, and expansions. [@claim:clm_cf75ef3889b0913764634c28bba112c8d81cf7ff6851ba075f50c4004f84dceb]
- The project builds on and credits LocAgent for automated code localization, and links to Moatless Framework and SWE-bench as related resources. [@claim:clm_d37382d2995290346c0126a641ec7da8b6a7c3f58311b893f995f4970659d40a]
- The project requires Python 3.12+ and an OpenAI API key or an LLM API compatible with the OpenAI format. [@claim:clm_e9105be3010d31a2f0f55e06335070133fbddaf3b44be1a834602e2cff3c544e]
<!-- rcw:end owner=source:src_befae1d8e55f5e9f9c115f1095ce15ed block=evidence -->

## Researcher notes

