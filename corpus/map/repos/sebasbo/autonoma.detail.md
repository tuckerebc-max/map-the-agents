# sebasbo/autonoma -- full detail

[Back to orientation](autonoma.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sebasbo/autonoma/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/be36f55d59f6abe7.json](../../../wiki/dossiers/sebasbo/autonoma/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/be36f55d59f6abe7.json)

## specifications (1 claim(s))

- [observation/documented] Autonoma is described as a Python package that uses AI/language models to analyze and modify codebases, verifying changes through automated testing. -- evidence: [readme.md#L3-L3](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L3-L3) (`clm_9bf4f6f82130e4befdd3154005fcce72c83ca96d35c5157b1a9c79f6435f0337`)

## components (1 claim(s))

- [observation/documented] The system comprises a PlannerAgent that plans tasks from a user query, a CoderAgent that generates/modifies code, a Tester that runs tests, and Pydantic models for entities like Project, Task, and CodeFile. -- evidence: [readme.md#L102-L106](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L102-L106) (`clm_5d438569df69b72944bf874e07f2ef137fd80346e84a9f1e3025d4a69cf15d94`)

## design-choices (2 claim(s))

- [observation/documented] CoderAgent takes a style_guide parameter defaulting to "pep8", and Tester takes a test_framework parameter defaulting to "unittest". -- evidence: [readme.md#L191-L194](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L191-L194), [readme.md#L175-L178](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L175-L178) (`clm_4221ecd60be8ec4d9c57ad79f86281b776d2e8270a1fab4ea1ff2ffbed058aea`)
- [observation/documented] The implementation reportedly uses Pydantic for data validation, asynchronous operations for agent coordination, prompt engineering for LLM interaction, and static analysis with AST manipulation for code insights. -- evidence: [readme.md#L38-L42](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L38-L42) (`clm_72676a276af48373f560a2ecedcea3e648312712ffe51f781c0deba9546af864`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are told to fork the repo, create a branch, write code and tests, ensure all tests pass by running pytest, and submit a pull request, with details in CONTRIBUTING.md. -- evidence: [readme.md#L278-L282](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L278-L282), [readme.md#L284-L284](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L284-L284) (`clm_dc76ab563050d627e2f815258cefc0e6a623c43d75ddce3f750be80da0133a15`)

## skills-patterns (1 claim(s))

- [observation/documented] The readme documents an extensible architecture allowing custom agents and tasks, with a Task model supporting fields like task_type, file_paths, and estimated_complexity. -- evidence: [readme.md#L23-L27](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L23-L27), [readme.md#L116-L122](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L116-L122) (`clm_aae15ac1b3656e659e0b0fec5f5aacb89aec83ef984b83fca920b24ca03d3ac5`)

## interfaces (3 claim(s))

- [observation/documented] AutonomaAgent exposes process_query(query, code_base) returning FinalResult, execute_project(project, code_base) returning ProjectResult, and execute_task(task, agent, codebase) returning TaskResult. -- evidence: [readme.md#L154-L156](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L154-L156), [readme.md#L151-L152](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L151-L152), [readme.md#L148-L149](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L148-L149) (`clm_d345e484196bc35510a64c44fb54462db84daf979e2348524d130b75ab355e58`)
- [observation/documented] AutonomaAgent's constructor accepts an LLM interface plus optional PlannerAgent, CoderAgent, and Tester instances, allowing component substitution. -- evidence: [readme.md#L142-L146](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L142-L146) (`clm_c7b559dd7f121c2aa37b74ffd2d14074c26dd2acfbebcbad90341591d2195176`)
- [observation/documented] Users integrate their own LLM by providing an object with a generate(prompt) -> str method, as shown in the custom LLM integration example. -- evidence: [readme.md#L223-L224](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L223-L224), [readme.md#L219-L221](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L219-L221) (`clm_c7908689fbe2a325c1b33e4967554cf13c9f479b1d4bb0cfac4affe8e1edda6a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The readme describes a multi-agent system where specialized agents operate asynchronously within an event-driven architecture and collaborate iteratively to generate, refactor, and test code. -- evidence: [readme.md#L36-L36](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L36-L36), [readme.md#L34-L34](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L34-L34) (`clm_7410540d27bdcb048d5a60131e611a3a4de217344ba48274e6fa8d206bdcca7d`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is installed via pip (pip install autonoma) and depends on Pydantic for its data models; the LLM interface itself is supplied by the user. -- evidence: [readme.md#L58-L61](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L58-L61), [readme.md#L38-L42](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L38-L42), [readme.md#L50-L52](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L50-L52) (`clm_248328965484c7b75c20265f9cea53007130fe8cedd5c88ad1d8ae96c97a1c6e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers wanting AI-assisted code modification, from small function changes to large-scale refactoring such as adding type hints and Google-style docstrings across a project. -- evidence: [readme.md#L257-L260](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L257-L260), [readme.md#L56-L56](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L56-L56) (`clm_73751486865ca7858e0adb4dea85bb2dddfd346d9f37add9f1d028a43a985197`)

