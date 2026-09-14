# ref-tools/ref-tools-mcp

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 83970a356277 @ 42028e6fd913d6f0

## Summary (orientation draft, not independently verified)

Selected evidence records: Ref is a Model Context Protocol server that gives AI coding tools or agents access to documentation for APIs, services, and libraries in a token-efficient way. The server exposes a ref_search_documentation tool with a required query parameter, described as a full sentence or question, for searching public web/GitHub docs and private resources like repos and PDFs.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (4 claim(s)):
  - [observation/documented] Ref uses MCP sessions to track search trajectory and minimize context usage. -- evidence: [README.md#L37-L37](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L37-L37)
  - [observation/documented] Within a session, repeated similar searches never return duplicate results, letting the agent both page deeper and adjust its prompt. -- evidence: [README.md#L40-L40](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L40-L40)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: local development uses npm install/build/watch/dev, and the MCP Inspector (npm run inspect) is suggested for debugging server interactions. -- evidence: [README.md#L133-L136](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L133-L136), [README.md#L128-L131](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L128-L131), [README.md#L117-L120](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L117-L120), [README.md#L140-L152](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L140-L152)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] Ref is a Model Context Protocol server that gives AI coding tools or agents access to documentation for APIs, services, and libraries in a token-efficient way. -- evidence: [README.md#L9-L9](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L9-L9)
  - [observation/documented] The server exposes a ref_search_documentation tool with a required query parameter, described as a full sentence or question, for searching public web/GitHub docs and private resources like repos and PDFs. -- evidence: [README.md#L95-L96](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L95-L96), [README.md#L93-L93](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L93-L93), [README.md#L110-L113](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L110-L113)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The README describes coding agents performing one or more searches and then reading a few resources in depth, refining queries iteratively for complex prompts. -- evidence: [README.md#L17-L17](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L17-L17), [README.md#L25-L35](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L25-L35)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The stdio server runs via npx ref-tools-mcp@latest with a REF_API_KEY environment variable; the hosted HTTP endpoint at api.ref.tools/mcp also uses an API key. -- evidence: [README.md#L77-L85](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L77-L85), [README.md#L66-L71](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L66-L71)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](ref-tools-mcp.detail.md) for every claim.)

Metadata and full claim list: [full detail](ref-tools-mcp.detail.md)
Human notes ([notes](ref-tools-mcp.notes.md), never overwritten by build)

[Back to map index](../../index.md)
