---
access: public
aliases: []
claim_ids:
- clm_0ac9b9ac6a2ce5213b29f7c2a42436a12453107d9814508371f3cf47b4b765f9
- clm_1814b3aea8dd6a4b762395e078e36e7396b50c4c78878d1f118f79a4641df959
- clm_19d08e2c552f04f4199c9d1b3b1af51239598a765197c56af54170f4b55ea0d6
- clm_4446b21208139668fc79b7f5953ad05100af2274e6e633ad3e7b6127c4e00849
- clm_460eb4147f005ea5fada7b5c716fb955b83414be81d37414ca049bb1c5f3df96
- clm_547d5ffd99603491b04822d28ed05a9864625bceff62796157215f3c87437a84
- clm_572b5baf15d504d8047314be4a3e15cc7dda6987d2d171a61d2fb29e59cbf374
- clm_60f51d9f110e62fbc9c8690d12adcebf09db8f54e746c97763183e00c7bd49cd
- clm_8317081bce5f36199ecbbba2fc62a3afbb2a4b9160a0f9a0a541f777f8fc9116
- clm_88c173fdb4c59b5275762327f2df36bf6837cb5ea088528467340a998d3e88f5
- clm_8945b7f141571b2c906f1ad0cfaecacdcaf29f4ff5117ae64a8f36100f1cddfd
- clm_ac0e5de89c6df646b1aa89bf69d8a184284c89c1c0497df48862d96b06c900de
- clm_ac9d19ec0edbee656154429592172e990d413fd95c52758dc30e2033864c8629
- clm_afb20134f481ac65142dedc12fb34a5403bc8602803f2a017450db8a699ae8f2
- clm_d0cd35e632df5fd84c5f0f9f20d85c1c61eac9afc63cdf429f67c0cc98f6e6d7
- clm_d4305e2bcd95c57f79f202607b3871be4ba278ce054de397fe929f95e954cdfc
- clm_fc424d5b361c131f420177957ffd52d65d1d9aac2a3625c80d23682269d5064c
- clm_fed0ede4f1461c9e8269e351001917126b9ee389b6d1a46b360b4b06484ea31c
maturity: draft
page_id: pg_29e5e2cf28805cc485bf691fc4cfbd6d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d807d78c881350ef90d7a8a6a8c9a552
title: crewAIInc/crewAI/README.md @ 894898f84c4a
updated_at: '2026-09-14T03:43:14Z'
---

# crewAIInc/crewAI/README.md @ 894898f84c4a

