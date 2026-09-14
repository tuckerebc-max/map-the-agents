---
access: public
aliases: []
claim_ids:
- clm_02f8b14f58cbc5df8576ce9b239b3a1e26d179175e985c4b04abe0f3931ee4b1
- clm_050c310343ee7feae2d43fd1f778d2b11c82a5caab9faf8c22bdcb6b81dec087
- clm_074c88385add766d5003f517a96ddca017cdb3dcdce878615a1a57b6744b42bb
- clm_10f06002b3f2c0c34738394a3662fc1b35e4c1eedeeda44352572bb350b0989a
- clm_2701ceb0f8e858d5699f41f356870853169a7b1d2aa67bb1dfc5d65d367fe851
- clm_2d2c107cf70f9f49db0a2ea0a6983581fb8fa5548bf255c27b70afadbb22c1d0
- clm_552e163742f7f42b3fefc3f90e9dcab93ac1375334f1846f2226ec6aeec6e814
- clm_5895287b01f0cf25aab589d0768ae7766de476164af741eae07fb02e9c0369cf
- clm_6c34f9e6b8a9db29fbafed5c90ac612ebc2abbd3cdbde4a7ee94b35f180552fb
- clm_6ce5bc5b736c28584d71c61550caff11cbfe26da5e1d196ce38cd422795b298f
- clm_7143d829c738f99caab5100fb3ee4c7487c5e22549f8c994cdef5fa4dfb3fdae
- clm_ba9e1793a934b91f5116341ad928df9273094d5e58628edc1a00bb76f3806939
maturity: draft
page_id: pg_5cd877ef707359238617db6f15597b72
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cf80ef25f5e25a2fb927ee4f4c8190a1
title: Danau5tin/tbench-agentic-data-pipeline/README.md @ 4489453eb3c2
updated_at: '2026-09-14T03:43:55Z'
---

# Danau5tin/tbench-agentic-data-pipeline/README.md @ 4489453eb3c2

<!-- rcw:begin owner=source:src_cf80ef25f5e25a2fb927ee4f4c8190a1 block=evidence -->
- Agents use role-specific scripts (e.g. get_task_parameters.py, create_dp.py, approve_datapoint.py) plus shared tools including validate_datapoint.py, patch_dp.py, and patch_additional_files.py. [@claim:clm_02f8b14f58cbc5df8576ce9b239b3a1e26d179175e985c4b04abe0f3931ee4b1]
- The generated datapoints are intended as training data for a separate scalable RL training project for terminal-based coding tasks. [@claim:clm_050c310343ee7feae2d43fd1f778d2b11c82a5caab9faf8c22bdcb6b81dec087]
- Idea generation agents take Terminal Bench seed tasks, generate multiple variations, select the best ideas, and output draft specifications to a shared workspace; refinement criteria are withheld until after brainstorming to maximize creativity. [@claim:clm_074c88385add766d5003f517a96ddca017cdb3dcdce878615a1a57b6744b42bb]
- The Task Manager exposes an API where agents claim tasks by type (e.g. get_next_task with an agent ID and task_types) and complete them with results via complete_task. [@claim:clm_10f06002b3f2c0c34738394a3662fc1b35e4c1eedeeda44352572bb350b0989a]
- Each generated datapoint is a directory containing prompt.md, a dockerfile (Ubuntu 24.04 or similar), tests.py pytest functions, weights.json, and a files/ directory with resources such as broken code and config files. [@claim:clm_2701ceb0f8e858d5699f41f356870853169a7b1d2aa67bb1dfc5d65d367fe851]
- The pipeline runs three specialized agent stages (idea generation, datapoint building, quality review), with agents working independently in parallel and coordinated by a central Task Manager that prevents duplication and handles failures. [@claim:clm_2d2c107cf70f9f49db0a2ea0a6983581fb8fa5548bf255c27b70afadbb22c1d0]
- Quality review agents check datapoints against quality standards, edit and re-validate as needed, categorize them, and either approve with metadata or reject with reasons. [@claim:clm_552e163742f7f42b3fefc3f90e9dcab93ac1375334f1846f2226ec6aeec6e814]
- The reported outcomes (331 validated datapoints, 100% Docker-validated environments, category and technology breakdowns) suggest the pipeline's output quality was measured, though these figures are README-reported rather than harness-verified. [@claim:clm_5895287b01f0cf25aab589d0768ae7766de476164af741eae07fb02e9c0369cf]
- Builder agents turn draft specifications into complete executable datapoints, iterating on a validation script until the Dockerfile builds, tests fail initially, dependencies are present, and test weights sum to 1.0. [@claim:clm_6c34f9e6b8a9db29fbafed5c90ac612ebc2abbd3cdbde4a7ee94b35f180552fb]
- The Task Manager provides atomic task claiming to avoid collisions, automatic timeout recovery, parent-child task tracking, and real-time status monitoring. [@claim:clm_6ce5bc5b736c28584d71c61550caff11cbfe26da5e1d196ce38cd422795b298f]
- Getting-started steps use git clone, 'uv sync' to install dependencies, and an init_seed_tasks.py script pointed at a Terminal Bench tasks path; validation relies on Docker and pytest. [@claim:clm_7143d829c738f99caab5100fb3ee4c7487c5e22549f8c994cdef5fa4dfb3fdae]
- Design rationale given: separate agent types for focus and parallel scaling, a shared filesystem instead of message passing for simplicity and debuggability, and a Task Manager for coordination, failure recovery, and monitoring. [@claim:clm_ba9e1793a934b91f5116341ad928df9273094d5e58628edc1a00bb76f3806939]
<!-- rcw:end owner=source:src_cf80ef25f5e25a2fb927ee4f4c8190a1 block=evidence -->

## Researcher notes

