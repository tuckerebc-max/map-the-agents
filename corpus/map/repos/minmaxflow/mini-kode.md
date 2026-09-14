# minmaxflow/mini-kode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4e7f9767e5ca @ 270e8b959f6026a5

## Summary (orientation draft, not independently verified)

Selected evidence records: Mini-Kode is an educational project to help developers understand modern coding-agent architecture, described as a complete yet manageable implementation of about 14K lines of production code. The product is invoked as the mini-kode command; it supports an interactive mode (bare command) and a non-interactive mode that executes a task supplied as a quoted argument.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Mini-Kode is an educational project to help developers understand modern coding-agent architecture, described as a complete yet manageable implementation of about 14K lines of production code. -- evidence: [README.md#L9-L9](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L9-L9), [README.md#L3-L3](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The source tree is organized into modules for tools, Ink-based UI, LLM client, permissions, config, CLI, agent logic, sessions, and shared utilities. -- evidence: [README.md#L104-L115](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L104-L115)
- design-choices (1 claim(s)):
  - [observation/documented] The architecture is layered: a terminal UI layer, an agent layer coordinating the LLM-plus-tool loop, an LLM layer with streaming and tool parsing, a tool layer, and an infrastructure layer for config and permissions. -- evidence: [docs/architecture.md#L5-L5](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/architecture.md#L5-L5), [docs/architecture.md#L11-L47](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/architecture.md#L11-L47)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors need Bun and pnpm, install with pnpm install, and use pnpm run dev, pnpm run build, and pnpm run test for development, building, and testing. -- evidence: [README.md#L83-L84](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L83-L84), [README.md#L77-L77](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L77-L77), [README.md#L64-L65](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L64-L65), [README.md#L80-L80](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L80-L80), [README.md#L69-L71](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L69-L71)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is invoked as the mini-kode command; it supports an interactive mode (bare command) and a non-interactive mode that executes a task supplied as a quoted argument. -- evidence: [README.md#L57-L58](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L57-L58), [README.md#L52-L52](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L52-L52), [README.md#L54-L54](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L54-L54)
  - [observation/documented] MCP servers are configured via .mini-kode/mcp.json with stdio and http transports; tools from connected servers are auto-registered, and ${ENV_VAR} references in args and headers are resolved from the environment. -- evidence: [docs/config.md#L140-L141](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L140-L141), [docs/tools.md#L129-L129](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L129-L129), [docs/config.md#L166-L169](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L166-L169), [docs/tools.md#L133-L136](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L133-L136), [docs/config.md#L136-L136](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L136-L136), [docs/config.md#L145-L145](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L145-L145)
- memory-state (1 claim(s)):
  - [observation/documented] The system reads an AGENTS.md file from the project root and includes it in system prompts, providing persistent project context across sessions that users can edit. -- evidence: [README.md#L96-L96](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L96-L96), [docs/llm-tool-integration.md#L80-L83](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L80-L83), [README.md#L98-L100](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L98-L100), [docs/llm-tool-integration.md#L78-L78](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L78-L78)
- orchestration (1 claim(s)):
  - [observation/documented] The agent executor runs a loop: build context, send the request with tool descriptions to the LLM, parse text or tool calls, execute tools, feed results back, and repeat until a final response; conversation length is managed via auto-compaction. -- evidence: [docs/llm-tool-integration.md#L87-L87](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L87-L87), [docs/llm-tool-integration.md#L70-L74](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L70-L74), [docs/llm-tool-integration.md#L47-L50](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L47-L50), [docs/architecture.md#L79-L83](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/architecture.md#L79-L83)
- tools-permissions (2 claim(s)):
More evidence: [full detail](mini-kode.detail.md)

Metadata and full claim list: [full detail](mini-kode.detail.md)
Human notes ([notes](mini-kode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
