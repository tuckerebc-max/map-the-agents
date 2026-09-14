# mervinpraison/praisonai

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 43a106db26d3 @ 462851b4fd2f608d

## Summary (orientation draft, not independently verified)

The snapshot contains only README content for PraisonAI, a Python/JS multi-agent framework describing a layered agent SDK, MCP tool integration, sandboxed tool execution, YAML workflows, and optional dashboard/UI extras. No code or contributor-workflow files are present in the evidence. Evidence coverage: 147 of 357 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The framework is framed as a five-layer stack (prompt, context, harness, loop, graph) plus a managed layer deciding where the agent runs, with each layer wrapping the one inside. -- evidence: [README.md#L139-L146](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L139-L146), [README.md#L114-L114](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L114-L114), [README.md#L118-L137](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L118-L137)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The core Python SDK exposes an Agent class constructed with parameters like instructions, role, goal, and output, and started via agent.start(...). -- evidence: [README.md#L155-L161](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L155-L161), [README.md#L101-L103](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L101-L103), [README.md#L106-L108](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L106-L108)
  - [observation/documented] MCP servers are attached as tools via MCP(), supporting stdio commands, HTTP URLs, and WebSocket endpoints with auth tokens and environment variables. -- evidence: [README.md#L503-L510](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L503-L510), [README.md#L512-L512](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L512-L512), [README.md#L500-L500](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L500-L500), [README.md#L497-L497](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L497-L497), [README.md#L494-L494](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L494-L494)
- memory-state (2 claim(s)):
  - [observation/documented] Agents accept memory, knowledge, and context parameters for persistence, selective retrieval, and auto-compaction, and handoffs isolate sub-agents to recent messages plus intersecting tools. -- evidence: [README.md#L178-L178](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L178-L178), [README.md#L170-L176](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L170-L176)
  - [observation/documented] Conversation state can be persisted to databases by passing a db() object with a database_url and session_id in the memory config, with messages, runs, and traces auto-persisted. -- evidence: [README.md#L571-L579](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L571-L579), [README.md#L568-L569](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L568-L569)
- orchestration (2 claim(s)):
  - [observation/documented] Tool execution can be offloaded to shared sandboxes via tools_run_on with backends including docker, e2b, modal, daytona, flyio, and others, so steps in a flow share one sandbox filesystem. -- evidence: [README.md#L259-L261](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L259-L261), [README.md#L284-L286](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L284-L286), [README.md#L251-L251](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L251-L251)
  - [observation/documented] A whole agent (model calls, loop, and tools) can be placed on a managed runtime via run_on, e.g. run_on="anthropic" hosted or run_on="docker" self-hosted; invalid targets raise a TypeError. -- evidence: [README.md#L289-L292](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L289-L292), [README.md#L309-L315](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L309-L315)
- tools-permissions (1 claim(s)):
  - [observation/documented] Agents support an approval=True option described as a human gate before risky tools run, alongside guardrails and hooks in the harness layer. -- evidence: [README.md#L139-L146](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L139-L146), [README.md#L192-L199](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L192-L199)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](praisonai.detail.md)

Metadata and full claim list: [full detail](praisonai.detail.md)
Human notes ([notes](praisonai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
