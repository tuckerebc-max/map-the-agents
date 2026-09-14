# startuphakk/openmonoagent.ai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f3f001dd5b33 @ 1b092f398ae5cb57

## Summary (orientation draft, not independently verified)

The snapshot is README and architecture documentation for OpenMono, a .NET 10 local-first coding agent bundling llama.cpp inference in Docker, with documented tool pipeline, sub-agents, permissions, MCP/LSP integration, and web search/scraping services. No source code or contributing guide content is included in the evidence. Evidence coverage: 155 of 301 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 43 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] OpenMono is described as a .NET 10 CLI coding agent that runs entirely on local hardware, pairing with its own llama.cpp inference server and Docker sandboxing. -- evidence: [docs/ARCHITECTURE.md#L3-L3](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L3-L3), [README.md#L42-L42](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L42-L42)
- components (2 claim(s)):
  - [observation/documented] Every tool call passes a 12-step pipeline including schema validation, plan-mode guard, capability check, caching, pre/post hooks, and artifact storage for results over 10 KB. -- evidence: [docs/ARCHITECTURE.md#L204-L220](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L204-L220), [README.md#L133-L134](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L133-L134)
  - [observation/documented] A Roslyn tool loads .cs files into an in-memory AdhocWorkspace with a 5-minute compilation cache, exposing actions like find-references, callers, diagnostics, type-hierarchy, and blast-radius. -- evidence: [docs/ARCHITECTURE.md#L296-L305](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L296-L305), [docs/ARCHITECTURE.md#L292-L292](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L292-L292)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README directs contributors to read CONTRIBUTING.md before opening a PR and welcomes contributions of tools, providers, LSP servers, playbooks, bug fixes, and docs. -- evidence: [README.md#L304-L311](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L304-L311)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI offers TUI mode by default and a classic scrolling terminal via `openmono agent --classic`; renderer selection falls back to classic when I/O is redirected. -- evidence: [docs/ARCHITECTURE.md#L354-L357](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L354-L357), [README.md#L67-L70](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L67-L70)
  - [observation/documented] A VS Code/Cursor extension connects to the agent over ACP on port 7475, started with `--acp-only --acp-port 7475`, sharing the same agent core as the CLI. -- evidence: [README.md#L211-L212](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L211-L212), [docs/ARCHITECTURE.md#L45-L45](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L45-L45)
- memory-state (2 claim(s)):
  - [observation/documented] Context management checkpoints at 65% context fill with an LLM summary and compacts at 80% as a fallback; thresholds track the real window read from llama.cpp `/props`. -- evidence: [docs/ARCHITECTURE.md#L234-L237](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L234-L237), [docs/ARCHITECTURE.md#L239-L239](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L239-L239)
  - [observation/documented] Sessions persist as JSONL under `~/.openmono/sessions/` with a header record plus messages, and checkpoints are stored in a sibling `.checkpoints.json` file. -- evidence: [docs/ARCHITECTURE.md#L228-L230](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L228-L230)
- orchestration (2 claim(s)):
  - [observation/documented] The agentic loop runs up to 25 iterations per turn, aborts on three identical repeated tool sequences (doom-loop detection), and ends when the LLM emits text with no tool calls. -- evidence: [README.md#L125-L126](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L125-L126), [docs/ARCHITECTURE.md#L194-L194](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L194-L194), [docs/ARCHITECTURE.md#L196-L196](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L196-L196)
More evidence: [full detail](openmonoagent.ai.detail.md)

Metadata and full claim list: [full detail](openmonoagent.ai.detail.md)
Human notes ([notes](openmonoagent.ai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
