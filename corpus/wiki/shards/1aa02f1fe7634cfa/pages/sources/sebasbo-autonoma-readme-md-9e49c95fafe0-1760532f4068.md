---
access: public
aliases: []
claim_ids:
- clm_248328965484c7b75c20265f9cea53007130fe8cedd5c88ad1d8ae96c97a1c6e
- clm_4221ecd60be8ec4d9c57ad79f86281b776d2e8270a1fab4ea1ff2ffbed058aea
- clm_5d438569df69b72944bf874e07f2ef137fd80346e84a9f1e3025d4a69cf15d94
- clm_72676a276af48373f560a2ecedcea3e648312712ffe51f781c0deba9546af864
- clm_73751486865ca7858e0adb4dea85bb2dddfd346d9f37add9f1d028a43a985197
- clm_7410540d27bdcb048d5a60131e611a3a4de217344ba48274e6fa8d206bdcca7d
- clm_9bf4f6f82130e4befdd3154005fcce72c83ca96d35c5157b1a9c79f6435f0337
- clm_aae15ac1b3656e659e0b0fec5f5aacb89aec83ef984b83fca920b24ca03d3ac5
- clm_c7908689fbe2a325c1b33e4967554cf13c9f479b1d4bb0cfac4affe8e1edda6a
- clm_c7b559dd7f121c2aa37b74ffd2d14074c26dd2acfbebcbad90341591d2195176
- clm_d345e484196bc35510a64c44fb54462db84daf979e2348524d130b75ab355e58
- clm_dc76ab563050d627e2f815258cefc0e6a623c43d75ddce3f750be80da0133a15
maturity: draft
page_id: pg_8cbec3fd74205b9c88e71760532f4068
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e2270b8ae5ce5a38a2ea92b90fca73e1
title: Sebasbo/Autonoma/readme.md @ 9e49c95fafe0
updated_at: '2026-09-14T02:38:48Z'
---

# Sebasbo/Autonoma/readme.md @ 9e49c95fafe0

<!-- rcw:begin owner=source:src_e2270b8ae5ce5a38a2ea92b90fca73e1 block=evidence -->
- The package is installed via pip (pip install autonoma) and depends on Pydantic for its data models; the LLM interface itself is supplied by the user. [@claim:clm_248328965484c7b75c20265f9cea53007130fe8cedd5c88ad1d8ae96c97a1c6e]
- CoderAgent takes a style_guide parameter defaulting to "pep8", and Tester takes a test_framework parameter defaulting to "unittest". [@claim:clm_4221ecd60be8ec4d9c57ad79f86281b776d2e8270a1fab4ea1ff2ffbed058aea]
- The system comprises a PlannerAgent that plans tasks from a user query, a CoderAgent that generates/modifies code, a Tester that runs tests, and Pydantic models for entities like Project, Task, and CodeFile. [@claim:clm_5d438569df69b72944bf874e07f2ef137fd80346e84a9f1e3025d4a69cf15d94]
- The implementation reportedly uses Pydantic for data validation, asynchronous operations for agent coordination, prompt engineering for LLM interaction, and static analysis with AST manipulation for code insights. [@claim:clm_72676a276af48373f560a2ecedcea3e648312712ffe51f781c0deba9546af864]
- The tool targets developers wanting AI-assisted code modification, from small function changes to large-scale refactoring such as adding type hints and Google-style docstrings across a project. [@claim:clm_73751486865ca7858e0adb4dea85bb2dddfd346d9f37add9f1d028a43a985197]
- The readme describes a multi-agent system where specialized agents operate asynchronously within an event-driven architecture and collaborate iteratively to generate, refactor, and test code. [@claim:clm_7410540d27bdcb048d5a60131e611a3a4de217344ba48274e6fa8d206bdcca7d]
- Autonoma is described as a Python package that uses AI/language models to analyze and modify codebases, verifying changes through automated testing. [@claim:clm_9bf4f6f82130e4befdd3154005fcce72c83ca96d35c5157b1a9c79f6435f0337]
- The readme documents an extensible architecture allowing custom agents and tasks, with a Task model supporting fields like task_type, file_paths, and estimated_complexity. [@claim:clm_aae15ac1b3656e659e0b0fec5f5aacb89aec83ef984b83fca920b24ca03d3ac5]
- Users integrate their own LLM by providing an object with a generate(prompt) -> str method, as shown in the custom LLM integration example. [@claim:clm_c7908689fbe2a325c1b33e4967554cf13c9f479b1d4bb0cfac4affe8e1edda6a]
- AutonomaAgent's constructor accepts an LLM interface plus optional PlannerAgent, CoderAgent, and Tester instances, allowing component substitution. [@claim:clm_c7b559dd7f121c2aa37b74ffd2d14074c26dd2acfbebcbad90341591d2195176]
- AutonomaAgent exposes process_query(query, code_base) returning FinalResult, execute_project(project, code_base) returning ProjectResult, and execute_task(task, agent, codebase) returning TaskResult. [@claim:clm_d345e484196bc35510a64c44fb54462db84daf979e2348524d130b75ab355e58]
- Repository development practice: contributors are told to fork the repo, create a branch, write code and tests, ensure all tests pass by running pytest, and submit a pull request, with details in CONTRIBUTING.md. [@claim:clm_dc76ab563050d627e2f815258cefc0e6a623c43d75ddce3f750be80da0133a15]
<!-- rcw:end owner=source:src_e2270b8ae5ce5a38a2ea92b90fca73e1 block=evidence -->

## Researcher notes

