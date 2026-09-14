# foundationagents/recode

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6e7223f71281 @ f31fb93ce4e5f3e0

## Summary (orientation draft, not independently verified)

Evidence is README documentation plus a requirements.txt file; the README describes ReCode's recursive code-generation agent design, its CLI/configuration interfaces, and reported benchmark results, while requirements.txt pins three dependencies.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Partial programs are organized in a tree where each node captures one sub-task and records its execution trace. -- evidence: [README.md#L17-L20](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L17-L20)
  - [observation/documented] The repository includes run.py as CLI entry point, agents/recode/ implementation, envs/ wrappers for alfworld, webshop, and sciworld, configs/, and utils/ with an async OpenAI wrapper and constrained executor. -- evidence: [README.md#L28-L33](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L28-L33)
- design-choices (1 claim(s)):
  - [observation/documented] ReCode unifies plan and action into a single code representation, treating high-level plans as placeholder functions that recursively decompose into executable primitives. -- evidence: [README.md#L7-L7](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L7-L7)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: setup requires a conda environment with Python 3.10 or newer, and the README suggests configuring the three benchmark environments separately since dependency conflicts are unconfirmed. -- evidence: [README.md#L59-L59](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L59-L59), [README.md#L61-L61](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L61-L61)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] run.py exposes flags including -a/--agent, -e/--env, -n/--instances, -c/--concurrent, --split, --seed, --max-depth, --profile, and -C/--config for YAML-based flag overrides. -- evidence: [README.md#L154-L160](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L154-L160)
  - [observation/documented] LLM access is configured via named profiles in configs/profiles.yaml selected with --profile; OPENAI_API_KEY serves as a fallback, and cost tracking loads configs/prices.json with a track_costs toggle. -- evidence: [README.md#L114-L114](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L114-L114), [README.md#L132-L137](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L132-L137)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A dynamic execution loop executes each node immediately, with fresh observations deciding whether to expand further, retry, or finish. -- evidence: [README.md#L17-L20](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L17-L20)
- tools-permissions (1 claim(s)):
  - [observation/documented] A constrained Python executor maintains environment variables, validates code blocks, and exposes the toolset available to the agent. -- evidence: [README.md#L17-L20](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L17-L20)
- evaluation (2 claim(s)):
  - [observation/documented] The README reports inference comparisons against ReAct, CodeAct, AdaPlanner, and ADaPT, claiming an average score of 60.8 (10.5 above the best baseline) and a perfect 100 in ALFWorld with claude-4-sonnet. -- evidence: [README.md#L39-L39](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L39-L39)
  - [observation/documented] The README reports SFT experiments with Qwen2.5-7B-Instruct giving ReCode+SFT an average of 70.4% versus ReAct+SFT (67.6%) and CodeAct+SFT (55.8%). -- evidence: [README.md#L47-L47](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L47-L47)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins openai==2.6.1, rich==14.2.0, and torch==2.9.0. -- evidence: [requirements.txt#L1-L3](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/requirements.txt#L1-L3)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](recode.detail.md)

Metadata and full claim list: [full detail](recode.detail.md)
Human notes ([notes](recode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
