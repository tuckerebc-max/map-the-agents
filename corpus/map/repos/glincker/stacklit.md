# glincker/stacklit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6aa017643d19 @ b685fa5ba411ed97

## Summary (orientation draft, not independently verified)

Evidence is README documentation plus an internal implementation plan for Stacklit, a Go CLI that generates a compact codebase index (stacklit.json, DEPENDENCIES.md, stacklit.html) for AI agents, with MCP server, git hooks, and a GitHub Action. Most claims are documented product behavior; the plan file is development guidance. Evidence coverage: 183 of 347 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Running stacklit init produces three artifacts: stacklit.json (committable index), DEPENDENCIES.md (Mermaid diagram, committable), and stacklit.html (interactive map, gitignored and regenerable). -- evidence: [README.md#L56-L60](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L56-L60)
  - [observation/documented] The visual map opened by 'stacklit view' offers four views: a force-directed dependency graph, a collapsible tree, a sortable searchable table, and a top-down dependency flow. -- evidence: [README.md#L227-L227](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L227-L227), [README.md#L229-L232](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L229-L232)
- design-choices (1 claim(s)):
  - [observation/documented] The tool is designed so AI agents read a small (~250-token) navigation map or stacklit.json instead of scanning many files, which the README claims cuts exploration from hundreds of thousands of tokens to a few thousand. -- evidence: [README.md#L75-L75](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L75-L75), [README.md#L3-L3](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L3-L3), [README.md#L71-L71](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L71-L71), [README.md#L73-L73](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L73-L73), [README.md#L137-L137](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L137-L137)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors build with 'make build' and run all tests with 'make test', per the README contributing section. -- evidence: [README.md#L331-L334](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L331-L334)
  - [observation/documented] Repository development practice: an internal plan document instructs agentic workers to use superpowers subagent-driven-development or executing-plans skills to implement tasks step-by-step with checkbox tracking. -- evidence: [docs/superpowers/plans/2026-04-12-growth-package.md#L3-L3](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/docs/superpowers/plans/2026-04-12-growth-package.md#L3-L3)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands including init (with --hook and --multi flags), generate, view, diff, serve, derive, export, and setup with per-tool variants for claude and cursor. -- evidence: [README.md#L254-L269](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L254-L269)
  - [observation/documented] The MCP server started via 'stacklit serve' exposes seven tools: get_overview, get_module, find_module, list_modules, get_dependencies, get_hot_files, and get_hints. -- evidence: [README.md#L173-L173](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L173-L173)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] 'stacklit setup' auto-detects Claude Code, Cursor, and Aider, injecting a ~250-token codebase map into each tool's config, configuring MCP integration, and installing a git hook to refresh the map on commits. -- evidence: [README.md#L118-L121](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L118-L121), [README.md#L125-L129](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L125-L129)
- tools-permissions (1 claim(s)):
  - [observation/documented] Parsing runs locally and no code is sent anywhere unless the optional --summary flag is used, which calls the Claude API. -- evidence: [README.md#L309-L310](https://github.com/glincker/stacklit/blob/6aa017643d19ab2718d42f098ee2a65717c2e3b6/README.md#L309-L310)
- evaluation (1 claim(s)):
More evidence: [full detail](stacklit.detail.md)

Metadata and full claim list: [full detail](stacklit.detail.md)
Human notes ([notes](stacklit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
