# kyegomez/swarms

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9f51ebc3dd70 @ aa32ac6bb13251a7

## Summary (orientation draft, not independently verified)

The evidence (all README.md) documents Swarms as a Python multi-agent orchestration framework with an Agent primitive, multiple prebuilt swarm architectures, MCP client/server integration, and pip/uv/poetry/Docker installation. Claims are limited to what the README states; no evaluation or repository-workflow evidence is present. Evidence coverage: 157 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Swarms is a Python multi-agent orchestration framework whose fundamental building block is an Agent combining an LLM, tools, and memory. -- evidence: [README.md#L120-L120](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L120-L120), [README.md#L52-L52](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L52-L52), [README.md#L49-L50](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L49-L50)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Agents are configured via parameters such as model_name, max_loops, system_prompt, agent_name, autosave, and verbose; max_loops='auto' lets the agent decide when its task is complete. -- evidence: [README.md#L144-L155](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L144-L155), [README.md#L126-L131](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L126-L131), [README.md#L139-L139](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L139-L139)
  - [observation/documented] Agents can consume external tools via MCP by setting mcp_url or mcp_urls, gaining tools from one or many MCP servers without manual configuration. -- evidence: [README.md#L182-L190](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L182-L190), [README.md#L177-L177](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L177-L177)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (10 claim(s)):
  - [observation/documented] The framework ships prebuilt multi-agent architectures including SequentialWorkflow, ConcurrentWorkflow, AgentRearrange, GraphWorkflow, MixtureOfAgents, GroupChat, and ForestSwarm. -- evidence: [README.md#L52-L52](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L52-L52), [README.md#L279-L290](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L279-L290)
  - [observation/documented] SequentialWorkflow runs agents in a strict linear pipeline where each agent's output feeds the next agent's input. -- evidence: [README.md#L265-L265](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L265-L265), [README.md#L318-L318](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L318-L318), [README.md#L298-L298](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L298-L298)
- tools-permissions (1 claim(s)):
  - [observation/documented] MCPDeployer servers support static API keys, a custom auth callable reading request headers, or an MCP TokenVerifier with required scopes; servers refuse to start without auth unless allow_anonymous=True is passed. -- evidence: [README.md#L214-L215](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L214-L215), [README.md#L232-L232](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L232-L232)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The package is installable via pip, uv, or poetry, and from source by cloning the repository and installing requirements.txt; a prebuilt Docker image kyegomez/swarms is also published. -- evidence: [README.md#L73-L75](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L73-L75), [README.md#L92-L93](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L92-L93), [README.md#L67-L69](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L67-L69), [README.md#L81-L84](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L81-L84), [README.md#L59-L61](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L59-L61)
  - [observation/documented] Configuration uses environment variables including OPENAI_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY, and WORKSPACE_DIR, with further setup documented externally. -- evidence: [README.md#L108-L108](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L108-L108), [README.md#L110-L115](https://github.com/kyegomez/swarms/blob/9f51ebc3dd702d71a28f75c308631506b8e00cc0/README.md#L110-L115)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(11 additional claim(s) omitted for length; see [full detail](swarms.detail.md) for every claim.)

Metadata and full claim list: [full detail](swarms.detail.md)
Human notes ([notes](swarms.notes.md), never overwritten by build)

[Back to map index](../../index.md)
