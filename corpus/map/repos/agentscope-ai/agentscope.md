# agentscope-ai/agentscope

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: modelscope/agentscope (github id 742244656).
Latest snapshot: commit b82253ba1b68 @ a07620e1b7cb9181

## Summary (orientation draft, not independently verified)

AgentScope is a Python agent framework (requires Python 3.11+) whose SDK exposes building blocks such as a ReAct loop, Toolkit, Model, Context, Event System, Permission & HITL, Middleware, Memory, and Workspace/Sandbox, plus a FastAPI-based agent service with a Web UI. Contributor-facing rules (Conventional Commits, lazy imports, pre-commit/pytest, responsible AI use) are documented in CONTRIBUTING_zh.md. Evidence coverage: 151 of 201 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The SDK exposes building blocks including a ReAct reasoning-acting loop, Toolkit, Model, Context, Event System, Permission & HITL, Middleware, Memory, and Workspace/Sandbox. -- evidence: [README.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L126-L136), [README_zh.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L126-L136)
  - [observation/documented] The agent service is a FastAPI backend with a pre-built Web UI offering multi-tenancy, multi-session isolation, channels (Feishu, Discord, DingTalk), RAG service, persistence, and scheduling. -- evidence: [README.md#L75-L86](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L75-L86), [README.md#L181-L181](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L181-L181), [README.md#L183-L192](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L183-L192)
- design-choices (1 claim(s)):
  - [observation/documented] The design philosophy is to leverage models' reasoning and tool-use abilities rather than constrain them with strict prompts and opinionated orchestrations. -- evidence: [README.md#L68-L70](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L68-L70), [README_zh.md#L68-L69](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L68-L69)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors must follow Conventional Commits for commit and PR titles, with GitHub Actions validating PR titles against main and blocking non-conforming ones. -- evidence: [CONTRIBUTING_zh.md#L152-L152](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L152-L152), [CONTRIBUTING_zh.md#L127-L127](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L127-L127)
  - [observation/documented] Repository development practice: optional dependencies must be lazily imported at the point of use rather than at module top, to keep 'import agentscope' lightweight; pre-commit and pytest must be run before a PR. -- evidence: [CONTRIBUTING_zh.md#L111-L111](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L111-L111), [CONTRIBUTING_zh.md#L191-L197](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L191-L197), [CONTRIBUTING_zh.md#L114-L115](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L114-L115), [CONTRIBUTING_zh.md#L93-L99](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/CONTRIBUTING_zh.md#L93-L99)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Toolkit manages Python tools, MCP servers, and skills, and ships built-in coding tools (shell, file edit, search) plus task/plan tools. -- evidence: [README.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L126-L136)
  - [observation/documented] Recent releases add A2A protocol support via an A2AAgent for chatting with remote A2A agents, and RealtimeAgent supporting DashScope, OpenAI, Gemini, and xAI realtime APIs. -- evidence: [README.md#L75-L86](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L75-L86), [docs/NEWS.md#L5-L24](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/docs/NEWS.md#L5-L24)
- memory-state (1 claim(s)):
  - [observation/documented] The memory building block is described as agentic memory with switchable backends, naming ReMe and Mem0. -- evidence: [README_zh.md#L126-L136](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README_zh.md#L126-L136)
- orchestration (1 claim(s)):
  - [observation/documented] The agent service offers leader-worker orchestration with built-in team tools and task planning, where a leader agent spawns and coordinates workers. -- evidence: [README.md#L183-L192](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L183-L192), [README.md#L196-L225](https://github.com/agentscope-ai/agentscope/blob/b82253ba1b680a67091c4de32f074477c30ba416/README.md#L196-L225)
- tools-permissions (1 claim(s)):
More evidence: [full detail](agentscope.detail.md)

Metadata and full claim list: [full detail](agentscope.detail.md)
Human notes ([notes](agentscope.notes.md), never overwritten by build)

[Back to map index](../../index.md)
