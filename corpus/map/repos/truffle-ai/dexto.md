# truffle-ai/dexto

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a910e0ef36f2 @ 491bca189af9a968

## Summary (orientation draft, not independently verified)

Dexto is a YAML-configured agent harness (Beta, Elastic License 2.0) with CLI/Web UI/server/MCP run modes, a TypeScript SDK, MCP tool integration, sub-agent spawning, persistent sessions and memory, configurable storage, and opt-out telemetry. All claims below are product-documentation observations from the README and memory docs; contributor-workflow claims were dropped per correction instructions. Evidence coverage: 194 of 289 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 101 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Dexto is described as an agent harness that turns LLMs into reliable, stateful agents able to take actions, remember context, and recover from errors, with agents defined in YAML configuration files. -- evidence: [README.md#L456-L456](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L456-L456), [README.md#L54-L56](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L54-L56), [README.md#L41-L41](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L41-L41)
- components (2 claim(s)):
  - [observation/documented] Storage is configurable with cache backends Redis or in-memory and database backends PostgreSQL, SQLite, or in-memory, plus session settings like maxSessions and sessionTTL. -- evidence: [README.md#L420-L423](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L420-L423), [README.md#L412-L418](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L412-L418), [README.md#L425-L427](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L425-L427)
  - [observation/documented] An MCPManager class in @dexto/core connects to MCP servers, exposes tools, prompts, and resources, executes tools, and disconnects all servers. -- evidence: [README.md#L395-L398](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L395-L398), [README.md#L388-L393](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L388-L393), [README.md#L400-L401](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L400-L401), [README.md#L403-L404](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L403-L404), [README.md#L383-L384](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L383-L384)
- design-choices (1 claim(s)):
  - [observation/documented] Agents are configuration-driven: each YAML file defines a unique agent combining LLM, MCP servers, system prompt, storage, and permissions, and reloading the file updates state, memory, and tools without code changes. -- evidence: [README.md#L456-L456](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L456-L456), [README.md#L482-L484](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L482-L484), [README.md#L54-L56](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L54-L56), [README.md#L460-L463](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L460-L463), [README.md#L471-L472](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L471-L472)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Dexto offers multiple run modes: Web UI (default), interactive CLI, server mode exposing REST and SSE APIs, and MCP server mode over stdio, with Discord and Telegram example integrations. -- evidence: [README.md#L245-L245](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L245-L245), [README.md#L273-L273](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L273-L273), [README.md#L238-L243](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L238-L243)
  - [observation/documented] CLI options include -a/--agent, -m/--model, --auto-approve, --no-elicitation, --mode, and --port, plus commands such as setup, deploy, agents install/list, session management, and search. -- evidence: [README.md#L604-L610](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L604-L610), [README.md#L612-L619](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L612-L619)
- memory-state (2 claim(s)):
  - [observation/documented] A memory system stores persistent information (preferences, context, facts, learned patterns) across sessions, supports tagging and pinned memories auto-loaded into system prompts, and can be viewed or cleared via the Web UI. -- evidence: [docs/examples/memory.md#L56-L56](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/examples/memory.md#L56-L56), [docs/examples/memory.md#L42-L45](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/examples/memory.md#L42-L45), [docs/docs/guides/configuring-dexto/memory.md#L18-L23](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/docs/guides/configuring-dexto/memory.md#L18-L23), [docs/docs/guides/configuring-dexto/memory.md#L25-L25](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/docs/guides/configuring-dexto/memory.md#L25-L25)
  - [observation/documented] Conversations persist across restarts; the CLI supports continuing the last conversation (-c), resuming a specific session (-r), and searching history, and the SDK exposes session history and message search. -- evidence: [README.md#L205-L205](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L205-L205), [README.md#L208-L208](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L208-L208), [README.md#L350-L353](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L350-L353), [README.md#L201-L201](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L201-L201), [README.md#L355-L357](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L355-L357), [README.md#L211-L212](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L211-L212)
- orchestration (1 claim(s)):
More evidence: [full detail](dexto.detail.md)

Metadata and full claim list: [full detail](dexto.detail.md)
Human notes ([notes](dexto.notes.md), never overwritten by build)

[Back to map index](../../index.md)
