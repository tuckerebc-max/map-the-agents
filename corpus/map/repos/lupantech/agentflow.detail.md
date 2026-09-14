# lupantech/agentflow -- full detail

[Back to orientation](agentflow.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lupantech/agentflow/b94006436b8712ab8682846fb0d886a5f174f2d4/185232572fb0fc34.json](../../../wiki/dossiers/lupantech/agentflow/b94006436b8712ab8682846fb0d886a5f174f2d4/185232572fb0fc34.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] AgentFlow is a modular agentic system with four specialized modules: Planner, Executor, Verifier, and Generator. -- evidence: [README.md#L45-L45](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L45-L45), [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70) (`clm_fb22f6c4cb5b292623cd525bc340d9622601fe403b3bc317e69d5b8e53a42d9e`)

## design-choices (1 claim(s))

- [observation/documented] The framework optimizes the planner agent within the system online using Flow-based Group Refined Policy Optimization (Flow-GRPO), rather than training a single LLM to interleave reasoning and tool calls. -- evidence: [README.md#L49-L49](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L49-L49), [README.md#L185-L185](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L185-L185) (`clm_b91fb7842463f8d814824923cd22e5681880815f51f4b62374e37ffa89582a97`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors are invited to open issues or submit pull requests, contact maintainers by email, or join the project's Slack community. -- evidence: [README.md#L372-L372](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L372-L372) (`clm_c94778b70c907e6eb92cd6b7b441b04c50f6ad37c1259c0194575e6c54cb75e5`)
- [observation/documented] Repository development practice: before running, users are recommended to verify API keys and environment using provided tool-test and LLM-engine-test scripts. -- evidence: [README.md#L188-L188](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L188-L188), [README.md#L123-L137](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L123-L137), [README.md#L140-L154](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L140-L154), [README.md#L120-L120](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L120-L120) (`clm_9f6ae7e8290f658915aa7aa059193456a2e18965bf07165ddf93ebe88fbaffea`)
- [observation/documented] Repository development practice: Flow-GRPO training uses a mixed dataset of Natural Questions and DeepMath-103K, prepared with data scripts, and runs via tmux scripts with hyperparameters in train/config.yaml. -- evidence: [README.md#L201-L210](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L201-L210), [README.md#L213-L214](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L213-L214), [README.md#L196-L196](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L196-L196), [README.md#L223-L224](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L223-L224), [README.md#L192-L192](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L192-L192) (`clm_0c073579a3572d7f90ef2abc26c9b7f3b3c18a806c4cbe43066224166ec71027`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Inference can be run via quick_start.py, which reports reasoning steps such as query analysis, action prediction, and command execution before producing an answer. -- evidence: [README.md#L159-L173](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L159-L173) (`clm_880898b67378453100fe46e69d1b56635c62f95343e76a35fc1ea0a1636d513a`)
- [observation/documented] Each agent module can use a different LLM engine; the planner's engine is set via llm_engine_name in run scripts, while Executor/Verifier/Generator default to Qwen-2.5-7B-Instruct via DashScope and can be changed in code. -- evidence: [README.md#L255-L256](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L255-L256), [README.md#L253-L253](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L253-L253), [README.md#L266-L267](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L266-L267), [README.md#L258-L264](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L258-L264) (`clm_d3915e82997e25fadc3713fdee858f69ece2ed4f7caf9e09ee5a858f7f8a6099`)

## memory-state (1 claim(s))

- [observation/documented] The four agent modules coordinate via evolving memory and integrated tools across multiple turns. -- evidence: [README.md#L157-L157](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L157-L157), [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70) (`clm_71942d74c4c349fc05d1162b97c59a539c20a04890ca765a676ae866770c8b88`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The system integrates multiple tools including base_generator, python_coder, google_search, wikipedia_search, and web_search. -- evidence: [README.md#L123-L137](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L123-L137), [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70) (`clm_8c0f434b642c33f5284995265e6220fb41fbac86ebd94f65cf1c101486b9e01e`)

## evaluation (2 claim(s))

- [observation/documented] The README reports that AgentFlow with a Qwen-2.5-7B backbone outperforms top baselines on 10 benchmarks (+14.9% search, +14.0% agentic, +14.5% math, +4.1% science), reportedly surpassing GPT-4o. -- evidence: [README.md#L67-L70](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L67-L70), [README.md#L283-L287](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L283-L287), [README.md#L289-L289](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L289-L289) (`clm_3da260ef8c4540202b27747d56d4fac1c07a1cea8252414cda2259cf9ae6f193`)
- [observation/documented] Benchmark runs (e.g., Bamboogle) produce per-task folders with evaluation data, execution logs, generated answers, and final score logs; a trained 7B Flow-GRPO planner is served with vLLM for evaluation. -- evidence: [README.md#L232-L235](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L232-L235), [README.md#L241-L242](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L241-L242), [README.md#L244-L247](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L244-L247) (`clm_30d5094f6ace7a1d006f2fa50d80f19080837a21b961d40eda090845c2057245`)

## dependencies (1 claim(s))

- [observation/documented] Setup recommends Python 3.11, installation via setup.sh, and API keys (OpenAI, Google, optionally DashScope or Together) configured in agentflow/.env. -- evidence: [README.md#L96-L98](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L96-L98), [README.md#L105-L110](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L105-L110), [README.md#L93-L93](https://github.com/lupantech/AgentFlow/blob/b94006436b8712ab8682846fb0d886a5f174f2d4/README.md#L93-L93) (`clm_a0f181cb5a91c0c9c24b5404a882ebc9dbfd4badb3f18d0875eb92642ef9045b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

