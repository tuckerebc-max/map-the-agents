# oooscoos/benzi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d9c7a3e63df7 @ 69afc1120b591d6f

## Summary (orientation draft, not independently verified)

README-only evidence (1 of 1 candidate file, complete) for Benzi, an AI coding agent that compiles a tree-sitter-based code index and answers via structured query tools, distributed as a VS Code extension and browser demo, with a documented SWE-bench Verified run.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A runtime tracer hooks every call during execution and overlays observed behavior back onto the static map; a separate markup engine indexes HTML/CSS/DOM-JS including frontend embedded in Python strings. -- evidence: [README.md#L148-L154](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L148-L154)
- design-choices (2 claim(s)):
  - [observation/documented] Benzi parses every project file with a tree-sitter-based compiler into a queryable map of symbols, call edges, references, and inheritance before answering questions. -- evidence: [README.md#L34-L34](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L34-L34), [README.md#L36-L36](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L36-L36)
  - [observation/documented] The index distinguishes proven edges (with evidence), ambiguous calls (full candidate lists kept), and runtime traces; unresolved calls are classified rather than silently dropped. -- evidence: [README.md#L148-L154](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L148-L154)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Benzi is available as a browser demo (read-only, any public GitHub repo) and as a VS Code extension with edit access; there is no headless or CLI mode yet. -- evidence: [README.md#L168-L169](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L168-L169), [README.md#L171-L171](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L171-L171)
- memory-state (1 claim(s)):
  - [observation/documented] Durable per-repo facts persist across restarts, so learned conventions are not re-derived each session. -- evidence: [README.md#L148-L154](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L148-L154)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The agent exposes 35+ tools; a sample of 16 includes get_callers, call_tree, trace_path, backflow, profile, skim_source, rollback_edit, and upgrade_to_pro. -- evidence: [README.md#L85-L85](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L85-L85), [README.md#L87-L104](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L87-L104)
  - [observation/documented] Every write passes syntax and semantic gates against the real language parser, and a broken parse auto-reverts the edit. -- evidence: [README.md#L108-L111](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L108-L111)
- evaluation (2 claim(s)):
  - [observation/documented] The README reports that a SWE-bench Verified run on DeepSeek v4-flash resolved 391/500 (78.2%) at $37.33 total, graded by the official harness in per-instance Docker containers with GitHub/PyPI network access blocked. -- evidence: [README.md#L54-L54](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L54-L54), [README.md#L56-L64](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L56-L64)
  - [observation/documented] A 24-bug cross-harness comparison reports Benzi reading the fewest source lines (9,125 with Sonnet vs 20,704 for Claude Code) and roughly a cent per bug on DeepSeek, while Claude Code is said to reach $0.18 per step on harder bugs. -- evidence: [README.md#L117-L122](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L117-L122), [README.md#L115-L115](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L115-L115), [README.md#L142-L142](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L142-L142)
- dependencies (1 claim(s)):
More evidence: [full detail](benzi.detail.md)

Metadata and full claim list: [full detail](benzi.detail.md)
Human notes ([notes](benzi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
