# trailhq/graft

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: nanonets/graft (github id 1288325627).
Latest snapshot: commit f9e65396e638 @ 0609a629c52368da

## Summary (orientation draft, not independently verified)

Graft builds a codebase understanding graph once and writes it into the repo as a folder of linked markdown files, one node per system, API, or concept. graft init registers an MCP server exposing six tools: graft_find_code, graft_file_api, graft_trace_calls, graft_find_all, graft_repo_map, and graft_check_freshness. Evidence coverage: 120 of 272 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Graft builds a codebase understanding graph once and writes it into the repo as a folder of linked markdown files, one node per system, API, or concept. -- evidence: [README.md#L114-L114](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L114-L114)
- components (1 claim(s)):
  - [observation/documented] Parsing uses tree-sitter at two fidelity tiers plus optional compiler-grade lsp_resolved edges via rust-analyzer, clangd, gopls, pyright, or typescript-language-server when on PATH; 23 languages total, unlisted languages are skipped. -- evidence: [README.md#L216-L220](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L216-L220), [README.md#L200-L201](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L200-L201), [README.md#L222-L224](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L222-L224), [README.md#L211-L214](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L211-L214), [README.md#L203-L209](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L203-L209)
- design-choices (2 claim(s)):
  - [observation/documented] The graph is a regenerable local cache: graft build adds graft/ to .gitignore, and only the wiring in .claude/ and instruction files is committed; teammates each run graft build themselves. -- evidence: [README.md#L82-L82](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L82-L82), [README.md#L116-L120](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L116-L120)
  - [observation/documented] Every query refreshes the graph against the working tree first via a ~3ms structural fingerprint check, never calling the LLM; disable per-command with --no-refresh or globally with GRAFT_NO_REFRESH=1. -- evidence: [README.md#L192-L192](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L192-L192)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] graft init registers an MCP server exposing six tools: graft_find_code, graft_file_api, graft_trace_calls, graft_find_all, graft_repo_map, and graft_check_freshness. -- evidence: [README.md#L303-L310](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L303-L310), [README.md#L301-L301](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L301-L301)
  - [observation/documented] Claude Code deep integration adds a live statusline (graph size, % enriched, stale warning), automatic structural graph refresh per query, per-prompt node injection, and post-edit blast-radius hooks; init is idempotent and merges rather than clobbers .claude/settings.json. -- evidence: [README.md#L324-L326](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L324-L326), [README.md#L338-L338](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L338-L338), [README.md#L322-L322](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L322-L322)
- memory-state (1 claim(s)):
  - [observation/documented] Each markdown node holds a model-written summary, inline crux code, content-hash-tracked sources, typed [[wikilinks]] (depends_on, part_of, uses, implements, produces), and user notes preserved across regeneration. -- evidence: [README.md#L244-L244](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L244-L244), [README.md#L234-L240](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L234-L240)
- orchestration (1 claim(s)):
  - [observation/documented] graft init wires multiple agents (Claude, Cursor, Gemini, Codex, Copilot, Kiro, Windsurf, Grok, AdaL) via marker-fenced instruction-file sections or owned skill/rule files, with flags like --agents, --dry-run, --no-mcp, --no-hooks, --no-statusline, --no-global. -- evidence: [README.md#L272-L272](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L272-L272), [README.md#L270-L270](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L270-L270), [README.md#L274-L285](https://github.com/trailhq/Graft/blob/f9e65396e638e517aecae0d731017f53084d70ed/README.md#L274-L285)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](graft.detail.md)

Metadata and full claim list: [full detail](graft.detail.md)
Human notes ([notes](graft.notes.md), never overwritten by build)

[Back to map index](../../index.md)
