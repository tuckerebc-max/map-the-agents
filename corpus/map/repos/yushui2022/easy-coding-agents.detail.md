# yushui2022/easy-coding-agents -- full detail

[Back to orientation](easy-coding-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yushui2022/easy-coding-agents/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/b4faae6386487368.json](../../../wiki/dossiers/yushui2022/easy-coding-agents/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/b4faae6386487368.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The project is a Python coding-agent runtime whose main.py provides a prompt_toolkit CLI, with core.engine.AgentEngine running an autonomous task-driven loop and core.task.TaskManager tracking pending, in-progress, completed, and skipped tasks. -- evidence: [README.md#L21-L33](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L21-L33), [README.md#L11-L14](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L11-L14) (`clm_adf4990862a0c1fb7b65a35ecafaff2eef6df10281d54ccbec8b3f18fe1712a3`)
- [observation/documented] Built-in tools include read (line-numbered, offset/limit), write, edit (unique-string replacement), smart_search (ripgrep-style with tree-sitter), glob, grep, bash, todo tools, ask_user/ask_selection, and agent management tools. -- evidence: [README.md#L66-L80](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L66-L80) (`clm_661dec3ba4969c2bd4c8a2b146c0a93b79a9fdda7729c6a6cc696f6bdcbd0c3d`)

## design-choices (1 claim(s))

- [observation/documented] The agent has three runtime modes: Plan (analyze without writing code until approval), Code (default autonomous implementation), and Chat (Q&A avoiding file changes); Shift+Tab cycles modes without restarting. -- evidence: [README.md#L87-L87](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L87-L87), [README.md#L89-L93](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L89-L93), [README.md#L95-L96](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L95-L96) (`clm_b5dda14ff871449e5396bc37648bb045de52b2733c0ecb0ff15536288e04b9de`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors install requirements.txt and requirements-dev.txt, run tests with 'python -m pytest tests -q', and can run fixture benchmarks via benchmark/memory_eval/run.py and benchmark/coding_memory/run.py commands. -- evidence: [README.md#L247-L249](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L247-L249), [README.md#L276-L279](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L276-L279), [README.md#L253-L257](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L253-L257), [README.md#L234-L237](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L234-L237) (`clm_6330d333c86292bbf8e4231cfb79979bc5af44f24198294056819bbf933c97ab`)
- [observation/documented] Repository development practice: the AI coder guide instructs modifying agents to add tools via a decorator registry in tools/ plus an import in core/engine.py, edit prompts in core/prompts.py, avoid blocking IO and time.sleep in the main loop, and write generated files to workspace/. -- evidence: [AI_CODER_GUIDE.md#L62-L65](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/AI_CODER_GUIDE.md#L62-L65), [AI_CODER_GUIDE.md#L68-L69](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/AI_CODER_GUIDE.md#L68-L69), [AI_CODER_GUIDE.md#L80-L85](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/AI_CODER_GUIDE.md#L80-L85) (`clm_2b9063aee4d162566d66fe15cc8be08c6b4640301f4b6556e3ab56f26d1a8752`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The CLI exposes slash commands for custom-agent management (/agent create, list, use, preview, edit, delete) and lets users invoke a specialist agent inline via @AgentName syntax. -- evidence: [README.md#L105-L113](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L105-L113) (`clm_0c8eab665bdd47ac89de026a5120d4294f81156c86177e3ff2e111dfb7cfcfe8`)

## memory-state (2 claim(s))

- [observation/documented] Memory is packaged as agent_memory_core, storing events, large tool outputs under refs/*.md, task nodes, claims with support status, and coding entities in SQLite, with quality gates requiring evidence for file-content claims, error explanations, and DONE transitions. -- evidence: [README.md#L156-L162](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L156-L162), [README.md#L145-L152](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L145-L152), [README.md#L166-L170](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L166-L170), [README.md#L305-L312](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L305-L312), [README.md#L139-L141](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L139-L141) (`clm_70eda541be796d8e6cc82028fb52639752ade0361a1fd547e53c86500f37efc7`)
- [observation/documented] The repository's MEMORY.md long-term memory file holds user preferences (documentation sync, async coding style, Chinese-localized rich logging) and session-derived decisions from prior projects, illustrating the agent's long-term memory persistence format. -- evidence: [MEMORY.md#L44-L44](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L44-L44), [MEMORY.md#L4-L10](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L4-L10), [MEMORY.md#L54-L54](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L54-L54), [MEMORY.md#L31-L40](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L31-L40) (`clm_d18680c237bdc683caf3c053956f63dd60003a180d09499a052b734ea34a31a4`)

## orchestration (1 claim(s))

- [observation/documented] The engine uses a double-buffered async queue (input_queue -> processing_queue -> AgentEngine._run_autonomous_loop) to separate user events from execution tasks and keep the CLI responsive during streaming and tool runs. -- evidence: [README.md#L60-L62](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L60-L62), [README.md#L54-L54](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L54-L54), [README.md#L56-L58](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L56-L58) (`clm_53e76b533dd7cf160bf24f6e1a199daadda836c5bcbc143f1f7184a4c5126737`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (3 claim(s))

- [observation/documented] A benchmark harness compares six memory baselines (no_memory, summary, long-context, keyword FTS, vector RAG, evidence-gated) on LongMemEval-S, LoCoMo10, and BEAM-lite, scoring retrieval/term recall, evidence source coverage, tokens, latency, and false-fact rate after a context wipe. -- evidence: [README.md#L211-L218](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L211-L218), [README.md#L174-L176](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L174-L176), [README.md#L189-L196](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L189-L196), [README.md#L200-L207](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L200-L207), [README.md#L180-L185](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L180-L185), [docs/BENCHMARKS.md#L115-L120](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/docs/BENCHMARKS.md#L115-L120) (`clm_be4597f148decf72d8985d6558fd5d6db5587ad04311d5689ae930338e431b85`)
- [observation/documented] The README reports evidence-gated memory at 0.40 retrieval recall and 0.87 evidence coverage on LongMemEval-S (100 cases), and the docs note LoCoMo10 answer-term recall remains low and is described as a current weakness. -- evidence: [docs/BENCHMARKS.md#L101-L111](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/docs/BENCHMARKS.md#L101-L111), [README.md#L189-L196](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L189-L196), [README.md#L222-L228](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L222-L228) (`clm_d432652a1b14bd4230a5a565b52defd13a0541554e6a6719f0a9c39ee8b42012`)
- [observation/documented] A SWE-bench-format memory probe checks whether issue context, failing-test evidence, task state, and false-DONE prevention survive memory reconstruction; it explicitly does not measure patch correctness, which requires the official SWE-bench Docker harness. -- evidence: [README.md#L281-L283](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L281-L283), [docs/BENCHMARKS.md#L206-L210](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/docs/BENCHMARKS.md#L206-L210), [docs/BENCHMARKS.md#L212-L213](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/docs/BENCHMARKS.md#L212-L213) (`clm_32c61942c7b7f9ce407e4dcf7e70eaace648d1b5e102959a0cb29f3ac42d4dcc`)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include rich, prompt_toolkit, aiofiles, python-dotenv, tree-sitter, tree-sitter-languages, openai, and questionary; requirements-dev.txt adds pytest>=7.0.0 on top of the base requirements. -- evidence: [requirements-dev.txt#L1-L2](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/requirements-dev.txt#L1-L2), [requirements.txt#L1-L8](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/requirements.txt#L1-L8) (`clm_ebc361911a1d7d7f0d2c793a9d1327a0b77c0b780c2ebed3bbca3b747a683401`)

## limitations (1 claim(s))

- [observation/documented] The README itself lists unsupported claims: official LongMemEval/LoCoMo leaderboard accuracy, SWE-bench patch resolved rate, general superiority over vector RAG or long-context baselines, and full production sandboxing or enterprise permission control. -- evidence: [README.md#L344-L347](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L344-L347) (`clm_643598215c175a689f4e71944392fe1caaad3b3474504fc901feecb906cfc159`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

