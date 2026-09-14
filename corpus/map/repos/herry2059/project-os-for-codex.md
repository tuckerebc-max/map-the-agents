# herry2059/project-os-for-codex

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3cb909ab9f61 @ 6d015e25229802c1

## Summary (orientation draft, not independently verified)

Project OS for Codex (v0.3.0) is an independent, Apache-2.0, Git-backed project-record control plane for Codex AI work, exposing a two-tool stdio MCP server, short-lived scoped AI credentials, a React/Vite + Node/Express stack with local JSON persistence, and fail-closed first-run checks. Contributor rules in AGENTS.md and README describe development workflow and Codex session protocol.

## Source coverage

Source coverage (partial): 3 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The stack is React, Vite, TypeScript, and Tailwind CSS on the frontend with Node.js and Express on the backend, persisting to local JSON files by default under an Apache-2.0 license. -- evidence: [README.md#L262-L266](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L262-L266)
- design-choices (2 claim(s)):
  - [observation/documented] Version 0.3.0 adds a fail-closed first-run contract: the MCP process verifies credential, project binding, scopes, and the exact two-tool surface before Codex uses it, with a project-level config allowlisting only released tools. -- evidence: [README.md#L80-L80](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L80-L80), [README.md#L82-L85](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L82-L85)
  - [observation/documented] The open-source design keeps private infrastructure behind replaceable adapter boundaries for Git, AI provider, knowledge base, and deployment/reverse proxy, with local JSON persistence for simple evaluation. -- evidence: [README.md#L169-L169](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L169-L169), [README.md#L171-L175](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L171-L175)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to work one vertical slice at a time, use pnpm, run pnpm run check before committing, and inspect affected UI in light and dark themes. -- evidence: [AGENTS.md#L7-L9](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L7-L9), [AGENTS.md#L21-L25](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L21-L25)
  - [observation/documented] Repository development practice: the Codex session protocol requires calling project_os_get_context before planning, running pnpm codex:doctor on failure, and only appending progress after verifying one vertical slice. -- evidence: [AGENTS.md#L36-L39](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/AGENTS.md#L36-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The released MCP surface contains exactly two tools: project_os_get_context for scoped context reads and project_os_append_progress for validated, idempotent progress appends. -- evidence: [README.md#L75-L76](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L75-L76), [README.md#L192-L196](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L192-L196)
  - [observation/documented] An Agent API endpoint accepts progress events via POST with X-Project-Key and Idempotency-Key headers, including verification notes, progress percentage, and next step. -- evidence: [README.md#L322-L328](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L322-L328), [README.md#L320-L320](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L320-L320)
- memory-state (1 claim(s)):
  - [observation/documented] The server creates a local Git-backed project record for kickoff, progress, issues, and handoff files, with important progress linked to Git commits as the durable record. -- evidence: [README.md#L138-L138](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L138-L138), [README.md#L140-L143](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L140-L143), [README.md#L104-L111](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L104-L111)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] AI credentials are short-lived (24 hours or 7 days), revocable independently, stored only as hashes, and cannot access members, keys, deletion, publication, or deployment. -- evidence: [README.md#L78-L78](https://github.com/herry2059/project-os-for-codex/blob/3cb909ab9f61958ae6be7fab54b2fd7c5f933140/README.md#L78-L78)
More evidence: [full detail](project-os-for-codex.detail.md)

Metadata and full claim list: [full detail](project-os-for-codex.detail.md)
Human notes ([notes](project-os-for-codex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
