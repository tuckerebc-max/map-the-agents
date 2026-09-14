# prasenjeet-symon/ogcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e76eaf72178d @ 15cde5cc5ac46f99

## Summary (orientation draft, not independently verified)

The snapshot contains only README.md slices describing Ogcode, a self-hosted Go coding agent with a SolidJS web UI, knowledge-graph session memory, plan mode with parallel git-worktree task execution, and tree-sitter file mapping. All claims below are documentation-based; no code or contributor-workflow evidence is present. Evidence coverage: 123 of 380 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Ogcode is described as a single Go binary with an embedded SolidJS web UI that runs locally, positioned as browser-native, self-hosted, and model-agnostic. -- evidence: [README.md#L125-L125](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L125-L125), [README.md#L127-L127](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L127-L127)
  - [observation/documented] The breakdown agent enforces a file-ownership rule so parallel tasks never edit the same files, and dependency chains are strictly linear with cycles rejected before execution. -- evidence: [README.md#L106-L109](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L106-L109)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are SKILL.md files whose names and descriptions appear in the prompt; the full body is loaded via a skill tool only when a task matches. -- evidence: [README.md#L459-L459](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L459-L459), [README.md#L461-L461](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L461-L461)
- interfaces (3 claim(s)):
  - [observation/documented] A file_map tool uses tree-sitter to outline declarations with line ranges; reading a file over 200 lines without a range returns the map instead of full contents. -- evidence: [README.md#L242-L249](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L242-L249), [README.md#L271-L271](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L271-L271), [README.md#L288-L288](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L288-L288)
  - [observation/documented] Ten tree-sitter grammars cover Go, TypeScript/JS/TSX, PHP, Python, Rust, Swift, Java, C#, and Dart, with a heuristic fallback scanner for other file types. -- evidence: [README.md#L338-L338](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L338-L338), [README.md#L299-L299](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L299-L299), [README.md#L301-L312](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L301-L312)
- memory-state (2 claim(s)):
  - [observation/documented] The README claims Agentic Session Memory recalls only task-relevant facts from a persistent knowledge graph per turn instead of replaying the full transcript, keeping per-turn prompt size flat. -- evidence: [README.md#L40-L40](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L40-L40), [README.md#L62-L62](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L62-L62)
  - [observation/documented] A knowledge graph structured as Topic → Concept → Fact is said to persist across sessions as semantic memory of the codebase. -- evidence: [README.md#L155-L169](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L155-L169)
- orchestration (2 claim(s)):
  - [observation/documented] Plan Mode breaks a locked plan into tasks with effort estimates (S/M/L/XL), complexity scores, and a dependency graph, shown on a visual Kanban board before execution. -- evidence: [README.md#L95-L100](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L95-L100), [README.md#L82-L93](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L82-L93)
  - [observation/documented] Each task runs in its own git worktree and isolated agent session; independent tasks execute in parallel, and finished tasks auto-commit, push, and open PRs via the gh CLI idempotently. -- evidence: [README.md#L95-L100](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L95-L100), [README.md#L115-L119](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L115-L119)
More evidence: [full detail](ogcode.detail.md)

Metadata and full claim list: [full detail](ogcode.detail.md)
Human notes ([notes](ogcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
