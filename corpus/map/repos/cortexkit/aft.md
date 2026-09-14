# cortexkit/aft

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c0c8e80220ac @ 6ee76353dadd17a8

## Summary (orientation draft, not independently verified)

AFT is a Rust binary plus TypeScript harness adapters (OpenCode, Pi, OMP) that replaces and augments coding agents' file/shell tools with tree-sitter parsing, indexed search, call graphs, background bash, and undo/safety features. Evidence is mostly README/ARCHITECTURE documentation; benchmarks are documented as not yet published. Evidence coverage: 98 of 202 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 4 of 42 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] AFT ships as a Rust binary with thin TypeScript adapter packages for OpenCode, Pi, and OMP, distributed via crates.io and npm. -- evidence: [README.md#L52-L52](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L52-L52), [README.md#L13-L20](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L13-L20)
  - [observation/documented] The Rust core includes tree-sitter parsing for ~30 languages, symbol/call-graph computation, diff/format/backup, an LSP client, trigram index, and semantic index. -- evidence: [README.md#L200-L227](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L200-L227)
- design-choices (1 claim(s)):
  - [observation/documented] Adapters hoist the host's built-in read/write/edit/grep tool slots so existing tool names are backed by AFT, while also registering an aft_-prefixed tool family; hoist_builtin_tools toggles this behavior. -- evidence: [README.md#L74-L76](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L74-L76), [README.md#L52-L52](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L52-L52)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions require an issue with the design-approved label before a PR is reviewable (typo fixes exempt), and bun run format plus cargo fmt must be run before submitting since CI rejects unformatted code. -- evidence: [README.md#L301-L301](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L301-L301), [README.md#L303-L303](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L303-L303)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The Rust core communicates with adapters over a JSON-over-stdio request/response protocol, with one persistent process per project root shared across sessions. -- evidence: [README.md#L229-L229](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L229-L229), [README.md#L198-L198](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L198-L198)
  - [observation/documented] Sensory tools include aft_outline, aft_zoom, aft_search (hybrid semantic+lexical), aft_callgraph, aft_inspect, and trigram-indexed grep/glob backed by a file watcher. -- evidence: [README.md#L112-L117](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L112-L117)
- memory-state (1 claim(s)):
  - [observation/documented] AFT data (backups, search indexes, LSP servers) persists under ~/.local/share/cortexkit/aft/, and aft_safety provides a per-file undo stack with named checkpoints that survives restarts. -- evidence: [README.md#L231-L231](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L231-L231), [README.md#L139-L143](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L139-L143)
- orchestration (1 claim(s)):
  - [observation/documented] The brainstem layer provides background bash tasks (bash_status, bash_kill, bash_watch) that survive restarts, PTY sessions driven via bash_write, and multi-tier output compression. -- evidence: [README.md#L139-L143](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/README.md#L139-L143)
- tools-permissions (1 claim(s)):
  - [observation/documented] Under sandbox.enabled, first-party bash commands run through Landlock (Linux) or Seatbelt (macOS); unsupported non-Unix platforms fail closed with sandbox_unavailable, and a one-command host escape prompts via an escalation permission ask. -- evidence: [ARCHITECTURE.md#L123-L128](https://github.com/cortexkit/aft/blob/c0c8e80220ac45e45be98a87c86b28db02c96f49/ARCHITECTURE.md#L123-L128)
- evaluation (1 claim(s)):
More evidence: [full detail](aft.detail.md)

Metadata and full claim list: [full detail](aft.detail.md)
Human notes ([notes](aft.notes.md), never overwritten by build)

[Back to map index](../../index.md)
