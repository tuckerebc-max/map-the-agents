# terragon-labs/terragon-oss

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 83142a17f397 @ 855649a683fe5a0c

## Summary (orientation draft, not independently verified)

The snapshot is Terragon, a cloud platform for delegating work to coding agents in sandboxed containers, with a terry CLI, MCP server, and GitHub-integrated task workflow. Most operational detail comes from README product descriptions and AGENTS.md contributor instructions; the repo is archived as-is with no maintenance guarantees.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Each agent runs in an isolated sandbox container with its own repository copy, letting it read files, edit, and run tests without affecting concurrent tasks or the local environment. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20)
  - [observation/documented] Tasks get unique branches, and agent work is checkpointed to GitHub with AI-generated commits and pull requests; this git workflow can be disabled for flexibility. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: local development requires Node.js 20+, pnpm 10.14.0+, Docker for PostgreSQL/Redis containers, and Stripe CLI for webhook forwarding; dependencies install via 'pnpm install'. -- evidence: [README.md#L39-L41](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L39-L41), [README.md#L24-L27](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L24-L27)
  - [observation/documented] Repository development practice: after schema changes, contributors push the Drizzle schema to the dev database with 'pnpm -C packages/shared drizzle-kit-push-dev', and 'pnpm dev' starts all development services. -- evidence: [README.md#L81-L81](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L81-L81), [README.md#L77-L79](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L77-L79), [README.md#L71-L73](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L71-L73), [README.md#L69-L69](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L69-L69)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The product ships a 'terry' CLI for local task takeover and continuation, plus an MCP server so MCP-compatible clients like Cursor and Claude Code can create and manage tasks. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Terragon supports multiple coding agents—Claude Code, OpenAI Codex, Amp, and Gemini—and is designed so support for additional agents can be added. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20)
  - [observation/documented] The product offers automations: recurring tasks or event-triggered workflows, such as triggers on new issues or pull requests, to automate repetitive development work. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] The repository is an as-is snapshot taken at Terragon's shutdown, with no guarantees of maintenance, support, or completeness. -- evidence: [README.md#L3-L3](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](terragon-oss.detail.md) for every claim.)

Metadata and full claim list: [full detail](terragon-oss.detail.md)
Human notes ([notes](terragon-oss.notes.md), never overwritten by build)

[Back to map index](../../index.md)
