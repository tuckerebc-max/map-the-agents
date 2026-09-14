# microsoft/autogen

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 027ecf0a379b @ 60762d77b55bc1fd

## Summary (orientation draft, not independently verified)

Evidence covers the AutoGen README (maintenance-mode notice, layered framework, install/quickstart samples), design docs on the publish-subscribe programming model and topics, FAQ on the 0.4 rewrite, and transparency FAQs describing intended uses, evaluation, and limitations.

## Source coverage

Source coverage (partial): 6 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] AutoGen is a framework for building multi-agent AI applications that can act autonomously or work alongside humans. -- evidence: [README.md#L16-L16](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L16-L16)
  - [observation/documented] AutoGen 0.4 is a ground-up rewrite featuring asynchronous messaging, scalable distributed agents, modular design, cross-language (.NET/Python) support, and full typing. -- evidence: [FAQ.md#L5-L10](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/FAQ.md#L5-L10), [FAQ.md#L56-L56](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/FAQ.md#L56-L56)
- components (1 claim(s)):
  - [observation/documented] The framework is layered: Core API (message passing, event-driven agents, local/distributed runtime), AgentChat API (higher-level prototyping), and Extensions API (LLM clients, code execution). -- evidence: [README.md#L181-L183](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L181-L183), [README.md#L179-L179](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L179-L179)
- design-choices (2 claim(s)):
  - [observation/documented] The programming model is publish-subscribe: agents subscribe to and publish events defined per the CloudEvents specification, with handlers matching event types. -- evidence: [docs/design/01 - Programming Model.md#L5-L5](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/01%20-%20Programming%20Model.md#L5-L5), [docs/design/01 - Programming Model.md#L18-L18](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/01%20-%20Programming%20Model.md#L18-L18), [docs/design/01 - Programming Model.md#L9-L9](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/01%20-%20Programming%20Model.md#L9-L9)
  - [observation/documented] Topics route published messages to agents; a TopicId has type and source, subscriptions use side-effect-free matcher and mapper functions, and the runtime instantiates agents on demand. -- evidence: [docs/design/02 - Topics.md#L44-L44](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L44-L44), [docs/design/02 - Topics.md#L48-L48](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L48-L48), [docs/design/02 - Topics.md#L19-L24](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L19-L24), [docs/design/02 - Topics.md#L7-L7](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L7-L7), [docs/design/02 - Topics.md#L41-L42](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/docs/design/02%20-%20Topics.md#L41-L42)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are limited to bug fixes, security patches, and documentation improvements due to maintenance mode; feature work is directed to Microsoft Agent Framework. -- evidence: [README.md#L216-L216](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L216-L216)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] AssistantAgent accepts a model client, optional workbench or tools, streaming flag, and max_tool_iterations; agents run via async run/run_stream with Console output. -- evidence: [README.md#L56-L60](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L56-L60), [README.md#L138-L147](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L138-L147), [README.md#L78-L95](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L78-L95)
  - [observation/documented] AutoGen Studio provides a no-code GUI for prototyping multi-agent workflows, launched with 'autogenstudio ui --port 8080 --appdir ./my-app'; it is explicitly not production-ready. -- evidence: [README.md#L40-L41](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L40-L41), [README.md#L158-L158](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L158-L158), [README.md#L168-L169](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L168-L169), [README.md#L160-L164](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L160-L164)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] AgentTool wraps an agent as a tool so a coordinator agent can invoke expert agents, enabling basic multi-agent orchestration with up to max_tool_iterations tool calls. -- evidence: [README.md#L120-L127](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L120-L127), [README.md#L138-L147](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L138-L147), [README.md#L129-L136](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L129-L136), [README.md#L106-L106](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L106-L106)
- tools-permissions (1 claim(s)):
  - [observation/documented] Agents can use MCP servers via McpWorkbench with StdioServerParams; the docs warn to connect only to trusted MCP servers since they may execute commands locally or expose sensitive data. -- evidence: [README.md#L101-L102](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L101-L102), [README.md#L71-L75](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L71-L75), [README.md#L78-L95](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L78-L95), [README.md#L67-L67](https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md#L67-L67)
- evaluation (1 claim(s)):
More evidence: [full detail](autogen.detail.md)

Metadata and full claim list: [full detail](autogen.detail.md)
Human notes ([notes](autogen.notes.md), never overwritten by build)

[Back to map index](../../index.md)
