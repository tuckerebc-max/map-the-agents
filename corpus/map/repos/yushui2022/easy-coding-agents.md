# yushui2022/easy-coding-agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 72fad500ec1e @ b4faae6386487368

## Summary (orientation draft, not independently verified)

Easy-Coding-Agent is a Python terminal coding-agent runtime with an autonomous tool-execution loop, three modes, custom agents, and an evidence-gated SQLite-backed memory package, plus a memory-subsystem benchmark harness. Evidence is mostly README/docs; benchmark numbers are self-reported retrieval/evidence metrics, not official leaderboard scores.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The project is a Python coding-agent runtime whose main.py provides a prompt_toolkit CLI, with core.engine.AgentEngine running an autonomous task-driven loop and core.task.TaskManager tracking pending, in-progress, completed, and skipped tasks. -- evidence: [README.md#L21-L33](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L21-L33), [README.md#L11-L14](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L11-L14)
  - [observation/documented] Built-in tools include read (line-numbered, offset/limit), write, edit (unique-string replacement), smart_search (ripgrep-style with tree-sitter), glob, grep, bash, todo tools, ask_user/ask_selection, and agent management tools. -- evidence: [README.md#L66-L80](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L66-L80)
- design-choices (1 claim(s)):
  - [observation/documented] The agent has three runtime modes: Plan (analyze without writing code until approval), Code (default autonomous implementation), and Chat (Q&A avoiding file changes); Shift+Tab cycles modes without restarting. -- evidence: [README.md#L87-L87](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L87-L87), [README.md#L89-L93](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L89-L93), [README.md#L95-L96](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L95-L96)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors install requirements.txt and requirements-dev.txt, run tests with 'python -m pytest tests -q', and can run fixture benchmarks via benchmark/memory_eval/run.py and benchmark/coding_memory/run.py commands. -- evidence: [README.md#L247-L249](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L247-L249), [README.md#L276-L279](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L276-L279), [README.md#L253-L257](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L253-L257), [README.md#L234-L237](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L234-L237)
  - [observation/documented] Repository development practice: the AI coder guide instructs modifying agents to add tools via a decorator registry in tools/ plus an import in core/engine.py, edit prompts in core/prompts.py, avoid blocking IO and time.sleep in the main loop, and write generated files to workspace/. -- evidence: [AI_CODER_GUIDE.md#L62-L65](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/AI_CODER_GUIDE.md#L62-L65), [AI_CODER_GUIDE.md#L68-L69](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/AI_CODER_GUIDE.md#L68-L69), [AI_CODER_GUIDE.md#L80-L85](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/AI_CODER_GUIDE.md#L80-L85)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI exposes slash commands for custom-agent management (/agent create, list, use, preview, edit, delete) and lets users invoke a specialist agent inline via @AgentName syntax. -- evidence: [README.md#L105-L113](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L105-L113)
- memory-state (2 claim(s)):
  - [observation/documented] Memory is packaged as agent_memory_core, storing events, large tool outputs under refs/*.md, task nodes, claims with support status, and coding entities in SQLite, with quality gates requiring evidence for file-content claims, error explanations, and DONE transitions. -- evidence: [README.md#L156-L162](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L156-L162), [README.md#L145-L152](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L145-L152), [README.md#L166-L170](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L166-L170), [README.md#L305-L312](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L305-L312), [README.md#L139-L141](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/README.md#L139-L141)
  - [observation/documented] The repository's MEMORY.md long-term memory file holds user preferences (documentation sync, async coding style, Chinese-localized rich logging) and session-derived decisions from prior projects, illustrating the agent's long-term memory persistence format. -- evidence: [MEMORY.md#L44-L44](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L44-L44), [MEMORY.md#L4-L10](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L4-L10), [MEMORY.md#L54-L54](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L54-L54), [MEMORY.md#L31-L40](https://github.com/yushui2022/easy-coding-agents/blob/72fad500ec1ee3273dbf0720c890f4dc4fa5e009/MEMORY.md#L31-L40)
- orchestration (1 claim(s)):
More evidence: [full detail](easy-coding-agents.detail.md)

Metadata and full claim list: [full detail](easy-coding-agents.detail.md)
Human notes ([notes](easy-coding-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
