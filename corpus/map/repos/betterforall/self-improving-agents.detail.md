# betterforall/self-improving-agents -- full detail

[Back to orientation](self-improving-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/betterforall/self-improving-agents/5f7823732d87c515ed7842d06bc3c2613ed0445b/2ffba66f8aa5de4e.json](../../../wiki/dossiers/betterforall/self-improving-agents/5f7823732d87c515ed7842d06bc3c2613ed0445b/2ffba66f8aa5de4e.json)

## specifications (1 claim(s))

- [observation/documented] The project defines four levels of self-improving code agents, each adding one key idea, from a simple improvement loop to an adversarial arena with self-modifying agents. -- evidence: [README.md#L3-L4](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L3-L4) (`clm_d6243040169d98da0b1a5c247c38910c14cfafcc6aae1dd1964d5d642b725f36`)

## components (5 claim(s))

- [observation/documented] Level 1 (autoresearch/) is a single-agent loop: the LLM proposes code, it is written to a file, benchmarked, kept if better, and repeated; bad proposals revert immediately. -- evidence: [README.md#L138-L141](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L138-L141), [README.md#L134-L136](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L134-L136), [README.md#L132-L132](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L132-L132) (`clm_546ec871b016f409478943efd740748638af2072056e095487e4d61ed4559723`)
- [observation/documented] Level 2 (feedback-loop/) adds a reviewer agent that returns structured feedback (issue type, severity, fix suggestion, confidence, detected pattern) explaining why a solution failed. -- evidence: [README.md#L151-L159](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L151-L159), [README.md#L147-L147](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L147-L147) (`clm_0bc4802f7de30dd2f1cdd9662f3ed9ad003e6045e5b7e2ae88212abf3bb15ed4`)
- [observation/documented] Level 3 (hyperagent/) has a meta-agent that rewrites the source of task_agent.py and meta_agent.py, with an immutable seed/ reference, live agent_code/ copies, and versioned generations/ snapshots. -- evidence: [README.md#L171-L173](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L171-L173), [README.md#L175-L179](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L175-L179) (`clm_0825d9b0e8687c769216166fdb299714053fdfa155db7ea5471ed8e3bd11ae10`)
- [observation/documented] HyperAgent rewrites are validated by a three-stage crash recovery: compile check, import check, and signature check; invalid rewrites revert to the last valid generation. -- evidence: [README.md#L185-L188](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L185-L188), [README.md#L190-L191](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L190-L191) (`clm_3635219370eec55e0ecfdf9529f5a9c497b299772a7a475768c7e546ca20e66d`)
- [observation/documented] Level 4a (Arena Single) pits one code agent against one test agent in adversarial co-evolution without tournament or population dynamics; 4b adds tournament selection where the worst agents are replaced by mutated winners. -- evidence: [README.md#L200-L201](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L200-L201), [README.md#L223-L225](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L223-L225) (`clm_450b80a4589363c19dd28eee16b4c76a2f440bdb97fc4839cbc23a350792ed18`)

## design-choices (3 claim(s))

- [observation/documented] Level 2 uses asymmetric information: the worker gets a small prompt with just the code, while the reviewer sees full history and prior feedback to spot cross-iteration patterns. -- evidence: [README.md#L165-L165](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L165-L165), [README.md#L161-L163](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L161-L163) (`clm_51e11ff704badfb13491898d069d20db68b7748c442be796ec5e95428f9bb1f5`)
- [observation/documented] In Arena Loop, code agents are described as mini-HyperAgents that can mutate their own propose() function, so the code-generating code itself evolves. -- evidence: [README.md#L227-L228](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L227-L228) (`clm_bcc5ed44ba5fa941733988366c022b83dfc64d30bc8d963ce970b2f3ba2e11f4`)
- [observation/documented] HyperAgent is a simplification of Meta's HyperAgents (DGM-H): it uses folder-based versioning instead of Docker containers. -- evidence: [README.md#L193-L194](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L193-L194) (`clm_435cbe12a8f0f615010d13bb0e01d8342346e3d50f66b48033a15e25253f3544`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Each level is run via a run.py entry point (e.g. python autoresearch/run.py) with a --task flag selecting tasks such as snake, support, or email_validation. -- evidence: [README.md#L83-L86](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L83-L86), [README.md#L89-L91](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L89-L91) (`clm_19a0eee0ba107a0ddb18d99ad3f27112b746e4c3976f1ca7935d4aba9006bc96`)
- [observation/documented] run_all.py runs experiments across all levels and generates comparison analysis, supporting --levels/--tasks filters and a --fresh flag to ignore previous results; analyze_results.py performs cross-level comparison after experiments are done. -- evidence: [README.md#L100-L101](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L100-L101), [README.md#L104-L105](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L104-L105), [README.md#L97-L97](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L97-L97) (`clm_1df0d851293d033a7673e0ce3e0f918a93633f344ead8594917281c1655e7ac7`)
- [observation/documented] The framework is task-agnostic: a new task is a folder in tasks/ with config.py (task name, metric, direction, prompt builder), initial_solution.py, and a benchmark.py that prints 'metric_name:value' to stdout. -- evidence: [README.md#L250-L255](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L250-L255), [README.md#L257-L262](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L257-L262), [README.md#L248-L248](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L248-L248), [README.md#L272-L272](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L272-L272) (`clm_709413796f564831061a919454bea05436e47a82627baf60c852b71846519bfe`)

## memory-state (1 claim(s))

- [observation/documented] All levels share tasks/checkpoint.py for resumable checkpointing using sequence-numbered JSON files with atomic writes (write to .tmp then os.replace), keeping only the last three checkpoints. -- evidence: [README.md#L332-L336](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L332-L336) (`clm_b2959b1a14e2b33efbbaeed7e88caecdb96af78e57a504f170a30b79db7e4b87`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (3 claim(s))

- [observation/documented] Experiments used Gemini 2.5 Flash across five levels and three tasks (email_validation, snake, support) in 15 total experiments, with per-level metrics, costs, and token counts reported. -- evidence: [experiment-results.md#L14-L30](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L14-L30), [experiment-results.md#L7-L10](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L7-L10) (`clm_70559fc3ab565d228764941c42db1cffbaba2f0a46ec4681726845199516f74a`)
- [observation/documented] Cross-validation shows Levels 1-3 scored 90-100% on email_validation's original 20 tests but dropped to 62-66% on the expanded 50-case adversarial suite, while Arena levels held at 70% on the combined suite. -- evidence: [experiment-results.md#L140-L143](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L140-L143), [experiment-results.md#L129-L136](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L129-L136), [experiment-results.md#L219-L219](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L219-L219) (`clm_3463f9d610c8dc6a766bad608c5e5a04d9fb7385a2b98eb27059e7a33a4d5930`)
- [observation/documented] For support, rubric-based boolean scoring (keyword match plus LLM YES/NO fallback) reduced judge noise from over 30 points to under 7; Feedback Loop scored highest (82.091) on the expanded 19 questions. -- evidence: [experiment-results.md#L151-L158](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L151-L158), [experiment-results.md#L106-L107](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L106-L107), [experiment-results.md#L160-L161](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L160-L161) (`clm_9330320c5a646097cdfdf3a2af2509ded50ce4fea9819d67d6d57cf4b7fb9cdf`)

## dependencies (1 claim(s))

- [observation/documented] Setup requires installing requirements.txt via pip and creating a .env file in the repo root containing a GEMINI_API_KEY obtained from Google AI Studio. -- evidence: [README.md#L67-L69](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L67-L69), [README.md#L71-L71](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L71-L71), [README.md#L73-L75](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L73-L75) (`clm_37d669749a1aa9d659d22f1371bb6089d098315e785f42762f5910572a1b24f8`)

## limitations (1 claim(s))

- [observation/documented] The results document acknowledges single runs per experiment (N=1, no error bars), a small task set of three tasks, and a single model (Gemini 2.5 Flash), so findings may not generalize. -- evidence: [experiment-results.md#L187-L191](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/experiment-results.md#L187-L191) (`clm_ef49a4f6948d2520039c9289c30bd8c1cf483950fa1fce48b69798b9031e3fd3`)

## relevance (1 claim(s))

- [observation/documented] The project frames itself as independent research comparing existing self-improving code-agent approaches and proposing new ones, with lineage traced to AlphaGo/RLVR, AutoResearch, HyperAgents, and GAN-style co-evolution. -- evidence: [README.md#L6-L7](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L6-L7), [README.md#L350-L355](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L350-L355), [README.md#L342-L344](https://github.com/BetterForAll/self-improving-agents/blob/5f7823732d87c515ed7842d06bc3c2613ed0445b/README.md#L342-L344) (`clm_df7163e766e5e41ca37312726e33c4ac886d4ea4c7f407019df11cf2007853c7`)

