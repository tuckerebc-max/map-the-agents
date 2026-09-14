# bombap/tiny-agent -- full detail

[Back to orientation](tiny-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bombap/tiny-agent/58ecae062ec6a7d405bda84447d774e5070bfa4d/f365606f97822f06.json](../../../wiki/dossiers/bombap/tiny-agent/58ecae062ec6a7d405bda84447d774e5070bfa4d/f365606f97822f06.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/code-inspected] A ReactAgentRuntime class implements IAgentRuntime, holding an LLMEngine, tools, providers, clients, state, and a message buffer. -- evidence: [src/runtimes/reactRuntime.ts#L15-L23](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L15-L23), [src/runtimes/reactRuntime.ts#L13-L13](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L13-L13) (`clm_77e00c46cd02a6f9d08325b5d0bc0b50619912d6994148731918f78d584db585`)
- [observation/code-inspected] buildContext substitutes {{key}} placeholders in templates with string values from the agent state. -- evidence: [src/context.ts#L4-L16](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L4-L16) (`clm_8884f29d1726d1e73b8999f7cf01cc19927c0e1c0fdbdbc27387525ee8f1ba7a`)
- [observation/code-inspected] formatPersonality renders an IAgentPersonality into prompt sections: Identity, Biography, Background Lore, Personality Style, and Rules. -- evidence: [src/context.ts#L42-L45](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L42-L45), [src/context.ts#L53-L54](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L53-L54), [src/context.ts#L47-L48](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L47-L48), [src/context.ts#L50-L51](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L50-L51), [src/context.ts#L56-L58](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/context.ts#L56-L58) (`clm_b287b4de7a75e9387c63bf06e93a9e4044a2af33d96872883ca83c662a713f43`)

## design-choices (3 claim(s))

- [observation/documented] The README advertises a ReAct (Reasoning & Acting) pattern implementation as a core feature of the agent. -- evidence: [README.md#L17-L22](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L17-L22) (`clm_ae0271fae68ec1f787bd8958fd953443d651599cf2aa7e97e1d1cf55903657ce`)
- [observation/documented] The project positions itself as a tinier, cleaner, less cluttered alternative to Eliza. -- evidence: [README.md#L7-L9](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L7-L9) (`clm_142aa1ab5d39a3fc8cec97df5df6ba57cf5eae66f4ed9350700145b0b998f63c`)
- [observation/documented] The README lists a configurable personality system, extensible tool system, multi-client support, and modular architecture as features. -- evidence: [README.md#L17-L22](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L17-L22) (`clm_85f25c666cabbcce24b537db05da1f153ba53ea74cfedba5a9d51fe061f73cfc`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: setup instructions say to install dependencies with pnpm install, copy .env.example to .env, and run the agent with pnpm dev. -- evidence: [README.md#L29-L32](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L29-L32), [README.md#L39-L42](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L39-L42), [README.md#L34-L37](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/README.md#L34-L37) (`clm_98a214d5f2b19ca9dce9cfca1629c910e119ea54dbbdbf8d831c42243f5b859d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/code-inspected] The runtime provides public methods to add clients, tools and providers, merge state updates, and disconnect all registered clients. -- evidence: [src/runtimes/reactRuntime.ts#L149-L151](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L149-L151), [src/runtimes/reactRuntime.ts#L169-L171](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L169-L171), [src/runtimes/reactRuntime.ts#L137-L139](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L137-L139), [src/runtimes/reactRuntime.ts#L157-L159](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L157-L159), [src/runtimes/reactRuntime.ts#L184-L189](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L184-L189) (`clm_86f277892e2f2221b21f5e995766cdb9f650b7a75d06db8aaee5d39ac928ab52`)

## memory-state (1 claim(s))

- [observation/code-inspected] The scratchpad is capped at 33 steps (oldest trimmed) and the message buffer at 33 messages with oldest-message eviction. -- evidence: [src/runtimes/reactRuntime.ts#L173-L178](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L173-L178), [src/runtimes/reactRuntime.ts#L101-L106](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L101-L106), [src/runtimes/reactRuntime.ts#L15-L23](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L15-L23) (`clm_27543b930701c920272a3b40b09909e94d0831ca67bb9b24d05503bb88d6a7f6`)

## orchestration (3 claim(s))

- [observation/code-inspected] The runtime loops calling _step() until state.completed is set; with SAFE_MODE enabled it stops after MAX_STEPS steps (default 20 from the MAX_STEPS env var). -- evidence: [src/runtimes/reactRuntime.ts#L11-L11](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L11-L11), [src/runtimes/reactRuntime.ts#L47-L60](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L47-L60) (`clm_efd654a61f1bab9ba1b02582a6721c5b905b9d2071e2fbf0ad403f3b6407e6c4`)
- [observation/code-inspected] Each step builds a context from a React template and a system prompt from a personality template, generates text via the LLM engine, and parses a JSON block from the response. -- evidence: [src/runtimes/reactRuntime.ts#L90-L92](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L90-L92), [src/runtimes/reactRuntime.ts#L86-L88](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L86-L88), [src/runtimes/reactRuntime.ts#L77-L81](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L77-L81), [src/runtimes/reactRuntime.ts#L83-L84](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L83-L84) (`clm_9b9395caa51b0c884f89e569ffc219122b021a5f0128953bb7d9258eafb9c376`)
- [observation/code-inspected] Parsed responses append Thought/Action/Observation entries to a scratchpad; actions are matched to tools by name and executed with the action input, with unknown tools logged as an observation. -- evidence: [src/runtimes/reactRuntime.ts#L98-L99](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L98-L99), [src/runtimes/reactRuntime.ts#L108-L122](https://github.com/bombap/tiny-agent/blob/58ecae062ec6a7d405bda84447d774e5070bfa4d/src/runtimes/reactRuntime.ts#L108-L122) (`clm_ce1fbfb04a9709b6aa96cf5679f538def96df57b59f027a9981ae973bdb03a53`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_e518af201242fa346508b809e3d2fc4167332afb53bed9bab43b187a3b772242

