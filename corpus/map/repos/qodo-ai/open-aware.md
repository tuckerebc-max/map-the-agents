# qodo-ai/open-aware

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 68976a9dd957 @ c4920608ae287716

## Summary (orientation draft, not independently verified)

The evidence (README only) documents Open Aware, an MCP server by Qodo exposing three code-intelligence tools (get_context, deep_research, ask) over pre-indexed popular open-source repositories, with a free tier limited to ~10 calls/minute and an enterprise variant for private repos.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The MCP server provides three tools: get_context for semantic code search, deep_research for complex codebase analysis, and ask for basic coding questions. -- evidence: [README.md#L114-L114](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L114-L114), [README.md#L35-L38](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L35-L38)
  - [observation/documented] get_context performs semantic search using vector embeddings, supports multi-repository queries, language filtering, and configurable result limits with relevance ranking. -- evidence: [README.md#L125-L129](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L125-L129), [README.md#L123-L123](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L123-L123)
- design-choices (1 claim(s)):
  - [observation/documented] A separate enterprise product, Qodo Aware, adds private repository indexing, custom indexing schedules, zero data retention, and enterprise security and usage plans. -- evidence: [README.md#L49-L54](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L49-L54)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Prompt examples recommend including the target repository name in the prompt to help the agent focus, and show patterns for invoking open-aware, deep-research, or get-context with a repositories list. -- evidence: [README.md#L210-L214](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L210-L214), [README.md#L223-L227](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L223-L227), [README.md#L202-L207](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L202-L207), [README.md#L217-L221](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L217-L221)
- interfaces (3 claim(s)):
  - [observation/documented] Open Aware exposes its code-intelligence capabilities through the Model Context Protocol, making it usable by any MCP-compatible AI assistant or development environment. -- evidence: [README.md#L76-L76](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L76-L76), [README.md#L8-L8](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L8-L8)
  - [observation/documented] The recommended MCP configuration points clients at the streamable HTTP endpoint https://open-aware.qodo.ai/mcp. -- evidence: [README.md#L80-L88](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L80-L88)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The free service covers only pre-indexed popular open-source libraries listed in indexed_repositories.json, with indexes updated daily; queries against unindexed repositories will not work. -- evidence: [README.md#L202-L207](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L202-L207), [README.md#L35-L38](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L35-L38)
- limitations (1 claim(s)):
  - [observation/documented] The free Open Aware tier is rate-limited to roughly 10 calls per minute, offers no private-repository access, and does not allow customization of indexing or tools. -- evidence: [README.md#L42-L43](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L42-L43), [README.md#L35-L38](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L35-L38)
- relevance (1 claim(s)):
  - [observation/documented] The tool targets code discovery and analysis use cases such as architecture understanding, security analysis, feature planning, and cross-repository comparison, with an explicit disclaimer that outputs are provided as-is and require user review and security testing. -- evidence: [README.md#L278-L289](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L278-L289), [README.md#L244-L248](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L244-L248), [README.md#L315-L319](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L315-L319), [README.md#L321-L321](https://github.com/qodo-ai/open-aware/blob/68976a9dd957f493a602b1063eaca553718c9254/README.md#L321-L321)

(3 additional claim(s) omitted for length; see [full detail](open-aware.detail.md) for every claim.)

Metadata and full claim list: [full detail](open-aware.detail.md)
Human notes ([notes](open-aware.notes.md), never overwritten by build)

[Back to map index](../../index.md)
