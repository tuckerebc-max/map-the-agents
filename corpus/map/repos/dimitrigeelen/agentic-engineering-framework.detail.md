# dimitrigeelen/agentic-engineering-framework -- full detail

[Back to orientation](agentic-engineering-framework.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/2ad642c0/0d88b5e5/35aaaaedc1c32269079b32de14aa31a7bebe2a54/a8e042de383354ce.json](../../../wiki/dossiers/2ad642c0/0d88b5e5/35aaaaedc1c32269079b32de14aa31a7bebe2a54/a8e042de383354ce.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A Component Fabric maps how code pieces relate, making a change's blast radius visible before the change rather than after. -- evidence: [README.md#L39-L43](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L39-L43) (`clm_de5e41cb55dc06640216ad9b756eed5fce68c429f99802f8d765a5da1578f526`)

## design-choices (1 claim(s))

- [observation/documented] The framework's core principle is traceability: nothing gets done without a task, with conversations, decisions, and artefacts captured in a record called the Context Fabric. -- evidence: [README.md#L32-L37](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L32-L37) (`clm_9b4a532ad64f09b6efaea344345be7a19e1f23f3ecb4fac7021de4079306b1bd`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a `fw` CLI (about 60 verbs across 11 sections) including work-on, audit, recall, fabric blast-radius, handover, serve, tier0 approve, and mcp lifecycle commands. -- evidence: [README.md#L698-L717](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L698-L717) (`clm_ba79378d9de5b1295aa6257570eb695a44253e321db25d1227ec501fa61aa929`)
- [observation/documented] A Framework MCP server exposes 22 capabilities (16 read-only, 6 agent-authority) to external agents; five sovereignty-bound verbs are deliberately never registered, and agent-authority tools shell out through bin/fw so the same gates fire. -- evidence: [README.md#L502-L507](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L502-L507) (`clm_69d3be32c32edff26ad8273753fad67457672887423e022e93b204dd645802f2`)

## memory-state (2 claim(s))

- [observation/documented] Three memory layers persist across sessions: working memory in .context/working/, project memory in .context/project/, and episodic memory of completed tasks in .context/episodic/. -- evidence: [README.md#L251-L255](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L251-L255), [README.md#L392-L395](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L392-L395) (`clm_42ed3a22da230600e92df9644d8e4aba2d18ddd7d1c987171fb7a92c244a3810`)
- [observation/documented] `fw recall` searches learnings, patterns, decisions, and episodics by meaning rather than keyword, and `fw handover --commit` writes a structured handover the next session reads on start. -- evidence: [README.md#L392-L395](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L392-L395), [README.md#L267-L269](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L267-L269), [README.md#L271-L273](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L271-L273) (`clm_9eed03bd4cd462e36b284541bccf52cd447c1b05748aa80c398525f2dc3d9d32`)

## orchestration (1 claim(s))

- [observation/documented] The framework wraps an external TermLink binary for cross-terminal, cross-host worker sessions, with bus manifest/read, dispatch send over SSH, and pickup verbs for coordination. -- evidence: [README.md#L489-L491](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L489-L491), [README.md#L493-L500](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L493-L500) (`clm_f1ff934219c8c2b10fde5cb3797cd1c5909e737680e6e3d7a51a33eda92a447f`)

## tools-permissions (3 claim(s))

- [observation/documented] A PreToolUse hook intercepts file modifications and refuses edits when no active task is set; build tasks with placeholder acceptance criteria are blocked (policy G-020). -- evidence: [README.md#L222-L225](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L222-L225), [README.md#L230-L231](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L230-L231) (`clm_b059a7d7ed3b4f852742f9ebbdf01aa4d84bd33e8a7826e6df65d85c24f2f250`)
- [observation/documented] A tiered authority model: Tier 0 destructive commands need human approval via `fw tier0 approve`, Tier 1 edits need an active task, Tier 2 exceptions are single-use and logged, Tier 3 read-only is pre-approved. -- evidence: [README.md#L333-L338](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L333-L338) (`clm_e83bc772c0ce2638c050d92f148cd129ffa3c080779829852e69977d23911b75`)
- [observation/documented] Approval verbs such as fw inception decide, fw arc close, and fw bvp confirm refuse to run under agent control and route to a human via the Watchtower dashboard. -- evidence: [README.md#L327-L331](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L327-L331) (`clm_250b88293dd96367dea437f48198c698874a270823a7a6962d13fd8789b0a5ff`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are bash 4.4+, git 2.20+, and python3 3.8+; PyYAML is optional (needed for fw serve and some helpers), and Node.js is optional with Python as fallback for TypeScript hooks. -- evidence: [README.md#L628-L634](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L628-L634) (`clm_2018c6219dfb72dfd0acb9ebefb027838218775f1c7f0a1ab9d19730b0b678e7`)

## limitations (1 claim(s))

- [observation/documented] The README states this is alpha software; multi-provider validation for Cursor, Aider, and Devin is designed but not validated, with Claude Code as the tested provider, and Watchtower auto-start is not yet shipped. -- evidence: [README.md#L641-L653](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L641-L653), [README.md#L638-L639](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L638-L639) (`clm_a703d06855b41af1fde2da0f877a5009fd53ed865795dc0dde14b0712c1c7e12`)

## relevance (1 claim(s))

- [observation/documented] The framework coordinates agents but does not execute them; it is not an agent runtime or multi-agent pipeline, and the model lives in the user's CLI agent while governance lives here. -- evidence: [README.md#L670-L670](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L670-L670), [README.md#L661-L661](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L661-L661), [README.md#L663-L668](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L663-L668) (`clm_f89df1ec02466e948c27e6ae512cda5579b82e707546d9a13546668e5ab43656`)

