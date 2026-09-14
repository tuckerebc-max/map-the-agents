# langroid/langroid

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 53c01d4e1a9e @ 15dd2d992e81e966

## Summary (orientation draft, not independently verified)

Langroid is a Python multi-agent framework for LLM applications built around Agent and Task abstractions, tool/function-calling via ToolMessage, and specialized agents like DocChatAgent and TableChatAgent, with configurable LLM, vector-store, and cache backends. Evidence is README documentation only; no code inspection in this snapshot. Evidence coverage: 134 of 278 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 100 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] Langroid is a Python framework for building LLM applications where users set up Agents equipped with optional components (LLM, vector-store, tools/functions) that collaborate by exchanging messages. -- evidence: [README.md#L38-L45](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L38-L45)
  - [observation/documented] The Agent class encapsulates LLM conversation state plus an optional vector-store and tools, acts as a message transformer, and by default provides three responder methods corresponding to LLM, Agent, and User. -- evidence: [README.md#L455-L493](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L455-L493)
- design-choices (1 claim(s)):
  - [observation/documented] The multi-agent paradigm is inspired by the Actor model, and the framework does not use LangChain or any other LLM framework, aiming to work with practically any LLM. -- evidence: [README.md#L38-L45](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L38-L45), [README.md#L47-L50](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L47-L50)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] A Claude Code plugin provides two skills: langroid:patterns for generating Langroid multi-agent code using proper design patterns, and langroid:add-pattern for recording newly learned patterns for future reference. -- evidence: [README.md#L52-L53](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L52-L53), [README.md#L552-L555](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L552-L555)
- interfaces (3 claim(s)):
  - [observation/documented] Tools are defined by subclassing ToolMessage with a request field naming the handling agent method, a purpose description, and typed arguments; agents enable tools via enable_message, and Pydantic validation errors are sent back to the LLM for self-correction. -- evidence: [README.md#L857-L862](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L857-L862), [README.md#L876-L883](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L876-L883), [README.md#L901-L911](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L901-L911)
  - [observation/documented] LLM configuration supports OpenAI models, any model behind an OpenAI-compatible API (e.g. "ollama/mistral"), and local models via chat_model strings such as "local/localhost:8000". -- evidence: [README.md#L106-L109](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L106-L109), [README.md#L776-L781](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L776-L781)
- memory-state (1 claim(s)):
  - [observation/documented] LLM API responses can be cached via Redis or Momento (CACHE_TYPE=momento); if Redis settings are absent, Langroid falls back to a pure-Python in-memory cache via Fakeredis. -- evidence: [README.md#L626-L659](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L626-L659)
- orchestration (1 claim(s)):
  - [observation/documented] A Task wraps an Agent, manages iteration over the agent's responder methods, and orchestrates multi-agent interaction via hierarchical, recursive task delegation; sub-tasks are treated as additional responders used round-robin after the agent's own responders. -- evidence: [README.md#L455-L493](https://github.com/langroid/langroid/blob/53c01d4e1a9e7c1dd829c97513aaf57f23b2945f/README.md#L455-L493)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](langroid.detail.md)

Metadata and full claim list: [full detail](langroid.detail.md)
Human notes ([notes](langroid.notes.md), never overwritten by build)

[Back to map index](../../index.md)
