# danau5tin/tbench-agentic-data-pipeline -- full detail

[Back to orientation](tbench-agentic-data-pipeline.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/danau5tin/tbench-agentic-data-pipeline/4489453eb3c2e395a62a7616565e762664bf8b24/e0d4b0f95d30ce67.json](../../../wiki/dossiers/danau5tin/tbench-agentic-data-pipeline/4489453eb3c2e395a62a7616565e762664bf8b24/e0d4b0f95d30ce67.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] Idea generation agents take Terminal Bench seed tasks, generate multiple variations, select the best ideas, and output draft specifications to a shared workspace; refinement criteria are withheld until after brainstorming to maximize creativity. -- evidence: [README.md#L95-L95](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L95-L95), [README.md#L91-L93](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L91-L93) (`clm_074c88385add766d5003f517a96ddca017cdb3dcdce878615a1a57b6744b42bb`)
- [observation/documented] Builder agents turn draft specifications into complete executable datapoints, iterating on a validation script until the Dockerfile builds, tests fail initially, dependencies are present, and test weights sum to 1.0. -- evidence: [README.md#L102-L106](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L102-L106), [README.md#L98-L100](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L98-L100) (`clm_6c34f9e6b8a9db29fbafed5c90ac612ebc2abbd3cdbde4a7ee94b35f180552fb`)
- [observation/documented] Quality review agents check datapoints against quality standards, edit and re-validate as needed, categorize them, and either approve with metadata or reject with reasons. -- evidence: [README.md#L109-L111](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L109-L111) (`clm_552e163742f7f42b3fefc3f90e9dcab93ac1375334f1846f2226ec6aeec6e814`)
- [observation/documented] Agents use role-specific scripts (e.g. get_task_parameters.py, create_dp.py, approve_datapoint.py) plus shared tools including validate_datapoint.py, patch_dp.py, and patch_additional_files.py. -- evidence: [README.md#L182-L184](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L182-L184), [README.md#L187-L189](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L187-L189) (`clm_02f8b14f58cbc5df8576ce9b239b3a1e26d179175e985c4b04abe0f3931ee4b1`)

## design-choices (1 claim(s))

- [observation/documented] Design rationale given: separate agent types for focus and parallel scaling, a shared filesystem instead of message passing for simplicity and debuggability, and a Task Manager for coordination, failure recovery, and monitoring. -- evidence: [README.md#L227-L229](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L227-L229), [README.md#L232-L234](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L232-L234), [README.md#L222-L224](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L222-L224) (`clm_ba9e1793a934b91f5116341ad928df9273094d5e58628edc1a00bb76f3806939`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Task Manager exposes an API where agents claim tasks by type (e.g. get_next_task with an agent ID and task_types) and complete them with results via complete_task. -- evidence: [README.md#L127-L128](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L127-L128), [README.md#L121-L121](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L121-L121) (`clm_10f06002b3f2c0c34738394a3662fc1b35e4c1eedeeda44352572bb350b0989a`)
- [observation/documented] Each generated datapoint is a directory containing prompt.md, a dockerfile (Ubuntu 24.04 or similar), tests.py pytest functions, weights.json, and a files/ directory with resources such as broken code and config files. -- evidence: [README.md#L142-L151](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L142-L151) (`clm_2701ceb0f8e858d5699f41f356870853169a7b1d2aa67bb1dfc5d65d367fe851`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The pipeline runs three specialized agent stages (idea generation, datapoint building, quality review), with agents working independently in parallel and coordinated by a central Task Manager that prevents duplication and handles failures. -- evidence: [README.md#L45-L45](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L45-L45), [README.md#L51-L51](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L51-L51), [README.md#L47-L49](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L47-L49) (`clm_2d2c107cf70f9f49db0a2ea0a6983581fb8fa5548bf255c27b70afadbb22c1d0`)
- [observation/documented] The Task Manager provides atomic task claiming to avoid collisions, automatic timeout recovery, parent-child task tracking, and real-time status monitoring. -- evidence: [README.md#L130-L134](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L130-L134) (`clm_6ce5bc5b736c28584d71c61550caff11cbfe26da5e1d196ce38cd422795b298f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] The reported outcomes (331 validated datapoints, 100% Docker-validated environments, category and technology breakdowns) suggest the pipeline's output quality was measured, though these figures are README-reported rather than harness-verified. -- evidence: [README.md#L58-L61](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L58-L61), [README.md#L65-L74](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L65-L74), [README.md#L77-L80](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L77-L80) (`clm_5895287b01f0cf25aab589d0768ae7766de476164af741eae07fb02e9c0369cf`)

## dependencies (1 claim(s))

- [observation/documented] Getting-started steps use git clone, 'uv sync' to install dependencies, and an init_seed_tasks.py script pointed at a Terminal Bench tasks path; validation relies on Docker and pytest. -- evidence: [README.md#L197-L198](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L197-L198), [README.md#L159-L163](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L159-L163), [README.md#L204-L204](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L204-L204), [README.md#L201-L201](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L201-L201) (`clm_7143d829c738f99caab5100fb3ee4c7487c5e22549f8c994cdef5fa4dfb3fdae`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The generated datapoints are intended as training data for a separate scalable RL training project for terminal-based coding tasks. -- evidence: [README.md#L3-L3](https://github.com/Danau5tin/tbench-agentic-data-pipeline/blob/4489453eb3c2e395a62a7616565e762664bf8b24/README.md#L3-L3) (`clm_050c310343ee7feae2d43fd1f778d2b11c82a5caab9faf8c22bdcb6b81dec087`)

