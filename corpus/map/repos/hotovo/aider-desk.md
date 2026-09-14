# hotovo/aider-desk

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cb7ee89bf213 @ 81767ba6a21ef502

## Summary (orientation draft, not independently verified)

Selected evidence records: The agent runtime is built on the Vercel AI SDK; SDK message parts are the runtime currency, while persistence uses AiderDesk's own ContextMessage types, converted at the agent boundary in src/main/agent/utils.ts. MCP is the standard tool boundary: servers connect via stdio or HTTP transports, tools are namespaced as <server><sep><tool>, and every invocation passes through the ApprovalManager.

## Source coverage

Source coverage (partial): 6 of 47 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Agent behavior is modeled as AgentProfile entities managed by agent-profile-manager.ts, with system prompts assembled via a prompts system supporting placeholder substitution; subagents are profiles invoked by a parent profile. -- evidence: [docs/adr/agent-system/0007-agent-profiles-and-system-prompts.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0007-agent-profiles-and-system-prompts.md#L32-L32)
- design-choices (3 claim(s)):
  - [observation/documented] The agent runtime is built on the Vercel AI SDK; SDK message parts are the runtime currency, while persistence uses AiderDesk's own ContextMessage types, converted at the agent boundary in src/main/agent/utils.ts. -- evidence: [docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0005-vercel-ai-sdk-as-agent-runtime.md#L32-L32)
  - [observation/documented] MCP is the standard tool boundary: servers connect via stdio or HTTP transports, tools are namespaced as <server><sep><tool>, and every invocation passes through the ApprovalManager. -- evidence: [docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L32-L32](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/agent-system/0006-mcp-for-tool-extensibility.md#L32-L32)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: every ADR must include a mandatory 'Guardrails for Agents' section with do/don't rules, and changes conflicting with an ADR require updating the ADR first or changing the approach. -- evidence: [docs/adr/README.md#L7-L7](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L7-L7)
  - [observation/documented] Repository development practice: new ADRs follow a template with global sequential numbering, retroactive ADRs may be Accepted only after verification against current source, and Accepted decisions are never edited in place. -- evidence: [docs/adr/README.md#L76-L80](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L76-L80), [docs/adr/template.md#L7-L7](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/template.md#L7-L7), [docs/adr/README.md#L103-L103](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/docs/adr/README.md#L103-L103)
- skills-patterns (1 claim(s)):
  - [observation/documented] Reusable expertise is packaged as Skills that load on demand with progressive disclosure to keep token usage lean; users can also inject custom shell commands, linters, and test suites into the AI's toolkit. -- evidence: [README.md#L85-L85](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L85-L85)
- interfaces (2 claim(s)):
  - [observation/documented] AiderDesk can connect to standard MCP servers for scoped access to external data, and can also expose itself as an MCP server to clients like Claude Desktop or Cursor. -- evidence: [README.md#L81-L81](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L81-L81)
  - [observation/documented] The product exposes a REST API for integrating AiderDesk with external tools and workflows, per the README capabilities list. -- evidence: [README.md#L91-L97](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L91-L97)
- memory-state (2 claim(s)):
  - [observation/documented] A smart context and memory engine uses vector embeddings (LanceDB) and repository mapping for semantic code search, with users able to pin documentation URLs and code symbols. -- evidence: [README.md#L52-L57](https://github.com/hotovo/aider-desk/blob/cb7ee89bf2131d4006eae69c96c5f7121346a1d8/README.md#L52-L57)
More evidence: [full detail](aider-desk.detail.md)

Metadata and full claim list: [full detail](aider-desk.detail.md)
Human notes ([notes](aider-desk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
