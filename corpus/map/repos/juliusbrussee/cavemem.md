# juliusbrussee/cavemem

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 166078dd7c46 @ f87f7425c04f96c8

## Summary (orientation draft, not independently verified)

The CLI offers commands including install/uninstall per IDE, status, config show/get/set/open, viewer, doctor, search, compress, reindex, export/import JSONL, and an stdio MCP server. The MCP server exposes search, timeline, get_observations, and list_sessions, plus an opt-in enrich tool; search and timeline return compact results while get_observations fetches full bodies.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Compression is deterministic and offline, never invoking a model; technical tokens (code, URLs, paths, commands, versions, dates, numbers, identifiers) are preserved byte-for-byte and prose is lossy only on filler/hedging words. -- evidence: [docs/compression.md#L5-L7](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/compression.md#L5-L7), [docs/compression.md#L3-L3](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/compression.md#L3-L3)
  - [observation/documented] Search is hybrid: SQLite FTS5 BM25 keyword matching blended with a local vector index, weighted by the tunable search.alpha setting (default 0.5). -- evidence: [docs/mcp.md#L26-L26](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/mcp.md#L26-L26), [README.md#L165-L178](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L165-L178), [README.md#L28-L35](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L28-L35)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must pass four gates (pnpm typecheck, lint, test, build) before merging, add changesets for package changes, use Conventional Commits, and get one review on PRs. -- evidence: [CLAUDE.md#L52-L60](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L52-L60), [docs/development.md#L42-L42](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/development.md#L42-L42), [CLAUDE.md#L89-L90](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L89-L90), [docs/development.md#L35-L40](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/development.md#L35-L40)
  - [observation/documented] Repository development practice: an end-to-end publish script (scripts/e2e-publish.sh) must pass in CI before changeset publish, driving real hook events, FTS search, and the MCP server in an isolated install prefix. -- evidence: [CLAUDE.md#L66-L69](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L66-L69)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI offers commands including install/uninstall per IDE, status, config show/get/set/open, viewer, doctor, search, compress, reindex, export/import JSONL, and an stdio MCP server. -- evidence: [README.md#L114-L128](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L114-L128)
  - [observation/documented] The MCP server exposes search, timeline, get_observations, and list_sessions, plus an opt-in enrich tool; search and timeline return compact results while get_observations fetches full bodies. -- evidence: [README.md#L138-L144](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L138-L144), [README.md#L136-L136](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L136-L136), [docs/mcp.md#L3-L3](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/mcp.md#L3-L3)
- memory-state (1 claim(s)):
  - [observation/documented] Memory persists in a local SQLite database with FTS5 updated via triggers; embeddings are computed out-of-band by a background worker that auto-spawns on the first hook and self-exits when idle. -- evidence: [docs/architecture.md#L21-L26](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/architecture.md#L21-L26), [README.md#L49-L49](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L49-L49)
- orchestration (1 claim(s)):
  - [observation/documented] Per-IDE installers wire hooks and MCP: Claude Code, OpenCode, Codex, Copilot, and Augment capture observations, while Cursor, Gemini CLI, Antigravity, and IBM Bob are query-only over memory captured elsewhere. -- evidence: [README.md#L55-L65](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L55-L65), [README.md#L26-L26](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L26-L26)
- tools-permissions (2 claim(s)):
  - [observation/documented] The viewer worker binds to 127.0.0.1 only, checks Host/Origin headers, and requires a local bearer token (mode 0600) on /api/* endpoints. -- evidence: [README.md#L180-L180](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L180-L180)
More evidence: [full detail](cavemem.detail.md)

Metadata and full claim list: [full detail](cavemem.detail.md)
Human notes ([notes](cavemem.notes.md), never overwritten by build)

[Back to map index](../../index.md)
