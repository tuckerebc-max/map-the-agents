# maximerobeyns/self_improving_coding_agent -- full detail

[Back to orientation](self_improving_coding_agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/maximerobeyns/self_improving_coding_agent/ed8275dca4d3c5dbf77229964351fe9b424797dc/2e3324ceb6b1bcdf.json](../../../wiki/dossiers/maximerobeyns/self_improving_coding_agent/ed8275dca4d3c5dbf77229964351fe9b424797dc/2e3324ceb6b1bcdf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The base_agent package contains modules for agents, benchmarks, callgraph, events, llm, oversight, schemas, tools, types, utils, and a web_server, plus a tests directory. -- evidence: [README.md#L127-L165](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L127-L165) (`clm_d86919cdede9853fb5d86cbc36b744e18fb5b81cd9692d1ca9c6cf836f549787`)

## design-choices (1 claim(s))

- [observation/documented] The system runs an iterative loop: evaluate the current agent on benchmark tasks, store results in an archive, run the agent on its own codebase for an improvement, then repeat with updated code. -- evidence: [README.md#L9-L13](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L9-L13) (`clm_a1b4b8cafb5c490d52548d6f462f7e400af747c5abd0b31327a7b52564ca71af`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup involves cloning the repo, exporting provider API keys locally, building a Docker image via a Makefile target (make image, or make image-mac on Apple Silicon), and pip-installing base_agent/requirements.txt plus swebench. -- evidence: [README.md#L21-L24](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L21-L24), [README.md#L33-L43](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L33-L43), [README.md#L45-L45](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L45-L45), [README.md#L47-L49](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L47-L49), [README.md#L56-L57](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L56-L57), [README.md#L59-L61](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L59-L61), [README.md#L51-L54](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L51-L54) (`clm_0c8f08285c064e1bcb1bf759c460328f2571f37eccd1f947d0bba4b171253a14`)
- [observation/documented] Repository development practice: the self-improvement loop is run with python runner.py after uncommenting desired benchmarks in base_agent/src/benchmarks/__init__.py, with options like --id and --workers; results go to results/run_<id>. -- evidence: [README.md#L105-L105](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L105-L105), [README.md#L92-L103](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L92-L103) (`clm_9a8402e0ec86b684883e4e295d728e5e5f09b84fa891b5b1398c6b81961caabf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Running the agent with --server true exposes a web page at localhost:8080 that visualizes event-bus events and the agent callgraph, with clickable event details, overseer messages, and collapsible sub-agent traces. -- evidence: [README.md#L65-L73](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L65-L73) (`clm_aa8476c85fd0f4f4484b2c1e518904122198b468106a0aa61259e60130c85b04`)
- [observation/documented] The agent is invoked as a Python module with command-line arguments (e.g. an initial prompt via -p), and options can be listed via --help. -- evidence: [README.md#L65-L73](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L65-L73), [README.md#L79-L86](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L79-L86) (`clm_5df7a669d63dc6a70cfc5f0332ab5006056e72a1342a1a36665450b70d8971d1`)

## memory-state (1 claim(s))

- [observation/documented] Evaluation results are stored in an archive as part of the improvement loop, and each run directory keeps experiment metadata plus per-iteration agent code, benchmark results, and meta-improvement logs. -- evidence: [README.md#L9-L13](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L9-L13), [README.md#L169-L180](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L169-L180) (`clm_ac7a78d2a4c0314bd4621cf96e34735aabb957b8d0f7abd9b69fe580292acb6b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The agent can execute shell commands, and the README instructs running it inside the provided Docker container for isolation from the host file system. -- evidence: [README.md#L19-L19](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L19-L19) (`clm_4d5f6963ab56dfa99b21a52709024edd859e33686653ff49f813f2577cf1f5d0`)

## evaluation (1 claim(s))

- [observation/documented] The loop's evaluation step measures the agent's performance on benchmark tasks, and per-iteration results include per-problem results.jsonl, summary perf.jsonl metrics, and detailed traces. -- evidence: [README.md#L9-L13](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L9-L13), [README.md#L169-L180](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L169-L180) (`clm_a930b162c6075251e66bf95cfc3c9d4dd4d0e2f11db0ea427be8068479e8e561`)

## dependencies (1 claim(s))

- [observation/documented] The agent supports multiple LLM inference providers (Anthropic, OpenAI, Gemini, Vertex, Fireworks, DeepSeek); exporting a provider key makes that provider's models available, and omitting one simply disables its models. -- evidence: [README.md#L26-L31](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L26-L31), [README.md#L33-L43](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L33-L43) (`clm_f2b20f6880afb856b6cb2d33b42971a51eadce99f8b99cac21449ed705d5b7dd`)

## limitations (1 claim(s))

- [observation/documented] The README describes the base agent as minimal: it lacks efficient file editing tools, devtools like tree-sitter or LSP integrations, and advanced reasoning structures, though it has building blocks to bootstrap and specialize itself. -- evidence: [README.md#L118-L123](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L118-L123) (`clm_5594d2ff8fda790f70672613faa20e04c9b5689f9a031b7f49834771c8a9b722`)

## relevance (1 claim(s))

- [observation/documented] The project is associated with the SICA paper presented at the ICLR 2025 Workshop on Scaling Self-Improving Foundation Models. -- evidence: [README.md#L184-L193](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L184-L193) (`clm_75dfbcd31214c297b999891a9b0794a8636505479632f634d7d457122f776017`)

