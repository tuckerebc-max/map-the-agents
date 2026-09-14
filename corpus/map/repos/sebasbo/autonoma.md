# sebasbo/autonoma

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9e49c95fafe0 @ be36f55d59f6abe7

## Summary (orientation draft, not independently verified)

The snapshot contains only the readme of Autonoma, a Python package that uses LLM-driven multi-agent orchestration (PlannerAgent, CoderAgent, Tester) to analyze, modify, and test codebases. All claims below are documentation-based; no source code is present in the evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Autonoma is described as a Python package that uses AI/language models to analyze and modify codebases, verifying changes through automated testing. -- evidence: [readme.md#L3-L3](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The system comprises a PlannerAgent that plans tasks from a user query, a CoderAgent that generates/modifies code, a Tester that runs tests, and Pydantic models for entities like Project, Task, and CodeFile. -- evidence: [readme.md#L102-L106](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L102-L106)
- design-choices (2 claim(s)):
  - [observation/documented] CoderAgent takes a style_guide parameter defaulting to "pep8", and Tester takes a test_framework parameter defaulting to "unittest". -- evidence: [readme.md#L191-L194](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L191-L194), [readme.md#L175-L178](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L175-L178)
  - [observation/documented] The implementation reportedly uses Pydantic for data validation, asynchronous operations for agent coordination, prompt engineering for LLM interaction, and static analysis with AST manipulation for code insights. -- evidence: [readme.md#L38-L42](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L38-L42)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to fork the repo, create a branch, write code and tests, ensure all tests pass by running pytest, and submit a pull request, with details in CONTRIBUTING.md. -- evidence: [readme.md#L278-L282](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L278-L282), [readme.md#L284-L284](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L284-L284)
- skills-patterns (1 claim(s)):
  - [observation/documented] The readme documents an extensible architecture allowing custom agents and tasks, with a Task model supporting fields like task_type, file_paths, and estimated_complexity. -- evidence: [readme.md#L23-L27](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L23-L27), [readme.md#L116-L122](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L116-L122)
- interfaces (3 claim(s)):
  - [observation/documented] AutonomaAgent exposes process_query(query, code_base) returning FinalResult, execute_project(project, code_base) returning ProjectResult, and execute_task(task, agent, codebase) returning TaskResult. -- evidence: [readme.md#L154-L156](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L154-L156), [readme.md#L151-L152](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L151-L152), [readme.md#L148-L149](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L148-L149)
  - [observation/documented] AutonomaAgent's constructor accepts an LLM interface plus optional PlannerAgent, CoderAgent, and Tester instances, allowing component substitution. -- evidence: [readme.md#L142-L146](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L142-L146)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The readme describes a multi-agent system where specialized agents operate asynchronously within an event-driven architecture and collaborate iteratively to generate, refactor, and test code. -- evidence: [readme.md#L36-L36](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L36-L36), [readme.md#L34-L34](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L34-L34)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package is installed via pip (pip install autonoma) and depends on Pydantic for its data models; the LLM interface itself is supplied by the user. -- evidence: [readme.md#L58-L61](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L58-L61), [readme.md#L38-L42](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L38-L42), [readme.md#L50-L52](https://github.com/Sebasbo/Autonoma/blob/9e49c95fafe0b1848e596ea8242fc24fd98d0f3b/readme.md#L50-L52)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](autonoma.detail.md)

Metadata and full claim list: [full detail](autonoma.detail.md)
Human notes ([notes](autonoma.notes.md), never overwritten by build)

[Back to map index](../../index.md)
