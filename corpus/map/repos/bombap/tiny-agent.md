# bombap/tiny-agent

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 58ecae062ec6 @ f365606f97822f06

## Summary (orientation draft, not independently verified)

TinyAgent is a minimal ReAct-pattern agent runtime in TypeScript with a configurable personality prompt system, extensible tools/providers, and a bounded message buffer; evidence covers README features and the ReactAgentRuntime/context source.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 4 documented, 8 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/code-inspected] A ReactAgentRuntime class implements IAgentRuntime, holding an LLMEngine, tools, providers, clients, state, and a message buffer. -- evidence: [src/runtimes/reactRuntime.ts#L15-L23](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L15-L23), [src/runtimes/reactRuntime.ts#L13-L13](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L13-L13)
  - [observation/code-inspected] buildContext substitutes {{key}} placeholders in templates with string values from the agent state. -- evidence: [src/context.ts#L4-L16](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L4-L16)
- design-choices (3 claim(s)):
  - [observation/documented] The README advertises a ReAct (Reasoning & Acting) pattern implementation as a core feature of the agent. -- evidence: [README.md#L17-L22](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L17-L22)
  - [observation/documented] The project positions itself as a tinier, cleaner, less cluttered alternative to Eliza. -- evidence: [README.md#L7-L9](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L7-L9)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: setup instructions say to install dependencies with pnpm install, copy .env.example to .env, and run the agent with pnpm dev. -- evidence: [README.md#L29-L32](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L29-L32), [README.md#L39-L42](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L39-L42), [README.md#L34-L37](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L34-L37)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/code-inspected] The runtime provides public methods to add clients, tools and providers, merge state updates, and disconnect all registered clients. -- evidence: [src/runtimes/reactRuntime.ts#L149-L151](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L149-L151), [src/runtimes/reactRuntime.ts#L169-L171](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L169-L171), [src/runtimes/reactRuntime.ts#L137-L139](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L137-L139), [src/runtimes/reactRuntime.ts#L157-L159](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L157-L159), [src/runtimes/reactRuntime.ts#L184-L189](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L184-L189)
- memory-state (1 claim(s)):
  - [observation/code-inspected] The scratchpad is capped at 33 steps (oldest trimmed) and the message buffer at 33 messages with oldest-message eviction. -- evidence: [src/runtimes/reactRuntime.ts#L173-L178](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L173-L178), [src/runtimes/reactRuntime.ts#L101-L106](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L101-L106), [src/runtimes/reactRuntime.ts#L15-L23](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L15-L23)
- orchestration (3 claim(s)):
  - [observation/code-inspected] The runtime loops calling _step() until state.completed is set; with SAFE_MODE enabled it stops after MAX_STEPS steps (default 20 from the MAX_STEPS env var). -- evidence: [src/runtimes/reactRuntime.ts#L11-L11](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L11-L11), [src/runtimes/reactRuntime.ts#L47-L60](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L47-L60)
  - [observation/code-inspected] Each step builds a context from a React template and a system prompt from a personality template, generates text via the LLM engine, and parses a JSON block from the response. -- evidence: [src/runtimes/reactRuntime.ts#L90-L92](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L90-L92), [src/runtimes/reactRuntime.ts#L86-L88](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L86-L88), [src/runtimes/reactRuntime.ts#L77-L81](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L77-L81), [src/runtimes/reactRuntime.ts#L83-L84](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L83-L84)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](tiny-agent.detail.md) for every claim.)

Metadata and full claim list: [full detail](tiny-agent.detail.md)
Human notes ([notes](tiny-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
