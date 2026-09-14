# langchain-ai/deepagents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c08cae693e00 @ a946885b8fc52b92

## Summary (orientation draft, not independently verified)

Deep Agents is an open-source Python agent harness built on LangGraph/LangChain's create_agent, with sub-agents, filesystem tools, context management, memory, skills, and a GitHub Action wrapper for the dcode coding agent; AGENTS.md documents contributor workflows.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Deep Agents is an open-source agent harness that runs out of the box and can be extended, overridden, or replaced piece by piece without forking. -- evidence: [README.md#L24-L24](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L24-L24), [README.md#L28-L31](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L28-L31)
- components (1 claim(s)):
  - [observation/documented] Documented features include sub-agents with isolated context windows, pluggable filesystem backends, context summarization with tool-output offloading, shell access, persistent memory, human-in-the-loop tool approval, skills, and custom or MCP tools. -- evidence: [README.md#L35-L42](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L35-L42)
- design-choices (2 claim(s)):
  - [observation/documented] The harness is model-agnostic: it works with any tool-calling LLM, including frontier APIs, open-weight hosted models, and self-hosted models via Ollama, vLLM, or llama.cpp. -- evidence: [README.md#L79-L79](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L79-L79), [README.md#L28-L31](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L28-L31)
  - [observation/documented] Deep Agents layers on LangChain's create_agent, which itself runs on the LangGraph graph runtime, bundling filesystem, sub-agents, context management, and skills on top. -- evidence: [README.md#L75-L75](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L75-L75), [README.md#L87-L87](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L87-L87)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors follow Conventional Commits with scopes, branch naming of username/scope/description, a PR template with a release-note summary, and unit tests split into tests/unit_tests and tests/integration_tests with warnings treated as errors. -- evidence: [AGENTS.md#L42-L42](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L42-L42), [AGENTS.md#L81-L83](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L81-L83), [AGENTS.md#L87-L87](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L87-L87), [AGENTS.md#L48-L51](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L48-L51), [AGENTS.md#L32-L32](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L32-L32)
  - [observation/documented] Repository development practice: the monorepo layout includes libs/deepagents, libs/code, libs/acp, libs/talon, libs/evals, and partner packages, with benchmarks run via package bench and bench-memory Make targets rather than pytest directly. -- evidence: [AGENTS.md#L111-L116](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L111-L116), [AGENTS.md#L131-L131](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/AGENTS.md#L131-L131)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The Python API exposes create_deep_agent, which accepts a model string, custom tools, and a system prompt, and is invoked with a messages payload. -- evidence: [README.md#L58-L64](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L58-L64), [README.md#L55-L56](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L55-L56)
  - [observation/documented] Any LangGraph CompiledStateGraph can be passed in as a sub-agent, allowing custom orchestration to plug into the harness. -- evidence: [README.md#L89-L89](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L89-L89)
- memory-state (1 claim(s)):
  - [observation/documented] The GitHub Action enables persistent memory by default through actions/cache, with memory_scope (pr, branch, or repo) and agent_name inputs controlling cache sharing and separation. -- evidence: [ACTION.md#L57-L59](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L57-L59), [ACTION.md#L55-L55](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/ACTION.md#L55-L55)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The product follows a 'trust the LLM' security model: the agent can do anything its tools allow, and boundaries should be enforced at the tool or sandbox level rather than by model self-policing. -- evidence: [README.md#L112-L112](https://github.com/langchain-ai/deepagents/blob/c08cae693e0036fcd45d979a7dfa3a7e306a0515/README.md#L112-L112)
More evidence: [full detail](deepagents.detail.md)

Metadata and full claim list: [full detail](deepagents.detail.md)
Human notes ([notes](deepagents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
