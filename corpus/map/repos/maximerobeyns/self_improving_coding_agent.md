# maximerobeyns/self_improving_coding_agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ed8275dca4d3 @ 2e3324ceb6b1bcdf

## Summary (orientation draft, not independently verified)

The repository hosts SICA, a self-improving coding agent that iteratively evaluates itself on benchmarks, archives results, and edits its own codebase. Evidence covers the improvement loop, setup/run instructions, multi-provider LLM configuration, Docker isolation, and a web-based event visualization interface.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The base_agent package contains modules for agents, benchmarks, callgraph, events, llm, oversight, schemas, tools, types, utils, and a web_server, plus a tests directory. -- evidence: [README.md#L127-L165](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L127-L165)
- design-choices (1 claim(s)):
  - [observation/documented] The system runs an iterative loop: evaluate the current agent on benchmark tasks, store results in an archive, run the agent on its own codebase for an improvement, then repeat with updated code. -- evidence: [README.md#L9-L13](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L9-L13)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves cloning the repo, exporting provider API keys locally, building a Docker image via a Makefile target (make image, or make image-mac on Apple Silicon), and pip-installing base_agent/requirements.txt plus swebench. -- evidence: [README.md#L21-L24](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L21-L24), [README.md#L33-L43](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L33-L43), [README.md#L45-L45](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L45-L45), [README.md#L47-L49](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L47-L49), [README.md#L56-L57](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L56-L57), [README.md#L59-L61](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L59-L61), [README.md#L51-L54](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L51-L54)
  - [observation/documented] Repository development practice: the self-improvement loop is run with python runner.py after uncommenting desired benchmarks in base_agent/src/benchmarks/__init__.py, with options like --id and --workers; results go to results/run_<id>. -- evidence: [README.md#L105-L105](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L105-L105), [README.md#L92-L103](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L92-L103)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Running the agent with --server true exposes a web page at localhost:8080 that visualizes event-bus events and the agent callgraph, with clickable event details, overseer messages, and collapsible sub-agent traces. -- evidence: [README.md#L65-L73](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L65-L73)
  - [observation/documented] The agent is invoked as a Python module with command-line arguments (e.g. an initial prompt via -p), and options can be listed via --help. -- evidence: [README.md#L65-L73](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L65-L73), [README.md#L79-L86](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L79-L86)
- memory-state (1 claim(s)):
  - [observation/documented] Evaluation results are stored in an archive as part of the improvement loop, and each run directory keeps experiment metadata plus per-iteration agent code, benchmark results, and meta-improvement logs. -- evidence: [README.md#L9-L13](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L9-L13), [README.md#L169-L180](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L169-L180)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The agent can execute shell commands, and the README instructs running it inside the provided Docker container for isolation from the host file system. -- evidence: [README.md#L19-L19](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L19-L19)
- evaluation (1 claim(s)):
  - [observation/documented] The loop's evaluation step measures the agent's performance on benchmark tasks, and per-iteration results include per-problem results.jsonl, summary perf.jsonl metrics, and detailed traces. -- evidence: [README.md#L9-L13](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L9-L13), [README.md#L169-L180](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/README.md#L169-L180)
- dependencies (1 claim(s)):
More evidence: [full detail](self_improving_coding_agent.detail.md)

Metadata and full claim list: [full detail](self_improving_coding_agent.detail.md)
Human notes ([notes](self_improving_coding_agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
