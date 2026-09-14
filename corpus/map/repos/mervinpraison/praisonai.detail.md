# mervinpraison/praisonai -- full detail

[Back to orientation](praisonai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mervinpraison/praisonai/43a106db26d399d312370f8eeca949a5ba135c5b/462851b4fd2f608d.json](../../../wiki/dossiers/mervinpraison/praisonai/43a106db26d399d312370f8eeca949a5ba135c5b/462851b4fd2f608d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The framework is framed as a five-layer stack (prompt, context, harness, loop, graph) plus a managed layer deciding where the agent runs, with each layer wrapping the one inside. -- evidence: [README.md#L139-L146](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L139-L146), [README.md#L114-L114](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L114-L114), [README.md#L118-L137](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L118-L137) (`clm_0c0c6fa241303cc5730cafd03f5423522d821313b173d4fac6bb3131cc9b838e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The core Python SDK exposes an Agent class constructed with parameters like instructions, role, goal, and output, and started via agent.start(...). -- evidence: [README.md#L155-L161](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L155-L161), [README.md#L101-L103](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L101-L103), [README.md#L106-L108](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L106-L108) (`clm_0d67bfe9ac7af15639aedb57120150e81a03a41c0f21ee6a3c6e520b941f92e7`)
- [observation/documented] MCP servers are attached as tools via MCP(), supporting stdio commands, HTTP URLs, and WebSocket endpoints with auth tokens and environment variables. -- evidence: [README.md#L503-L510](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L503-L510), [README.md#L512-L512](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L512-L512), [README.md#L500-L500](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L500-L500), [README.md#L497-L497](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L497-L497), [README.md#L494-L494](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L494-L494) (`clm_da0fe3e18e76737aabb7a4360f6da53c48a6dddb83d98c4b43058eb7b7173f73`)
- [observation/documented] Custom tools are defined with an @tool decorator on plain Python functions whose docstrings describe usage to the model. -- evidence: [README.md#L187-L190](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L187-L190), [README.md#L556-L561](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L556-L561), [README.md#L519-L522](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L519-L522) (`clm_9b035dfcd9c4e8efe879df445e4c7f55598bcaa6cfb1f8019b0b976603d70b89`)
- [observation/documented] AgentFlow composes multi-step graphs with route(), parallel(), and repeat() steps, and the same graph can be expressed in YAML without Python. -- evidence: [README.md#L231-L239](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L231-L239), [README.md#L241-L241](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L241-L241), [README.md#L227-L229](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L227-L229) (`clm_77465c804367522c8b66964e7a27fe7d080893a3d6f216df1012e4750e80620a`)
- [observation/documented] The praisonai CLI offers subcommands for workflows, memory, knowledge, sessions, tools, MCP, scheduling, and managed sandboxes such as 'managed ps' and 'managed stop --all'. -- evidence: [README.md#L325-L328](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L325-L328), [README.md#L706-L718](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L706-L718) (`clm_d4ed013b3ee1954ed979bde78b4afb0dbebdff6c70ed0ea5aeb83556d79f7392`)

## memory-state (2 claim(s))

- [observation/documented] Agents accept memory, knowledge, and context parameters for persistence, selective retrieval, and auto-compaction, and handoffs isolate sub-agents to recent messages plus intersecting tools. -- evidence: [README.md#L178-L178](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L178-L178), [README.md#L170-L176](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L170-L176) (`clm_d8a7b329bbd820169566b5ced2372733cf6a5c0730cd6dc20d944a8b44acd6fa`)
- [observation/documented] Conversation state can be persisted to databases by passing a db() object with a database_url and session_id in the memory config, with messages, runs, and traces auto-persisted. -- evidence: [README.md#L571-L579](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L571-L579), [README.md#L568-L569](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L568-L569) (`clm_9d418cdc7c4c65e2593b9f4c968b8cba197e24d918117c981a2193312f90869e`)

## orchestration (2 claim(s))

- [observation/documented] Tool execution can be offloaded to shared sandboxes via tools_run_on with backends including docker, e2b, modal, daytona, flyio, and others, so steps in a flow share one sandbox filesystem. -- evidence: [README.md#L259-L261](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L259-L261), [README.md#L284-L286](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L284-L286), [README.md#L251-L251](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L251-L251) (`clm_e80065a90d4718f5fcec188c5a94a9f3c5b16da5b398ea34e8367ff0ee743544`)
- [observation/documented] A whole agent (model calls, loop, and tools) can be placed on a managed runtime via run_on, e.g. run_on="anthropic" hosted or run_on="docker" self-hosted; invalid targets raise a TypeError. -- evidence: [README.md#L289-L292](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L289-L292), [README.md#L309-L315](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L309-L315) (`clm_a52eae588fa7fd2c1606a8a8d4d4a65057dc1e9fdba32976f5dd86b230d97cc0`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents support an approval=True option described as a human gate before risky tools run, alongside guardrails and hooks in the harness layer. -- evidence: [README.md#L139-L146](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L139-L146), [README.md#L192-L199](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L192-L199) (`clm_6026a1114b459f592abc0b17eb768f9e2271d75799f991f52830f5b0591da263`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Distribution is split into a core SDK (pip install praisonaiagents), a CLI package (pip install praisonai), optional extras for claw, flow, and ui, and an npm package named praisonai. -- evidence: [README.md#L95-L99](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L95-L99), [README.md#L342-L346](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L342-L346), [README.md#L65-L66](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L65-L66), [README.md#L350-L352](https://github.com/MervinPraison/PraisonAI/blob/43a106db26d399d312370f8eeca949a5ba135c5b/README.md#L350-L352) (`clm_5257b89cd44710650b619e7f2e0830cd35aa49f7573c4d885bb5e6e4352f128f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

