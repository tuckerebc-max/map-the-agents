# rath-team/openrath

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 82819467b001 @ 5bcf2c869c8a34af

## Summary (orientation draft, not independently verified)

OpenRath is a PyTorch-like multi-agent, multi-session Python framework whose core runtime objects are Session, Sandbox, Memory, Tool, Agent, Workflow, and Selector, with a v2.0.0 durable production layer (PostgreSQL/Redis/S3 data plane, Agent Server, effect ledger). Evidence is README documentation only; no code-inspected behavior is available. Evidence coverage: 161 of 218 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] OpenRath exposes core runtime objects: Session (conversation state and inter-agent lineage), Sandbox (tool execution placement), Memory, Tool, Agent, Workflow, and Selector. -- evidence: [README.md#L23-L23](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L23-L23), [README.md#L27-L33](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L27-L33)
  - [observation/documented] v2.0.0 adds a durable production layer: @step/@router boundaries compile to immutable plans; Runs, Events, and Checkpoints survive process and worker restarts, with leases, fencing, retries, and resumable queues. -- evidence: [README.md#L73-L80](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L73-L80), [README.md#L59-L62](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L59-L62)
- design-choices (2 claim(s)):
  - [observation/documented] The framework maps PyTorch concepts to agent concepts: Session as Tensor, Sandbox/Backend as Device, Memory as Parameter, Tool as Function, Agent as nn.Linear, Workflow as nn.Module, Selector as control flow. -- evidence: [README.md#L43-L51](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L43-L51)
  - [observation/documented] OpenRath is Session-first rather than agent-loop-first, so multi-agent, multi-branch, durable-memory, sandboxed, and lineage-traced workloads share one flowing value. -- evidence: [README.md#L53-L53](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L53-L53), [README.md#L147-L147](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L147-L147)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Session supports fork(), detach(), merge(...), JSONL serialization, sandbox binding via session.to("local", spec="./"), plus from_user_message and from_agent_prompt constructors. -- evidence: [README.md#L241-L246](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L241-L246), [README.md#L237-L237](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L237-L237)
  - [observation/documented] FlowToolCall is the model-visible tool abstraction combining name, description, JSON schema, and a Python call over a Session; BackendTool* is the lower-level payload consumed by sandbox backends. -- evidence: [README.md#L286-L287](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L286-L287), [README.md#L280-L280](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L280-L280)
- memory-state (2 claim(s)):
  - [observation/documented] The base install ships a zero-dependency local memory backend storing data under .openrath/memory/ with lexical BM25 recall, optional embeddings, and OpenViking as an optional external backend. -- evidence: [README.md#L262-L262](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L262-L262)
  - [observation/documented] Agent memory APIs include memory= binding at construction, remember_memory, recall_memory, commit_memory, and commit_on_forward=True for automatic commits. -- evidence: [README.md#L272-L276](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L272-L276)
- orchestration (1 claim(s)):
  - [observation/documented] flow.Selector is an LLM-backed router over self-describing workflows that returns the next workflow or a no-op EmptyWorkflow, keeping if/while control flow in plain Python. -- evidence: [README.md#L308-L314](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L308-L314), [README.md#L306-L306](https://github.com/Rath-Team/OpenRath/blob/82819467b001896c8b22f98ba99f1634c78b0cfc/README.md#L306-L306)
- tools-permissions (1 claim(s)):
More evidence: [full detail](openrath.detail.md)

Metadata and full claim list: [full detail](openrath.detail.md)
Human notes ([notes](openrath.notes.md), never overwritten by build)

[Back to map index](../../index.md)
