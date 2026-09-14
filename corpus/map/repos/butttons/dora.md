# butttons/dora

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f4edb8fd349e @ f6d9ac8d861f83d6

## Summary (orientation draft, not independently verified)

dora is a CLI that turns a SCIP index into a queryable SQLite database, giving AI agents structured answers about a codebase instead of grepping files and reading imports. The tool has two layers: a SCIP layer that runs a configured indexer, parses the resulting protobuf, and loads symbols, references, and file dependencies into SQLite; and a tree-sitter layer that parses source on demand via WebAssembly grammars for things SCIP doesn't cover. Evidence coverage: 199 of 319 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] dora is a CLI that turns a SCIP index into a queryable SQLite database, giving AI agents structured answers about a codebase instead of grepping files and reading imports. -- evidence: [README.md#L3-L3](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The tool has two layers: a SCIP layer that runs a configured indexer, parses the resulting protobuf, and loads symbols, references, and file dependencies into SQLite; and a tree-sitter layer that parses source on demand via WebAssembly grammars for things SCIP doesn't cover. -- evidence: [README.md#L158-L158](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L158-L158), [README.md#L160-L160](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L160-L160)
  - [observation/documented] The SQLite schema stores denormalized counts (symbol_count, dependency_count, dependent_count, reference_count) so most queries are index lookups rather than aggregations. -- evidence: [README.md#L162-L162](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L162-L162)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the docs/ directory is an Astro starter template; its README instructs contributors to scaffold with 'pnpm create astro' and run pnpm install/dev/build/preview from the project root to develop and build the docs site. -- evidence: [docs/README.md#L32-L39](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/docs/README.md#L32-L39), [docs/README.md#L30-L30](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/docs/README.md#L30-L30), [docs/README.md#L3-L5](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/docs/README.md#L3-L5)
  - [observation/documented] Repository development practice: the root README points contributors to CONTRIBUTING.md for contribution guidance. -- evidence: [README.md#L173-L173](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L173-L173)
- skills-patterns (1 claim(s)):
  - [observation/documented] dora generates integration assets under .dora/docs (SKILL.md, SNIPPET.md) that can be symlinked into .claude/skills/dora or .windsurf/skills/dora and appended to CLAUDE.md or AGENTS.md, enabling a /dora skill reference. -- evidence: [AGENTS.README.md#L88-L90](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L88-L90), [AGENTS.README.md#L110-L110](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L110-L110), [AGENTS.README.md#L458-L461](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L458-L461), [AGENTS.README.md#L476-L478](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L476-L478), [AGENTS.README.md#L79-L82](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L79-L82), [AGENTS.README.md#L75-L75](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/AGENTS.README.md#L75-L75)
- interfaces (2 claim(s)):
  - [observation/documented] All commands output TOON, a compact JSON encoding optimized for LLM token usage, by default; passing --json yields standard JSON. -- evidence: [README.md#L138-L138](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L138-L138)
  - [observation/documented] dora mcp starts an MCP server over stdio, and the README shows registering it with Claude Code via 'claude mcp add --transport stdio dora -- dora mcp'. -- evidence: [README.md#L133-L134](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L133-L134), [README.md#L129-L130](https://github.com/butttons/dora/blob/f4edb8fd349e142e78dea3258c3cd754a27d37bb/README.md#L129-L130)
- memory-state (1 claim(s)):
More evidence: [full detail](dora.detail.md)

Metadata and full claim list: [full detail](dora.detail.md)
Human notes ([notes](dora.notes.md), never overwritten by build)

[Back to map index](../../index.md)
