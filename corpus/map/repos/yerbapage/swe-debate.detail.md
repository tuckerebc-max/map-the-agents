# yerbapage/swe-debate -- full detail

[Back to orientation](swe-debate.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yerbapage/swe-debate/8a7d46263e7bea4cd6563c19166b7592ac386b13/10d5332ff95b9469.json](../../../wiki/dossiers/yerbapage/swe-debate/8a7d46263e7bea4cd6563c19166b7592ac386b13/10d5332ff95b9469.json)

## specifications (1 claim(s))

- [observation/documented] SWE-Debate is described as a competitive multi-agent debate framework for software issue resolution that uses graph-guided localization and structured debate. -- evidence: [README.md#L7-L7](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L7-L7) (`clm_69bc5ec94c149224c341c6834c49dbea67906714df56c83a66e6806acc9bdff0`)

## components (2 claim(s))

- [observation/documented] The project includes an Entity Localization Pipeline built on the Moatless framework. -- evidence: [README.md#L11-L11](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L11-L11) (`clm_6aee5d31a8ed678a7ea6e77c7146f3032dfba56f3fefd32ac8f530a4ecf31185`)
- [observation/documented] Documented features include entity extraction from issue descriptions, graph-driven search over code dependencies, localization chain generation, multi-agent debate, and automated solution-plan generation. -- evidence: [README.md#L13-L17](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L13-L17) (`clm_8035ea9deabf7ce2557cf6d84d427458fda970e6a06f90baf0cf9e89290425ba`)

## design-choices (1 claim(s))

- [observation/documented] The example uses four deepseek-chat completion models with distinct temperatures (0.7, 0.7, 1, 0.2) for ReAct, discriminator, and value roles, all set to REACT response format. -- evidence: [README.md#L84-L87](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L84-L87), [README.md#L78-L82](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L78-L82) (`clm_6620062f79d27f9edbb7fa2391588145c8dbaff3e912e97f2fe6515c9408efc8`)

## workflows (1 claim(s))

- [observation/documented] Setup workflow: clone the project, install dependencies, then copy .env.example to .env and set OPENAI_API_KEY and optionally OPENAI_BASE_URL. -- evidence: [README.md#L50-L50](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L50-L50), [README.md#L36-L36](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L36-L36), [README.md#L53-L55](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L53-L55) (`clm_5d9d2a83c5ab7d890160aee287c445b3e23036c6ec21d136c884b69cad8d89b0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The EntityLocalizationPipeline is configured with a model name and max_depth, and run via run_pipeline taking instance data, a file context, and max_initial_entities. -- evidence: [README.md#L60-L61](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L60-L61), [README.md#L64-L67](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L64-L67), [README.md#L70-L75](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L70-L75) (`clm_4dde719c4211c3530e92467b9bca3ff5c51956f87e983a6408cbe24d08c06255`)

## memory-state (1 claim(s))

- [observation/documented] Search trajectories are persisted to a per-instance JSON file under a trajectory directory keyed by instance ID and date. -- evidence: [README.md#L99-L101](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L99-L101), [README.md#L142-L157](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L142-L157) (`clm_8996364c8eadf65410f6ada7d2ed5afbe39d4464b1184f7f7a688669de4995d4`)

## orchestration (1 claim(s))

- [observation/documented] The example MCTS flow uses a SearchTree with a CodingAgent, ValueFunction, AgentDiscriminator (5 agents, 3 rounds), and a FeedbackAgent, with limits on depth, iterations, and expansions. -- evidence: [README.md#L103-L113](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L103-L113), [README.md#L125-L129](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L125-L129), [README.md#L123-L123](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L123-L123), [README.md#L142-L157](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L142-L157), [README.md#L131-L133](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L131-L133) (`clm_cf75ef3889b0913764634c28bba112c8d81cf7ff6851ba075f50c4004f84dceb`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The project requires Python 3.12+ and an OpenAI API key or an LLM API compatible with the OpenAI format. -- evidence: [README.md#L31-L32](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L31-L32) (`clm_e9105be3010d31a2f0f55e06335070133fbddaf3b44be1a834602e2cff3c544e`)
- [observation/documented] Installation involves pip installing requirements from localization/requirements.txt plus the moatless-tree-search package. -- evidence: [README.md#L44-L45](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L44-L45), [README.md#L41-L41](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L41-L41) (`clm_17091cf4874fbaa403f699dfbf47b791be7c412338b90a295486e329a1e40704`)
- [observation/documented] The project builds on and credits LocAgent for automated code localization, and links to Moatless Framework and SWE-bench as related resources. -- evidence: [README.md#L169-L169](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L169-L169), [README.md#L163-L165](https://github.com/YerbaPage/SWE-Debate/blob/8a7d46263e7bea4cd6563c19166b7592ac386b13/README.md#L163-L165) (`clm_d37382d2995290346c0126a641ec7da8b6a7c3f58311b893f995f4970659d40a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

