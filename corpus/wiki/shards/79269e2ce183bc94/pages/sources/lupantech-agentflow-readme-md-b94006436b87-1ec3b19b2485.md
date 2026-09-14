---
access: public
aliases: []
claim_ids:
- clm_0c073579a3572d7f90ef2abc26c9b7f3b3c18a806c4cbe43066224166ec71027
- clm_30d5094f6ace7a1d006f2fa50d80f19080837a21b961d40eda090845c2057245
- clm_3da260ef8c4540202b27747d56d4fac1c07a1cea8252414cda2259cf9ae6f193
- clm_71942d74c4c349fc05d1162b97c59a539c20a04890ca765a676ae866770c8b88
- clm_880898b67378453100fe46e69d1b56635c62f95343e76a35fc1ea0a1636d513a
- clm_8c0f434b642c33f5284995265e6220fb41fbac86ebd94f65cf1c101486b9e01e
- clm_9f6ae7e8290f658915aa7aa059193456a2e18965bf07165ddf93ebe88fbaffea
- clm_a0f181cb5a91c0c9c24b5404a882ebc9dbfd4badb3f18d0875eb92642ef9045b
- clm_b91fb7842463f8d814824923cd22e5681880815f51f4b62374e37ffa89582a97
- clm_c94778b70c907e6eb92cd6b7b441b04c50f6ad37c1259c0194575e6c54cb75e5
- clm_d3915e82997e25fadc3713fdee858f69ece2ed4f7caf9e09ee5a858f7f8a6099
- clm_fb22f6c4cb5b292623cd525bc340d9622601fe403b3bc317e69d5b8e53a42d9e
maturity: draft
page_id: pg_6e9ffb3ef7aa5c57bf591ec3b19b2485
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_228b920afb3f53da8fb99e7fee5afc51
title: lupantech/AgentFlow/README.md @ b94006436b87
updated_at: '2026-09-14T02:14:55Z'
---

# lupantech/AgentFlow/README.md @ b94006436b87

<!-- rcw:begin owner=source:src_228b920afb3f53da8fb99e7fee5afc51 block=evidence -->
- Repository development practice: Flow-GRPO training uses a mixed dataset of Natural Questions and DeepMath-103K, prepared with data scripts, and runs via tmux scripts with hyperparameters in train/config.yaml. [@claim:clm_0c073579a3572d7f90ef2abc26c9b7f3b3c18a806c4cbe43066224166ec71027]
- Benchmark runs (e.g., Bamboogle) produce per-task folders with evaluation data, execution logs, generated answers, and final score logs; a trained 7B Flow-GRPO planner is served with vLLM for evaluation. [@claim:clm_30d5094f6ace7a1d006f2fa50d80f19080837a21b961d40eda090845c2057245]
- The README reports that AgentFlow with a Qwen-2.5-7B backbone outperforms top baselines on 10 benchmarks (+14.9% search, +14.0% agentic, +14.5% math, +4.1% science), reportedly surpassing GPT-4o. [@claim:clm_3da260ef8c4540202b27747d56d4fac1c07a1cea8252414cda2259cf9ae6f193]
- The four agent modules coordinate via evolving memory and integrated tools across multiple turns. [@claim:clm_71942d74c4c349fc05d1162b97c59a539c20a04890ca765a676ae866770c8b88]
- Inference can be run via quick_start.py, which reports reasoning steps such as query analysis, action prediction, and command execution before producing an answer. [@claim:clm_880898b67378453100fe46e69d1b56635c62f95343e76a35fc1ea0a1636d513a]
- The system integrates multiple tools including base_generator, python_coder, google_search, wikipedia_search, and web_search. [@claim:clm_8c0f434b642c33f5284995265e6220fb41fbac86ebd94f65cf1c101486b9e01e]
- Repository development practice: before running, users are recommended to verify API keys and environment using provided tool-test and LLM-engine-test scripts. [@claim:clm_9f6ae7e8290f658915aa7aa059193456a2e18965bf07165ddf93ebe88fbaffea]
- Setup recommends Python 3.11, installation via setup.sh, and API keys (OpenAI, Google, optionally DashScope or Together) configured in agentflow/.env. [@claim:clm_a0f181cb5a91c0c9c24b5404a882ebc9dbfd4badb3f18d0875eb92642ef9045b]
- The framework optimizes the planner agent within the system online using Flow-based Group Refined Policy Optimization (Flow-GRPO), rather than training a single LLM to interleave reasoning and tool calls. [@claim:clm_b91fb7842463f8d814824923cd22e5681880815f51f4b62374e37ffa89582a97]
- Repository development practice: contributors are invited to open issues or submit pull requests, contact maintainers by email, or join the project's Slack community. [@claim:clm_c94778b70c907e6eb92cd6b7b441b04c50f6ad37c1259c0194575e6c54cb75e5]
- Each agent module can use a different LLM engine; the planner's engine is set via llm_engine_name in run scripts, while Executor/Verifier/Generator default to Qwen-2.5-7B-Instruct via DashScope and can be changed in code. [@claim:clm_d3915e82997e25fadc3713fdee858f69ece2ed4f7caf9e09ee5a858f7f8a6099]
- AgentFlow is a modular agentic system with four specialized modules: Planner, Executor, Verifier, and Generator. [@claim:clm_fb22f6c4cb5b292623cd525bc340d9622601fe403b3bc317e69d5b8e53a42d9e]
<!-- rcw:end owner=source:src_228b920afb3f53da8fb99e7fee5afc51 block=evidence -->

## Researcher notes

