# hotovo/aider-desk -- full detail

[Back to orientation](aider-desk.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hotovo/aider-desk/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/81767ba6a21ef502.json](../../../wiki/dossiers/hotovo/aider-desk/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/81767ba6a21ef502.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Agent behavior is modeled as AgentProfile entities managed by agent-profile-manager.ts, with system prompts assembled via a prompts system supporting placeholder substitution; subagents are profiles invoked by a parent profile. -- evidence: [docs/adr/agent-system/0007-agent-profiles-and-system-prompts.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0007-agent-profiles-and-system-prompts.md#L32-L32) (`clm_c99b008d74db552cc37541c39f16eb8bdd9f0c8aede342b037ae08b384a0292c`)

## design-choices (3 claim(s))

- [observation/documented] The agent runtime is built on the Vercel AI SDK; SDK message parts are the runtime currency, while persistence uses AiderDesk's own ContextMessage types, converted at the agent boundary in src/main/agent/utils.ts. -- evidence: [docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L32-L32) (`clm_ed124be0cfc3618cb36dde9851403ce8fd6d40ce5dece7df95b743bdfd8c52f1`)
- [observation/documented] MCP is the standard tool boundary: servers connect via stdio or HTTP transports, tools are namespaced as <server><sep><tool>, and every invocation passes through the ApprovalManager. -- evidence: [docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L32-L32) (`clm_300fac2017e23e353be305cb27401a8f2c09f52995941a2fee0206d0185c98e3`)
- [observation/documented] The ADR set was written retroactively by analyzing the existing codebase, documenting de-facto decisions that are descriptive of current architecture and prescriptive for future changes. -- evidence: [docs/adr/README.md#L103-L103](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L103-L103) (`clm_83588e36928427d7e20021b8153c665ff1b59d50beac42fb2faf24404ea9beea`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: every ADR must include a mandatory 'Guardrails for Agents' section with do/don't rules, and changes conflicting with an ADR require updating the ADR first or changing the approach. -- evidence: [docs/adr/README.md#L7-L7](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L7-L7) (`clm_9813c92cc8a5d7265e9f2d1e9767c0b515cc229ad39154aebb9da2144e7e5dcf`)
- [observation/documented] Repository development practice: new ADRs follow a template with global sequential numbering, retroactive ADRs may be Accepted only after verification against current source, and Accepted decisions are never edited in place. -- evidence: [docs/adr/README.md#L76-L80](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L76-L80), [docs/adr/template.md#L7-L7](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/template.md#L7-L7), [docs/adr/README.md#L103-L103](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L103-L103) (`clm_915110b53b566041c048c8578b226d2d84a2347d511aa977e073d9667ab4b760`)
- [observation/documented] Repository development practice: the ADR review checklist requires tracing call paths against source, separating current behavior from desired future state, and avoiding absolute security or durability claims unless the code enforces them. -- evidence: [docs/adr/README.md#L86-L91](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L86-L91) (`clm_2d4cd98a783a23e48c175d22742ab00c20dec9a496038197f369091daec82af3`)

## skills-patterns (1 claim(s))

- [observation/documented] Reusable expertise is packaged as Skills that load on demand with progressive disclosure to keep token usage lean; users can also inject custom shell commands, linters, and test suites into the AI's toolkit. -- evidence: [README.md#L85-L85](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L85-L85) (`clm_8c6443d6c17272ceb8d414daa5b61333f83c0303bbeb96740e7a8c9f2afdf923`)

## interfaces (2 claim(s))

- [observation/documented] AiderDesk can connect to standard MCP servers for scoped access to external data, and can also expose itself as an MCP server to clients like Claude Desktop or Cursor. -- evidence: [README.md#L81-L81](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L81-L81) (`clm_bfdeab3a107ce81461a8fe3fb6f78574b97e8724f8ba46b4ad8238f5699cb808`)
- [observation/documented] The product exposes a REST API for integrating AiderDesk with external tools and workflows, per the README capabilities list. -- evidence: [README.md#L91-L97](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L91-L97) (`clm_2eb2b0957915324c71e58973483be6eb5106787eb2ba93b71b177c0edf04d411`)

## memory-state (2 claim(s))

- [observation/documented] A smart context and memory engine uses vector embeddings (LanceDB) and repository mapping for semantic code search, with users able to pin documentation URLs and code symbols. -- evidence: [README.md#L52-L57](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L52-L57) (`clm_07b4b9eb83f4db0adc9cde9a1b14fba384b7c1c968e62db921a2bbbf02308ee2`)
- [observation/documented] Chat history, task metadata, and settings are stored locally on the user's machine in a lightweight local database, keeping workspace data private and offline. -- evidence: [README.md#L91-L97](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L91-L97) (`clm_9b92fd737eedd4215096c41eab7893509e6b7571dd6b934aebcc650c4269d4b9`)

## orchestration (1 claim(s))

- [observation/documented] Tasks can be duplicated or forked to explore alternative paths, specific messages can be deleted from chat history to curate context, and Git worktrees give each task an isolated directory with a built-in merge workflow. -- evidence: [README.md#L52-L57](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L52-L57) (`clm_1552526c4e8e5e77a298131e763368e071259007856cc45e197a6218319e144f`)

## tools-permissions (1 claim(s))

- [observation/documented] The product features tool approval gates where users approve tools and authorize destructive actions; per the ADRs, all MCP tool invocations route through the ApprovalManager. -- evidence: [docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L32-L32), [README.md#L35-L37](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L35-L37) (`clm_bd9f650e4c3d85dd5fdb4407f0d16710d10fb56eb61c8da9556d59a8c856aeac`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The frontend is built with React 19 and Tailwind CSS; the agent runtime depends on the Vercel AI SDK, with MCP support via @ai-sdk/mcp and @modelcontextprotocol/sdk. -- evidence: [docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L27-L28](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L27-L28), [README.md#L91-L97](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L91-L97), [docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L32-L32) (`clm_c78f72502626a43e2f4063c55520e33b6b6dc4eb1b2be02e8813858be74c0bf6`)

## limitations (1 claim(s))

- [inference/documented] The ADRs note trade-offs: SDK upgrades can shift part/type shapes requiring a dedicated pass, and MCP connection lifecycle issues (restarts, timeouts, unauthorized states) must be handled robustly across process boundaries. -- evidence: [docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L48-L49](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L48-L49), [docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L48-L49](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L48-L49) (`clm_f3a4b28ad837cead0e510162283f8474745ef8141638cb2f2abed046a3b4b409`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