<!-- rcw:begin owner=source:src_d807d78c881350ef90d7a8a6a8c9a552 block=evidence -->
- Agent JSONC definitions specify role, goal, backstory, LLM, and tools; `{placeholder}` values in agent/task text are filled from `inputs` defaults in `crew.jsonc`, with the CLI prompting for missing values at run time. [@claim:clm_0ac9b9ac6a2ce5213b29f7c2a42436a12453107d9814508371f3cf47b4b765f9]
- Flows provide secure, consistent state management between tasks; the documented example defines typed Pydantic state (e.g., sentiment, confidence) on a Flow subclass. [@claim:clm_1814b3aea8dd6a4b762395e078e36e7396b50c4c78878d1f118f79a4641df959]
- CrewAI requires Python >=3.10 and <3.14 and uses UV for dependency management and package handling. [@claim:clm_19d08e2c552f04f4199c9d1b3b1af51239598a765197c56af54170f4b55ea0d6]
- CrewAI is released under the MIT License. [@claim:clm_4446b21208139668fc79b7f5953ad05100af2274e6e633ad3e7b6127c4e00849]
- Repository development practice: docs under `docs/edge/` publish immediately under the Edge version selector and are frozen into immutable `docs/v<X.Y.Z>/` snapshots at release; CI rejects PRs modifying frozen snapshots without a `[docs-freeze]` title prefix. [@claim:clm_460eb4147f005ea5fada7b5c716fb955b83414be81d37414ca049bb1c5f3df96]
- CrewAI is described as an open-source Python framework for building production-ready multi-agent workflows, offering high-level abstractions and low-level APIs. [@claim:clm_547d5ffd99603491b04822d28ed05a9864625bceff62796157215f3c87437a84]
- New crew projects are JSON-first: agents live in `agents/*.jsonc`, tasks and crew settings in `crew.jsonc`, with optional `knowledge/`, `skills/`, and `tools/` directories; a `--classic` flag yields the older Python/YAML scaffold. [@claim:clm_572b5baf15d504d8047314be4a3e15cc7dda6987d2d171a61d2fb29e59cbf374]
- Repository development practice: contributors clone the repo, run `uv sync --all-groups --all-extras`, install pre-commit hooks, run tests with `uv run pytest lib/crewai/tests/ -x -q`, and type-check with `uv run mypy lib/`. [@claim:clm_60f51d9f110e62fbc9c8690d12adcebf09db8f54e746c97763183e00c7bd49cd]
- CrewAI is positioned for multi-step work needing specialized agents, tool use, structured outputs, human review, and workflows combining autonomous reasoning with explicit business logic. [@claim:clm_8317081bce5f36199ecbbba2fc62a3afbb2a4b9160a0f9a0a541f777f8fc9116]
- Agents can integrate with external tools, APIs, and databases, and the framework advertises tools, memory, knowledge, checkpointing, async execution, and MCP/A2A support. [@claim:clm_88c173fdb4c59b5275762327f2df36bf6837cb5ea088528467340a998d3e88f5]
- The CrewAI CLI supports `crewai create crew <name>`, `crewai install`, and `crewai run`, and is installed via `uv tool install crewai`. [@claim:clm_8945b7f141571b2c906f1ad0cfaecacdcaf29f4ff5117ae64a8f36100f1cddfd]
- Flows support logical operators `or_` and `and_` combined with `@start`, `@listen`, and `@router` decorators to build complex triggering conditions and conditional routing. [@claim:clm_ac0e5de89c6df646b1aa89bf69d8a184284c89c1c0497df48862d96b06c900de]
- On Windows, a chroma-hnswlib==0.7.6 build error (missing float.h) can occur, requiring Visual Studio Build Tools with Desktop development with C++ to resolve. [@claim:clm_ac9d19ec0edbee656154429592172e990d413fd95c52758dc30e2033864c8629]
- Official CrewAI Skills can be installed for AI coding agents (Claude Code plugins or `npx skills add crewaiinc/skills`), covering scaffolding, agent/task design, and a docs MCP query skill. [@claim:clm_afb20134f481ac65142dedc12fb34a5403bc8602803f2a017450db8a699ae8f2]
- By default agents use the OpenAI API for model queries; other connections such as local models via Ollama and LM Studio are supported, and custom-trained or fine-tuned models can be integrated. [@claim:clm_d0cd35e632df5fd84c5f0f9f20d85c1c61eac9afc63cdf429f67c0cc98f6e6d7]
- Besides a sequential process, CrewAI supports a hierarchical process that automatically assigns a manager agent to coordinate task planning and execution via delegation and result validation. [@claim:clm_d4305e2bcd95c57f79f202607b3871be4ba278ce054de397fe929f95e954cdfc]
- The framework offers two complementary models: Crews for autonomous, role-based agent collaboration, and Flows for event-driven workflows with precise control and state management. [@claim:clm_fc424d5b361c131f420177957ffd52d65d1d9aac2a3625c80d23682269d5064c]
- CrewAI collects anonymous telemetry (versions, OS, agent/task counts, process type, LLM used, tool names); prompts, task descriptions, and API responses are not collected unless `share_crew` is enabled, and telemetry can be disabled via OTEL_SDK_DISABLED=true. [@claim:clm_fed0ede4f1461c9e8269e351001917126b9ee389b6d1a46b360b4b06484ea31c]
<!-- rcw:end owner=source:src_d807d78c881350ef90d7a8a6a8c9a552 block=evidence -->

## Researcher notes

