# linghungegeg/linghun -- full detail

[Back to orientation](linghun.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/linghungegeg/linghun/05d8457bd04aa1b0eec4608e4effccf799bd43ad/64bad13006da78ed.json](../../../wiki/dossiers/linghungegeg/linghun/05d8457bd04aa1b0eec4608e4effccf799bd43ad/64bad13006da78ed.json)

## specifications (1 claim(s))

- [observation/documented] Linghun is described as a local-first, evidence-first AI coding terminal that connects large models to real projects, tools, permissions, verification, and context. -- evidence: [README.md#L5-L5](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L5-L5), [README.md#L7-L7](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L7-L7), [README.md#L27-L27](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L27-L27) (`clm_33fbf20b1a9930d2c3b7f4daf116b17ef5b15228bc3360e9f870c0fcf93b6dbc`)

## components (2 claim(s))

- [observation/documented] Built-in tool paths include Read, Write, Edit, MultiEdit, Grep, Glob, Bash, Todo, Diff, and Git, with file writes and commands passing through permission, path, security, and result-summary boundaries. -- evidence: [README.md#L338-L338](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L338-L338) (`clm_2bf2731d4e64bd81e8671568e3a767596dbdc0b32bea71fc66ab42e5fda68c39`)
- [observation/documented] The CLI package bundles a codebase-memory-mcp binary for Windows x64, Linux x64, and macOS on both Apple Silicon and Intel. -- evidence: [README.md#L364-L367](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L364-L367), [README.md#L362-L362](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L362-L362) (`clm_bb97a1f1030db0d6558f04c5b423b68c51a192d99bffebcc30a167aa16333d59`)

## design-choices (2 claim(s))

- [observation/documented] The design philosophy places key constraints at the system layer rather than in prompts: tool execution, permissions, evidence, verification, Git, indexing, caching, and failure learning form one main chain. -- evidence: [README.md#L133-L133](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L133-L133), [README.md#L135-L135](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L135-L135) (`clm_576e25eef5c87199f9db080e6fe52691f59352e8af40aff6c45650f530af0c0b`)
- [observation/documented] Verification-aware delivery distinguishes PASS, PARTIAL, FAIL, TIMEOUT, STALE, and CANCELLED outcomes, and separates focused verification, mock verification, real smoke tests, and unverified conclusions. -- evidence: [README.md#L352-L352](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L352-L352) (`clm_b6f85409ad478c4725a2be0b01b43bca46bd2193ea35b232612ebe815ea6d790`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: an internal execution-plan document mandates strict phase ordering (phases 0-7), per-phase minimal verification, independent re-checks, recorded completed/blocked items, and forbids skipping phases or substituting hidden text fixes for underlying event fixes. -- evidence: [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L15-L19](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L15-L19), [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L9-L11](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L9-L11), [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L21-L21](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L21-L21) (`clm_9499e3bc21ee02dc53feffca3a2aec0cde6969986b826abe5e9e558ad16c45e4`)
- [observation/documented] Repository development practice: the execution plan requires establishing a fact baseline of Linghun and CCB call chains without modifying business code, with deliverables including call-chain comparison tables, output-source inventories, and minimal reproducible examples. -- evidence: [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L155-L159](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L155-L159), [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L137-L137](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L137-L137) (`clm_296e1809b87e6ea4d1321eba9b23196215f0f053106c434efddc211a14a2aaec`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product is distributed as the npm package @linghun/cli, installed globally and launched with the `linghun` command; a capitalized `Linghun` entry is also supported on Windows. -- evidence: [README.md#L189-L191](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L189-L191), [README.md#L195-L197](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L195-L197), [README.md#L193-L193](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L193-L193), [README.md#L183-L185](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L183-L185), [README.md#L20-L23](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L20-L23) (`clm_98cc2cf2cb779bf3faeaf66ac7c4b018f1e5b4f07fcbb645f141a38fcfca5cc1`)
- [observation/documented] Model configuration is done via a `/model setup` wizard asking for API base URL, API key, model name, and reasoning level; `/model doctor` checks provider configuration. -- evidence: [README.md#L215-L218](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L215-L218), [README.md#L209-L211](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L209-L211), [README.md#L224-L226](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L224-L226) (`clm_9d54b6a1238fb0756d0648211894a33aa4420fcfda720c62a226055456511d1e`)
- [observation/documented] The App Bridge currently supports only a Local HTTP Connector: transport must be http and baseUrl must be loopback (localhost, 127.0.0.1, or [::1]); external apps implement GET /linghun/capabilities and POST /linghun/execute, validated via /apps validate and connected via /apps connect. -- evidence: [README.md#L524-L528](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L524-L528), [README.md#L530-L530](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L530-L530) (`clm_59057bff1521de1b2fa4b2c439ab621a87f3d975d8a8ac95d7d7221731a0e985`)
- [observation/documented] The provider runtime supports OpenAI-compatible, DeepSeek, and Anthropic Messages-style endpoints with streaming, tool calls, usage, reasoning, timeouts, and provider diagnostics; the main screen does not leak provider, baseUrl, endpointProfile, or plaintext keys. -- evidence: [README.md#L401-L401](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L401-L401), [README.md#L399-L399](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L399-L399) (`clm_9f65794d16e696936cf50332b67a7cdc78adb5ebdb09fd92cd7df9c7c20fce29`)

## memory-state (2 claim(s))

- [observation/documented] API keys are stored by default in a user-level private provider.env outside the project; configuration precedence is shell environment variables, then provider.env, then project/default settings. -- evidence: [README.md#L220-L220](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L220-L220) (`clm_49f9fbd62a87eb4fc6debc663d14c1ad79df1f18480a892b9731ed7f5c1fdd05`)
- [observation/documented] At startup Linghun detects LINGHUN.md; if missing it only gives a light prompt and does not auto-write it, creating a base template only when the user explicitly runs /memory init. -- evidence: [README.md#L415-L415](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L415-L415) (`clm_bd6174f8da110bcabc442682c62d035851006ed9c6d63e0fd023eea9a8cf24e5`)

## orchestration (2 claim(s))

- [observation/documented] A central scheduler combines task type, permissions, evidence, memory, failure records, provider state, workflow state, user state, context pressure, and verification needs to decide each turn's route (read code, clarify, verify, chat, or enter complex task flows). -- evidence: [README.md#L431-L431](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L431-L431), [README.md#L433-L433](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L433-L433) (`clm_9bf1f7346e3e1cfdd9cba101b262c4e644305b116a4db78eca34b7db7d767d5b`)
- [observation/documented] Workflow Matrix decomposes complex goals into phase, slice, role, risk hint, runtime proposal, and evidence requirement, reusing /job, /fork, /agents, verification, and Git stable-point suggestions at the execution layer. -- evidence: [README.md#L389-L389](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L389-L389) (`clm_7b25ad77dd48817528f587ebd28b2b03b3fe1b3f85706b3e765502bb6b5880e7`)

## tools-permissions (1 claim(s))

- [observation/documented] The runtime permission model keeps code execution on the local machine, stores provider keys outside the project, and routes remote channels, external capabilities, file writes, Bash, Git, and index refreshes back through local permission boundaries. -- evidence: [README.md#L346-L346](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L346-L346) (`clm_f036c8f398e19d277da0754533b2463056daa7aeb71b6e6bc42c36837ea22a84`)

## evaluation (1 claim(s))

- [observation/documented] The README reports a Terminal-Bench 2.1 submission with a pending PR (#165) and a current score of 78.43%, noting official ranking is pending the PR merge. -- evidence: [README.md#L35-L35](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L35-L35), [README.md#L37-L37](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L37-L37) (`clm_dc6bc4e9c07a48539c7844a5947eca8d886b433b25f0518903ca7ef6daaa7a45`)

## dependencies (1 claim(s))

- [observation/documented] The CLI requires Node.js 22 or newer and a Node package manager such as npm or pnpm; the README badge also marks the project as Windows-first and Apache-2.0 licensed. -- evidence: [README.md#L9-L14](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L9-L14), [README.md#L178-L179](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L178-L179) (`clm_e65d0200556dfb9f3eb90f17254264fa68d1b2ea7f7a92d06948e3aa07ad79dc`)

## limitations (2 claim(s))

- [observation/documented] The README states the reported scenario-based gains (e.g., +25% to +50% for complex tasks) are architecture-level estimates, not precise measurements or speedup promises for arbitrary projects. -- evidence: [README.md#L161-L168](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L161-L168), [README.md#L170-L170](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/README.md#L170-L170) (`clm_0880ace14152d4fc9ee4d22cb0815d6e1b9cb15f3f8178e8eca23407603b6731`)
- [observation/documented] Per the execution plan, Linghun's agent-tree-enter currently only sets expandedId to expand details and does not switch into a sub-agent transcript like CCB's viewingAgentTaskId does. -- evidence: [docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L94-L94](https://github.com/linghungegeg/Linghun/blob/05d8457bd04aa1b0eec4608e4effccf799bd43ad/docs/LINGHUN_CCB_TOOL_OUTPUT_EXECUTION_PLAN.md#L94-L94) (`clm_e4e336260875350bf56ab19875be4e49415e115843e29472075ce552c641ef07`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

