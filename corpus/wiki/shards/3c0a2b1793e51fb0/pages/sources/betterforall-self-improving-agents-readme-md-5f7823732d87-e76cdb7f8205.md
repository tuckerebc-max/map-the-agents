---
access: public
aliases: []
claim_ids:
- clm_0825d9b0e8687c769216166fdb299714053fdfa155db7ea5471ed8e3bd11ae10
- clm_0bc4802f7de30dd2f1cdd9662f3ed9ad003e6045e5b7e2ae88212abf3bb15ed4
- clm_19a0eee0ba107a0ddb18d99ad3f27112b746e4c3976f1ca7935d4aba9006bc96
- clm_1df0d851293d033a7673e0ce3e0f918a93633f344ead8594917281c1655e7ac7
- clm_3635219370eec55e0ecfdf9529f5a9c497b299772a7a475768c7e546ca20e66d
- clm_37d669749a1aa9d659d22f1371bb6089d098315e785f42762f5910572a1b24f8
- clm_435cbe12a8f0f615010d13bb0e01d8342346e3d50f66b48033a15e25253f3544
- clm_450b80a4589363c19dd28eee16b4c76a2f440bdb97fc4839cbc23a350792ed18
- clm_51e11ff704badfb13491898d069d20db68b7748c442be796ec5e95428f9bb1f5
- clm_546ec871b016f409478943efd740748638af2072056e095487e4d61ed4559723
- clm_709413796f564831061a919454bea05436e47a82627baf60c852b71846519bfe
- clm_b2959b1a14e2b33efbbaeed7e88caecdb96af78e57a504f170a30b79db7e4b87
- clm_bcc5ed44ba5fa941733988366c022b83dfc64d30bc8d963ce970b2f3ba2e11f4
- clm_d6243040169d98da0b1a5c247c38910c14cfafcc6aae1dd1964d5d642b725f36
- clm_df7163e766e5e41ca37312726e33c4ac886d4ea4c7f407019df11cf2007853c7
maturity: draft
page_id: pg_4a8b82f733e15ec58087e76cdb7f8205
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f718246686d85a4fa768db72f9e241cd
title: BetterForAll/self-improving-agents/README.md @ 5f7823732d87
updated_at: '2026-09-14T01:38:01Z'
---

# BetterForAll/self-improving-agents/README.md @ 5f7823732d87

<!-- rcw:begin owner=source:src_f718246686d85a4fa768db72f9e241cd block=evidence -->
- Level 3 (hyperagent/) has a meta-agent that rewrites the source of task_agent.py and meta_agent.py, with an immutable seed/ reference, live agent_code/ copies, and versioned generations/ snapshots. [@claim:clm_0825d9b0e8687c769216166fdb299714053fdfa155db7ea5471ed8e3bd11ae10]
- Level 2 (feedback-loop/) adds a reviewer agent that returns structured feedback (issue type, severity, fix suggestion, confidence, detected pattern) explaining why a solution failed. [@claim:clm_0bc4802f7de30dd2f1cdd9662f3ed9ad003e6045e5b7e2ae88212abf3bb15ed4]
- Each level is run via a run.py entry point (e.g. python autoresearch/run.py) with a --task flag selecting tasks such as snake, support, or email_validation. [@claim:clm_19a0eee0ba107a0ddb18d99ad3f27112b746e4c3976f1ca7935d4aba9006bc96]
- run_all.py runs experiments across all levels and generates comparison analysis, supporting --levels/--tasks filters and a --fresh flag to ignore previous results; analyze_results.py performs cross-level comparison after experiments are done. [@claim:clm_1df0d851293d033a7673e0ce3e0f918a93633f344ead8594917281c1655e7ac7]
- HyperAgent rewrites are validated by a three-stage crash recovery: compile check, import check, and signature check; invalid rewrites revert to the last valid generation. [@claim:clm_3635219370eec55e0ecfdf9529f5a9c497b299772a7a475768c7e546ca20e66d]
- Setup requires installing requirements.txt via pip and creating a .env file in the repo root containing a GEMINI_API_KEY obtained from Google AI Studio. [@claim:clm_37d669749a1aa9d659d22f1371bb6089d098315e785f42762f5910572a1b24f8]
- HyperAgent is a simplification of Meta's HyperAgents (DGM-H): it uses folder-based versioning instead of Docker containers. [@claim:clm_435cbe12a8f0f615010d13bb0e01d8342346e3d50f66b48033a15e25253f3544]
- Level 4a (Arena Single) pits one code agent against one test agent in adversarial co-evolution without tournament or population dynamics; 4b adds tournament selection where the worst agents are replaced by mutated winners. [@claim:clm_450b80a4589363c19dd28eee16b4c76a2f440bdb97fc4839cbc23a350792ed18]
- Level 2 uses asymmetric information: the worker gets a small prompt with just the code, while the reviewer sees full history and prior feedback to spot cross-iteration patterns. [@claim:clm_51e11ff704badfb13491898d069d20db68b7748c442be796ec5e95428f9bb1f5]
- Level 1 (autoresearch/) is a single-agent loop: the LLM proposes code, it is written to a file, benchmarked, kept if better, and repeated; bad proposals revert immediately. [@claim:clm_546ec871b016f409478943efd740748638af2072056e095487e4d61ed4559723]
- The framework is task-agnostic: a new task is a folder in tasks/ with config.py (task name, metric, direction, prompt builder), initial_solution.py, and a benchmark.py that prints 'metric_name:value' to stdout. [@claim:clm_709413796f564831061a919454bea05436e47a82627baf60c852b71846519bfe]
- All levels share tasks/checkpoint.py for resumable checkpointing using sequence-numbered JSON files with atomic writes (write to .tmp then os.replace), keeping only the last three checkpoints. [@claim:clm_b2959b1a14e2b33efbbaeed7e88caecdb96af78e57a504f170a30b79db7e4b87]
- In Arena Loop, code agents are described as mini-HyperAgents that can mutate their own propose() function, so the code-generating code itself evolves. [@claim:clm_bcc5ed44ba5fa941733988366c022b83dfc64d30bc8d963ce970b2f3ba2e11f4]
- The project defines four levels of self-improving code agents, each adding one key idea, from a simple improvement loop to an adversarial arena with self-modifying agents. [@claim:clm_d6243040169d98da0b1a5c247c38910c14cfafcc6aae1dd1964d5d642b725f36]
- The project frames itself as independent research comparing existing self-improving code-agent approaches and proposing new ones, with lineage traced to AlphaGo/RLVR, AutoResearch, HyperAgents, and GAN-style co-evolution. [@claim:clm_df7163e766e5e41ca37312726e33c4ac886d4ea4c7f407019df11cf2007853c7]
<!-- rcw:end owner=source:src_f718246686d85a4fa768db72f9e241cd block=evidence -->

## Researcher notes

