---
access: public
aliases: []
claim_ids:
- clm_0c0c6fa241303cc5730cafd03f5423522d821313b173d4fac6bb3131cc9b838e
- clm_0d67bfe9ac7af15639aedb57120150e81a03a41c0f21ee6a3c6e520b941f92e7
- clm_5257b89cd44710650b619e7f2e0830cd35aa49f7573c4d885bb5e6e4352f128f
- clm_6026a1114b459f592abc0b17eb768f9e2271d75799f991f52830f5b0591da263
- clm_77465c804367522c8b66964e7a27fe7d080893a3d6f216df1012e4750e80620a
- clm_9b035dfcd9c4e8efe879df445e4c7f55598bcaa6cfb1f8019b0b976603d70b89
- clm_9d418cdc7c4c65e2593b9f4c968b8cba197e24d918117c981a2193312f90869e
- clm_a52eae588fa7fd2c1606a8a8d4d4a65057dc1e9fdba32976f5dd86b230d97cc0
- clm_d4ed013b3ee1954ed979bde78b4afb0dbebdff6c70ed0ea5aeb83556d79f7392
- clm_d8a7b329bbd820169566b5ced2372733cf6a5c0730cd6dc20d944a8b44acd6fa
- clm_da0fe3e18e76737aabb7a4360f6da53c48a6dddb83d98c4b43058eb7b7173f73
- clm_e80065a90d4718f5fcec188c5a94a9f3c5b16da5b398ea34e8367ff0ee743544
maturity: draft
page_id: pg_f8ec9585d33656b0a4f3d1e2739aee11
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9d8940d0cfd752b3be1362afc603db8b
title: MervinPraison/PraisonAI/README.md @ 43a106db26d3
updated_at: '2026-09-14T02:17:33Z'
---

# MervinPraison/PraisonAI/README.md @ 43a106db26d3

<!-- rcw:begin owner=source:src_9d8940d0cfd752b3be1362afc603db8b block=evidence -->
- The framework is framed as a five-layer stack (prompt, context, harness, loop, graph) plus a managed layer deciding where the agent runs, with each layer wrapping the one inside. [@claim:clm_0c0c6fa241303cc5730cafd03f5423522d821313b173d4fac6bb3131cc9b838e]
- The core Python SDK exposes an Agent class constructed with parameters like instructions, role, goal, and output, and started via agent.start(...). [@claim:clm_0d67bfe9ac7af15639aedb57120150e81a03a41c0f21ee6a3c6e520b941f92e7]
- Distribution is split into a core SDK (pip install praisonaiagents), a CLI package (pip install praisonai), optional extras for claw, flow, and ui, and an npm package named praisonai. [@claim:clm_5257b89cd44710650b619e7f2e0830cd35aa49f7573c4d885bb5e6e4352f128f]
- Agents support an approval=True option described as a human gate before risky tools run, alongside guardrails and hooks in the harness layer. [@claim:clm_6026a1114b459f592abc0b17eb768f9e2271d75799f991f52830f5b0591da263]
- AgentFlow composes multi-step graphs with route(), parallel(), and repeat() steps, and the same graph can be expressed in YAML without Python. [@claim:clm_77465c804367522c8b66964e7a27fe7d080893a3d6f216df1012e4750e80620a]
- Custom tools are defined with an @tool decorator on plain Python functions whose docstrings describe usage to the model. [@claim:clm_9b035dfcd9c4e8efe879df445e4c7f55598bcaa6cfb1f8019b0b976603d70b89]
- Conversation state can be persisted to databases by passing a db() object with a database_url and session_id in the memory config, with messages, runs, and traces auto-persisted. [@claim:clm_9d418cdc7c4c65e2593b9f4c968b8cba197e24d918117c981a2193312f90869e]
- A whole agent (model calls, loop, and tools) can be placed on a managed runtime via run_on, e.g. run_on="anthropic" hosted or run_on="docker" self-hosted; invalid targets raise a TypeError. [@claim:clm_a52eae588fa7fd2c1606a8a8d4d4a65057dc1e9fdba32976f5dd86b230d97cc0]
- The praisonai CLI offers subcommands for workflows, memory, knowledge, sessions, tools, MCP, scheduling, and managed sandboxes such as 'managed ps' and 'managed stop --all'. [@claim:clm_d4ed013b3ee1954ed979bde78b4afb0dbebdff6c70ed0ea5aeb83556d79f7392]
- Agents accept memory, knowledge, and context parameters for persistence, selective retrieval, and auto-compaction, and handoffs isolate sub-agents to recent messages plus intersecting tools. [@claim:clm_d8a7b329bbd820169566b5ced2372733cf6a5c0730cd6dc20d944a8b44acd6fa]
- MCP servers are attached as tools via MCP(), supporting stdio commands, HTTP URLs, and WebSocket endpoints with auth tokens and environment variables. [@claim:clm_da0fe3e18e76737aabb7a4360f6da53c48a6dddb83d98c4b43058eb7b7173f73]
- Tool execution can be offloaded to shared sandboxes via tools_run_on with backends including docker, e2b, modal, daytona, flyio, and others, so steps in a flow share one sandbox filesystem. [@claim:clm_e80065a90d4718f5fcec188c5a94a9f3c5b16da5b398ea34e8367ff0ee743544]
<!-- rcw:end owner=source:src_9d8940d0cfd752b3be1362afc603db8b block=evidence -->

## Researcher notes

