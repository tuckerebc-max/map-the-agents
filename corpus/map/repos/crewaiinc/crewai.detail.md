# crewaiinc/crewai -- full detail

[Back to orientation](crewai.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/crewaiinc/crewai/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/0d6e6df1020dcd85.json](../../../wiki/dossiers/crewaiinc/crewai/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/0d6e6df1020dcd85.json)

## specifications (3 claim(s))

- [observation/documented] CrewAI is described as an open-source Python framework for building production-ready multi-agent workflows, offering high-level abstractions and low-level APIs. -- evidence: [README.md#L58-L59](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L58-L59) (`clm_547d5ffd99603491b04822d28ed05a9864625bceff62796157215f3c87437a84`)
- [observation/documented] CrewAI requires Python >=3.10 and <3.14 and uses UV for dependency management and package handling. -- evidence: [README.md#L196-L196](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L196-L196), [README.md#L202-L202](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L202-L202) (`clm_19d08e2c552f04f4199c9d1b3b1af51239598a765197c56af54170f4b55ea0d6`)
- [observation/documented] CrewAI is released under the MIT License. -- evidence: [README.md#L623-L623](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L623-L623) (`clm_4446b21208139668fc79b7f5953ad05100af2274e6e633ad3e7b6127c4e00849`)

## components (1 claim(s))

- [observation/documented] New crew projects are JSON-first: agents live in `agents/*.jsonc`, tasks and crew settings in `crew.jsonc`, with optional `knowledge/`, `skills/`, and `tools/` directories; a `--classic` flag yields the older Python/YAML scaffold. -- evidence: [README.md#L261-L261](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L261-L261), [README.md#L283-L283](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L283-L283), [README.md#L269-L281](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L269-L281), [README.md#L285-L287](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L285-L287) (`clm_572b5baf15d504d8047314be4a3e15cc7dda6987d2d171a61d2fb29e59cbf374`)

## design-choices (1 claim(s))

- [observation/documented] The framework offers two complementary models: Crews for autonomous, role-based agent collaboration, and Flows for event-driven workflows with precise control and state management. -- evidence: [README.md#L681-L681](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L681-L681), [README.md#L176-L176](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L176-L176), [README.md#L169-L169](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L169-L169), [README.md#L61-L62](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L61-L62) (`clm_fc424d5b361c131f420177957ffd52d65d1d9aac2a3625c80d23682269d5064c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run `uv sync --all-groups --all-extras`, install pre-commit hooks, run tests with `uv run pytest lib/crewai/tests/ -x -q`, and type-check with `uv run mypy lib/`. -- evidence: [README.md#L562-L567](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L562-L567), [README.md#L574-L575](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L574-L575), [README.md#L571-L571](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L571-L571) (`clm_60f51d9f110e62fbc9c8690d12adcebf09db8f54e746c97763183e00c7bd49cd`)
- [observation/documented] Repository development practice: docs under `docs/edge/` publish immediately under the Edge version selector and are frozen into immutable `docs/v<X.Y.Z>/` snapshots at release; CI rejects PRs modifying frozen snapshots without a `[docs-freeze]` title prefix. -- evidence: [README.md#L579-L588](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L579-L588) (`clm_460eb4147f005ea5fada7b5c716fb955b83414be81d37414ca049bb1c5f3df96`)

## skills-patterns (1 claim(s))

- [observation/documented] Official CrewAI Skills can be installed for AI coding agents (Claude Code plugins or `npx skills add crewaiinc/skills`), covering scaffolding, agent/task design, and a docs MCP query skill. -- evidence: [README.md#L134-L134](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L134-L134), [README.md#L122-L127](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L122-L127), [README.md#L129-L132](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L129-L132), [README.md#L114-L120](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L114-L120) (`clm_afb20134f481ac65142dedc12fb34a5403bc8602803f2a017450db8a699ae8f2`)

## interfaces (3 claim(s))

- [observation/documented] Flows support logical operators `or_` and `and_` combined with `@start`, `@listen`, and `@router` decorators to build complex triggering conditions and conditional routing. -- evidence: [README.md#L499-L506](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L499-L506), [README.md#L442-L443](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L442-L443), [README.md#L523-L527](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L523-L527), [README.md#L439-L440](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L439-L440) (`clm_ac0e5de89c6df646b1aa89bf69d8a184284c89c1c0497df48862d96b06c900de`)
- [observation/documented] The CrewAI CLI supports `crewai create crew <name>`, `crewai install`, and `crewai run`, and is installed via `uv tool install crewai`. -- evidence: [README.md#L661-L663](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L661-L663), [README.md#L263-L265](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L263-L265), [README.md#L226-L228](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L226-L228), [README.md#L665-L665](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L665-L665), [README.md#L379-L382](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L379-L382) (`clm_8945b7f141571b2c906f1ad0cfaecacdcaf29f4ff5117ae64a8f36100f1cddfd`)
- [observation/documented] Agent JSONC definitions specify role, goal, backstory, LLM, and tools; `{placeholder}` values in agent/task text are filled from `inputs` defaults in `crew.jsonc`, with the CLI prompting for missing values at run time. -- evidence: [README.md#L293-L297](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L293-L297), [README.md#L299-L299](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L299-L299), [README.md#L312-L323](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L312-L323) (`clm_0ac9b9ac6a2ce5213b29f7c2a42436a12453107d9814508371f3cf47b4b765f9`)

## memory-state (1 claim(s))

- [observation/documented] Flows provide secure, consistent state management between tasks; the documented example defines typed Pydantic state (e.g., sentiment, confidence) on a Flow subclass. -- evidence: [README.md#L458-L463](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L458-L463), [README.md#L453-L456](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L453-L456), [README.md#L178-L181](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L178-L181) (`clm_1814b3aea8dd6a4b762395e078e36e7396b50c4c78878d1f118f79a4641df959`)

## orchestration (1 claim(s))

- [observation/documented] Besides a sequential process, CrewAI supports a hierarchical process that automatically assigns a manager agent to coordinate task planning and execution via delegation and result validation. -- evidence: [README.md#L388-L388](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L388-L388) (`clm_d4305e2bcd95c57f79f202607b3871be4ba278ce054de397fe929f95e954cdfc`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents can integrate with external tools, APIs, and databases, and the framework advertises tools, memory, knowledge, checkpointing, async execution, and MCP/A2A support. -- evidence: [README.md#L396-L402](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L396-L402), [README.md#L717-L717](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L717-L717) (`clm_88c173fdb4c59b5275762327f2df36bf6837cb5ea088528467340a998d3e88f5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] By default agents use the OpenAI API for model queries; other connections such as local models via Ollama and LM Studio are supported, and custom-trained or fine-tuned models can be integrated. -- evidence: [README.md#L677-L677](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L677-L677), [README.md#L713-L713](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L713-L713), [README.md#L538-L538](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L538-L538) (`clm_d0cd35e632df5fd84c5f0f9f20d85c1c61eac9afc63cdf429f67c0cc98f6e6d7`)
- [observation/documented] CrewAI collects anonymous telemetry (versions, OS, agent/task counts, process type, LLM used, tool names); prompts, task descriptions, and API responses are not collected unless `share_crew` is enabled, and telemetry can be disabled via OTEL_SDK_DISABLED=true. -- evidence: [README.md#L594-L594](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L594-L594), [README.md#L598-L617](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L598-L617), [README.md#L592-L592](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L592-L592) (`clm_fed0ede4f1461c9e8269e351001917126b9ee389b6d1a46b360b4b06484ea31c`)

## limitations (1 claim(s))

- [observation/documented] On Windows, a chroma-hnswlib==0.7.6 build error (missing float.h) can occur, requiring Visual Studio Build Tools with Desktop development with C++ to resolve. -- evidence: [README.md#L236-L236](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L236-L236) (`clm_ac9d19ec0edbee656154429592172e990d413fd95c52758dc30e2033864c8629`)

## relevance (1 claim(s))

- [observation/documented] CrewAI is positioned for multi-step work needing specialized agents, tool use, structured outputs, human review, and workflows combining autonomous reasoning with explicit business logic. -- evidence: [README.md#L544-L544](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L544-L544), [README.md#L548-L552](https://github.com/crewAIInc/crewAI/blob/894898f84c4ac0a89f24bf7bee6c381eb0e67f51/README.md#L548-L552) (`clm_8317081bce5f36199ecbbba2fc62a3afbb2a4b9160a0f9a0a541f777f8fc9116`)

